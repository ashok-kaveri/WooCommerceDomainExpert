# WooCommerce Domain Expert

Streamlit-based QA orchestration for **PluginHive's WooCommerce shipping plugins** —
Multi-Carrier Shipping, the per-carrier plugins (UPS, FedEx, Canada Post, USPS,
Royal Mail, Australia Post, DHL, Aramex …), Table Rate Shipping Pro, Shipment
Tracking Pro, Estimated Delivery Date, and Bookings.

It is the WooCommerce sibling of `MCSLDomainExpert` (Shopify). The workflow shape
is deliberately shared so QA can move between them; everything platform-specific —
navigation, API, locators, prerequisites — is WooCommerce-native.

## Knowledge Sources

Two primary sources, plus the code:

| Source | What it gives | How it is loaded |
|---|---|---|
| **[PluginHive Knowledge Base](https://www.pluginhive.com/knowledge-base/)** | Product behaviour, setup steps, carrier specifics, troubleshooting — 457 WooCommerce articles | `scripts/scrape_woo_kb.py` → `docs/kb_snapshots/` → `ingest/kb_loader.py` → Chroma |
| **Trello** (`ph-Woo-WIP-Releases`) | Release cards, AC, comments, checklists, developer assignment | `pipeline/trello_client.py` |
| Plugin source | `multi-carrier-shipping-plugin-for-woocommerce`, `woocommerce-shipping-pro` | `ingest/codebase_loader.py` |
| Automation repo | `ups-woo-automation` — Playwright POMs and specs | `rag/code_indexer.py` |

The KB is the headline difference from MCSLDomainExpert, which leans on an
internal wiki. Re-sync it with:

```bash
.venv/bin/python scripts/scrape_woo_kb.py            # incremental, skips unchanged
.venv/bin/python scripts/scrape_woo_kb.py --plugin ups
.venv/bin/python scripts/scrape_woo_kb.py --list     # discover only
```

Discovery is sitemap-driven, so new KB articles are picked up automatically.
Articles whose slug names another platform (Shopify, Magento, PrestaShop,
BigCommerce) are excluded.

## What This App Does

The dashboard helps QA move a release through these stages:
1. load Trello release cards
2. validate and refine AC
3. generate and publish test cases
4. run AI QA verification
5. generate or update automation
6. run automation, post results, generate docs, and raise bugs
7. prepare sign-off and handoff output

Entrypoint:
- [pipeline_dashboard.py](pipeline_dashboard.py:1)

## Current Dashboard Tabs

Top-level tabs:
1. `📝 User Story`
2. `🔀 Move Cards`
3. `🧾 Validate AC`
4. `🧪 Generate TC`
5. `🤖 AI QA Verifier`
6. `⚙️ Generate Automation Script`
7. `📋 History`
8. `✅ Sign Off`
9. `📘 Handoff Docs`

Planned next major workflow:
- `🚚 New Carrier Validation`
  - verify the site is reachable and the plugin is active at the right version
  - set store address, units, currency
  - create the shipping zone and attach the PluginHive method
  - manual carrier-registration checkpoint (no API exists for this)
  - seed the deterministic QA product catalogue
  - generate the carrier env file with product IDs
  - run smoke / sanity / regression
  - publish readiness report

## Current QA Flow

Shared release state is loaded in `🧾 Validate AC` and reused in downstream tabs.
QA can narrow the loaded cards before `Load Cards`, then adjust the active-card subset from any pipeline tab without reloading the Trello list.

## Codex / Claude Skill Bundle

Repo-local skills live under [skills](skills:1). They mirror the MCSLDomainExpert
skill pipeline but use WooCommerce-native admin paths, evidence rules, automation
repo paths, labels, and support-doc structure.

Core cycle:
1. `woo-domain-core`
2. `woo-trello-operator`
3. `woo-ac-writer-reviewer`
4. `woo-dashboard-tc-publisher`
5. `woo-ai-qa-testcase-prep`
6. `woo-ai-qa-browser`
7. `woo-automation-writer`
8. `woo-bug`
9. `woo-signoff-message`
10. `woo-handoff-docs`

Maintenance and external workflow helpers:
- `woo-rag-sync`
- `woo-knowledge-maintainer`
- `woo-slack-operator`
- `woo-store-actions` — WooCommerce REST API cookbook
- `woo-feature-prerequisites` — what must be configured before a card is testable

When dashboard behavior changes materially, update the matching skill alongside [AGENTS.md](AGENTS.md:1) and this README.

### Handoff Docs Format
- take the guide title from the user prompt, not Trello metadata
- use only the prompt's plugin name as the guide title and single-guide file base
- place `Version <no> – Released: <date>` directly under the H1
- do not show an automatic `UPDATE` badge in the header
- use `PluginHive: WooCommerce` as the header subtitle
- make the version/release line slightly more prominent in the header
- use exactly these index columns: `Story Id`, `Title`, `Trello Card Link`
- render `Included Story Cards` in the boxed section-heading style
- keep the `Story Id` column wide enough to read cleanly
- default to one Support Guide when the user says to generate the guide without naming a doc type
- start each story card with a boxed title block for visual separation
- do not add an extra accent strip inside that boxed title block
- do not add an extra accent strip inside the boxed `Included Story Cards` heading either
- keep normal sections free of internal or technical detail
- keep developer-only cards in the trailing `Technical Cards` section
- do not include feature-flag wording in handoff docs

### `🧾 Validate AC`
- select Trello board, list, and release label
- optionally select a subset of cards from the chosen list
- click `Load Cards`
- auto-run per-card Woo validation and diagnosis
- auto-run release-level `Release Intelligence`
- show `Step 1: Card Requirements`
- run WooCommerce site prerequisite checks when needed (plugin version, zone, method settings)
- generate or review `AI Suggested User Story & AC`
- save, comment, skip, or share AC
- run `Domain Validation`
- apply fixes and re-validate

Important current behavior:
- there is no separate manual `Analyze loaded cards` step
- active-card subset editing stays available after load across Validate AC, Generate TC, AI QA, and Automation
- generated AC is revalidated immediately
- fix and revalidate preserve requirement research context

### `🧪 Generate TC`
- generate test cases from the current AC draft in session
- reuse saved TCs when present
- regenerate with reviewer feedback
- support manual edits and explicit re-review
- share to Slack DM or channel
- publish full QA summary to Trello
- publish positive TCs to Google Sheets
- perform duplicate checks before sheet write

Important current behavior:
- TC generation does not rely only on stale `card.desc` when a newer AC draft exists
- retry after partial publish failure should not duplicate the Trello summary comment

### `🤖 AI QA Verifier`
- runs TC-first AI QA against the live app
- uses the WooCommerce browser flow by default; if a card names Shopify, BigCommerce, Magento, or PrestaShop, ask QA first and run it only when QA confirms the shared behaviour should be tested through the available flow
- reuses generated and reviewed test cases
- normalises navigation wording to wp-admin destinations such as `orders`, `products`, `shipping`, `pluginsettings`, and `upsregistration` — WooCommerce admin is URL-addressable, so navigation is a goto, not a click chain
- uses the `ups-woo-automation` page-object locators for the order metabox (Generate Packages → Calculate Rates → Confirm Shipment → Print Label), bulk actions, plugin settings select2 widgets, and request/response `<pre>` logs
- supports `qa_needed` follow-up and reruns
- supports failed-finding review and notify-dev flow
- supports ask-domain-expert
- persists final approval for downstream automation and sign-off

### `⚙️ Generate Automation Script`
- `① Write Automation Code`
- Playwright generation targets `ups-woo-automation` only
- cards explicitly scoped to Shopify, BigCommerce, Magento, or PrestaShop should not generate automation yet
- detect existing-vs-new automation targets with `feature_detector` and `find_pom`
- optional Chrome-agent exploration for locator grounding
- auto-fix loop for generated code
- `② Run Automation & Post to Slack`
- `③ Generate Documentation`
- `🐛 Bug Reporter` for manual QA-found bugs

## Woo-Specific Rules

### Validation And Analysis

These stay Woo-native:
- `validate_card(...)`
- `diagnose_customer_ticket(...)`
- `analyse_release(...)`
- `build_requirement_research_context(...)`

MCSL parity work should change workflow shape and UX order, not replace
WooCommerce rules with Shopify rules.

### Prerequisite ("Toggle") Flow

MCSL toggles are SaaS feature flags keyed by an account UUID. WooCommerce has no
equivalent — the plugins are self-hosted. Here a prerequisite is one of:

- **which plugin version is active** on the site (`system_status` → `active_plugins`)
- **a plugin setting** on the Multi-Carrier shipping method
  (`shipping/zones/<id>/methods/<instance_id>` → `settings`)
- **a WooCommerce core setting** (`settings/<group>/<id>`)

So the capture runs over the REST API rather than by driving a browser:
- detect prerequisites from card title, description, and comments
- read live site state over `wc/v3`
- compute enabled / missing / unknown before notifying
- notify the assigned developer through Slack
- poll for confirmation and unblock QA when confirmed

Key files:
- [pipeline/toggle_state.py](pipeline/toggle_state.py:1)
- [pipeline/woo_api.py](pipeline/woo_api.py:1)
- [tests/test_toggle_state.py](tests/test_toggle_state.py:1)

### Automation Matching

Automation generation should prefer updating existing Woo automation when a matching area already exists.

Key files:
- [pipeline/automation_writer.py](pipeline/automation_writer.py:1)
- [pipeline/feature_detector.py](pipeline/feature_detector.py:1)

## Important Files

- [pipeline_dashboard.py](pipeline_dashboard.py:1)
- [pipeline/card_processor.py](pipeline/card_processor.py:1)
- [pipeline/smart_ac_verifier.py](pipeline/smart_ac_verifier.py:1)
- [pipeline/domain_validator.py](pipeline/domain_validator.py:1)
- [pipeline/automation_writer.py](pipeline/automation_writer.py:1)
- [pipeline/feature_detector.py](pipeline/feature_detector.py:1)
- [pipeline/doc_generator.py](pipeline/doc_generator.py:1)
- [pipeline/bug_tracker.py](pipeline/bug_tracker.py:1)
- [pipeline/request_expectations.py](pipeline/request_expectations.py:1)
- [pipeline/carrier_knowledge.py](pipeline/carrier_knowledge.py:1)
- [pipeline/woo_api.py](pipeline/woo_api.py:1) — WooCommerce REST client
- [pipeline/woo_admin.py](pipeline/woo_admin.py:1) — wp-admin URL builders
- [pipeline/woo_product_seed.py](pipeline/woo_product_seed.py:1) — deterministic catalogue
- [scripts/scrape_woo_kb.py](scripts/scrape_woo_kb.py:1) — KB sync

## Local References

Expected sibling repo (shared workflow shape, Shopify platform):
- `../MCSLDomainExpert`

Expected local repos:
- `config.WOO_AUTOMATION_REPO_PATH` → `ups-woo-automation`
- `config.WOO_PLUGIN_REPO_PATH` → `multi-carrier-shipping-plugin-for-woocommerce`
- `config.WOO_SHIPPING_PRO_REPO_PATH` → `woocommerce-shipping-pro`

## Run Locally

```bash
cd "$WOO_REPO"  # path to your WooCommerceDomainExpert clone
PYTHONPATH=. .venv/bin/streamlit run pipeline_dashboard.py
```

## Slack QA Bot

Ask QA questions from Slack and get answers in-thread. Backed by
`pipeline/slack_qa_bot.py` (Socket Mode daemon), `pipeline/qa_question_router.py`
(routing), and `pipeline/qa_metrics.py` (deterministic counts).

The bot answers only when **explicitly addressed**, so multiple domain-expert bots
(Woo, FedEx, AUPost) can share a channel without all of them replying:
- **DM** the bot — every DM is answered.
- **@mention** the app in a channel (real Slack mention → `app_mention`, routed only
  to this app).
- **Trigger keyword** in an allowlisted channel (`SLACK_QA_CHANNELS`), e.g.
  `@woobot how many cases ran?`. Keywords come from `SLACK_QA_TRIGGERS`
  (default `woobot`); a leading `@` is optional. Un-addressed chatter is ignored.

It can also **generate Woo support guides** (PDF) from Trello:
- `@woobot generate support guide for <card url/id>` → one card → PDF
- `@woobot generate support guide for lane "<name>"` → one combined PDF
- `@woobot generate per-card support guides for lane "<name>"` → one PDF per card

Routing:
- Metric intents → exact counts (no LLM). e.g. *"how many cases automated"* →
  spec/`test()` counts; *"how many cases ran in the release"* → latest
  `reports/ai-summary.json` from the automation repo.
- Support-guide intents → Trello fetch + `handoff_docs` PDF (needs `files:write` scope + `reportlab`).
- Everything else → RAG over **both** the wiki/KB collection and the
  automation/code collection.

> To make the real autocomplete mention read `@wooBot`, rename the app's bot user
> in Slack (App → **App Home** → *Edit* the display name / default username). The
> `SLACK_QA_TRIGGERS` keyword works regardless of the app's display name.

### One-time Slack app setup

1. **Socket Mode** → enable → create an **App-Level Token** with `connections:write`
   → put it in `.env` as `SLACK_APP_TOKEN=xapp-...`.
2. **Event Subscriptions** → subscribe to bot events: `app_mention`, `message.im`,
   and `message.groups` (private channels) / `message.channels` (public channels).
3. **OAuth scopes**: `app_mentions:read`, `chat:write`, `im:history`, `im:read`,
   `im:write`, and `groups:history` (for private channels) / `channels:history`
   (for public). Reinstall the app if you add scopes. Invite the bot to the channel.

### Env

```bash
SLACK_BOT_TOKEN=xoxb-...                 # already used by the rest of the app
SLACK_APP_TOKEN=xapp-...                 # Socket Mode app-level token
SLACK_QA_CHANNELS=qa_members_internal    # optional; comma-separated names or IDs
SLACK_QA_TRIGGERS=woobot                 # optional; channel address keyword(s), default 'woobot'
```

### Run

```bash
scripts/run_slack_bot.sh --check    # verify tokens/config
scripts/run_slack_bot.sh            # start the daemon (leave running)
```

## Focused Validation Commands

```bash
.venv/bin/python -m py_compile pipeline_dashboard.py pipeline/card_processor.py
.venv/bin/python -m pytest -q                       # full suite
.venv/bin/python -m pytest -q tests/test_toggle_state.py
.venv/bin/python -m pytest -q tests/test_kb_loader.py
.venv/bin/python -m pytest -q tests/test_label_flows.py
.venv/bin/python -m pytest -q tests/test_qa_question_router.py
```

## Setup

```bash
python3.11 -m venv .venv
.venv/bin/pip install -r requirements.txt
cp .env.template .env        # then fill in the values
.venv/bin/python scripts/scrape_woo_kb.py
PYTHONPATH=. .venv/bin/python ingest/run_ingest.py --sources kb_articles
```

## Supporting Docs

- [CLAUDE.md](CLAUDE.md:1)
- [docs/FEDEX_FLOW_PARITY_NOTES.md](docs/FEDEX_FLOW_PARITY_NOTES.md:1)
- [docs/WOO_PLATFORM_ADAPTATION_PLAN.md](docs/WOO_PLATFORM_ADAPTATION_PLAN.md:1)
- [docs/WOO_CARRIER_KNOWLEDGE_RESEARCH.md](docs/WOO_CARRIER_KNOWLEDGE_RESEARCH.md:1)
- [docs/WOO_CARRIER_SUPPORT_REGISTRY.md](docs/WOO_CARRIER_SUPPORT_REGISTRY.md:1)
- [docs/WOO_CARRIER_CAPABILITY_MATRIX.md](docs/WOO_CARRIER_CAPABILITY_MATRIX.md:1)
- [docs/WOO_CARRIER_REQUEST_REGISTRY.md](docs/WOO_CARRIER_REQUEST_REGISTRY.md:1)
- [docs/NEW_CARRIER_VALIDATION_PLAN.md](docs/NEW_CARRIER_VALIDATION_PLAN.md:1)
