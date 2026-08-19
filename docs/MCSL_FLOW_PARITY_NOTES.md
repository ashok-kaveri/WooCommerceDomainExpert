# MCSL Flow Parity Notes

This document tracks workflow parity only. It is not a claim that the WooCommerce plugins and the Shopify MCSL app share the same domain logic — they do not.

Comparison repo:
- `../MCSLDomainExpert`

Woo source of truth:
- [pipeline_dashboard.py](pipeline_dashboard.py:1)

## What Parity Means

Parity means:
- similar QA stage order
- similar release-state progression
- similar user affordances around generation, validation, publish, review, automation, docs, and sign-off

Parity does not mean:
- copying MCSL navigation
- copying MCSL carrier assumptions
- replacing Woo rules with MCSL logic

## Current Parity Status By Stage

### Validate AC

Woo now follows the MCSL-style sequence:
- `Load Cards`
- select a subset before loading when QA only wants part of a list
- auto-run validation, diagnosis, and release analysis
- show `Release Intelligence`
- show `Step 1: Card Requirements`
- show `AI Suggested User Story & AC`
- show `Domain Validation`
- allow fix and revalidate

Important Woo-specific difference:
- toggle flow is richer and app-state-aware, and should stay different from MCSL

Shared parity affordance:
- after loading, QA can edit the active card subset from every pipeline tab while preserving the original loaded-card list

### Generate TC

Woo supports the same core flow shape:
- generate test cases
- review and regenerate with feedback
- manual edit and re-review
- Slack share
- publish to Trello and Sheets
- duplicate review before sheet write

Current correctness behavior:
- generation uses the current AC draft, not only stale Trello description
- existing saved TCs are also reviewed against the current AC draft
- partial publish retry should not duplicate the Trello summary comment

Remaining differences:
- mostly wording and layout
- not a major flow gap

### AI QA Verifier

Woo already has the main MCSL-style AI QA flow:
- TC-first execution
- reruns and `qa_needed`
- failed-finding review
- ask-domain-expert
- final approval and save

Intentional Woo difference:
- execution and reasoning use Woo automation, Woo request expectations, and Woo carrier knowledge

### Generate Automation Script

Woo now includes the main MCSL-style automation stages:
- `① Write Automation Code`
- `② Run Automation & Post to Slack`
- `③ Generate Documentation`
- `🐛 Bug Reporter`

Additional parity already present:
- existing-vs-new feature detection
- `find_pom`-style automation matching
- per-card run breakdown
- failed-test detail
- richer generation summary

## Intentional Woo Differences That Must Stay

- WooCommerce embedded-app navigation
- multi-carrier expectation logic
- Woo toggle and store-state capture
- Woo automation repo structure
- Woo request and log verification rules

## Remaining Work

Most remaining parity work is now:
- wording and layout cleanup where QA wants closer MCSL familiarity
- live Trello, Slack, and app validation of the newest flows
- small parity fixes only when they improve Woo workflow without damaging Woo-specific behavior
