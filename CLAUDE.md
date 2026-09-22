# CLAUDE.md

Working notes for future agents in this repo.

## Read This First

If docs and code disagree, trust current code, especially:
- [pipeline_dashboard.py](pipeline_dashboard.py:1)

Use these docs as the current handoff set:
- [README.md](README.md:1)
- [docs/MCSL_FLOW_PARITY_NOTES.md](docs/MCSL_FLOW_PARITY_NOTES.md:1)
- [docs/WOO_PLATFORM_ADAPTATION_PLAN.md](docs/WOO_PLATFORM_ADAPTATION_PLAN.md:1)
- [docs/WOO_CARRIER_KNOWLEDGE_RESEARCH.md](docs/WOO_CARRIER_KNOWLEDGE_RESEARCH.md:1)
- [docs/WOO_REST_API_RATE_SHOPPING.md](docs/WOO_REST_API_RATE_SHOPPING.md:1)
- [docs/NEW_CARRIER_VALIDATION_PLAN.md](docs/NEW_CARRIER_VALIDATION_PLAN.md:1)

## Repo Intent

This is the **WooCommerce** version of the QA orchestration platform. It covers
PluginHive's WooCommerce shipping plugins on WordPress: Multi-Carrier Shipping,
the per-carrier plugins, Table Rate Shipping Pro, Shipment Tracking Pro,
Estimated Delivery Date, and Bookings.

Its sibling is `MCSLDomainExpert` (Shopify). Same workflow shape, different
platform.

Do:
- reuse the MCSL workflow shape where it helps QA flow
- keep validation, diagnosis, automation targeting, and request reasoning WooCommerce-native
- prefer current implementation over old planning notes

Do not:
- copy Shopify navigation assumptions into WooCommerce
- reintroduce app-iframe, single-endpoint, or hamburger-menu navigation — WooCommerce admin is URL-addressable
- reintroduce account-UUID feature toggles — WooCommerce plugins are self-hosted
- treat stale docs as source of truth without checking the dashboard code

## Knowledge Sources

The primary knowledge source is the **public PluginHive Knowledge Base**, plus
**Trello**. This is the main structural difference from MCSLDomainExpert, which
leans on an internal wiki.

| Source | Loader | Notes |
|---|---|---|
| `https://www.pluginhive.com/knowledge-base/` | `scripts/scrape_woo_kb.py` → `ingest/kb_loader.py` | sitemap-driven discovery; 457 WooCommerce articles |
| Trello `ph-Woo-WIP-Releases` (`6657f8c2f080d70f774be782`) | `pipeline/trello_client.py` | release cards |
| `multi-carrier-shipping-plugin-for-woocommerce` | `ingest/codebase_loader.py` | plugin PHP |
| `woocommerce-shipping-pro` | `ingest/codebase_loader.py` | shared shipping layer |
| `ups-woo-automation` | `rag/code_indexer.py` | Playwright POMs and specs |

KB snapshots carry a metadata header (`Source:`, `Plugin:`) that `kb_loader`
parses, so RAG answers cite the live KB URL and can be filtered by plugin.
Do not hand-edit files in `docs/kb_snapshots/` — re-run the scraper.

When adding to `FOREIGN_PLATFORMS` in the scraper, remember it lists platforms to
**exclude**. WooCommerce must never appear there.

## Platform Layer

WooCommerce-specific modules, all new relative to MCSL:

- [pipeline/woo_api.py](pipeline/woo_api.py:1) — REST client (`wc/v3`, Basic auth with consumer key/secret)
- [pipeline/woo_admin.py](pipeline/woo_admin.py:1) — wp-admin URL builders
- [pipeline/woo_product_seed.py](pipeline/woo_product_seed.py:1) — deterministic, find-or-create catalogue

Credentials come from `.env`: `WOO_SITE_URL`, `WOO_CONSUMER_KEY`,
`WOO_CONSUMER_SECRET`, `WP_ADMIN_USER`, `WP_ADMIN_PASSWORD`. The automation repo
uses the lowercase names (`site_url`, `CONSUMER_KEY`, `CONSUMER_SECRET`,
`userName`, `pass`); `WooCredentials.from_env_mapping` accepts both.

## Current Dashboard Split

Keep this split unless the user explicitly asks to change it:
1. `🧾 Validate AC`
2. `🧪 Generate TC`
3. `🤖 AI QA Verifier`
4. `⚙️ Generate Automation Script`

Shared release state is stored in Streamlit session and reused across tabs:
- board, list, release label, loaded cards
- validations, diagnoses, release analysis
- AC drafts, test cases, AI QA reports, approvals, automation outputs

## Validate AC Rules

Current intended flow:
- `Load Cards`
- auto-run validation, diagnosis, and release analysis
- show `Release Intelligence`
- show `Step 1: Card Requirements`
- run site prerequisite checks if needed
- show `AI Suggested User Story & AC`
- show `Domain Validation`
- allow `Apply Fixes to AC`
- allow `Re-validate after fix`

Important:
- there should not be a separate `Analyze loaded cards` button
- generated AC should be revalidated immediately
- fix and revalidate should preserve research context

## Generate TC Rules

Current intended flow:
- generate TCs from the current AC draft in session
- reuse existing saved TCs when available
- support feedback-based regeneration, manual edits, and explicit re-review
- support Slack DM and channel sharing
- publish Trello full summary and positive cases to Sheets

Important:
- do not generate or review TCs only from stale `card.desc` when a newer AC draft exists
- avoid duplicate Trello comments on retry after partial publish failure

## Handoff Docs Rules

Current intended handoff format:
- take the guide title from the user prompt, not from Trello metadata
- use only the prompt's plugin name as the guide title and single-guide file base
- place `Version <no> – Released: <date>` directly under the H1
- do not show an automatic `UPDATE` badge in the header
- use `PluginHive: WooCommerce` as the header subtitle
- make the version/release line slightly more prominent in the header
- show exactly these index columns: `Story Id`, `Title`, `Trello Card Link`
- render `Included Story Cards` in the boxed section-heading style
- keep the `Story Id` column wide enough to read cleanly
- default to one Support Guide when the user says to generate the guide without naming a doc type
- start each story card with a boxed title block for visual separation
- do not add an extra accent strip inside that boxed title block
- do not add an extra accent strip inside the boxed `Included Story Cards` heading either
- keep normal sections free of internal or technical detail
- keep developer-only cards in a trailing `Technical Cards` section
- do not include feature-flag wording in handoff docs
- **ignore testing observations recorded in card comments.** A comment noting
  what someone saw while testing — triage advice for an unrelated failure, a
  defect this card does not change, anything called pre-existing, separate or
  "unrelated to this fix" — is an internal QA note, not release content. It
  never becomes a prerequisite, a caveat or a known limitation; raise it in the
  final report instead. Comments are still read for genuine late prerequisites.
  The rule lives in five parallel places — `skills/woo-handoff-docs/SKILL.md`,
  `skills/woo-handoff-docs/references/handoff_doc_formats.md`
  (`Observations vs. Release Content`), `skills/woo-handoff-docs/agents/openai.yaml`,
  `.claude/agents/woo-handoff-docs.md`, and the dashboard's own prompt in
  [pipeline/handoff_docs.py](pipeline/handoff_docs.py:1). Change all five together.

## Test Document Rules

The QA **test-result document** is a separate artifact from the handoff docs
above. It is the internal evidence doc: one test case per Trello checklist item,
executed against a QA store, with screenshots and an `Observation:` per case.

- skill: `skills/woo-test-document/`
- renderer: [scripts/generate_test_document.py](scripts/generate_test_document.py)
  (python-docx → `.docx`, then LibreOffice/Pages → PDF)
- output: `data/test_documents/`, screenshots in
  `data/test_documents/screenshots/`, per-card steps in
  `data/test_documents/<card>_steps.json`
- layout, palette and execution traps:
  `skills/woo-test-document/references/test_document_format.md`

Keep it separate from `pipeline/handoff_docs.py`. The two documents have
different audiences, formats and renderers — do not converge them, and do not add
test-document concerns (screenshot slots, per-case status, observations) to the
handoff pipeline.

Important:
- the environment is **per card**. Expect the user to give `site_url` and
  `userName` in the request; fall back to the card, then
  `carrier-envs/<carrier>.env`, then the automation repo `.env`, then
  `WOO_SITE_URL` — and always confirm which was used. These disagree in practice.
- never write an observation or a status for a case that was not run; mark it
  `Not run` and say why
- a human signs in; credentials are never typed by the agent and never accepted
  in chat
- UPS **Debug Mode** dumps the request/response and halts the label flow, so the
  order never records tracking. Check it before blaming the plugin, and restore
  whatever you change.

## AI QA Rules

Keep TC-first verification as the default path.

Navigation is **URL-based**. `_Woo_NAV_MAP` in
[pipeline/smart_ac_verifier.py](pipeline/smart_ac_verifier.py:1) maps every
destination to a real wp-admin or storefront URL. There is no app iframe, no
single endpoint, and no hamburger search — do not reintroduce them.

The label flow that matters, grounded in `ups-woo-automation`:

```
orders → open order → Generate Packages → Calculate Rates
       → pick service → Confirm Shipment → Print Label + tracking note
```

Rate evidence must be captured **between** Calculate Rates and Confirm Shipment;
after confirmation the rate list is gone.

Use automation for navigation, locators, and repeated flows. Use codebase, KB,
request registry, and carrier registries for expectation building and setup
guidance. Do not reduce AI QA back to AC-only execution.

## Automation Rules

Current intended flow:
- `① Write Automation Code`
- `② Run Automation & Post to Slack`
- `③ Generate Documentation`
- `🐛 Bug Reporter`

Matching behaviour:
- detect existing-vs-new feature areas
- prefer updating existing coverage in `ups-woo-automation`
- use `feature_detector` and `find_pom`

## New Carrier Validation Rules

```
1. verify site reachable + plugin active at the expected version
2. set store address, units, currency
3. create the shipping zone and attach the PluginHive method
4. STOP — manual carrier registration in wp-admin
5. seed the deterministic product catalogue
6. write carrier-envs/<carrier>.env
7. run smoke / sanity / regression
8. report readiness
```

Important:
- do not pre-create orders; the automation repo creates them from env-backed product IDs
- product provisioning must populate `SIMPLE_PRODUCTS_JSON`, `VARIABLE_PRODUCTS_JSON`,
  `DIGITAL_PRODUCTS_JSON`, `DANGEROUS_PRODUCTS_JSON`
- use deterministic product templates matching the automation repo's `ensureStoreProducts()`
- **carrier-env key names must match `ups-woo-automation/env_sample` exactly** —
  `site_url`, `userName`, `pass`, `CONSUMER_KEY`, `CONSUMER_SECRET`, `CARRIER`,
  `SLACK_WEBHOOK_URL`. The automation reads `process.env.<those names>`;
  renaming any of them silently breaks every suite.
- only variable products carry a `variation_id` in the `*_PRODUCTS_JSON` values;
  simple, digital, and dangerous entries have `product_id` only
- **step 4 cannot be scripted.** Carrier credentials are entered by a human on
  `admin.php?page=ph_multi_carrier_<carrier>_registration`. There is no REST
  endpoint. Say so rather than inventing a workaround.

## Prerequisite ("Toggle") Rules

WooCommerce has no account-scoped feature flags. A prerequisite here is:
- the active plugin version (`system_status` → `active_plugins`), or
- a plugin setting on the Multi-Carrier shipping method instance, or
- a WooCommerce core setting.

`pipeline/toggle_state.py` reads all three over REST and returns
enabled / missing / unknown. It keeps the MCSL function names
(`capture_store_and_toggle_state`, `compute_toggle_status`) so the dashboard is
unchanged, and exposes `store_uuid` / `account_uuid` as aliases for the site URL.

If touching this flow:
- keep live REST state as the source of truth
- do not reintroduce browser-scraped toggle maps

## Optional Dependency Shims

This repo includes compatibility shims for local test and import stability:
`streamlit.py`, `langchain_anthropic/`, `langchain_core/`, `chromadb/`,
`langchain_chroma/`, `langchain_ollama/`, `langchain_text_splitters/`.

Do not remove them casually without checking test coverage and local `.venv` behavior.

## Docs To Keep Updated

When workflow changes materially, update:
- [README.md](README.md:1)
- [CLAUDE.md](CLAUDE.md:1)
- [AGENTS.md](AGENTS.md:1)
- [docs/WOO_PLATFORM_ADAPTATION_PLAN.md](docs/WOO_PLATFORM_ADAPTATION_PLAN.md:1)

When carrier reasoning changes, also update:
- [docs/WOO_CARRIER_KNOWLEDGE_RESEARCH.md](docs/WOO_CARRIER_KNOWLEDGE_RESEARCH.md:1)
- [docs/WOO_CARRIER_SUPPORT_REGISTRY.md](docs/WOO_CARRIER_SUPPORT_REGISTRY.md:1)
- [docs/WOO_CARRIER_CAPABILITY_MATRIX.md](docs/WOO_CARRIER_CAPABILITY_MATRIX.md:1)
- [docs/WOO_CARRIER_REQUEST_REGISTRY.md](docs/WOO_CARRIER_REQUEST_REGISTRY.md:1)

## Useful Commands

```bash
.venv/bin/python -m py_compile pipeline_dashboard.py pipeline/card_processor.py
.venv/bin/python -m pytest -q
.venv/bin/python -m pytest -q tests/test_toggle_state.py
.venv/bin/python -m pytest -q tests/test_kb_loader.py
.venv/bin/python scripts/scrape_woo_kb.py
PYTHONPATH=. .venv/bin/streamlit run pipeline_dashboard.py

# QA test-result document from a Trello card
.venv/bin/python scripts/generate_test_document.py SI23TDil \
  --steps data/test_documents/SI23TDil_steps.json \
  --plugin "WooCommerce UPS Shipping Plugin with Print Label" --version 6.6.4
```
