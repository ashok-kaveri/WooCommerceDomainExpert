"""
WordPress / WooCommerce admin URL builders.

MCSLDomainExpert built Shopify admin URLs of the form
`https://admin.shopify.com/store/<slug>/apps/<app>`. WooCommerce has no such
per-store admin host: the store *is* the WordPress site, and the plugin
settings live under `/wp-admin/`. Everything that needs an admin link builds
it here so the paths stay in one place.

Paths verified against:
- ups-woo-automation/src/pages/wooCommerceAdmin/*.ts
- multi-carrier-shipping-plugin-for-woocommerce/.../class-ph-multi-carrier-admin-menu.php
"""
from __future__ import annotations

from urllib.parse import urlencode

import config

# Plugin menu slug registered by the Multi-Carrier plugin
MULTI_CARRIER_MENU = "ph_multi_carrier_admin_menu"

# Carrier registration submenu slugs, keyed by carrier code
CARRIER_REGISTRATION_SLUGS = {
    "fedex": "ph_multi_carrier_fedex_registration",
    "ups": "ph_multi_carrier_ups_registration",
    "usps": "ph_multi_carrier_usps_rest_registration",
}


def site_url(site: str | None = None) -> str:
    """Normalised site origin, no trailing slash."""
    return (site or config.WOO_SITE_URL or "").rstrip("/")


def admin_url(path: str = "", site: str | None = None, **params: str) -> str:
    """
    Build a /wp-admin URL.

    admin_url()                                   -> <site>/wp-admin/
    admin_url("admin.php", page="wc-orders")      -> <site>/wp-admin/admin.php?page=wc-orders
    admin_url("plugins.php")                      -> <site>/wp-admin/plugins.php
    """
    base = f"{site_url(site)}/wp-admin/{path.lstrip('/')}"
    return f"{base}?{urlencode(params)}" if params else base


def dashboard_url(site: str | None = None) -> str:
    return admin_url(site=site)


def plugins_url(site: str | None = None) -> str:
    return admin_url("plugins.php", site=site)


def orders_url(site: str | None = None) -> str:
    return admin_url("admin.php", site=site, page="wc-orders")


def order_url(order_id: int | str, site: str | None = None) -> str:
    return admin_url("admin.php", site=site, page="wc-orders", action="edit", id=str(order_id))


def products_url(site: str | None = None) -> str:
    return f"{site_url(site)}/wp-admin/edit.php?post_type=product"


def status_url(site: str | None = None) -> str:
    return admin_url("admin.php", site=site, page="wc-status")


def shipping_settings_url(section: str = "", site: str | None = None) -> str:
    params = {"page": "wc-settings", "tab": "shipping"}
    if section:
        params["section"] = section
    return admin_url("admin.php", site=site, **params)


def plugin_settings_url(site: str | None = None) -> str:
    """The Multi-Carrier plugin's own settings screen."""
    return admin_url("admin.php", site=site, page=MULTI_CARRIER_MENU)


def carrier_registration_url(carrier_code: str, site: str | None = None) -> str:
    """
    Carrier registration screen for a carrier code. Unknown carriers fall back
    to the plugin's main menu rather than inventing a slug.
    """
    slug = CARRIER_REGISTRATION_SLUGS.get(carrier_code.strip().lower())
    return admin_url("admin.php", site=site, page=slug or MULTI_CARRIER_MENU)


# Backwards-compatible alias — older call sites asked for an "app url".
# In WooCommerce that is the plugin settings screen.
def app_url(site: str | None = None) -> str:
    return plugin_settings_url(site)
