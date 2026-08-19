"""
Live WooCommerce site prerequisite ("toggle") state capture for Validate AC.

MCSL toggles are SaaS feature flags keyed by account UUID, read out of the
embedded app's network responses. WooCommerce has no such thing: the plugins are
self-hosted, and a "toggle" is one of

  * a **plugin setting** on the Multi-Carrier shipping method
    (reachable over REST at shipping/zones/<id>/methods/<instance_id>),
  * a **WooCommerce core setting** (settings/<group>/<id>),
  * or simply **which plugin version is active** on the site
    (system_status → active_plugins).

So this module captures that state over the WooCommerce REST API rather than by
driving a browser. The public surface is unchanged — `capture_site_toggle_state`
(aliased as `capture_store_and_toggle_state`) and `compute_toggle_status` — so
the dashboard and notifier scripts call it exactly as before.
"""
from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from typing import Any

logger = logging.getLogger(__name__)

_TRUTHY = {"yes", "true", "1", "on", "enabled", "enable"}
_FALSY = {"no", "false", "0", "off", "disabled", "disable", ""}


@dataclass
class ToggleCaptureResult:
    """Captured prerequisite state for one WooCommerce site."""
    app_url: str
    site_url: str = ""
    wc_version: str = ""
    wp_version: str = ""
    # plugin name -> version, for every active plugin on the site
    plugin_versions: dict[str, str] = field(default_factory=dict)
    # normalised setting/flag name -> bool
    toggle_map: dict[str, bool] = field(default_factory=dict)
    # unnormalised settings, kept so QA can read the actual stored value
    raw_settings: dict[str, Any] = field(default_factory=dict)
    error: str = ""

    # ── backwards-compatible aliases ────────────────────────────────
    # MCSL callers read .store_uuid / .account_uuid. WooCommerce has neither;
    # the site URL is the identity. Keep the attributes so shared UI code and
    # message templates don't need per-platform branches.
    @property
    def store_uuid(self) -> str:
        return self.site_url

    @property
    def account_uuid(self) -> str:
        return self.site_url


def _normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]", "", str(text or "").lower())


def normalize_toggle_name(name: str) -> str:
    return _normalize(name)


def _coerce_bool(value: Any) -> bool | None:
    """WooCommerce stores booleans as 'yes'/'no' strings as often as real bools.

    Returns None for anything that is not clearly a boolean. In particular a
    numeric setting like `woocommerce_price_num_decimals = 2` is a *number*, not
    a flag — coercing it would put "numberofdecimals: enabled" in the
    prerequisite report, which is meaningless.
    """
    if isinstance(value, bool):
        return value
    if isinstance(value, int) and value in (0, 1):
        return bool(value)
    if isinstance(value, str):
        lowered = value.strip().lower()
        if lowered in _TRUTHY:
            return True
        if lowered in _FALSY:
            return False
    return None


def _extract_toggle_map(payload: Any) -> dict[str, bool]:
    """
    Flatten any WooCommerce settings-ish payload into {normalised_name: bool}.

    Handles the three shapes the REST API actually returns:
      * a settings list      [{"id": "enabled", "value": "yes"}, ...]
      * a settings dict      {"enabled": "yes", "debug": False}
      * a shipping method    {"settings": {"title": {...}, "enabled": {"value": "yes"}}}
    """
    result: dict[str, bool] = {}

    def _record(name: Any, value: Any) -> None:
        key = _normalize(name)
        if not key:
            return
        coerced = _coerce_bool(value)
        if coerced is not None:
            result[key] = coerced

    def _walk(node: Any) -> None:
        if isinstance(node, dict):
            # {"id"/"key"/"name": ..., "value"/"enabled"/"active"/"status": ...}
            name = node.get("id") or node.get("key") or node.get("name")
            if name is not None:
                for value_key in ("value", "enabled", "active", "status", "default"):
                    if value_key in node:
                        _record(name, node[value_key])
                        break
            for child_key, child in node.items():
                if isinstance(child, (dict, list)):
                    if isinstance(child, dict) and any(
                        k in child for k in ("value", "enabled", "active", "status")
                    ):
                        for value_key in ("value", "enabled", "active", "status"):
                            if value_key in child:
                                _record(child_key, child[value_key])
                                break
                    _walk(child)
                else:
                    _record(child_key, child)
        elif isinstance(node, list):
            for item in node:
                _walk(item)

    _walk(payload)
    return result


def compute_toggle_status(
    required_toggles: list[str], toggle_map: dict[str, bool]
) -> dict[str, list[str]]:
    """
    Split the required prerequisites into enabled / missing / unknown.

    enabled — present in the captured state and switched on
    missing — present in the captured state but switched off
    unknown — not found on the site at all (wrong plugin version, wrong screen,
              or the card named something that isn't a real setting)
    """
    status: dict[str, list[str]] = {"enabled": [], "missing": [], "unknown": []}
    for toggle in required_toggles or []:
        key = _normalize(toggle)
        if key not in toggle_map:
            status["unknown"].append(toggle)
        elif toggle_map[key]:
            status["enabled"].append(toggle)
        else:
            status["missing"].append(toggle)
    return status


def _plugin_versions(system_status: dict[str, Any]) -> dict[str, str]:
    return {
        str(p.get("name", "")).strip(): str(p.get("version", "")).strip()
        for p in (system_status.get("active_plugins") or [])
        if p.get("name")
    }


def capture_site_toggle_state(
    site_url: str = "",
    *,
    client: Any = None,
    include_zone_methods: bool = True,
) -> ToggleCaptureResult:
    """
    Read the live prerequisite state off a WooCommerce site.

    Captures, in order:
      1. system_status  — WP/WC versions and every active plugin's version
      2. shipping zone methods — the Multi-Carrier method's own settings, which
         is where most per-feature plugin toggles actually live
      3. WooCommerce settings groups that gate shipping behaviour

    Never raises: transport and permission failures come back on `.error` so the
    dashboard can show partial state instead of blanking the tab.
    """
    result = ToggleCaptureResult(app_url=site_url, site_url=site_url)
    try:
        if client is None:
            from pipeline.woo_api import WooClient, WooCredentials

            creds = WooCredentials.from_config()
            if site_url:
                creds = WooCredentials(
                    site_url=site_url,
                    consumer_key=creds.consumer_key,
                    consumer_secret=creds.consumer_secret,
                    api_version=creds.api_version,
                )
            client = WooClient(creds)
            result.site_url = creds.site_url
            result.app_url = site_url or creds.site_url
    except Exception as exc:  # missing credentials, bad URL
        result.error = f"Could not build a WooCommerce client: {exc}"
        return result

    toggle_map: dict[str, bool] = {}

    try:
        status = client.get_system_status() or {}
        environment = status.get("environment") or {}
        result.wp_version = str(environment.get("wp_version", ""))
        result.wc_version = str(environment.get("version", ""))
        result.site_url = result.site_url or str(environment.get("site_url", ""))
        result.plugin_versions = _plugin_versions(status)
        result.raw_settings["settings"] = status.get("settings") or {}
        toggle_map.update(_extract_toggle_map(status.get("settings") or {}))
    except Exception as exc:
        result.error = f"system_status unavailable: {exc}"

    if include_zone_methods:
        try:
            zone_methods = {}
            for zone in client.list_shipping_zones():
                for method in client.list_zone_methods(zone["id"]):
                    label = f"{zone.get('name', zone['id'])}:{method.get('method_id')}"
                    zone_methods[label] = method
                    toggle_map[_normalize(f"{method.get('method_id')} enabled")] = bool(
                        method.get("enabled")
                    )
                    toggle_map.update(_extract_toggle_map(method.get("settings") or {}))
            result.raw_settings["shipping_methods"] = zone_methods
        except Exception as exc:
            result.error = (result.error + " | " if result.error else "") + \
                f"shipping zones unavailable: {exc}"

    result.toggle_map = toggle_map
    return result


# Name kept from the MCSL flow so dashboard and script call sites are unchanged.
def capture_store_and_toggle_state(app_url: str = "", timeout_ms: int = 25000) -> ToggleCaptureResult:
    """
    Compatibility wrapper. `app_url` may be a bare site URL or a wp-admin URL;
    only the origin is used. `timeout_ms` is accepted and ignored — this path no
    longer drives a browser.
    """
    site = (app_url or "").strip()
    if site:
        match = re.match(r"^(https?://[^/]+)", site)
        site = match.group(1) if match else site
    return capture_site_toggle_state(site)
