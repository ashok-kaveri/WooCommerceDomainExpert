---
name: woo-store-actions
description: Use when the user wants to perform any WooCommerce REST API action on a PluginHive QA WordPress/WooCommerce site — create/update/delete products (simple, variable with variations, virtual/downloadable), create/cancel/delete/update orders (preset, custom, with any status), batch create/update/delete, manage stock, shipping zones and methods, coupons, customers, refunds, order notes, read system status and active plugin versions, seed the deterministic QA catalogue, write a carrier-env file for the automation repo, or drive a new-carrier setup end to end. Credentials come from this repo's .env (WOO_SITE_URL / WOO_CONSUMER_KEY / WOO_CONSUMER_SECRET) or from ups-woo-automation/.env and carrier-envs/<carrier>.env automatically; if a site is not found there, asks for credentials.
---

# WooCommerce Store Actions (Woo)

Use this skill when the user asks to do anything with a WooCommerce store via the
WooCommerce REST API for PluginHive's WooCommerce shipping plugins:

**Products**
- "create 3 products" / "create a variable product with Colour and Size"
- "list all products and give me the IDs"
- "delete the product called Red Shirt"
- "set the product to draft" / "publish it again"
- "update variation weight to 2.5kg" / "change the price of size M to ₹250"
- "change the SKU" / "set dimensions on Red Shirt"
- "allow backorders on this product" / "stop selling when out of stock"
- "mark this product as virtual / downloadable — no shipping required"
- "set the sale price" / "remove the sale price"
- "batch update these 20 products in one call"
- "seed the standard QA catalogue on this site"

**Orders**
- "create a test order" / "create an order that is already paid"
- "create an order for Ravi Kumar at MG Road Bengaluru"
- "create an order with the dangerous-goods product"
- "create a multi-package order so the plugin splits it"
- "cancel order 1801" / "delete all the QA test orders"
- "update the shipping address on order 1802"
- "list all processing orders" / "how many open orders are there?"
- "add an order note" / "read the shipment tracking meta on this order"
- "create an order on the India Post carrier-env"

**Stock**
- "set stock of Red Shirt to 9999" / "add 50 stock to Red Shirt"
- "set stock on every variation of this product"

**Shipping & plugin state**
- "list the shipping zones" / "what methods are on the US zone?"
- "add the Multi-Carrier method to the Rest of the World zone"
- "which PluginHive plugins are active, and at what version?"
- "what WooCommerce and WordPress version is this site on?"
- "check the plugin's settings page" / "give me the admin URL for UPS registration"

**Setup & validation**
- "set up this site for new-carrier validation"
- "seed products and write the carrier-env file"
- "onboard a new carrier end-to-end"
- "smoke test by creating one order through the new env"

---

## Store & Auth Resolution

WooCommerce authentication is **consumer key + consumer secret**, sent as HTTP
Basic auth over HTTPS. There is no per-store admin host: the store *is* the
WordPress site, so `WOO_SITE_URL` fully identifies it.

### Logic (4 checks, in order)

```
1. No site mentioned by user
   → use WOO_SITE_URL / WOO_CONSUMER_KEY / WOO_CONSUMER_SECRET from this repo's .env
   → no questions asked

2. User mentions a carrier by name ("india post", "blue dart", "fedex", "dhl")
   → use carrier-envs/<carrier>.env from the automation repo
   → that file may carry its own site_url / CONSUMER_KEY / CONSUMER_SECRET plus
     the seeded product JSONs (SIMPLE_PRODUCTS_JSON, VARIABLE_PRODUCTS_JSON,
     DIGITAL_PRODUCTS_JSON, DANGEROUS_PRODUCTS_JSON)

3. User mentions a site URL or host
   → normalise it (add https://, strip trailing slash and /wp-admin)
   → match it against the site_url in the root .env and every carrier-env
       match    → use those credentials
       no match → STOP and say: "I need a consumer key and secret for <site>"

4. User supplies explicit credentials
   → use exactly what they gave, skip env lookup
```

Never invent credentials, and never fall back to the default site when the user
named a different one — say what is missing instead.

### Implementation

```python
import sys
from pathlib import Path

REPO = Path.cwd()          # WooCommerceDomainExpert
sys.path.insert(0, str(REPO))

import config
from pipeline.woo_api import WooClient, WooCredentials, WooApiError


def _read_env_file(path: Path) -> dict:
    env = {}
    if path and path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                k, _, v = line.partition("=")
                env[k.strip()] = v.strip().strip("'\"")
    return env


_automation_root = Path((config.WOO_AUTOMATION_REPO_PATH or "").strip())
_root_env        = _read_env_file(_automation_root / ".env")
_carrier_env_dir = _automation_root / "carrier-envs"

_CARRIER_KEYWORDS = {
    "india post": "indiapost", "indiapost": "indiapost",
    "blue dart": "blue-dart",  "bluedart": "blue-dart",
    "fedex": "fedex", "ups": "ups", "usps": "usps", "dhl": "dhl",
    "canada post": "canadapost", "canadapost": "canadapost",
    "australia post": "auspost", "auspost": "auspost",
    "royal mail": "royalmail",  "royalmail": "royalmail",
    "aramex": "aramex", "postnord": "postnord", "purolator": "purolator",
}


def resolve_client(user_text: str = "", explicit: dict | None = None) -> WooClient:
    """Return a WooClient for whichever store the user meant."""
    if explicit:
        return WooClient(WooCredentials.from_env_mapping(explicit))

    text = (user_text or "").lower()
    for keyword, slug in _CARRIER_KEYWORDS.items():
        if keyword in text:
            env = _read_env_file(_carrier_env_dir / f"{slug}.env")
            if env:
                return WooClient(WooCredentials.from_env_mapping(env))

    # Repo .env first, automation root .env as a fallback
    try:
        return WooClient(WooCredentials.from_config())
    except WooApiError:
        return WooClient(WooCredentials.from_env_mapping(_root_env))
```

### Connection check — always run before the first write

```python
woo = resolve_client()
status = woo.get_system_status()
env = status.get("environment", {})
print("Site        :", env.get("site_url"))
print("WordPress   :", env.get("wp_version"))
print("WooCommerce :", env.get("version"))
print("PHP         :", env.get("php_version"))

for plugin in woo.active_plugins():
    if "pluginhive" in (plugin.get("author_name") or "").lower() \
       or "ph " in (plugin.get("name") or "").lower():
        print(f"  {plugin['name']} — {plugin['version']}")
```

### What to say to the user in each case

| Situation | What to say |
|---|---|
| 401 / `woocommerce_rest_authentication_error` | "The consumer key/secret was rejected. Regenerate it under WooCommerce → Settings → Advanced → REST API with **Read/Write** permission." |
| 401 only on writes | "The key is Read-only. It needs Read/Write for this action." |
| 404 on `/wp-json/` | "The REST API isn't reachable — permalinks may be set to Plain, or a security plugin is blocking `/wp-json/`." |
| Site not in any env | "I don't have credentials for `<site>`. Give me a consumer key and secret, or tell me which carrier-env it lives in." |
| HTTP, not HTTPS | "Basic auth only works over HTTPS. Over HTTP the key must go in the query string, which I won't do — use the HTTPS URL." |

---

## The API surface

Base URL is `<site>/wp-json/wc/v3/`. Everything below goes through `WooClient`,
which handles auth, timeouts, and error wrapping.

| Resource | Endpoint |
|---|---|
| Products | `products`, `products/<id>`, `products/batch` |
| Variations | `products/<id>/variations`, `.../variations/batch` |
| Orders | `orders`, `orders/<id>`, `orders/batch` |
| Order notes | `orders/<id>/notes` |
| Refunds | `orders/<id>/refunds` |
| Customers | `customers`, `customers/<id>` |
| Coupons | `coupons` |
| Shipping zones | `shipping/zones`, `shipping/zones/<id>/methods`, `.../locations` |
| Shipping classes | `products/shipping_classes` |
| Settings | `settings`, `settings/<group>`, `settings/<group>/<id>` |
| System status | `system_status` |
| Reports | `reports/orders/totals`, `reports/products/totals` |

---

## Product Actions

### 1. List Products

```python
woo = resolve_client()
for p in woo.get("products", {"per_page": 50, "status": "any"}):
    print(p["id"], "|", p["name"], "|", p["type"], "|", p.get("price"), "|", p["status"])
```

Useful filters: `search`, `sku`, `type` (`simple|variable|grouped|external`),
`status` (`any|draft|publish`), `stock_status`, `category`, `per_page` (max 100),
`page`.

### 2. Create a Simple Product

```python
product = woo.create_product({
    "name": "QA Simple Product",
    "type": "simple",
    "status": "publish",
    "regular_price": "10.00",
    "description": "Created for QA.",
    "sku": "qa-simple-1",
    "weight": "1",
    "dimensions": {"length": "5", "width": "5", "height": "5"},
    "manage_stock": True,
    "stock_quantity": 99999,
})
print(product["id"], product["permalink"])
```

### 3. Create a Virtual / Downloadable Product

Virtual products are the WooCommerce equivalent of a Shopify "no shipping
required" variant — they are excluded from shipping-rate calculation, which
matters for mixed-cart test cases.

```python
woo.create_product({
    "name": "QA Digital Product",
    "type": "simple",
    "status": "publish",
    "regular_price": "9.99",
    "virtual": True,
    "downloadable": True,
    "sku": "qa-digital-1",
})
```

### 4. Create a Variable Product with Variations

Two steps: create the parent with `attributes` marked `variation: true`, then
create each variation.

```python
parent = woo.create_product({
    "name": "QA Variable Product",
    "type": "variable",
    "status": "publish",
    "attributes": [
        {"position": 0, "name": "Colour", "options": ["Black", "Green"],
         "variation": True, "visible": True},
        {"position": 1, "name": "Size", "options": ["S", "M"],
         "variation": True, "visible": True},
    ],
})

for colour in ("Black", "Green"):
    for size in ("S", "M"):
        woo.create_variation(parent["id"], {
            "status": "publish",
            "regular_price": "10.00",
            "sku": f"qa-var-{colour}-{size}".lower(),
            "weight": "1",
            "dimensions": {"length": "5", "width": "5", "height": "5"},
            "manage_stock": True,
            "stock_quantity": 99999,
            "attributes": [{"name": "Colour", "option": colour},
                           {"name": "Size", "option": size}],
        })
```

For many variations, use the batch endpoint instead of a loop:

```python
woo.post(f"products/{parent['id']}/variations/batch", {"create": payloads})
```

Batch accepts up to 100 items per call — chunk anything larger.

### 5. Update a Product — Any Field

```python
woo.put(f"products/{product_id}", {
    "regular_price": "199.00",
    "sale_price": "149.00",          # "" clears the sale price
    "weight": "2.5",
    "dimensions": {"length": "20", "width": "15", "height": "10"},
    "shipping_class": "heavy",
    "backorders": "notify",          # "no" | "notify" | "yes"
    "stock_status": "instock",       # "instock" | "outofstock" | "onbackorder"
    "status": "draft",               # "draft" | "publish" | "private"
    "meta_data": [{"key": "_ph_dangerous_goods", "value": "yes"}],
})
```

### 6. Update One Variation

```python
woo.put(f"products/{parent_id}/variations/{variation_id}",
        {"regular_price": "250.00", "weight": "2.5"})
```

### 7. Delete a Product by Name

```python
matches = [p for p in woo.search_products("Red Shirt") if p["name"] == "Red Shirt"]
if not matches:
    print("No exact match — not deleting anything.")
else:
    for p in matches:
        woo.delete(f"products/{p['id']}", force=True)   # force=True skips the trash
        print("deleted", p["id"], p["name"])
```

Always confirm an exact name match before deleting. `force=False` moves the
product to trash instead, which is the safer default when the user is unsure.

### 8. Batch Create / Update / Delete

```python
woo.post("products/batch", {
    "create": [{"name": "A", "type": "simple", "regular_price": "5"}],
    "update": [{"id": 123, "regular_price": "7"}],
    "delete": [456, 789],
})
```

### 9. Set Stock

```python
# Simple product
woo.put(f"products/{pid}", {"manage_stock": True, "stock_quantity": 9999})

# Every variation of a variable product
for v in woo.list_variations(parent_id):
    woo.put(f"products/{parent_id}/variations/{v['id']}",
            {"manage_stock": True, "stock_quantity": 500})
```

WooCommerce has no `BYPASS_STOCK` flag the way Shopify does. To keep test orders
from draining inventory, seed with `stock_quantity: 99999`, or set
`manage_stock: False` on QA products.

### 10. Seed the Deterministic QA Catalogue

Prefer this over hand-rolling products — it creates exactly the catalogue the
Playwright suite expects, and it is find-or-create, so re-running is safe.

```python
from pipeline.woo_product_seed import create_seed_products, seed_results_to_env

results = create_seed_products(carrier_code="ups", client=woo)
for group, items in results.items():
    for r in items:
        print(f"{group:10} {r.product_id:>6}  {'new' if r.created else 'reused'}  {r.name}")

env_values = seed_results_to_env(results)   # *_PRODUCTS_JSON for the carrier-env
```

---

## Order Actions

### 11. Create a Test Order

```python
address = {
    "first_name": "Test", "last_name": "Customer",
    "address_1": "123 Main Street", "city": "Chicago",
    "state": "IL", "postcode": "60601", "country": "US",
    "phone": "555-555-5555", "email": "qa+woo@pluginhive.com",
}

order = woo.create_order({
    "payment_method": "cod",
    "payment_method_title": "QA Test Order",
    "set_paid": True,               # lands the order in Processing
    "status": "processing",
    "billing": address,
    "shipping": {k: v for k, v in address.items() if k != "email"},
    "line_items": [{"product_id": 123, "quantity": 1}],
})
print(order["id"], order["number"], order["status"])
```

For a variable product, include `variation_id` alongside `product_id`.

### 12. Create an Order Through a Carrier Env (project helper)

```bash
# Single order via a specific carrier env
python3 -c "
from pipeline.order_creator import create_order, get_carrier_env_for_code
print(create_order(get_carrier_env_for_code('ups')))
"
```

```bash
# Dangerous-goods order
python3 -c "
from pipeline.order_creator import create_order, get_carrier_env_for_code
print(create_order(get_carrier_env_for_code('ups'), use_dangerous_products=True))
"
```

```bash
# Multi-package order (multiple distinct products so packing splits it)
python3 -c "
from pipeline.order_creator import create_order_multi_package
print(create_order_multi_package(num_packages=3))
"
```

### 13. Create an Order with a Chosen Shipping Line

To pin a specific carrier rate on an order without going through checkout:

```python
woo.create_order({
    "set_paid": True,
    "status": "processing",
    "billing": address,
    "shipping": {k: v for k, v in address.items() if k != "email"},
    "line_items": [{"product_id": 123, "quantity": 1}],
    "shipping_lines": [{
        "method_id": "ph_multicarrier",
        "method_title": "UPS Ground",
        "total": "12.50",
    }],
})
```

### 14. List / Filter Orders

```python
for o in woo.list_orders({"status": "processing", "per_page": 50}):
    print(o["id"], o["number"], o["status"], o["total"], o["date_created"])
```

Filters: `status`, `customer`, `after`, `before`, `search`, `product`,
`per_page`, `page`.

### 15. Update, Cancel, Delete an Order

```python
woo.update_order(order_id, {"status": "cancelled"})
woo.update_order(order_id, {"shipping": {**address, "city": "Boston", "postcode": "02108"}})
woo.delete(f"orders/{order_id}", force=True)     # permanent; force=False → trash
```

### 16. Bulk Clean Up QA Orders

```python
victims = [o["id"] for o in woo.list_orders({"search": "qa+woo@pluginhive.com", "per_page": 100})]
print("about to delete", len(victims), "orders")     # confirm with the user first
woo.post("orders/batch", {"delete": victims})
```

Deleting orders is irreversible with `force=True`. State the count and get a
clear yes before running it.

### 17. Order Notes and Plugin Meta

Shipment tracking and label data written by PluginHive plugins live in order
meta and order notes — this is where label-generation evidence comes from.

```python
order = woo.get_order(order_id)
for meta in order.get("meta_data", []):
    if str(meta.get("key", "")).startswith("_ph"):
        print(meta["key"], "=", meta["value"])

for note in woo.get(f"orders/{order_id}/notes"):
    print(note["date_created"], note["note"])

woo.post(f"orders/{order_id}/notes", {"note": "QA: label generated", "customer_note": False})
```

### 18. Refunds

```python
woo.post(f"orders/{order_id}/refunds", {"amount": "10.00", "reason": "QA test refund"})
```

---

## Shipping & Plugin State

### 19. Shipping Zones and Methods

```python
for zone in woo.list_shipping_zones():
    print(zone["id"], zone["name"])
    for m in woo.list_zone_methods(zone["id"]):
        print("   ", m["method_id"], "|", m["method_title"], "| enabled:", m["enabled"])
```

Add the Multi-Carrier method to a zone:

```python
woo.post(f"shipping/zones/{zone_id}/methods", {"method_id": "ph_multicarrier"})
```

Zone `0` is "Locations not covered by your other zones" (Rest of the World).

### 20. Which PluginHive Plugins Are Active, and at What Version

This is the single most useful call for release triage — it answers "is the
build actually deployed on the QA site?"

```python
for p in woo.active_plugins():
    print(f"{p['name']:55} {p['version']}")
```

### 21. Admin URLs

```python
from pipeline import woo_admin

woo_admin.dashboard_url()                      # <site>/wp-admin/
woo_admin.orders_url()                         # WooCommerce orders list
woo_admin.order_url(1234)                      # single order edit screen
woo_admin.products_url()                       # products list
woo_admin.status_url()                         # WooCommerce → Status
woo_admin.shipping_settings_url()              # WooCommerce → Settings → Shipping
woo_admin.plugin_settings_url()                # Multi Carrier plugin menu
woo_admin.carrier_registration_url("ups")      # UPS registration screen
```

Registration screen slugs come from the plugin's own admin menu
(`ph_multi_carrier_<carrier>_registration`).

---

## New-Carrier Setup, End to End

WooCommerce has no app-install OAuth flow. The plugin is installed on the site
once, and each carrier is registered by hand inside wp-admin. So the pipeline is
shorter than the MCSL one, and it has one mandatory manual stop.

```
Phase 1  Confirm the site is reachable and the plugin is active   (API)
Phase 2  STOP — user registers the carrier in wp-admin            (manual)
Phase 3  Seed the deterministic QA catalogue                      (API)
Phase 4  Write carrier-envs/<carrier>.env for the automation repo (file)
Phase 5  Smoke-test by creating one order through that env        (API)
Phase 6  Report readiness                                          (summary)
```

```python
from pathlib import Path
import config
from pipeline.woo_product_seed import create_seed_products, seed_results_to_env
from pipeline.order_creator import create_order
from pipeline import woo_admin

carrier = "ups"
woo = resolve_client()

# ── Phase 1 ────────────────────────────────────────────────────────
plugins = {p["name"]: p["version"] for p in woo.active_plugins()}
print("Active PluginHive plugins:", {k: v for k, v in plugins.items() if "PH " in k or "PluginHive" in k})

# ── Phase 2 — STOP. Do not try to automate this. ───────────────────
print(f"Register {carrier} here, then tell me when it's saved:")
print("  ", woo_admin.carrier_registration_url(carrier))
# ...wait for the user...

# ── Phase 3 ────────────────────────────────────────────────────────
results = create_seed_products(carrier_code=carrier, client=woo)
env_values = seed_results_to_env(results)

# ── Phase 4 ────────────────────────────────────────────────────────
env_dir = Path(config.WOO_AUTOMATION_REPO_PATH) / "carrier-envs"
env_dir.mkdir(parents=True, exist_ok=True)
env_path = env_dir / f"{carrier}.env"
env_path.write_text("\n".join([
    f"CARRIER={carrier}",
    f"site_url={config.WOO_SITE_URL}",
    f"CONSUMER_KEY={config.WOO_CONSUMER_KEY}",
    f"CONSUMER_SECRET={config.WOO_CONSUMER_SECRET}",
    f"userName={config.WP_ADMIN_USER}",
    f"pass={config.WP_ADMIN_PASSWORD}",
    *(f"{k}={v}" for k, v in env_values.items()),
]) + "\n")
print("wrote", env_path)

# ── Phase 5 ────────────────────────────────────────────────────────
print("smoke order:", create_order(env_path))
```

Phase 2 is not optional and cannot be scripted: carrier credentials (account
number, licence key, client id/secret) are entered by a human on the plugin's
registration screen. If the user asks you to automate it, say plainly that the
plugin exposes no API for carrier registration.

---

## Execution Pattern

Run actions as a self-contained script from the repo root so imports resolve:

```bash
cd /Users/<you>/Documents/Pluginhive/AILearning/WooCommerceDomainExpert
./.venv/bin/python - <<'PY'
import sys; sys.path.insert(0, ".")
# paste the action code here
PY
```

Rules:
- Read before you write. List and show the user what matched before changing it.
- One confirmation for destructive actions (delete product, delete order,
  batch delete), stating exactly what will be affected and how many.
- Never write to a production site. If `WOO_SITE_URL` doesn't look like a QA or
  staging host, ask before any write.
- Prefer the project helpers (`woo_product_seed`, `order_creator`, `woo_admin`)
  over raw payloads — they already match what the automation repo expects.

---

## Response Format

Report back with:

1. **What ran** — the site, the action, the resource ids touched.
2. **Result** — ids, order numbers, permalinks, admin URLs the user can click.
3. **What changed on the store** — created vs reused vs updated vs deleted.
4. **Next step**, when there is an obvious one (register the carrier, run the
   smoke suite, re-check plugin version).

Example:

```
Site      : https://woocommerce-432251-5575216.cloudwaysapps.com
Action    : seeded QA catalogue for carrier "ups"
Products  : simple 2 (reused), variable 2 (reused), digital 2 (reused), dangerous 1 (created 4412)
Carrier env: ups-woo-automation/carrier-envs/ups.env  (written)
Smoke order: 3771 — processing — <site>/wp-admin/admin.php?page=wc-orders&action=edit&id=3771
Next      : register UPS credentials at <site>/wp-admin/admin.php?page=ph_multi_carrier_ups_registration
```

---

## Important Notes

- **Auth is Basic over HTTPS.** Keys go in the `Authorization` header, never in
  the URL. If the site is HTTP-only, stop and say so rather than putting the
  secret in a query string.
- **Read/Write permission** is required for anything except listing. A key
  generated as Read-only fails writes with a 401 and a confusing message.
- **`per_page` caps at 100.** Paginate with `page` for anything larger; the
  total count comes back in the `X-WP-Total` response header.
- **Batch endpoints cap at 100 items** per `create`/`update`/`delete` array.
- **`force=True` is permanent.** Without it, products and orders go to trash and
  can be restored.
- **Variations are separate resources.** Changing a parent product does not
  change its variations' price, weight, or dimensions.
- **Virtual products are skipped by shipping**, which is exactly what makes them
  useful for mixed-cart rate tests.
- **Plugin data lives in meta.** Tracking numbers, label ids, and packaging
  decisions come back under `meta_data` on the order, usually `_ph*` keys.
- **No app iframe.** The plugin settings render inline in wp-admin, so browser
  flows navigate straight to `admin.php?page=...` — there is nothing to switch
  frames into.
