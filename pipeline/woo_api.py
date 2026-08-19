"""
WooCommerce REST API client.

This is the Woo equivalent of the WooCommerce REST API layer in MCSLDomainExpert.
Everything that talks to a QA WooCommerce store — product seeding, order
creation, settings inspection — goes through here so credential handling and
error reporting stay in one place.

Auth: WooCommerce REST API consumer key/secret. Over HTTPS these go as HTTP
Basic auth, which is what WooCommerce recommends and what
`ups-woo-automation/src/api/client/wooApiClient.ts` already uses.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any

import requests
from requests.auth import HTTPBasicAuth

import config

logger = logging.getLogger(__name__)

DEFAULT_TIMEOUT = 30


class WooApiError(RuntimeError):
    """Raised when the WooCommerce REST API returns an error response."""

    def __init__(self, message: str, *, status: int | None = None, body: str = ""):
        super().__init__(message)
        self.status = status
        self.body = body


@dataclass(frozen=True)
class WooCredentials:
    site_url: str
    consumer_key: str
    consumer_secret: str
    api_version: str = "wc/v3"

    @classmethod
    def from_config(cls) -> "WooCredentials":
        return cls(
            site_url=config.WOO_SITE_URL,
            consumer_key=config.WOO_CONSUMER_KEY,
            consumer_secret=config.WOO_CONSUMER_SECRET,
            api_version=config.WOO_API_VERSION or "wc/v3",
        )

    @classmethod
    def from_env_mapping(cls, env: dict[str, str]) -> "WooCredentials":
        """
        Build credentials from a carrier-env / automation .env mapping.

        Accepts both this repo's WOO_* names and the automation repo's
        lowercase `site_url` / `CONSUMER_KEY` / `CONSUMER_SECRET` names.
        """
        return cls(
            site_url=(env.get("WOO_SITE_URL") or env.get("site_url") or config.WOO_SITE_URL),
            consumer_key=(env.get("WOO_CONSUMER_KEY") or env.get("CONSUMER_KEY")
                          or config.WOO_CONSUMER_KEY),
            consumer_secret=(env.get("WOO_CONSUMER_SECRET") or env.get("CONSUMER_SECRET")
                             or config.WOO_CONSUMER_SECRET),
            api_version=(env.get("WOO_API_VERSION") or config.WOO_API_VERSION or "wc/v3"),
        )

    def validate(self) -> None:
        missing = [
            name for name, value in (
                ("WOO_SITE_URL", self.site_url),
                ("WOO_CONSUMER_KEY", self.consumer_key),
                ("WOO_CONSUMER_SECRET", self.consumer_secret),
            ) if not str(value).strip()
        ]
        if missing:
            raise WooApiError(
                "Missing WooCommerce credentials: " + ", ".join(missing)
                + ". Set them in .env (WooCommerce > Settings > Advanced > REST API)."
            )


class WooClient:
    """Thin requests wrapper over the WooCommerce REST API."""

    def __init__(self, credentials: WooCredentials | None = None, *, timeout: int = DEFAULT_TIMEOUT):
        self.creds = credentials or WooCredentials.from_config()
        self.creds.validate()
        self.timeout = timeout
        self._session = requests.Session()
        self._session.auth = HTTPBasicAuth(self.creds.consumer_key, self.creds.consumer_secret)

    # ── plumbing ────────────────────────────────────────────────────

    def _url(self, path: str) -> str:
        base = self.creds.site_url.rstrip("/")
        return f"{base}/wp-json/{self.creds.api_version}/{path.lstrip('/')}"

    def request(self, method: str, path: str, **kwargs: Any) -> Any:
        url = self._url(path)
        kwargs.setdefault("timeout", self.timeout)
        resp = self._session.request(method, url, **kwargs)
        if not resp.ok:
            raise WooApiError(
                f"{method} {url} failed with HTTP {resp.status_code}",
                status=resp.status_code,
                body=resp.text[:2000],
            )
        if not resp.content:
            return None
        try:
            return resp.json()
        except ValueError as exc:
            raise WooApiError(f"{method} {url} returned non-JSON body", body=resp.text[:2000]) from exc

    def get(self, path: str, params: dict[str, Any] | None = None) -> Any:
        return self.request("GET", path, params=params or {})

    def post(self, path: str, payload: dict[str, Any]) -> Any:
        return self.request("POST", path, json=payload)

    def put(self, path: str, payload: dict[str, Any]) -> Any:
        return self.request("PUT", path, json=payload)

    def delete(self, path: str, *, force: bool = True) -> Any:
        return self.request("DELETE", path, params={"force": str(force).lower()})

    # ── products ────────────────────────────────────────────────────

    def search_products(self, name: str, per_page: int = 20) -> list[dict[str, Any]]:
        return self.get("products", {"search": name, "per_page": per_page}) or []

    def create_product(self, payload: dict[str, Any]) -> dict[str, Any]:
        return self.post("products", payload)

    def create_variation(self, product_id: int, payload: dict[str, Any]) -> dict[str, Any]:
        return self.post(f"products/{product_id}/variations", payload)

    def list_variations(self, product_id: int) -> list[dict[str, Any]]:
        return self.get(f"products/{product_id}/variations", {"per_page": 100}) or []

    # ── orders ──────────────────────────────────────────────────────

    def create_order(self, payload: dict[str, Any]) -> dict[str, Any]:
        return self.post("orders", payload)

    def get_order(self, order_id: int) -> dict[str, Any]:
        return self.get(f"orders/{order_id}")

    def update_order(self, order_id: int, payload: dict[str, Any]) -> dict[str, Any]:
        return self.put(f"orders/{order_id}", payload)

    def list_orders(self, params: dict[str, Any] | None = None) -> list[dict[str, Any]]:
        return self.get("orders", params or {"per_page": 20}) or []

    # ── shipping / settings (read-only helpers used by QA reasoning) ─

    def list_shipping_zones(self) -> list[dict[str, Any]]:
        return self.get("shipping/zones") or []

    def list_zone_methods(self, zone_id: int) -> list[dict[str, Any]]:
        return self.get(f"shipping/zones/{zone_id}/methods") or []

    def get_system_status(self) -> dict[str, Any]:
        """Active plugins, WC version, PHP version — useful for release triage."""
        return self.get("system_status") or {}

    def active_plugins(self) -> list[dict[str, Any]]:
        return (self.get_system_status() or {}).get("active_plugins", []) or []
