---
name: woo-rag-sync
description: Use inside WooCommerceDomainExpert when QA asks Codex or Claude to re-sync the PluginHive knowledge base or pull latest and reindex RAG knowledge for the plugin source, Shipping Pro, or the automation repo. The KB is scraped from pluginhive.com and is this project's primary source. Plugin repos use their current branch unless QA provides one; automation is branch-aware and must ask QA for a branch unless provided. Never run a full reindex unless explicitly requested.
---

# Woo RAG Sync

Use this skill when QA says:

- "sync the knowledge base" / "re-scrape the KB" / "the KB is stale"
- "pull latest and sync knowledge"
- "update RAG"
- "sync code knowledge"
- "pull latest plugin/shipping-pro/automation"
- "full re-index"
- "update knowledge from latest code changes"

This skill replaces needing to open the dashboard for RAG sync.

## Read First

Before running sync/reindex:

1. Read `AGENTS.md`.
2. Read `references/rag_sync_flow.md`.
3. Use:
   - `scripts/scrape_woo_kb.py` — refresh the KB mirror
   - `ingest.kb_loader.load_kb_articles` — chunk it for Chroma
   - `rag.code_indexer.sync_from_git`
   - `rag.code_indexer.index_codebase`

## Knowledge Base Sync (do this first)

The PluginHive knowledge base is this project's primary source, and it changes
independently of any repo — nothing to `git pull`. Refresh it before reindexing:

```bash
.venv/bin/python scripts/scrape_woo_kb.py            # incremental; skips unchanged articles
.venv/bin/python scripts/scrape_woo_kb.py --plugin ups
.venv/bin/python scripts/scrape_woo_kb.py --list     # discover only, no fetch
.venv/bin/python scripts/scrape_woo_kb.py --force    # rewrite even when unchanged
```

Then reindex just the KB:

```bash
PYTHONPATH=. .venv/bin/python ingest/run_ingest.py --sources kb_articles
```

Notes:
- Discovery is sitemap-driven, so new articles appear automatically. Report the
  discovered / in-scope counts back to QA — a sudden drop means the site changed.
- Articles whose slug names another platform (Shopify, Magento, PrestaShop,
  BigCommerce) are excluded by `FOREIGN_PLATFORMS`. That list is what to
  **exclude** — never add WooCommerce to it.
- `docs/kb_snapshots/` is generated. Never hand-edit a snapshot; re-scrape.

## Branch Rules

Branch handling:

- Plugin source (`woo_plugin`, `woo_shipping_pro`): pull current branch by default; use a specific branch only when QA provides one.
- KB: not a repo — re-scrape it instead of pulling.
- Automation: branch can change. Ask QA for branch unless they already provided it.

Automation examples:

- "sync automation current branch" -> use current branch.
- "sync automation main" -> use `main`.
- "sync automation release/1.2.3" -> use that branch.
- "sync automation" with no branch -> ask QA which branch.

Do not guess the automation branch.

## Safe Defaults

When QA says "sync latest knowledge" without more detail:

1. Re-scrape the KB and reindex `kb_articles`.
2. Sync the Multi-Carrier plugin repo on its current branch.
3. Sync the Shipping Pro repo on its current branch.
4. Ask which automation branch to sync.
5. Do not run a full RAG rebuild.

When QA says "full reindex", confirm which scope:

- KB only (`--sources kb_articles`)
- code only
- everything via `ingest/run_ingest.py` (KB + sheets + the 3 code repos; `wiki`
  is excluded from the default and only runs when asked for explicitly)

## Code Knowledge Store

the Multi-Carrier plugin repo, the Shipping Pro repo, and automation use the separate code knowledge collection through `rag.code_indexer`.

Use `sync_from_git` for normal latest changes:

```bash
PYTHONPATH=. .venv/bin/python skills/woo-rag-sync/scripts/rag_sync.py sync --target woo_plugin
PYTHONPATH=. .venv/bin/python skills/woo-rag-sync/scripts/rag_sync.py sync --target woo_shipping_pro
PYTHONPATH=. .venv/bin/python skills/woo-rag-sync/scripts/rag_sync.py sync --target automation --branch "<branch>"
```

Use full code reindex only when explicitly asked:

```bash
PYTHONPATH=. .venv/bin/python skills/woo-rag-sync/scripts/rag_sync.py full-reindex --target automation --branch "<branch>"
```

## Main Knowledge Store

Wiki lives in the main `woo_knowledge` collection.

Use source-only delete/reload, not `ingest/run_ingest.py --sources wiki`, because `run_ingest.py` clears the whole main collection first.

Safe source-only commands:

```bash
PYTHONPATH=. .venv/bin/python skills/woo-rag-sync/scripts/rag_sync.py sync --target wiki
```

Full main rebuild is only for explicit reset:

```bash
PYTHONPATH=. .venv/bin/python ingest/run_ingest.py
```

## Status

Before a risky sync, check status:

```bash
PYTHONPATH=. .venv/bin/python skills/woo-rag-sync/scripts/rag_sync.py status
```

For automation branch choices:

```bash
PYTHONPATH=. .venv/bin/python skills/woo-rag-sync/scripts/rag_sync.py status --target automation
```

## Safety

- Do not pull automation without a branch/current-branch instruction from QA.
- Do not run full main RAG rebuild unless QA explicitly asks.
- If a repo has dirty local changes, stop and ask before pulling.
- If network/git pull fails due to sandbox, rerun with escalation.
- Summarize changed files/chunks after sync.

## Output

Return:

- target
- branch used
- pull result
- commit before/after
- files changed/deleted
- chunks updated/indexed
- whether full reindex was used
- any QA action needed
