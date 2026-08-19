"""
Woo Order Creator
=================
Creates test WooCommerce orders for use by the AI QA Agent.

Product IDs come from carrier-env files (SIMPLE_PRODUCTS_JSON,
VARIABLE_PRODUCTS_JSON, DIGITAL_PRODUCTS_JSON, DANGEROUS_PRODUCTS_JSON),
written by `pipeline.woo_product_seed`. Each carrier has its own env file in
`ups-woo-automation/carrier-envs/`.

Orders are created through the WooCommerce REST API (`wc/v3/orders`) with
`set_paid: true`, which is the Woo equivalent of WooCommerce's
`financial_status: paid` — the order lands in Processing so shipping-label
flows can act on it.
"""
from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

from dotenv import dotenv_values

import config
from pipeline.carrier_knowledge import get_carrier_env_path
from pipeline.woo_api import WooClient, WooCredentials

logger = logging.getLogger(__name__)

# Default carrier-env path (falls back to the automation repo root .env)
_CARRIER_ENV_DIR = Path(config.WOO_AUTOMATION_REPO_PATH) / "carrier-envs"


def _read_carrier_env(carrier_env_path: str | Path) -> dict[str, str]:
    """Read a carrier-env file and return its key-value pairs."""
    path = Path(carrier_env_path)
    if not path.exists():
        raise FileNotFoundError(f"Carrier env file not found: {path}")
    return {k: v for k, v in dotenv_values(str(path)).items() if v is not None}


def _get_carrier_env_path(carrier_code: str) -> Path:
    """Return the carrier-env file path for a given carrier code."""
    return get_carrier_env_path(carrier_code)


def _default_address() -> dict[str, Any]:
    """Default test shipping address for order creation (WooCommerce shape)."""
    return {
        "first_name": "Test",
        "last_name": "Customer",
        "address_1": "123 Main Street",
        "city": "Chicago",
        "state": "IL",
        "postcode": "60601",
        "country": "US",
        "phone": "555-555-5555",
        "email": "qa+woo@pluginhive.com",
    }


def _build_line_items(
    env_data: dict[str, str],
    use_dangerous: bool = False,
    product_count: int = 1,
) -> list[dict]:
    """Build WooCommerce line_items from carrier-env product JSON.

    product_count > 1 creates an order with multiple distinct products so
    the plugin's box-packing splits it into multiple packages.
    """
    key = "DANGEROUS_PRODUCTS_JSON" if use_dangerous else "SIMPLE_PRODUCTS_JSON"
    raw = env_data.get(key, "")
    if not raw:
        raw = env_data.get("SIMPLE_PRODUCTS_JSON", "[]")

    products = json.loads(raw)
    if not products:
        raise ValueError(f"No products found in carrier-env {key}")

    line_items = []
    for product in products[: max(1, product_count)]:
        item: dict[str, Any] = {"product_id": int(product["product_id"]), "quantity": 1}
        if product.get("variation_id"):
            item["variation_id"] = int(product["variation_id"])
        line_items.append(item)
    return line_items


def _client_for_env(env: dict[str, str]) -> WooClient:
    return WooClient(WooCredentials.from_env_mapping(env))


def _order_reference(order: dict[str, Any]) -> str:
    """Prefer the human-facing order number, fall back to the numeric id."""
    return str(order.get("number") or order.get("id"))


def _create(
    env: dict[str, str],
    line_items: list[dict],
    address: dict[str, Any],
) -> dict[str, Any]:
    payload = {
        "payment_method": "cod",
        "payment_method_title": "QA Test Order",
        "set_paid": True,
        "status": "processing",
        "billing": address,
        "shipping": {k: v for k, v in address.items() if k != "email"},
        "line_items": line_items,
    }
    return _client_for_env(env).create_order(payload)


def create_order(
    carrier_env_path: str | Path,
    address_override: dict | None = None,
    use_dangerous_products: bool = False,
) -> str:
    """
    Create a single test WooCommerce order.

    Returns the WooCommerce order number as a string.
    Raises WooApiError on API failure.
    """
    env = _read_carrier_env(carrier_env_path)
    line_items = _build_line_items(env, use_dangerous=use_dangerous_products, product_count=1)
    order = _create(env, line_items, address_override or _default_address())
    reference = _order_reference(order)
    logger.info("Created WooCommerce order: %s", reference)
    return reference


def _automation_root_env() -> Path:
    """Return the root .env path for the ups-woo-automation repo."""
    return Path(config.WOO_AUTOMATION_REPO_PATH) / ".env"


def create_order_multi_package(
    carrier_env_path: str | Path | None = None,
    num_packages: int = 2,
    address_override: dict | None = None,
) -> str:
    """Create a single WooCommerce order with multiple line items so the
    plugin's packing splits it into multiple packages (one per distinct
    product).

    Falls back to the automation repo root .env when no carrier-specific env
    is available (e.g. the carrier-envs/ directory is absent).

    Returns the WooCommerce order number as a string.
    """
    env_path = Path(carrier_env_path) if carrier_env_path else None
    if not env_path or not env_path.exists():
        env_path = _automation_root_env()
    env = _read_carrier_env(env_path)

    line_items = _build_line_items(env, use_dangerous=False, product_count=max(2, num_packages))
    order = _create(env, line_items, address_override or _default_address())
    reference = _order_reference(order)
    logger.info("Created multi-package order %s with %d line items", reference, len(line_items))
    return reference


def create_bulk_orders(
    carrier_env_path: str | Path,
    count: int = 3,
    address_override: dict | None = None,
    use_dangerous_products: bool = False,
) -> list[str]:
    """
    Create N test WooCommerce orders.

    Returns list of order number strings.
    """
    order_ids = []
    for i in range(count):
        try:
            oid = create_order(
                carrier_env_path,
                address_override=address_override,
                use_dangerous_products=use_dangerous_products,
            )
            order_ids.append(oid)
            logger.info("Bulk order %d/%d: %s", i + 1, count, oid)
        except Exception as e:
            logger.error("Failed to create bulk order %d/%d: %s", i + 1, count, e)
            raise
    return order_ids


def get_carrier_env_for_code(carrier_code: str) -> Path:
    """Public helper: return the env file path for a carrier code string."""
    return _get_carrier_env_path(carrier_code)
