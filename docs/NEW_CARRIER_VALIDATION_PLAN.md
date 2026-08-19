# New Carrier Validation Plan

The workflow that gets a QA WooCommerce site ready for a newly added carrier,
then runs the existing automation suites against it.

## How this differs from the MCSL plan

MCSL provisions a fresh Shopify dev store and installs the app through Partner
OAuth. **None of that applies here.** A WooCommerce QA site is a WordPress
install that already has the plugins on it. There is no store to create, no app
to install, and no OAuth token to scrape.

What replaces those steps is smaller and mostly API-driven — with one hard
manual stop that cannot be automated away.

## Goal

QA should be able to use the dashboard to:

1. confirm the site is reachable and the plugin is active at the expected version
2. set the store address, weight/dimension units, and currency the scenarios assume
3. create the shipping zone and attach the PluginHive shipping method
4. stop for a manual carrier-registration checkpoint
5. seed the deterministic product catalogue
6. write those product IDs into a carrier env file
7. run smoke, sanity, and regression automation
8. monitor progress and review a readiness report

Reuse existing automation and WooCommerce tooling rather than inventing a new runner.

## Scope Clarification

The automation repo already creates orders during suite execution
(`src/api/controllers/orderController.ts` via `createWooOrder`).

So this feature does **not** create orders up front. What it does:

- ensure the required product catalogue exists
- capture `product_id` and, for variable products, `variation_id`
- write them into the carrier env file the automation reads

## The manual checkpoint (step 4)

Carrier credentials — account number, licence key, client id/secret — are
entered by a human on the plugin's registration screen:

```
<site>/wp-admin/admin.php?page=ph_multi_carrier_<carrier>_registration
```

There is no REST endpoint for carrier registration. The same is true of
WooCommerce REST API keys: they are created at
`WooCommerce > Settings > Advanced > REST API`, and the consumer secret is shown
exactly once.

If asked to automate either, say plainly that no API exists rather than building
a brittle UI-scraping path around it.

## Confirmed Local Integrations

### Automation repo

Local repo: `$WOO_AUTOMATION_REPO_PATH` (`ups-woo-automation`)

Capabilities already present:
- WordPress admin login and stored session (`src/pages/auth/loginPage.ts`)
- WooCommerce order list and order-screen shipment flow
  (`src/pages/wooCommerceAdmin/ordersPage.ts`)
- plugin settings screens (`src/pages/UPSplugin/settings.ts`)
- WooCommerce REST client (`src/api/client/wooApiClient.ts`)
- find-or-create standard products (`src/api/controllers/productSetupController.ts`)
- order creation from product ids (`src/api/controllers/orderController.ts`)
- tagged suites: `@smoke`, `@sanity`, `@regression`

Env it reads (`env_sample`):

```
site_url, userName, pass, CONSUMER_KEY, CONSUMER_SECRET, CARRIER, SLACK_WEBHOOK_URL
```

Plus the seeded product JSONs this repo writes:

```
SIMPLE_PRODUCTS_JSON, VARIABLE_PRODUCTS_JSON, DIGITAL_PRODUCTS_JSON, DANGEROUS_PRODUCTS_JSON
```

### This repo

| Step | Module |
|---|---|
| 1–3 site prep | `pipeline/new_carrier_onboarding.prepare_site_for_carrier` |
| REST calls | `pipeline/woo_api.WooClient` |
| admin URLs | `pipeline/woo_admin` |
| 5 seeding | `pipeline/woo_product_seed.create_seed_products` |
| 6 env file | `pipeline/new_carrier_validation.write_carrier_env_file` |
| 7 suites | `pipeline/new_carrier_runner.run_carrier_suite` |

## Product Catalogue

Names match the automation repo's `STANDARD_PRODUCTS` so both tools converge on
one catalogue:

| Group | Products |
|---|---|
| simple | `1. Simple Product`, `2. Simple Product` |
| variable | `1. Variable Product`, `2. Variable Product` (Colour × Size) |
| digital | `1. Digital Product`, `2. Digital Product` (virtual + downloadable) |
| dangerous | `<carrier> Dangerous Goods Product` (only for carriers with DG scenarios) |

Seeding is **find-or-create by product name**. Running it twice reuses the
existing products instead of duplicating the catalogue — verify this stays true
if the seeding logic is ever changed.

Defaults: price `10.00`, weight `1`, dimensions `5×5×5`, `manage_stock` with
`stock_quantity: 99999`. WooCommerce has no `BYPASS_STOCK` equivalent, so a high
stock count is how test orders avoid draining inventory.

## Readiness Report

Report, per site:

- WordPress / WooCommerce / PHP versions
- every active PluginHive plugin and its version, against the version the
  release targets
- the shipping zone and whether the PluginHive method is enabled on it
- which products were reused vs created
- the carrier-env file path that was written
- suite results by tag, with failures listed
- anything left manual and unverified (carrier registration, licence activation)

A run is only "ready" when the plugin version matches the release target. A
green suite against the wrong build proves nothing.
