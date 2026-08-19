# AGENTS.md

Working notes for future agents in this repo.

## Read This First

If docs and code disagree, trust current code, especially:
- [pipeline_dashboard.py](pipeline_dashboard.py:1)

Use these docs as the current handoff set:
- [README.md](README.md:1)
- [CLAUDE.md](CLAUDE.md:1)
- [docs/MCSL_FLOW_PARITY_NOTES.md](docs/MCSL_FLOW_PARITY_NOTES.md:1)
- [docs/WOO_PLATFORM_ADAPTATION_PLAN.md](docs/WOO_PLATFORM_ADAPTATION_PLAN.md:1)
- [docs/WOO_CARRIER_KNOWLEDGE_RESEARCH.md](docs/WOO_CARRIER_KNOWLEDGE_RESEARCH.md:1)

## Repo Intent

This is the **WooCommerce** version of the QA orchestration platform, covering
PluginHive's WooCommerce shipping plugins on WordPress. Its sibling is
`MCSLDomainExpert` (Shopify).

Knowledge comes primarily from the public PluginHive Knowledge Base
(`https://www.pluginhive.com/knowledge-base/`, synced by
`scripts/scrape_woo_kb.py`) and Trello (`ph-Woo-WIP-Releases`).

Do:
- reuse the MCSL workflow shape where it helps QA flow
- keep validation, diagnosis, automation targeting, and request reasoning WooCommerce-native
- prefer current implementation over old planning notes

Do not:
- copy Shopify navigation assumptions into WooCommerce
- reintroduce app-iframe / single-endpoint / hamburger navigation — wp-admin is URL-addressable
- reintroduce account-UUID feature toggles — the plugins are self-hosted
- treat stale docs as source of truth without checking the dashboard code

## Codex / Claude Skills

This repo includes WooCommerce-local skills under [skills](skills:1). They are the
Codex/Claude-app equivalent of the dashboard workflow and should stay
WooCommerce-native.

Current skill set:
- `woo-domain-core`
- `woo-trello-operator`
- `woo-ac-writer-reviewer`
- `woo-dashboard-tc-publisher`
- `woo-ai-qa-testcase-prep`
- `woo-ai-qa-browser`
- `woo-automation-writer`
- `woo-bug`
- `woo-signoff-message`
- `woo-handoff-docs`
- `woo-rag-sync`
- `woo-knowledge-maintainer`
- `woo-slack-operator`
- `woo-store-actions`
- `woo-feature-prerequisites`

If changing a dashboard flow, also update the corresponding skill. Do not leave
copied Shopify-only wording — app iframes, `admin.shopify.com` URLs, hamburger
search, LABEL CREATED badges, Label Batch pages, account-UUID toggles — unless
the WooCommerce code actually uses that behaviour.

## Current Dashboard Split

Keep this split unless the user explicitly asks to change it:
1. `🧾 Validate AC`
2. `🧪 Generate TC`
3. `🤖 AI QA Verifier`
4. `⚙️ Generate Automation Script`

Shared release state is stored in Streamlit session and reused across tabs:
- board
- list
- release label
- loaded cards
- full loaded card list for active-card subset editing
- validations
- diagnoses
- release analysis
- AC drafts
- test cases
- AI QA reports
- approvals
- automation outputs

## Validate AC Rules

Current intended flow:
- `Load Cards`
- support selecting a card subset before load
- auto-run Woo validation, diagnosis, and release analysis
- show `Release Intelligence`
- show `Step 1: Card Requirements`
- run Woo-specific toggle/store-state handling if needed
- show `AI Suggested User Story & AC`
- show `Domain Validation`
- allow `Apply Fixes to AC`
- allow `Re-validate after fix`

Important:
- there should not be a separate `Analyze loaded cards` button
- after load, the active-card subset editor should remain available across Validate AC, Generate TC, AI QA, and Automation tabs
- generated AC should be revalidated immediately
- fix and revalidate should preserve research context
- Woo toggle flow should remain Woo-specific

## Generate TC Rules

Current intended flow:
- generate TCs from the current AC draft in session
- reuse existing saved TCs when available
- support feedback-based regeneration
- support manual edits
- support explicit TC re-review after manual edits
- support Slack DM and channel sharing
- publish Trello full summary and positive cases to Sheets

Important:
- do not generate or review TCs only from stale `card.desc` when a newer AC draft exists
- avoid duplicate Trello comments on retry after partial publish failure

## AI QA Rules

Keep TC-first verification as the default path.

Current execution scope:
- AI QA browser execution uses the current WooCommerce browser flow by default.
- AC, TC, and handoff docs can be platform-aware for WooCommerce (WordPress).
- If a card is explicitly WooCommerce, BigCommerce, Magento, or PrestaShop, keep the AC/TC/docs platform-specific and ask QA whether to execute it through the available WooCommerce flow. If QA confirms, AI QA can test it because Woo features are generally shared across platforms; keep the reported platform visible in evidence.

Use automation for:
- navigation
- locators
- repeated flows
- known Playwright page-object patterns such as the OrdersPage metabox sequence, bulk actions, select2 settings widgets, request/response `<pre>` logs, and label download checks

Use codebase, KB, wiki, request registry, and carrier registries for:
- expectation building
- request and response reasoning
- setup guidance

Important:
- AI QA navigation aliases should normalize QA/model wording like `Shipping`, `All Products`, and `Rate Automation` to supported Woo destinations
- carrier-specific AI QA plans should preserve both carrier display name and internal carrier code so order creation can choose the right automation env

Do not reduce AI QA back to AC-only execution.

## Automation Rules

Current intended flow:
- `① Write Automation Code`
- `② Run Automation & Post to Slack`
- `③ Generate Documentation`
- `🐛 Bug Reporter`

Current automation matching behavior:
- detect existing-vs-new feature areas
- prefer updating existing Woo automation coverage
- use `feature_detector` and `find_pom`

Current automation execution scope:
- Playwright automation generation and runs target the WooCommerce Woo automation repo only.
- For cards explicitly scoped to WooCommerce, BigCommerce, Magento, or PrestaShop, ask QA before generating WooCommerce automation. Generate it only when QA confirms the shared behavior should be covered through the current WooCommerce automation repo.

## Toggle Rules

Toggle flow is Woo-specific and already has live-state support.

Current behavior:
- detect toggle details from card text and comments
- derive default store and app URL from Woo knowledge
- capture live `store_uuid`, `account_uuid`, and toggle state from app or API responses
- compute enabled vs missing toggles
- notify Ashok or developer through Slack
- poll replies and unblock QA when confirmed

If touching toggle flow:
- keep live state as the source of truth when available
- do not regress to store-name-only logic

## Optional Dependency Shims

This repo includes compatibility shims for local test and import stability:
- `streamlit.py`
- `langchain_anthropic/`
- `langchain_core/`
- `chromadb/`
- `langchain_chroma/`
- `langchain_ollama/`
- `langchain_text_splitters/`

Do not remove them casually without checking test coverage and local `.venv` behavior.

## Docs To Keep Updated

When workflow changes materially, update:
- [README.md](README.md:1)
- [AGENTS.md](AGENTS.md:1)
- [docs/FEDEX_FLOW_PARITY_NOTES.md](docs/FEDEX_FLOW_PARITY_NOTES.md:1)
- [docs/WOO_PLATFORM_ADAPTATION_PLAN.md](docs/WOO_PLATFORM_ADAPTATION_PLAN.md:1)

When carrier reasoning changes, also update:
- [docs/WOO_CARRIER_KNOWLEDGE_RESEARCH.md](docs/WOO_CARRIER_KNOWLEDGE_RESEARCH.md:1)
- [docs/WOO_CARRIER_SUPPORT_REGISTRY.md](docs/WOO_CARRIER_SUPPORT_REGISTRY.md:1)
- [docs/WOO_CARRIER_CAPABILITY_MATRIX.md](docs/WOO_CARRIER_CAPABILITY_MATRIX.md:1)
- [docs/WOO_CARRIER_REQUEST_REGISTRY.md](docs/WOO_CARRIER_REQUEST_REGISTRY.md:1)

## Useful Commands

```bash
python3 -m py_compile pipeline_dashboard.py pipeline/card_processor.py
pytest -q tests/test_dashboard.py::test_dash01_scaffold
pytest -q tests/test_dashboard.py::test_ui10b_validate_ac_matches_fedex_auto_analysis_flow
pytest -q tests/test_dashboard.py::test_ui10c_generate_tc_uses_current_ac_and_avoids_duplicate_trello_publish
pytest -q tests/test_toggle_state.py
```
