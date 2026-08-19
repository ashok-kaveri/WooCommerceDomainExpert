"""
New-carrier onboarding for WooCommerce.

MCSL's version of this module drove Shopify Partner OAuth with Playwright:
create a dev store, install the app, create a custom dev app, scrape the
one-shot `shpat_*` Admin API token. **None of that exists for WooCommerce.**

A WooCommerce QA site is a WordPress install that already has the plugins on it.
Onboarding a carrier means:

  1. confirm the site is reachable and the plugin is active at the right version
  2. set the store address, units, and currency the scenarios assume
  3. create the shipping zone and attach the PluginHive shipping method
  4. STOP — a human registers the carrier credentials in wp-admin
  5. seed products and write the carrier-env (see `woo_product_seed` and
     `new_carrier_validation.write_carrier_env_file`)

Steps 1–3 run over the WooCommerce REST API. Steps 4 and 5 are separate: step 4
has no API at all, and step 5 belongs to the seeding/env modules.

The public names from the MCSL module are kept so the dashboard imports keep
working; the two that describe Shopify-only concepts now fail loudly with an
explanation instead of pretending to work.
"""
from __future__ import annotations

import logging
import time
from dataclasses import dataclass, field
from typing import Any

import config
from pipeline import woo_admin
from pipeline.woo_api import WooApiError, WooClient, WooCredentials

logger = logging.getLogger(__name__)

# Kept for dashboard imports. WooCommerce has no partner portal — these point at
# the equivalent wp-admin screens instead.
DEFAULT_PARTNER_STORES_URL = "wp-admin/plugins.php"
DEFAULT_PARTNER_APPS_URL = "wp-admin/admin.php?page=wc-settings&tab=advanced&section=keys"

# Substrings that identify a PluginHive plugin in the active-plugins list.
PLUGINHIVE_PLUGIN_MARKERS = ("pluginhive", "ph multi carrier", "multi carrier shipping",
                             "woocommerce shipping pro", "shipment tracking",
                             "estimated delivery", "table rate shipping")

DEFAULT_SHIPPING_METHOD_ID = "ph_multicarrier"


@dataclass(frozen=True)
class NewCarrierOnboardingResult:
    store_name: str
    store_created: bool          # site reachable and responding on wc/v3
    app_installed: bool          # a PluginHive plugin is active on the site
    woo_site_url: str
    app_url: str                 # plugin settings screen
    stdout: str
    stderr: str
    returncode: int
    started_at: float
    finished_at: float
    # WooCommerce-specific detail
    wp_version: str = ""
    wc_version: str = ""
    plugin_versions: dict[str, str] = field(default_factory=dict)
    zone_id: int | None = None
    method_instance_id: int | None = None

    @property
    def duration_seconds(self) -> float:
        return max(0.0, self.finished_at - self.started_at)


def _client(site_url: str) -> WooClient:
    base = WooCredentials.from_config()
    creds = WooCredentials(
        site_url=site_url or base.site_url,
        consumer_key=base.consumer_key,
        consumer_secret=base.consumer_secret,
        api_version=base.api_version,
    )
    return WooClient(creds)


def _pluginhive_plugins(active_plugins: list[dict[str, Any]]) -> dict[str, str]:
    found: dict[str, str] = {}
    for plugin in active_plugins or []:
        name = str(plugin.get("name", ""))
        author = str(plugin.get("author_name", ""))
        haystack = f"{name} {author}".lower()
        if any(marker in haystack for marker in PLUGINHIVE_PLUGIN_MARKERS):
            found[name] = str(plugin.get("version", ""))
    return found


def prepare_site_for_carrier(
    *,
    site_url: str = "",
    zone_name: str = "",
    zone_country: str = "",
    shipping_method_id: str = DEFAULT_SHIPPING_METHOD_ID,
    store_settings: dict[str, str] | None = None,
    client: WooClient | None = None,
) -> NewCarrierOnboardingResult:
    """Steps 1–3: verify the site, apply store settings, ensure zone + method.

    Idempotent — an existing zone with the same name is reused, and the method
    is only added when it is not already on that zone.

    Never raises for an unreachable site or a missing plugin: those come back on
    `.stderr` with a non-zero `returncode`, so the dashboard can show a partial
    result instead of blanking the tab.
    """
    started = time.time()
    site = (site_url or config.WOO_SITE_URL or "").rstrip("/")
    out: list[str] = []
    err: list[str] = []
    wp_version = wc_version = ""
    plugins: dict[str, str] = {}
    zone_id: int | None = None
    instance_id: int | None = None

    try:
        woo = client or _client(site)
    except WooApiError as exc:
        return NewCarrierOnboardingResult(
            store_name=site, store_created=False, app_installed=False,
            woo_site_url=site, app_url=woo_admin.plugin_settings_url(site or None),
            stdout="", stderr=str(exc), returncode=1,
            started_at=started, finished_at=time.time(),
        )

    # ── 1. reachable + plugin active ────────────────────────────────
    reachable = False
    try:
        status = woo.get_system_status() or {}
        environment = status.get("environment") or {}
        wp_version = str(environment.get("wp_version", ""))
        wc_version = str(environment.get("version", ""))
        site = site or str(environment.get("site_url", ""))
        reachable = True
        out.append(f"Site reachable: {site}")
        out.append(f"WordPress {wp_version} | WooCommerce {wc_version} | "
                   f"PHP {environment.get('php_version', '?')}")

        plugins = _pluginhive_plugins(status.get("active_plugins") or [])
        if plugins:
            for name, version in plugins.items():
                out.append(f"  active: {name} {version}")
        else:
            err.append("No PluginHive plugin is active on this site — "
                       "install and activate it before onboarding a carrier.")
    except Exception as exc:
        err.append(f"system_status failed: {exc}")

    # ── 2. store settings ───────────────────────────────────────────
    for setting_id, value in (store_settings or {}).items():
        try:
            woo.put(f"settings/general/{setting_id}", {"value": value})
            out.append(f"  set {setting_id} = {value}")
        except Exception as exc:
            err.append(f"could not set {setting_id}: {exc}")

    # ── 3. shipping zone + method ───────────────────────────────────
    if zone_name:
        try:
            zones = woo.list_shipping_zones()
            existing = next((z for z in zones if str(z.get("name", "")).strip() == zone_name), None)
            if existing:
                zone_id = int(existing["id"])
                out.append(f"Reusing shipping zone {zone_name!r} (id {zone_id})")
            else:
                created = woo.post("shipping/zones", {"name": zone_name})
                zone_id = int(created["id"])
                out.append(f"Created shipping zone {zone_name!r} (id {zone_id})")

            if zone_country:
                woo.request("PUT", f"shipping/zones/{zone_id}/locations",
                            json=[{"code": zone_country, "type": "country"}])
                out.append(f"  zone locations set to {zone_country}")

            methods = woo.list_zone_methods(zone_id)
            match = next((m for m in methods if m.get("method_id") == shipping_method_id), None)
            if match:
                instance_id = int(match["instance_id"])
                out.append(f"  {shipping_method_id} already on the zone (instance {instance_id})")
            else:
                added = woo.post(f"shipping/zones/{zone_id}/methods",
                                 {"method_id": shipping_method_id})
                instance_id = int(added["instance_id"])
                out.append(f"  added {shipping_method_id} (instance {instance_id})")
        except Exception as exc:
            err.append(f"shipping zone setup failed: {exc}")

    # ── 4. the manual step ──────────────────────────────────────────
    out.append("")
    out.append("NEXT — manual, no API exists for this:")
    out.append(f"  register the carrier at {woo_admin.plugin_settings_url(site or None)}")

    return NewCarrierOnboardingResult(
        store_name=site,
        store_created=reachable,
        app_installed=bool(plugins),
        woo_site_url=site,
        app_url=woo_admin.plugin_settings_url(site or None),
        stdout="\n".join(out),
        stderr="\n".join(err),
        returncode=0 if reachable and plugins and not err else 1,
        started_at=started,
        finished_at=time.time(),
        wp_version=wp_version,
        wc_version=wc_version,
        plugin_versions=plugins,
        zone_id=zone_id,
        method_instance_id=instance_id,
    )


def create_store_and_install_app(
    *,
    store_name: str,
    partner_stores_url: str = DEFAULT_PARTNER_STORES_URL,
    partner_apps_url: str = DEFAULT_PARTNER_APPS_URL,
    app_search_name: str = "",
    app_card_id: str = "",
    app_slug: str = "",
    plan_name: str = "",
    timeout_seconds: int = 900,
    **kwargs: Any,
) -> NewCarrierOnboardingResult:
    """Compatibility entry point for the dashboard's onboarding button.

    There is no WooCommerce equivalent of "create a dev store and install the
    app": the site already exists and the plugin is installed through WordPress.
    So this runs :func:`prepare_site_for_carrier` against `store_name` — treated
    as a site URL — and reports what it found.

    The Shopify-only arguments are accepted and ignored so existing call sites
    do not break.
    """
    if not store_name.strip():
        raise ValueError("A site URL is required")
    return prepare_site_for_carrier(site_url=store_name.strip(), **kwargs)


@dataclass(frozen=True)
class DevAppTokenResult:
    store_name: str
    app_name: str
    app_id: str
    admin_token: str
    storefront_token: str
    granted_admin_scopes: tuple[str, ...]
    requested_admin_scopes: tuple[str, ...]
    missing_admin_scopes: tuple[str, ...]
    app_created: bool
    app_installed: bool
    token_revealed: bool
    stdout: str
    stderr: str
    returncode: int
    started_at: float
    finished_at: float

    @property
    def duration_seconds(self) -> float:
        return max(0.0, self.finished_at - self.started_at)


DEFAULT_DEV_APP_NAME = "WooCommerce QA REST key"
DEFAULT_ADMIN_SCOPES: tuple[str, ...] = ("read_write",)
DEFAULT_STOREFRONT_SCOPES: tuple[str, ...] = ()


def create_dev_app_and_reveal_token(
    *,
    store_name: str,
    app_name: str = DEFAULT_DEV_APP_NAME,
    admin_scopes: tuple[str, ...] | list[str] = DEFAULT_ADMIN_SCOPES,
    storefront_scopes: tuple[str, ...] | list[str] = DEFAULT_STOREFRONT_SCOPES,
    timeout_seconds: int = 900,
) -> DevAppTokenResult:
    """WooCommerce REST keys are generated by a human in wp-admin.

    WooCommerce > Settings > Advanced > REST API > Add key, with **Read/Write**
    permission. The consumer secret is shown once and cannot be retrieved
    afterwards, and there is no API to create a key — the endpoint that would do
    it is itself authenticated by a key.

    This returns a result describing the manual step rather than pretending to
    automate it. Put the values in `.env` as `WOO_CONSUMER_KEY` /
    `WOO_CONSUMER_SECRET`, or in `carrier-envs/<carrier>.env` as
    `CONSUMER_KEY` / `CONSUMER_SECRET`.
    """
    started = time.time()
    site = (store_name or config.WOO_SITE_URL or "").rstrip("/")
    keys_url = f"{site}/wp-admin/admin.php?page=wc-settings&tab=advanced&section=keys"
    message = (
        "WooCommerce REST API keys cannot be created programmatically.\n"
        f"Create one at: {keys_url}\n"
        "  - Description: " + app_name + "\n"
        "  - User: an administrator\n"
        "  - Permissions: Read/Write\n"
        "The consumer secret is shown once. Copy both values into .env as "
        "WOO_CONSUMER_KEY and WOO_CONSUMER_SECRET."
    )
    return DevAppTokenResult(
        store_name=site,
        app_name=app_name,
        app_id="",
        admin_token="",
        storefront_token="",
        granted_admin_scopes=(),
        requested_admin_scopes=tuple(admin_scopes),
        missing_admin_scopes=tuple(admin_scopes),
        app_created=False,
        app_installed=False,
        token_revealed=False,
        stdout=message,
        stderr="Manual step — no API available.",
        returncode=1,
        started_at=started,
        finished_at=time.time(),
    )
