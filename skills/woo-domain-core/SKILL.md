---
name: woo-domain-core
description: Use when working inside the WooCommerceDomainExpert project and the user asks anything about PluginHive's WooCommerce shipping plugins on WordPress/WooCommerce — Multi-Carrier Shipping, the per-carrier plugins (UPS, FedEx, Canada Post, USPS, Royal Mail, Australia Post, DHL, Aramex), Table Rate Shipping Pro, Shipment Tracking Pro, Estimated Delivery Date, Bookings — their QA domain, wp-admin flows, carrier/API behaviour, project architecture, the PluginHive knowledge base, local RAG/code knowledge, or wants research-backed answers that may require browsing beyond the indexed knowledge base. This is the shared domain/research core for AC, TC, AI QA, automation, handoff, and support tasks.
---

# Woo Domain Core

Use this skill as the shared knowledge and research layer for the WooCommerceDomainExpert project.

It should make Codex/Claude behave like the project Domain Expert:

- know the WooCommerce plugin architecture, with WordPress admin as the live AI QA/automation surface
- understand dashboard pipeline stages
- use local project knowledge before guessing
- browse official/current sources when local knowledge is missing or stale
- cite where facts came from
- feed research-backed conclusions into US/AC, TC, AI QA, automation, and handoff work

## First Reads

Always start with:

1. `AGENTS.md`
2. `CLAUDE.md` if extra session context is needed
3. `skills/woo-domain-core/references/research_workflow.md`
4. `docs/kb_snapshots/` — the local mirror of the PluginHive knowledge base, and
   this project's primary knowledge source

Then read only the project files directly relevant to the task.

## What This Skill Covers

Use for questions or tasks about:

- PluginHive plugin behaviour on WordPress/WooCommerce
- wp-admin plugin settings screens and the storefront cart/checkout rate flow
- platform-specific navigation for docs and manual QA when a card names Shopify,
  BigCommerce, Magento, or PrestaShop
- the order-screen label flow: Generate Packages → Calculate Rates → Confirm
  Shipment → Print Label
- bulk label generation via the WordPress bulk-action control
- shipping zones, shipping methods, and why a rate does or does not appear
- shipping classes, box packing, per-item packing, weight/dimension units
- carrier request/response fields and constraints
- return labels, void shipment, client-side reset
- product-level shipping fields and per-carrier special services
- request/response logs (the `<pre>` blocks and WooCommerce → Status → Logs)
- generated AC/TC correctness
- AI QA evidence strategy
- automation/POM/spec patterns
- support/business handoff facts
- research that local RAG may not have yet

## Research Order

Use this order:

1. `AGENTS.md` and local skills
2. **`docs/kb_snapshots/`** — the PluginHive KB mirror; grep it before anything
   else for product behaviour, setup steps, and troubleshooting. Each file's
   header carries the live `Source:` URL to cite and the `Plugin:` it belongs to.
3. local project files
4. plugin source under `WOO_PLUGIN_REPO_PATH` / `WOO_SHIPPING_PRO_REPO_PATH`
5. automation repo files under `WOO_AUTOMATION_REPO_PATH`
6. Chroma-backed RAG context if the index is built
7. official/current web sources when needed

Quick KB lookup:

```bash
grep -ril "residential address" docs/kb_snapshots/ | head
grep -l "Plugin: ups" docs/kb_snapshots/*.md | wc -l
```

If the KB mirror is empty or stale, re-sync it rather than guessing:

```bash
.venv/bin/python scripts/scrape_woo_kb.py
```

Browse the web when:

- the user asks to research, browse, verify, or use latest/current information
- the KB mirror does not answer the question
- WooCommerce/WordPress/PluginHive or carrier rules may have changed
- public docs/API behavior is needed for AC/TC correctness
- a linked PR, docs page, Zendesk, changelog, or issue is referenced and its content is not already provided

For web research, prefer:

- the live PluginHive knowledge base — `https://www.pluginhive.com/knowledge-base/`
  (the local mirror may lag; the live page is authoritative)
- official PluginHive product and docs pages
- official WooCommerce and WordPress developer docs
- the carrier's own API documentation for request/response field questions
- project-linked PRs/issues/docs if accessible

Avoid relying on random blogs unless no official source exists, and clearly mark any inference.

## Answer Style

For Q&A:

- answer directly
- mention local/project source and web source when used
- separate known fact from inference
- include exact file references for local code facts
- include links for web sources

For generation tasks:

- summarize the research that matters
- use the research to improve the output
- do not dump long source notes unless the user asks

## Relationship To Other Skills

Other Woo skills should use this skill's research posture:

- `woo-trello-operator`: fetch the real card/list/comments/members first when the user gives Trello references.
- `woo-ac-writer-reviewer`: research first, then generate/review US + AC, then Trello comment only.
- `woo-dashboard-tc-publisher`: generate dashboard TCs, compact Trello comment, and positive-only CSV rows for the `Ai` tab.
- `woo-ai-qa-testcase-prep`: create detailed AI QA executable TCs when browser verification needs richer steps.
- `woo-ai-qa-browser`: verify reviewed TCs in Chrome with evidence, cleanup, and locator trace handoff.
- `woo-automation-writer`: use reviewed TCs plus AI QA evidence/locator traces to write Playwright automation in `WOO_AUTOMATION_REPO_PATH`.
- `woo-bug`: format QA-found bugs, check Backlog duplicates, and create Trello Backlog cards only when asked.
- `woo-signoff-message`: fetch release/list cards, ask for Backlog links, prepare the QA sign-off message, and send to Slack only after QA confirms channel/message.
- `woo-handoff-docs`: generate Support Guide and/or Business Brief PDFs from approved cards.
- `woo-slack-operator`: search users/channels, read messages, reply in threads, and send DMs/channel posts only when asked.
- `woo-rag-sync`: re-scrape the PluginHive KB and safely sync/reindex plugin
  source, automation, and KB knowledge.
- `woo-store-actions`: run WooCommerce REST API actions against a QA site.
- `woo-feature-prerequisites`: check what must be configured before a card is testable.
- `woo-knowledge-maintainer`: after the card cycle, update approved-card RAG, QA feedback, and outdated durable rules.

Normal card-cycle order:

```text
Trello card/list/comments
  -> domain research
  -> US + AC comment
  -> dashboard TCs + Trello/CSV publish package
  -> AI QA browser verification + locator trace
  -> bug follow-up if needed
  -> automation writer
  -> sign-off message
  -> handoff docs
  -> RAG sync if source repos/docs changed
  -> knowledge maintainer
```

Use Trello/Slack operator skills for actual external reads/writes. Generation skills should prepare content; operator skills should perform Trello/Slack actions when the user clearly asked for those actions.

## Do Not

- Do not invent plugin limits or carrier API rules.
- Do not assume the KB mirror or local RAG is complete.
- Do not use stale memory for current WooCommerce/WordPress/PluginHive rules if
  browsing is available and relevant.
- Do not carry Shopify/MCSL assumptions across: there is no app iframe, no single
  app endpoint, no hamburger navigation, and no account-UUID feature toggles.
- Do not update Trello, Slack, Sheets, or repo files unless the user asks for that action.
- Do not browse for secrets or private data.
