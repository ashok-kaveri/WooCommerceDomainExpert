# New Carrier Validation Plan

Implementation plan for adding a new Woo workflow that provisions the minimum WooCommerce test data required for a newly added carrier, then runs the existing automation suites against that store and carrier configuration.

## Goal

When a new carrier is introduced in Woo, QA should be able to use the dashboard to:
- create a WooCommerce dev store
- install the Woo app
- complete a manual carrier-registration checkpoint
- create the required WooCommerce products for automation
- write those product IDs into a carrier env file
- run smoke, sanity, and regression automation
- monitor progress and review a final readiness report

This workflow should reuse existing automation and WooCommerce tooling rather than inventing a new runner.

## Scope Clarification

The automation repo already creates orders during suite execution.

That means this feature does **not** need to create orders up front as part of setup.

What it **does** need to do:
- create the required WooCommerce product catalog
- capture `product_id` and `variant_id`
- write them into the carrier env file used by automation

## Confirmed Local Integrations

### Woo automation repo

Local repo:
- `$WOO_AUTOMATION_REPO_PATH`

Relevant capabilities already present:
- create WooCommerce dev store
- install app into store
- reuse WooCommerce login/session
- run tagged suites:
  - `@smoke`
  - `@sanity`
  - `@regression`
- create orders from product IDs in env files

Key references:
- [$WOO_AUTOMATION_REPO_PATH/tests/onboardingFlow/createStoreAndInstallApp.spec.ts]($WOO_AUTOMATION_REPO_PATH/tests/onboardingFlow/createStoreAndInstallApp.spec.ts:1)
- [$WOO_AUTOMATION_REPO_PATH/support/pages/createStore/createStorePage.ts]($WOO_AUTOMATION_REPO_PATH/support/pages/createStore/createStorePage.ts:1)
- [$WOO_AUTOMATION_REPO_PATH/support/setup/login.setup.ts]($WOO_AUTOMATION_REPO_PATH/support/setup/login.setup.ts:1)
- [$WOO_AUTOMATION_REPO_PATH/support/pages/wooAPI/createOrderAPI.ts]($WOO_AUTOMATION_REPO_PATH/support/pages/wooAPI/createOrderAPI.ts:1)

### WooCommerce actions repo

Local repo:
- `$WOO_ACTIONS_PATH`

Relevant capabilities already present:
- create WooCommerce products
- create WooCommerce orders
- list products
- list orders
- deterministic API endpoints for product and order creation

Key references:
- [$WOO_ACTIONS_PATH/src/index.js]($WOO_ACTIONS_PATH%20/src/index.js:1)
- [$WOO_ACTIONS_PATH/src/modules/Generator.js]($WOO_ACTIONS_PATH%20/src/modules/Generator.js:1)
- [$WOO_ACTIONS_PATH/config.json]($WOO_ACTIONS_PATH%20/config.json:1)

## Existing Product Env Contract

The automation repo currently expects these env keys:
- `SIMPLE_PRODUCTS_JSON`
- `VARIABLE_PRODUCTS_JSON`
- `DIGITAL_PRODUCTS_JSON`
- `DANGEROUS_PRODUCTS_JSON`

Each entry uses:

```json
{"product_id": 123, "variant_id": 456}
```

Confirmed from:
- [$WOO_AUTOMATION_REPO_PATH/support/pages/wooAPI/createOrderAPI.ts]($WOO_AUTOMATION_REPO_PATH/support/pages/wooAPI/createOrderAPI.ts:39)
- [$WOO_AUTOMATION_REPO_PATH/carrier-envs/ups.env]($WOO_AUTOMATION_REPO_PATH/carrier-envs/ups.env:1)
- [$WOO_AUTOMATION_REPO_PATH/carrier-envs/packaging-fedexrest.env]($WOO_AUTOMATION_REPO_PATH/carrier-envs/packaging-fedexrest.env:1)

## Product Types Required

For the first version of this workflow, Woo should create the product categories already expected by automation:
- simple
- variable
- digital
- dangerous

Recommended minimum seeded counts:
- simple: 2
- variable: 2
- digital: 2
- dangerous: 1

These should be deterministic, not random, so the setup is reproducible across reruns.

## Workflow Design

### Stage 1: Store Provisioning

Inputs:
- carrier name
- target store name
- release label or run label
- optional region / country / currency

Actions:
- create WooCommerce dev store
- install Woo app
- persist run metadata

### Stage 2: Manual Carrier Registration Checkpoint

The dashboard should stop here and instruct QA to:
- add the new carrier account in the app
- enter carrier credentials
- enable any required services / options
- confirm the carrier is visible in the app

This step remains manual because it often involves secrets and carrier-specific decisions.

### Stage 3: Product Provisioning

The dashboard should:
- call the WooCommerce actions repo
- create the required product categories
- collect `product_id` and `variant_id`
- persist the created product set into Woo history

Output shape:

```json
{
  "simple": [{"product_id": 1, "variant_id": 11}],
  "variable": [{"product_id": 2, "variant_id": 22}],
  "digital": [{"product_id": 3, "variant_id": 33}],
  "dangerous": [{"product_id": 4, "variant_id": 44}]
}
```

### Stage 4: Carrier Env Generation

Create a new env file in:
- `config.WOO_AUTOMATION_REPO_PATH/carrier-envs/`

Include:
- `CARRIER`
- `WOO_SITE_URL`
- `WOO_CONSUMER_SECRET`
- `WOO_API_VERSION`
- `WOOURL`
- `APPURL`
- `SIMPLE_PRODUCTS_JSON`
- `VARIABLE_PRODUCTS_JSON`
- `DIGITAL_PRODUCTS_JSON`
- `DANGEROUS_PRODUCTS_JSON`

Optional additions:
- region-specific addresses
- Slack webhook if required by the automation repo

### Stage 5: Suite Execution

Use the existing automation repo directly.

Run sequence:
1. smoke
2. sanity
3. regression

Suggested commands:

```bash
npx playwright test --grep "@smoke"
npx playwright test --grep "@sanity"
npx playwright test --grep "@regression"
```

The workflow should allow:
- run only smoke
- run smoke + sanity
- run full smoke + sanity + regression

### Stage 6: Monitoring And Report

The dashboard should show:
- current stage
- running suite
- pass / fail / skipped counts
- report links
- major failure summary
- final readiness verdict

Final output should answer:
- was the new carrier setup valid?
- were the required products provisioned?
- did smoke pass?
- did sanity pass?
- did regression pass?
- what remains blocked?

## Proposed Woo Additions

### New dashboard tab

Add a new top-level tab:
- `🚚 New Carrier Validation`

Suggested sections:
- Carrier Setup
- Manual Carrier Registration
- Create Products
- Generate Carrier Env
- Run Smoke
- Run Sanity
- Run Regression
- Results

### New backend modules

Recommended first-pass modules:
- `pipeline/new_carrier_validation.py`
- `pipeline/woo_product_seed.py`
- `pipeline/carrier_env_builder.py`
- `pipeline/automation_runner.py`
- `pipeline/carrier_validation_report.py`

## Session State / Persistence

Recommended state keys:
- `new_carrier_run`
- `new_carrier_store_name`
- `new_carrier_name`
- `new_carrier_stage`
- `new_carrier_products`
- `new_carrier_env_path`
- `new_carrier_smoke_result`
- `new_carrier_sanity_result`
- `new_carrier_regression_result`
- `new_carrier_report`

Persisted history should include:
- store name
- carrier
- created product IDs
- generated env file path
- suite outcomes
- report summary

## Implementation Order

### Milestone 1

Deliver the core path:
- new tab scaffold
- store setup integration
- manual QA checkpoint
- create required products
- generate env file
- run smoke
- produce a basic report

### Milestone 2

Expand to:
- sanity and regression orchestration
- richer reporting
- rerun controls
- history integration
- better carrier-specific product templates if needed

## Non-Goals For The First Version

Do not add these to the first delivery:
- AI-driven carrier credential entry
- random catalog generation
- pre-creating orders outside the automation repo
- broad automatic inference of every carrier-specific edge case

The first version should be deterministic and orchestration-focused.

## Recommendation

The first code step should be:
1. add the new tab scaffold
2. add product seeding + env generation backend
3. wire one smoke-run path end-to-end

That gives a useful vertical slice without waiting for the full regression orchestration UI.
