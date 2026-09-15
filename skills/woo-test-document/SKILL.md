---
name: woo-test-document
description: Use inside WooCommerceDomainExpert ONLY for the internal QA test-result document — the evidence doc a tester produces by running a card's Trello checklist against the QA store and pasting screenshots per test case, output as .docx plus .pdf. Trigger on "test document", "test result doc", "run the checklist and capture screenshots", "QA evidence document". Do NOT use for release handoff documents, Support Guides or Business Briefs — those belong to woo-handoff-docs and this skill must never generate, alter or re-render them.
---

# Woo Test Document

Build the QA test-result document for a PluginHive WooCommerce release card: the
PluginHive-branded doc with a cover page, Document History and Testing details
tables, the replicated problem, a TEST RESULT summary, then one section per
Trello checklist group with steps, expected result, screenshots and an
`Observation:` line per case.

## Boundary: This Is Not The Support Guide

`woo-handoff-docs` owns release handoff documents — Support Guide and Business
Brief. This skill owns the internal QA test-result document. They share nothing,
and it must stay that way:

| | woo-handoff-docs | woo-test-document |
|---|---|---|
| Audience | support / merchants | QA and dev, internal |
| Content | how the feature behaves, in plain words | per-case steps, screenshots, pass/fail |
| Source | approved US/AC, card narrative | the card's **checklists**, executed |
| Renderer | `pipeline/handoff_docs.py` (reportlab, Markdown → PDF) | `scripts/generate_test_document.py` (python-docx → .docx) |
| Output | `data/handoff_docs/` | `data/test_documents/` |

Rules:

- Never edit `pipeline/handoff_docs.py`, `tests/test_handoff_docs.py`,
  `skills/woo-handoff-docs/**`, or anything in `data/handoff_docs/` from this
  skill. If the test document needs a renderer change, change
  `scripts/generate_test_document.py` only.
- Never reuse the handoff Markdown→PDF pipeline for this document, and never add
  test-document concerns (screenshot slots, per-case status, Observation lines)
  to it.
- The two documents have different house styles. The handoff PDF's navy/gold
  header and boxed story-card sections are **not** this document's format; this
  document follows `references/test_document_format.md`. Do not converge them.
- If the user's request is ambiguous — "generate the document for this release" —
  ask which one they mean rather than guessing. Naming a plugin and a version
  usually means the handoff guide; naming a card and its checklist usually means
  the test document.
- If a single request genuinely needs both, run each skill separately against its
  own inputs and outputs. Do not merge them into one artifact.

## First Reads

1. `AGENTS.md`
2. `skills/woo-test-document/references/test_document_format.md` — the exact layout
3. `scripts/generate_test_document.py` — the renderer
4. `data/test_documents/SI23TDil_steps.json` — a complete worked example

Use `woo-trello-operator` to read cards, `woo-store-actions` for REST-based store
setup, `woo-slack-operator` for sends, and `woo-ai-qa-browser` for browser driving
conventions.

## Input: A Card Or A Lane

The user gives either a single card (`https://trello.com/c/SI23TDil`, or a short
link) or a lane/list name. For a lane, list the cards first and confirm which ones
to run before executing anything — a lane can be a dozen cards and each card is a
real store run.

Read the full card: description, **checklists**, comments, attachments, labels.
The checklists are the test cases. Comments often carry dev notes and late
caveats that change what "expected" means — never skip them.

## Step 0 — Ask Which Environment, And Get Signed In

Do this before reading checklists or writing a single test case. Never infer the
environment and never start executing against whatever store happens to be open.

**The environment is per card, not per session.** Different carriers and cards
live on different stores with different accounts. Resolve it for *each* card and
never carry one card's store over to the next. All three config sources disagreed
on the UPS v6.6.4 card: `.env` `WOO_SITE_URL` and `ups-woo-automation/.env`
`site_url` both said `…-5575216`, while the card was actually tested on
`…-5542255`.

**Expect the user to supply the environment in the request.** This is the normal
path — the store set varies far more than any config file tracks, so the user
gives it inline when asking for the document, typically as:

```
site_url: https://woocommerce-432251-5542255.cloudwaysapps.com/
userName: vyshnavi@pluginhive.com
```

Take `site_url` and `userName` from that verbatim and use them. If the user also
pastes a password, see the credential rules below — acknowledge it, do not use
it, and carry on with the sign-in step.

Resolve in this order, then **always confirm with the user before running**:

1. What the user gave in the request for this card — wins over everything below.
2. **The card itself.** Comments and linked test-result docs usually name the
   store (`Store URL: https://…`). Check attachments too.
3. `carrier-envs/<carrier>.env` → `site_url`, where `<carrier>` comes from the
   card's carrier label (e.g. `UPS`). This file is written by the new-carrier
   flow and may not exist.
4. The automation repo's `.env` (`WOO_AUTOMATION_REPO_PATH`) → `site_url`.
5. This repo's `.env` → `WOO_SITE_URL`.

State which source you used, so a wrong default is visible:

> For card SI23TDil (label: UPS) I'm going to use
> `https://…-5542255.cloudwaysapps.com/` — that's the store named in the card's
> test-result comment. Note `.env` points at `…-5575216` instead. Correct?

Those env files also carry `userName` for the store. Use it to tell the user
*which account* to sign in as; never read or use `pass`.

**For a lane**, resolve every card first, group them by store, and present the
grouping before executing anything:

> These 6 cards span 2 stores: 4 on `…-5542255`, 2 on `…-5575216`. You'll need to
> be signed into both. Run them store by store?

Confirm before proceeding:

- the wp-admin URL, stated back to the user
- that it is a **QA/staging store, not production** — if you cannot tell, ask
- the plugin under test is installed and **active at the version on the card**
- whether creating real orders and carrier shipments on it is acceptable, and
  whether the carrier account is test or live (a test account returns SAMPLE
  labels and masked tracking; a live one bills real money)

**Get a session — check the user's own Chrome first.** This is the default path
and usually means no login step at all.

1. Navigate the user's real Chrome (`mcp__claude-in-chrome__*`) to
   `<store>/wp-admin/` and read the page. If it is the dashboard rather than
   `wp-login.php`, there is already a session: use Chrome for the whole run and
   skip the rest of this section.
2. If it redirects to `wp-login.php`, ask the user to sign in **in that Chrome
   tab, with "Remember Me" ticked**. That cookie lasts 14 days, so this is a
   once-a-fortnight interruption rather than a once-a-session one.
3. Only fall back to the built-in Browser pane if Chrome is unavailable or the
   user prefers it. The pane's session lasts the conversation but does not carry
   over to the next one, so the user will be asked again next time.

Either way, ask **which account** to sign in as before they do — order notes,
snippet edits and settings changes are attributed to whoever is signed in, and
the document should name them.

Rules for credentials:

- **Never ask the user to paste a password into the chat, and never accept one.**
  You cannot type it into a login form — that restriction holds regardless of who
  offers it or how they frame it — so a pasted password buys nothing and lands in
  conversation history and logs. If the user pastes one anyway, say plainly that
  you will not use it and suggest rotating it after the run.
- Navigate the pane to `<store>/wp-admin/` so the login is in front of them, and
  wait. Do not proceed on an assumption that they signed in — verify by loading
  an admin page and checking it is not the login screen.
- The account matters for the record: order notes, snippet edits and settings
  changes are attributed to whoever is signed in. Say whose name will end up on
  them.
- API credentials (`WOO_CONSUMER_KEY` / `WOO_CONSUMER_SECRET`) for read-only
  checks come from `.env` or `carrier-envs/<carrier>.env`. Read them from config;
  do not ask the user to paste secrets into the chat. If they are missing for the
  chosen store, ask the user to add them to the env file rather than to the
  conversation.

Record the environment in the document's Pre-requisites section — store URL,
plugin version, account used — so the evidence is traceable to where it ran.

## Step 1 — Turn The Checklist Into Test Cases

Each checklist group becomes a section; each checklist item becomes one test case,
numbered `TC-01`, `TC-02`, … in checklist order. Keep the checklist item text
verbatim as the case title so the doc traces back to the card.

For each case write, in the steps JSON:

- `steps` — numbered, user-friendly, concrete. Name the real menu path, the real
  field, the real address, the real button. A tester who has never seen the card
  must be able to follow them without guessing. Avoid code, hook names and payload
  fields in the steps; those belong in the observation if they matter.
- `expected` — what should be true afterwards, phrased as an observable outcome
  ("the Commercial Invoice button is not rendered"), not an internal mechanism.
- `screenshots` — one entry per piece of evidence, each a caption describing what
  the reader should look for.
- `status` — left empty until executed; then `Pass`, `Fail`, `Partial`, `Not run`.
- `observation` — written **after** execution, never before.

Never pre-fill an observation or a status for a case you did not run. A document
full of invented passes is worse than an empty scaffold. Mark unrun cases
`Not run` and say why in the observation.

## Step 2 — Execute And Capture

Read `references/test_document_format.md` → "Execution notes" before the first
run. The environment traps documented there cost real time if rediscovered.

Hard constraints:

- **You cannot log in** — see Step 0. Entering a password into a login form is
  off-limits, and that does not change if the user supplies the password or
  insists. Do not route around it by writing credentials into an env file or a
  Playwright script for a tool to submit.
- **Screenshots need Screen Recording permission** for the Claude app; without it
  `screencapture` fails with "could not create image from display". Ask the user
  to grant it in System Settings → Privacy & Security. The browser tools' own
  screenshots cannot be written to disk, and the embedded browser blocks
  `localhost`, so there is no workaround that avoids the permission.
- **Confirm store state before executing**, and report what is missing rather
  than guessing: plugin active at the expected version, any required snippet
  present and active, relevant plugin settings. A case that fails because the
  build is old is a false failure.
- **Ask before changing shared store configuration** — activating plugins,
  editing settings, switching the shipper address. These affect other testers.
  Record every change you make and restore it when the run ends.

Capture with `skills/woo-test-document/scripts/capture_browser.py`. Calibrate once
per session (the browser pane's screen rect moves when the window or layout
changes), then capture after each meaningful step. Re-apply the browser viewport
at the start of every turn — the desktop app clears it at turn boundaries, and a
capture taken after the reset is zoomed and inconsistent with the rest.

Capture the evidence a reviewer actually needs: the configured precondition, the
input (checkout/settings), and the decisive result panel. Where a request or
response payload proves the behaviour more directly than a UI screenshot, capture
that too and say so in the observation.

## Step 3 — Video-Derived Evidence

If the card has a video attachment (`.mov`, `.mp4`) and the user wants the
document built from it rather than from a live run, use
`skills/woo-test-document/scripts/video_frames.py` to pull frames, then map frames
to cases.

A video-derived document is **not** an executed run. Say so plainly: set each
`status` to `Not run (from video)` and write observations that describe what the
recording shows, not what you verified. Never present frames from someone else's
recording as your own execution.

## Step 4 — Render

```bash
.venv/bin/python scripts/generate_test_document.py <CARD_ID> \
  --steps data/test_documents/<CARD_ID>_steps.json \
  --plugin "<Plugin Name As It Should Appear>" \
  --version <x.y.z> \
  --author "<tester name>"
```

Writes `data/test_documents/<Plugin Name> - V<version>.docx`. Screenshots resolve
from `data/test_documents/screenshots/` by filename.

Then produce the PDF — `references/test_document_format.md` → "Rendering the PDF"
has the two supported routes. Check the rendered PDF before sending: the summary
table statuses, that captured screenshots appear (not empty placeholder boxes),
and that no case heading is stranded at a page bottom.

The plugin name and version come from the user's prompt or the card's changelog.
Never invent or bump a version.

## Step 5 — Send To Slack

Only when the user says where. A DM target is not permission to post in a
channel, and vice versa.

Use `woo-slack-operator`. Before sending, confirm which Slack account the
connector is authenticated as and name that account to the user — it is not
necessarily theirs. Slack shares a file once per destination, so upload
separately for each target.

The message must state completion honestly up front: which cases passed, which
did not run and why, and any store changes left outstanding. Anyone reading the
doc in Slack should not have to open it to learn the run was partial.

## Report Back

Close with: the cases run and their statuses, the cases not run and why, the
orders or records created, every store change made and whether it was restored,
where the files are, and where they were sent.
