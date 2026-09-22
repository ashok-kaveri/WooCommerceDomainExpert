---
name: woo-handoff-docs
description: Use when working inside the WooCommerceDomainExpert project after cards are approved and the user wants professional release handoff documents like the dashboard Handoff Docs tab: Support Guide, Business Brief, or both, generated from approved US/AC, TCs, AI QA evidence, release/card metadata, prerequisites, and member ownership. If the user requests only one document, generate only that document and PDF.
---

# Woo Handoff Docs

Use this skill to generate professional handoff documents for approved PluginHive Woo release cards on WordPress/WooCommerce.

It mirrors the dashboard `Handoff Docs` tab:

- Combined release Support Guide
- Combined release Business Brief
- Optional single-card Support Guide / Business Brief for quick review
- Markdown + PDF output
- Trello/Slack-ready artifacts when requested

Default release delivery is one combined PDF per document type. If the user asks for only one document type, generate only that combined document. Use single-card documents only when the user explicitly asks for one card.

## First Reads

Before generating:

1. Read `AGENTS.md`.
2. Read:
   - `skills/woo-handoff-docs/references/handoff_doc_formats.md`
3. Inspect only directly relevant project files:
   - `pipeline/handoff_docs.py`
   - `pipeline_dashboard.py`

Use `woo-domain-core` research when local context is incomplete or customer-facing explanations need current Woo/PluginHive/WooCommerce facts.
Use `woo-trello-operator` to fetch card details/members or attach/comment PDFs when explicitly requested.
Use `woo-slack-operator` to send PDFs or messages to Slack when explicitly requested.

For release packages, always use full live Trello card context when available: description, comments, labels, attachments/checklist summaries, approved AC/TCs, and AI QA evidence. QA comments often contain late caveats and must not be skipped.

**Testing observations in comments are not guide content.** QA and developer comments also record what someone noticed while testing: a troubleshooting tip, an unrelated defect, or a limitation the commenter explicitly calls separate from this card's change. Those are internal testing notes — never copy them into `Prerequisites`, `Expected Behaviour`, or any other section. A comment belongs in the guide only when it states something this card's change requires or affects. See `Observations vs. Release Content` in `references/handoff_doc_formats.md`.

## Document Title & Release Header

The document title comes from the **user's prompt**, not from the Trello release list name, board name, or a card title. Expect the prompt to carry the plugin name, the version, and the release date, for example:

```
Plugin Name: Multi-Carrier Shipping Plugin for WooCommerce
Version 3.4.2 – Released: Aug 18th, 2026
```

Build the document from exactly that:

- H1 = `# <Plugin Name>`
- the line immediately after the H1 = `Version <version> – Released: <release date>`
- `--title` passed to the render script = `<Plugin Name>`
- when generating a single requested guide, markdown/PDF filename base = `<Plugin Name>`

Example opening of a combined Support Guide:

```markdown
# Multi-Carrier Shipping Plugin for WooCommerce

Version 3.4.2 – Released: Aug 18th, 2026

## Included Story Cards
| Story Id | Title | Trello Card Link |
|---|---|---|
```

Renderer behaviour this relies on, in `render_pdf_bytes`:

- the H1 is stripped from the body, and the `--title` argument becomes the large header title
- the first non-heading, non-bullet line after the H1 becomes the italic line inside the navy header panel — that is where the version/release-date line lands, so keep it to one short line
- the gold subtitle strip is generated from the title and platform scope, so do not hand-write it

Rules:

- keep the version and release date exactly as the user wrote them, including the month format they used
- state the version and release date once, in the header line only — never repeat them in a card section
- never invent, infer, or bump a plugin name, version number, or release date. If the prompt is missing one, ask for it once before rendering; if the user says to proceed without it, write `Version not provided` rather than a guess
- if the user gives a different title wording in the prompt, use their wording verbatim

## Excluded Cards

Before anything else, drop cards that are not part of the release story set. Exclude any card carrying one of these labels:

- `SL: ON Hold`
- `SL: Carrier Platform`
- `Spill Over`
- `SL: Closed By Support`

Rules:

- Match labels case-insensitively and tolerate emoji, colour prefixes, and extra spacing around the name.
- Exclude the card from the index table as well as the body. A card left out of the body but listed in the index reads as a missing section.
- Include an excluded card only when the user names it or explicitly asks for it. Naming the card is the instruction — do not ask again.
- Never drop the card silently. Always report which cards were excluded and which label triggered it, so a short release is visibly deliberate.

## Prerequisite Audit

Before writing a release package, check every card for prerequisites — anything that must already be true on the site before the feature can be seen or demoed.

A prerequisite here is one of:

- the plugin build the card needs
- a plugin setting a merchant has to turn on
- a WooCommerce store setting
- a manual carrier registration in the WordPress admin

Rules:

- Search the whole card, not just the description: comments, checklists, attachments, approved AC, TCs, and QA evidence. A late prerequisite is often named only in a QA or developer comment.
- A prerequisite is something the reader needs in place to use or verify *this card's change*. A testing observation is not a prerequisite, even when it appears in the same comment: a tip for diagnosing an unrelated failure, a defect seen in passing, or anything the commenter flags as pre-existing or unrelated stays out of the document. Report it in the final response instead.
- Write prerequisites in the card's `Prerequisites` section in plain merchant language — the setting as a support person would read it on screen, plus where to find it.
- Say so explicitly when a card needs nothing set up beforehand.
- Never guess. If a card clearly needs something enabled but the card never says what, write `Not stated in the card` and flag it in the final response.
- There is no prerequisite column in the index table. The index table stays three columns: `Story Id`, `Title`, `Trello Card Link`.

## No Internal Or Technical Detail In Normal Sections

Both documents are written for people who have never seen the code. Keep internal and technical detail out of all normal card sections and the release overview.

Not allowed anywhere outside the `## Technical Cards` section:

- code, class, file, method, or function names
- request or response field names, node names, payload or log field names
- API, endpoint, schema, database, hook, or filter references
- version strings used as an explanation, internal engineering terms, ticket-tracker jargon
- callouts naming an exact request or log field, such as `Request node to verify:`. These belonged to the old format and must not appear

Describe what support sees on screen and what the merchant experiences instead. When a card's evidence points at a carrier request or a log, say what support should look for in plain words — "the rate shown at checkout now includes the discounted price" — and where to look, without naming the field.

Purely internal or developer-only cards still belong in the combined document, but only inside the trailing `## Technical Cards` section.

## Technical Cards

Use one trailing `## Technical Cards` section after all normal card sections.

Rules:

- Put every purely internal or developer-only card here
- Keep the card in the index table in its normal release position
- Use `### <Story ID> - <Card title>` for each entry
- Keep each entry to two to four lines: what changed and why it matters
- Avoid deep internals even here; mention an exact internal name only when the entry makes no sense without it
- Do not add walkthrough, prerequisites, or expected-behaviour subsections inside this section

## Platform Audit

Before writing Support Guide or Business Brief content, run this audit for every card:

- Detect the customer/test platform from the title, labels, description, comments, linked ticket, PR notes, AC, TCs, and QA evidence.
- If no platform is explicit, default the QA/support platform to WooCommerce (WordPress).
- If a customer/ticket explicitly names BigCommerce, Magento, or PrestaShop, use that platform in support steps, prerequisites, and business wording.
- Treat the underlying feature as shared Woo behavior unless the card limits the implementation scope, but document/test on the customer-reported platform.

## Inputs

Best input package:

- plugin name, version, release date (from the prompt — see `Document Title & Release Header`)
- card name/id/url
- release name
- approved US + AC
- reviewed TCs
- AI QA summary/evidence
- support sign-off notes
- developed by / tested by
- prerequisites
- known limitations
- rollout notes

If some inputs are missing, still generate a useful draft, but mark unknown fields clearly. Do not invent ownership, release numbers, versions, dates, prerequisites, or unsupported limitations.

## Document Selection

Generate based on user request:

- "support guide", "support doc", "demo doc", "customer support explanation" -> combined release Support Guide only
- "business brief", "business doc", "stakeholder doc", "marketing/sales summary" -> combined release Business Brief only
- "handoff docs", "both docs", "support and business" -> both combined release PDFs
- "single card", "only this card", or a specific card id/name -> single-card document for that card

If the user just says to generate the handoff/guide without naming a doc type, default to one combined Support Guide.

## Support Guide Purpose

The Support Guide is for support/demo teams who need to understand the feature well enough to explain it to customers.

It must be practical, professional, support-friendly, and very crisp, with no technical jargon at all outside `Technical Cards` — see `No Internal Or Technical Detail In Normal Sections`.

- Include the Index Page with exactly these columns: "Story Id", "Title", "Trello Card Link"
- Explain the brief feature summary under a heading called "Brief Description". Keep it very crisp
- include where support can see it inside the relevant walkthrough steps
- explain what the merchant should experience
- include walkthrough steps
- include prerequisites

Do not write vague release notes. This should be a real support enablement document.

## PDF Generation

When the user asks for PDF:

1. Generate the markdown first.
2. Save the markdown under `data/handoff_docs/`.
3. Render PDF using:
   `skills/woo-handoff-docs/scripts/render_handoff_pdf.py`

Pass the prompt-derived title so the header panel matches the document:

```bash
python3 skills/woo-handoff-docs/scripts/render_handoff_pdf.py \
  --markdown "data/handoff_docs/Multi-Carrier Shipping Plugin for WooCommerce.md" \
  --title "Multi-Carrier Shipping Plugin for WooCommerce"
```

For one requested release document, create one combined PDF containing all selected/approved release cards.

For both, create two combined PDFs: one Support Guide package and one Business Brief package.

## Slack Delivery

Send with `scripts/send_handoff_pdf_to_slack.py`. Nothing is sent without `--yes`, so always dry-run first and show the resolved target.

```bash
# dry run — prints target, filename, size, message text
python3 scripts/send_handoff_pdf_to_slack.py --pdf <pdf path> --title "<doc title>"

# DM to the doc owner (default target)
python3 scripts/send_handoff_pdf_to_slack.py --pdf <pdf path> --title "<doc title>" --yes

# team channel: bare --channel targets qa_members_internal
python3 scripts/send_handoff_pdf_to_slack.py --pdf <pdf path> --title "<doc title>" --channel --yes
```

**When the request already names a destination, that is the approval — do not ask again.**
"DM me the PDF", "send it to me", "share it in #qa-team" all authorise that one send: dry-run,
then send in the same turn, then report the target and file id. Re-sending a corrected version
of a document the user already asked to be sent needs no fresh approval either.

Ask first only when:

- the user asked for a document but named no destination, or
- the send target differs from the one they named — in particular, approval for a DM is never
  approval for a team channel, and vice versa.

Always report the outcome: target, file id on success, or the exact Slack error on failure.

## Combined Release Package Structure

Combined Support Guide:

```markdown
# <Plugin Name>

Version <version> – Released: <release date>

## Included Story Cards
| Story Id | Title | Trello Card Link |
|---|---|---|

## <Story ID> - <Card title>
### Brief Description
...

## Technical Cards
### <Story ID> - <Card title>
...
```

Do not add a `How Support Should Use This Package` section. The index page is followed directly by the first card section.

Combined Business Brief:

```markdown
# <Plugin Name>

Version <version> – Released: <release date>

## Release Overview
...

## Included Updates
| Story Id | Title | Trello Card Link |
|---|---|---|

## <Story ID> - <Card title>
### Brief Description
...

## Technical Cards
### <Story ID> - <Card title>
...
```

## Support Guide Structure

For each card section inside the combined Support Guide, follow the sample release support guide style:

```markdown
# Support Guide: <Story ID or concise feature name>

## Brief Description
...

## Prerequisites
...

## Step-by-Step Support Walkthrough
...

## Expected Behaviour
...
```

Do not add `Merchant-Safe Explanation`, `Common Questions & Troubleshooting`, or `Support Escalation Packet` sections. The card section ends after `Expected Behaviour`.

## Quality Bar

Before finalizing:

- make it understandable for support people
- verify the header carries the prompt's plugin name, version, and release date, and that nothing about them was invented
- verify the index table has exactly three columns: `Story Id`, `Title`, `Trello Card Link`
- verify no internal setup shorthand or feature-flag wording appears anywhere in either document
- verify no technical detail survived outside `Technical Cards` — no field, node, class, file, endpoint, or log-field names, and no `Request node to verify:` style callouts
- verify no card labelled `SL: ON Hold`, `SL: Carrier Platform`, `Spill Over`, or `SL: Closed By Support` slipped into the index table or the body
- verify purely internal-only cards were moved to `Technical Cards`
- keep merchant-facing wording safe and clear
- do not expose implementation details that customers do not need
- verify every claim comes from card/AC/TC/AI QA evidence or researched domain facts
- verify every live Trello QA comment and checklist has been considered before finalizing a release package
- verify no testing observation from a comment has been written into the document as a prerequisite, caveat, or known limitation
- do not add a generic `Where to Find This in Woo` section; include exact platform-aware navigation in the relevant walkthrough step instead
- every story card starts on a new page, including the first — the index page stands alone and the renderer inserts the breaks, so never hand-place one
- verify no card heading starts at the bottom of a page without its detail table/content following on the same page
- keep the support guide thorough enough for a support call
- keep the business brief short and polished

## Final Response

Return:

- document(s) generated
- the title, version, and release date used in the header
- markdown path if saved
- PDF path if rendered
- which cards were excluded and the label that triggered each exclusion
- any missing inputs or assumptions

Use absolute file paths in final responses.
