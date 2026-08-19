# Handoff Document Formats

This reference is based on:

- `pipeline/handoff_docs.py`
- dashboard `Handoff Docs` tab
- sample support package `docs/Woo378_Support_Guide.docx`

## Document Header

The title is built from the user's prompt, never from a Trello list, board, or card. The prompt carries the plugin name, version, and release date:

```
Plugin Name: Multi-Carrier Shipping Plugin for WooCommerce
Version 3.4.2 – Released: Aug 18th, 2026
```

Which becomes:

```markdown
# Multi-Carrier Shipping Plugin for WooCommerce

Version 3.4.2 – Released: Aug 18th, 2026
```

Rules:

- H1 = `<Plugin Name>`, and the same string is passed to the render script as `--title`
- the version/release-date line sits immediately after the H1, as the first body line, and nowhere else
- keep the user's own version and date formatting, including the month style they wrote
- never invent or bump a plugin name, version, or date; ask once when the prompt omits one

How `render_pdf_bytes` consumes it:

- the H1 is stripped from the body, and `--title` becomes the large navy-panel title
- the first non-heading, non-bullet line after the H1 becomes the italic description line in the header panel — that is the version/release-date line, so keep it short and on one line
- the gold subtitle strip is generated from the title and platform scope; do not hand-write it

## Sample Support Guide Style

The attached release package uses:

- branded PluginHive / WooCommerce Woo Shipping App release header
- plugin name, release version and release date in the header
- no automatic `UPDATE` badge in the header
- a slightly more prominent version/release-date line in the header
- one combined release PDF with card-by-card sections
- support guide label
- release details
- index page with `Story Id`, `Title`, `Trello Card Link`
- a boxed heading treatment for `Included Story Cards`
- a wider `Story Id` column so the header reads cleanly
- brief description
- prerequisites
- support/demo walkthrough
- expected behavior

Support guide examples from the sample:

- explain background silently operating fixes clearly
- state when nothing needs to be set up beforehand
- specify scope such as international-only or domestic-only
- give concrete scenarios with expected support observations

## Support Guide Tone

Professional, practical, support-ready.

Audience:

- support team
- demo team
- implementation/support leads

The support reader should be able to explain the feature to a merchant without asking engineering.

Use:

- clear brief description
- concrete paths and steps
- "what support should observe"

Avoid:

- technical detail of any kind in a normal card section — code, class, file, or method names, request/response or log field names, node names, API, schema, endpoint, hook, or database references, internal engineering terms, and `Request node to verify:` style callouts. The `Technical Cards` section is the only exemption
- internal setup shorthand or feature-flag wording
- deep code/internal implementation details
- vague "works correctly" wording
- unsupported claims
- excessive QA/test-count language

## Combined Support Guide Required Sections

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

Index page rules:

- use exactly three columns: `Story Id`, `Title`, `Trello Card Link`
- render `Included Story Cards` inside the boxed section-heading treatment
- keep the `Story Id` column wide enough to avoid cramped header wrapping
- `Story ID` is the story/card number only
- `Title` is the card title
- `Trello Card Link` is a markdown link to the card, labelled with the story id, for example `[941](https://trello.com/c/abc123)`; use `-` when no card URL is known
- list technical cards in their normal position here even though their body section moves to the end
- add no further columns — prerequisites live in each card's `Prerequisites` section, not in this table

## Per-Card Support Guide Required Sections

```markdown
# Support Guide: <Story ID or concise feature name>

## Brief Description
Very crisp. 1 short paragraph.

## Prerequisites
Anything that must already be true on the site before the feature can be seen or demoed:
the plugin build the card needs, a plugin or store setting to turn on, or a manual carrier
registration. Written the way it reads on screen, with where to find it. Say so plainly when
nothing needs setting up.

## Step-by-Step Support Walkthrough
Use Scenario A/B/C when useful. Put exact navigation inside the action step, for example WooCommerce > Orders, Multi Carrier > <carrier> registration, wp-admin > Products, WooCommerce > Settings > Shipping, WooCommerce > Status > Logs, or the storefront cart/checkout.

## Expected Behaviour
Summarize the key signal.
```

Do not add `Merchant-Safe Explanation`, `Common Questions & Troubleshooting`, or `Support Escalation Packet`. The card section ends after `Expected Behaviour`.

Card section heading rules:

- each story card should start with a boxed heading for `<Story ID> - <Card title>` so the next card is visually distinct
- keep the boxed heading on the new page that opens that card

## Technical Cards Section Structure

```markdown
## Technical Cards

### <Story ID> - <Card title>
Two to four lines: what changed, and why it matters.
```

Rules:

- one `## Technical Cards` H2, placed after the last normal card section, and omitted when the release has no technical cards
- a technical card is developer-only work — API-only change, library or version upgrade, refactor, internal clean-up, infrastructure — with nothing support or the merchant can see or do
- a card with both a technical part and a visible part stays a normal card, and its technical half stays out of the body
- each entry is an H3 so the short entries flow together; the renderer already breaks a page before the `## Technical Cards` H2 itself, so never hand-place a break
- this is the only place technical detail is allowed. Name a version, endpoint, or field only when the entry makes no sense without it, and keep it to the name itself
- no walkthrough, prerequisites, or expected-behaviour subsections inside these entries

## Combined Business Brief Required Structure

```markdown
# <Plugin Name>

Version <version> – Released: <release date>

## Release Overview
2-3 sentences describing the release value.

## Included Updates
| Story Id | Title | Trello Card Link |
|---|---|---|

## <Story ID> - <Card title>
Per-card plain-English business brief.
```

## Per-Card Business Brief Required Structure

```markdown
## <Feature Name in Plain English>
*One sentence headline value.*

### Brief Description
2-3 sentences.

### What's New
- 3-5 bullets.

### Who Benefits
2-3 merchant/support scenarios.

### Availability
One line.
```

Rules:

- max about 400 words
- plain business English
- no developer/tester attribution
- no QA notes
- no internal Trello links in body
- no technical detail
- mention setup only when the merchant or rollout must act, and then in plain words

## Release QA Guardrails

- Build release packages from full live Trello card context when available: description, labels, comments, checklists, approved AC/TCs, and AI QA evidence.
- Treat QA comments as required review input because late caveats often appear there.
- Take the plugin name, version, and release date from the prompt and put them in the header exactly once, per `Document Header`.
- Run a platform audit for every card. Detect WooCommerce, BigCommerce, Magento, or PrestaShop from the card/ticket evidence. If no platform is explicit, default to WooCommerce (WordPress). If a customer/ticket names a non-WooCommerce platform, use that platform in support steps and business wording while treating the feature as shared Woo behavior unless the card limits scope.
- Exclude cards labelled `SL: ON Hold`, `SL: Carrier Platform`, `Spill Over`, or `SL: Closed By Support` from both the index table and the body, matching labels case-insensitively. Include one only when the user names it. Report every exclusion and the label behind it; never drop a card silently.
- Run a prerequisite audit per card across the whole card, not only the description — a late prerequisite is often named only in a QA or developer comment. Write it in plain language in the card's `Prerequisites` section. Never guess; write `Not stated in the card` and flag it.
- Run a technical-card audit per card and collect developer-only cards into the trailing `Technical Cards` section.
- Keep every normal card section free of technical detail, including request, response, payload, and log field names. Say what support should observe on screen and where to look instead.
- Do not include a generic `Where to Find This in Woo` section. The detailed walkthrough is the source of truth for where support should go.
- Keep feature-specific paths and carrier-specific steps inside the walkthrough sections.
- Every story card section starts on a new PDF page, including the first — the index page stands alone. `render_pdf_bytes` inserts a page break before each `<Story ID> - <Title>` heading, so do not add manual page breaks or blank filler.
- Before final PDF generation, verify no card starts at the bottom of a page without the card detail table/content following on the same page.

## PDF Rendering

Use `pipeline.handoff_docs.render_pdf_bytes` through the skill helper script, passing the prompt-derived title:

```bash
python3 skills/woo-handoff-docs/scripts/render_handoff_pdf.py \
  --markdown "data/handoff_docs/Multi-Carrier Shipping Plugin for WooCommerce.md" \
  --title "Multi-Carrier Shipping Plugin for WooCommerce"
```

This gives the same polished dashboard PDF styling.

For a generic "generate the guide" request, render one combined Support Guide PDF. Render a Business Brief or two-document package only when the user explicitly asks for it. Create individual PDFs only for explicit single-card requests.
