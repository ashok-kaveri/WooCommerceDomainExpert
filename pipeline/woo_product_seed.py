"""Deterministic WooCommerce product creation for new-carrier validation.

This mirrors `ensureStoreProducts()` in
`ups-woo-automation/src/api/controllers/productSetupController.ts`, so the
products this module creates are the ones the Playwright suite expects to find.

Groups created:

- simple
- variable (with a Colour/Size variation)
- digital  (virtual + downloadable)
- dangerous (only when the carrier flow needs hazardous-goods coverage)

Seeding is **find-or-create by product name**, so running it twice against the
same store reuses the existing products instead of duplicating the catalogue.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any

from pipeline.woo_api import WooApiError, WooClient, WooCredentials

logger = logging.getLogger(__name__)

DEFAULT_SPECS = {
    "price": "10.00",
    "weight": "1",
    "length": "5",
    "width": "5",
    "height": "5",
}


@dataclass(frozen=True)
class ProductSeedSpec:
    group: str
    name: str
    description: str
    product_type: str = "simple"
    virtual: bool = False
    downloadable: bool = False
    price: str = DEFAULT_SPECS["price"]
    weight: str = DEFAULT_SPECS["weight"]
    attributes: list[dict[str, Any]] = field(default_factory=list)
    meta_data: list[dict[str, Any]] = field(default_factory=list)


@dataclass(frozen=True)
class ProductSeedResult:
    group: str
    product_id: int
    variation_id: int | None
    name: str
    created: bool


def _dimensions() -> dict[str, str]:
    return {
        "length": DEFAULT_SPECS["length"],
        "width": DEFAULT_SPECS["width"],
        "height": DEFAULT_SPECS["height"],
    }


def _seed_specs(carrier_code: str, *, include_dangerous: bool = True) -> list[ProductSeedSpec]:
    """
    Names deliberately match the automation repo's STANDARD_PRODUCTS so both
    tools converge on the same catalogue. The carrier code only tags the
    carrier-specific dangerous-goods product.
    """
    prefix = carrier_code.strip() or "new-carrier"
    specs = [
        ProductSeedSpec(group="simple", name="1. Simple Product",
                        description="Standard test product: 1. Simple Product"),
        ProductSeedSpec(group="simple", name="2. Simple Product",
                        description="Standard test product: 2. Simple Product"),
        ProductSeedSpec(group="variable", name="1. Variable Product",
                        description="Standard test product: 1. Variable Product",
                        product_type="variable",
                        attributes=[
                            {"position": 0, "name": "Colour", "options": ["Black", "Green"],
                             "variation": True, "visible": True},
                            {"position": 1, "name": "Size", "options": ["S", "M"],
                             "variation": True, "visible": True},
                        ]),
        ProductSeedSpec(group="variable", name="2. Variable Product",
                        description="Standard test product: 2. Variable Product",
                        product_type="variable",
                        attributes=[
                            {"position": 0, "name": "Colour", "options": ["Black", "Green"],
                             "variation": True, "visible": True},
                            {"position": 1, "name": "Size", "options": ["S", "M"],
                             "variation": True, "visible": True},
                        ]),
        ProductSeedSpec(group="digital", name="1. Digital Product",
                        description="Standard test product: 1. Digital Product",
                        virtual=True, downloadable=True),
        ProductSeedSpec(group="digital", name="2. Digital Product",
                        description="Standard test product: 2. Digital Product",
                        virtual=True, downloadable=True),
    ]
    if include_dangerous:
        specs.append(
            ProductSeedSpec(
                group="dangerous",
                name=f"{prefix} Dangerous Goods Product",
                description=f"Hazardous-goods product for {prefix} carrier scenarios.",
                price="129.99",
                # PluginHive shipping plugins read hazmat flags off product meta.
                meta_data=[{"key": "_ph_dangerous_goods", "value": "yes"}],
            )
        )
    return specs


def _slugify(name: str) -> str:
    return "".join(ch if ch.isalnum() else "-" for ch in name).strip("-").lower()


def _build_payload(spec: ProductSeedSpec) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "name": spec.name,
        "type": spec.product_type,
        "status": "publish",
        "description": spec.description,
        "sku": _slugify(spec.name),
    }
    if spec.product_type == "variable":
        payload["attributes"] = spec.attributes
    else:
        payload.update({
            "regular_price": spec.price,
            "weight": spec.weight,
            "dimensions": _dimensions(),
            "manage_stock": True,
            "stock_quantity": 99999,
        })
        if spec.virtual:
            payload["virtual"] = True
        if spec.downloadable:
            payload["downloadable"] = True
    if spec.meta_data:
        payload["meta_data"] = spec.meta_data
    return payload


def _default_variation_payload() -> dict[str, Any]:
    return {
        "status": "publish",
        "regular_price": DEFAULT_SPECS["price"],
        "description": "Default variant",
        "weight": DEFAULT_SPECS["weight"],
        "dimensions": _dimensions(),
        "manage_stock": True,
        "stock_quantity": 99999,
        "attributes": [
            {"name": "Colour", "option": "Black"},
            {"name": "Size", "option": "S"},
        ],
    }


def _find_by_name(client: WooClient, name: str) -> dict[str, Any] | None:
    for product in client.search_products(name):
        if str(product.get("name", "")).strip() == name:
            return product
    return None


def create_seed_products(
    *,
    carrier_code: str,
    credentials: WooCredentials | None = None,
    client: WooClient | None = None,
    include_dangerous: bool = True,
    timeout_seconds: int = 30,
) -> dict[str, list[ProductSeedResult]]:
    """
    Ensure the deterministic seed catalogue exists on the WooCommerce store.

    Idempotent: existing products with the same name are reused, so this is
    safe to call before every carrier run.
    """
    woo = client or WooClient(credentials, timeout=timeout_seconds)
    results: dict[str, list[ProductSeedResult]] = {
        "simple": [], "variable": [], "digital": [], "dangerous": [],
    }

    for spec in _seed_specs(carrier_code, include_dangerous=include_dangerous):
        existing = _find_by_name(woo, spec.name)
        if existing:
            product, created = existing, False
            logger.info("Reusing product %s (id=%s)", spec.name, product.get("id"))
        else:
            product = woo.create_product(_build_payload(spec))
            created = True
            logger.info("Created product %s (id=%s)", spec.name, product.get("id"))

        product_id = product.get("id")
        if not product_id:
            raise WooApiError(f"WooCommerce product response missing id for {spec.name}")
        product_id = int(product_id)

        variation_id: int | None = None
        if spec.product_type == "variable":
            variations = woo.list_variations(product_id)
            if not variations:
                variations = [woo.create_variation(product_id, _default_variation_payload())]
            variation_id = int(variations[0]["id"])

        results[spec.group].append(
            ProductSeedResult(
                group=spec.group,
                product_id=product_id,
                variation_id=variation_id,
                name=str(product.get("name") or spec.name),
                created=created,
            )
        )

    return results


def seed_results_to_env(results: dict[str, list[ProductSeedResult]]) -> dict[str, str]:
    """
    Render seed results as the *_PRODUCTS_JSON env values the carrier-env
    files and the automation repo consume.
    """
    import json

    env: dict[str, str] = {}
    for group, key in (
        ("simple", "SIMPLE_PRODUCTS_JSON"),
        ("variable", "VARIABLE_PRODUCTS_JSON"),
        ("digital", "DIGITAL_PRODUCTS_JSON"),
        ("dangerous", "DANGEROUS_PRODUCTS_JSON"),
    ):
        env[key] = json.dumps([
            {"product_id": r.product_id, "variation_id": r.variation_id, "name": r.name}
            for r in results.get(group, [])
        ])
    return env
