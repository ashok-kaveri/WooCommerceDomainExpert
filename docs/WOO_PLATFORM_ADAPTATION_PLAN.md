# WooCommerce Domain Expert Adaptation Plan

A current-state adaptation map, not a gap tracker.

## Goal

Keep the MCSL workflow shape where it improves throughput, while grounding
reasoning and execution in WooCommerce truth:
- the PluginHive WooCommerce plugins and their carriers
- wp-admin plugin settings screens and the storefront rate flow
- the `ups-woo-automation` repo
- the plugin's request/response logs and request expectations
- live site prerequisite state read over the WooCommerce REST API

## Current Platform Status

The repo is past first-pass planning. Core workflow layers are already implemented.

Already implemented:
- split QA workflow tabs
- Trello-driven release loading
- AC generation and validation
- release intelligence
- TC generation, review, feedback regeneration, share, and publish
- TC-first AI QA execution
- failed-finding review and developer notification
- approval and sign-off flow
- automation writing, run, docs, and manual bug reporter flow
- live site prerequisite capture over REST
- carrier knowledge and request registry support
- WooCommerce REST client, wp-admin URL builders, and deterministic product seeding
- KB mirror sync from `pluginhive.com/knowledge-base/`

## Current Workflow Model

### 1. Validate AC
- load release cards from Trello
- run Woo validation, diagnosis, and release analysis automatically
- review card requirements
- check live site prerequisites (plugin version, zone, method settings)
- generate or review AI AC
- validate, fix, and revalidate AC

### 2. Generate TC
- generate test cases from the current AC draft
- review, regenerate, edit, and re-review
- share to Slack
- publish Trello summary and positive cases to Sheets

### 3. AI QA Verifier
- execute ranked reviewed test cases
- gather evidence from live app behavior
- use the WooCommerce browser flow by default; when a card explicitly names Shopify, BigCommerce, Magento, or PrestaShop, ask QA whether to execute it through the available flow and proceed only after confirmation
- normalise navigation wording to supported wp-admin destinations before execution
- reuse `ups-woo-automation` page-object patterns: the order metabox sequence
  (Generate Packages → Calculate Rates → Confirm Shipment → Print Label), bulk
  actions, select2 settings widgets, and the request/response `<pre>` logs
- preserve carrier display name and internal carrier code for carrier-specific order setup
- support reruns and `qa_needed`
- review findings and bugs

### 4. Generate Automation Script
- detect existing-vs-new automation targets
- generate or update automation
- run automation
- post results
- generate docs
- raise manual QA bugs

## Woo-Specific Operating Rules

### Navigation
- AC/TC/docs can be platform-aware on WordPress/WooCommerce
- if a card does not explicitly name a platform, default QA/support wording to WooCommerce
- AI QA browser and automation execution use the WooCommerce flow; cards that
  explicitly name another platform require QA confirmation first, because the
  underlying feature is usually shared
- navigation should use wp-admin URLs and automation knowledge, not MCSL app routes

### Verification
- many scenarios create orders through the WooCommerce REST API
- buyer-visible rates can only be verified on the storefront cart/checkout
- rate evidence must be captured between Calculate Rates and Confirm Shipment
- request and log verification uses the plugin's `<pre>` blocks and WooCommerce
  → Status → Logs, with Debug Mode enabled first

### Prerequisite Handling
- live REST state is the source of truth: plugin version, shipping method
  settings, WooCommerce settings
- there are no account-scoped feature flags here; carrier registration and
  licence activation cannot be read over REST and must be confirmed by a human
- Slack escalation remains part of orchestration

### Analysis
- validation, diagnosis, and release intelligence must stay WooCommerce-native
- MCSL is a workflow reference only

## Important Current Files

- [pipeline_dashboard.py](pipeline_dashboard.py:1)
- [pipeline/card_processor.py](pipeline/card_processor.py:1)
- [pipeline/smart_ac_verifier.py](pipeline/smart_ac_verifier.py:1)
- [pipeline/automation_writer.py](pipeline/automation_writer.py:1)
- [pipeline/feature_detector.py](pipeline/feature_detector.py:1)
- [pipeline/toggle_state.py](pipeline/toggle_state.py:1)
- [pipeline/bug_tracker.py](pipeline/bug_tracker.py:1)
- [pipeline/woo_api.py](pipeline/woo_api.py:1)
- [pipeline/woo_admin.py](pipeline/woo_admin.py:1)
- [pipeline/woo_product_seed.py](pipeline/woo_product_seed.py:1)
- [scripts/scrape_woo_kb.py](scripts/scrape_woo_kb.py:1)

## Current Improvement Areas

The highest-value remaining work is:
- more live end-to-end validation against Trello, Slack, Sheets, and site data
- wider plugin coverage in the AI QA locator knowledge: the metabox locators are
  currently grounded in the standalone UPS plugin (`ups_` / `wf_ups_` prefixes);
  the Multi-Carrier plugin uses its own prefixes and needs the same treatment
- a shipping-zone precheck in AI QA, since "no rates" is a zone problem at least
  as often as a carrier problem

## Documentation Rule

If workflow changes again, update this file together with:
- [README.md](README.md:1)
- [CLAUDE.md](CLAUDE.md:1)
- [AGENTS.md](AGENTS.md:1)
- [docs/MCSL_FLOW_PARITY_NOTES.md](docs/MCSL_FLOW_PARITY_NOTES.md:1)
