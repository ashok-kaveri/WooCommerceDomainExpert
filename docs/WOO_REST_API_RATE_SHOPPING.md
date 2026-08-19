# WooCommerce API Recipes — Store Setup, Shipping Zones, Rate Verification

How to drive a QA WooCommerce site from code: set it up, make the PluginHive
shipping plugin quote rates, and turn a quote into a real order.

MCSLDomainExpert's equivalent document is built around Shopify's GraphQL
`draftOrderCalculate` and Storefront `cartCreate`. WooCommerce has neither.
Rates come from WooCommerce's own shipping engine, which the plugin plugs into
as a shipping method, so the API story is different in kind — not a translation.

---

## Big picture: how a PluginHive rate actually gets produced

```
buyer enters a destination
        │
        ▼
WC()->shipping()->calculate_shipping( $packages )
        │
        ├── WooCommerce builds "packages" from the cart (contents + destination)
        │
        ▼
each shipping method registered on the matching zone runs
        │
        ├── PH shipping method → carrier API call (rate request)
        │
        ▼
rates render in cart / checkout
```

Two consequences that shape every test:

1. **A rate only appears if a shipping zone matches the destination *and* the
   PluginHive method is enabled on that zone.** "No rates showing" is a zone
   problem at least as often as it is a carrier problem — check the zone first.
2. **There is no admin-side "quote me a rate" endpoint.** The REST API can
   create an order with a `shipping_lines` entry you supply, but it does not run
   the shipping engine. To see a real carrier quote you either go through the
   storefront (cart/checkout) or through the order screen's *Calculate Rates*
   button, which calls the plugin directly.

---

## Store prerequisites

### 1. Confirm the plugin is active and at the expected version

```python
from pipeline.woo_api import WooClient
woo = WooClient()

status = woo.get_system_status()
env = status["environment"]
print(env["site_url"], "| WP", env["wp_version"], "| WC", env["version"], "| PHP", env["php_version"])

for p in woo.active_plugins():
    print(f"{p['name']:60} {p['version']}")
```

If the build under test is not in that list, stop — everything downstream is
testing the wrong code.

### 2. Set the store address (ship-from)

The ship-from address decides domestic vs international, and therefore which
services and which customs fields apply.

```python
for setting_id, value in [
    ("woocommerce_store_address", "100 Residency Road"),
    ("woocommerce_store_city", "Bengaluru"),
    ("woocommerce_default_country", "IN:KA"),
    ("woocommerce_store_postcode", "560025"),
    ("woocommerce_currency", "INR"),
    ("woocommerce_weight_unit", "kg"),
    ("woocommerce_dimension_unit", "cm"),
]:
    woo.put(f"settings/general/{setting_id}", {"value": value})
```

Weight and dimension units matter more than they look: the plugin converts to
the carrier's expected units, so a store set to `g` while the products are
authored in `kg` produces silently wrong rates.

### 3. Create a shipping zone and attach the PluginHive method

```python
zone = woo.post("shipping/zones", {"name": "India", "order": 1})
woo.post(f"shipping/zones/{zone['id']}/locations", [{"code": "IN", "type": "country"}])
method = woo.post(f"shipping/zones/{zone['id']}/methods", {"method_id": "ph_multicarrier"})
print("zone", zone["id"], "method instance", method["instance_id"])
```

Zone id `0` is "Locations not covered by your other zones". A method there acts
as the catch-all — useful when a test only cares that *some* rate comes back.

### 4. Read and change the method's own settings

This is where most per-feature plugin toggles live, and it is the one plugin
surface the REST API does expose.

```python
m = woo.get(f"shipping/zones/{zone_id}/methods/{instance_id}")
for key, field in m["settings"].items():
    print(f"{key:40} = {field.get('value')!r}   ({field.get('label')})")

woo.put(f"shipping/zones/{zone_id}/methods/{instance_id}",
        {"settings": {"packing_method": "box_packing", "debug": "yes"}})
```

`pipeline/toggle_state.py` flattens exactly this payload into the
enabled/missing/unknown prerequisite view the dashboard shows.

---

## Rate verification — the three paths

### Path A: storefront cart (what the buyer sees) — the ground truth

The only path that exercises the whole chain: cart contents → packages → zone
match → plugin → carrier API → rendered rate. Drive it in the browser.

```
1. navigate: "shop"      → add the product to the cart
2. navigate: "cart"      → open the shipping calculator, enter the destination
3. read the rate rows    → carrier name, service name, amount
4. navigate: "checkout"  → confirm the same rates carry through
```

Use this whenever the card is about which rates appear, their order, their
labels, or their price. Nothing else proves it.

### Path B: order screen *Calculate Rates* (what the merchant sees)

On the WooCommerce order edit screen, the plugin's metabox offers
**Generate Packages → Calculate Rates**. This calls the carrier with the
order's real contents and destination, and shows the returned services in
`#wf_ups_service_select`.

Use this for label-generation scenarios: it is the same rate call, but it feeds
straight into **Confirm Shipment**.

Rates are visible only between *Calculate Rates* and *Confirm Shipment* — once
the shipment is confirmed the rate list is replaced by the shipment result. Any
rate evidence has to be captured in that window.

### Path C: REST order with a supplied shipping line (setup, not verification)

```python
woo.create_order({
    "set_paid": True,
    "status": "processing",
    "billing": address,
    "shipping": {k: v for k, v in address.items() if k != "email"},
    "line_items": [{"product_id": 123, "quantity": 1}],
    "shipping_lines": [{
        "method_id": "ph_multicarrier",
        "method_title": "UPS Next Day Air",
        "total": "42.50",
    }],
})
```

The amount here is whatever you pass — WooCommerce does **not** re-quote it.
This is how you stage an order that already has a chosen service, so a label
test can start from a known state. It is never evidence that the plugin returned
that rate.

---

## Turning a quote into a shipment

```
1. Create the order            (REST, Path C — or through the storefront)
2. Open the order edit screen  admin.php?page=wc-orders&action=edit&id=<id>
3. Generate Packages           .button.ups_generate_packages
4. Calculate Rates             .button.wf_ups_generate_packages_rates
5. Pick the service            #wf_ups_service_select
6. Confirm Shipment            .button.ups_create_shipment
7. Evidence                    "Print Label" link + tracking number in the order note
```

The raw carrier request and response render in the first two `<pre>` blocks on
the shipment-confirm screen — request first, response second. Enable **Debug
Mode** in the plugin settings first, or those blocks are empty.

---

## Building a carrier-env for the automation repo

`ups-woo-automation` reads products from env-backed ids. Seed first, then write
the env — never hand-author the ids.

```python
from pathlib import Path
import config
from pipeline.woo_product_seed import create_seed_products, seed_results_to_env

results = create_seed_products(carrier_code="ups", client=woo)
env_values = seed_results_to_env(results)

env_path = Path(config.WOO_AUTOMATION_REPO_PATH) / "carrier-envs" / "ups.env"
env_path.parent.mkdir(parents=True, exist_ok=True)
env_path.write_text("\n".join([
    "CARRIER=ups",
    f"site_url={config.WOO_SITE_URL}",
    f"CONSUMER_KEY={config.WOO_CONSUMER_KEY}",
    f"CONSUMER_SECRET={config.WOO_CONSUMER_SECRET}",
    f"userName={config.WP_ADMIN_USER}",
    f"pass={config.WP_ADMIN_PASSWORD}",
    *(f"{k}={v}" for k, v in env_values.items()),
]) + "\n")
```

Seeding is find-or-create by product name, matching the automation repo's own
`ensureStoreProducts()`, so re-running it reuses the catalogue instead of
duplicating it.

---

## The complete "set up a carrier store" pipeline

```
Phase 1  Verify site reachable, plugin active and at the right version   (API)
Phase 2  Set store address, units, currency                              (API)
Phase 3  Create the shipping zone and attach the PH method               (API)
Phase 4  STOP — user registers carrier credentials in wp-admin           (manual)
Phase 5  Seed the deterministic QA catalogue                             (API)
Phase 6  Write carrier-envs/<carrier>.env                                (file)
Phase 7  Smoke-test: create one order, calculate rates, confirm shipment  (API + UI)
```

Phase 4 cannot be scripted. Carrier credentials (account number, licence key,
client id/secret) are entered by a human on the plugin's registration screen —
`admin.php?page=ph_multi_carrier_<carrier>_registration`. There is no REST
endpoint for it. Say so plainly rather than inventing a workaround.

---

## Which API does what

| Need | Use |
|---|---|
| Is the build deployed? | `system_status` → `active_plugins` |
| Store address, units, currency | `settings/general/<id>` |
| Zones and which methods run | `shipping/zones`, `shipping/zones/<id>/methods` |
| Plugin feature toggles | the method instance's `settings` object |
| Create test products | `products`, `products/<id>/variations` (or `woo_product_seed`) |
| Create test orders | `orders` (or `pipeline.order_creator`) |
| Read label/tracking result | the order's `meta_data` and `orders/<id>/notes` |
| **See a real carrier quote** | **storefront cart/checkout, or the order screen's Calculate Rates** |

---

## Known gotchas

- **`per_page` caps at 100.** The total count comes back in the `X-WP-Total`
  header; paginate with `page`.
- **Basic auth needs HTTPS.** Over plain HTTP WooCommerce expects the key in the
  query string — don't do that; use the HTTPS host.
- **A Read-only key fails writes with a 401** and a message that reads like an
  auth failure rather than a permission one.
- **Permalinks set to "Plain" break `/wp-json/`.** A 404 on the API root usually
  means permalinks, or a security plugin blocking REST.
- **Variations don't inherit** price, weight, or dimensions from the parent.
  Setting them on the parent alone leaves the variations at zero weight, which
  produces rate errors that look like carrier problems.
- **Virtual products are excluded from shipping packages**, which is what makes
  them useful for mixed-cart tests — and what makes an all-virtual cart show no
  rates at all.
- **Deleting with `force=true` is permanent.** Without it items go to trash.

---

## Related

- [skills/woo-store-actions/SKILL.md](../skills/woo-store-actions/SKILL.md) — the action cookbook
- [pipeline/woo_api.py](../pipeline/woo_api.py) — the client
- [pipeline/woo_admin.py](../pipeline/woo_admin.py) — wp-admin URL builders
- [pipeline/woo_product_seed.py](../pipeline/woo_product_seed.py) — deterministic catalogue
- [docs/NEW_CARRIER_VALIDATION_PLAN.md](NEW_CARRIER_VALIDATION_PLAN.md) — the QA workflow
