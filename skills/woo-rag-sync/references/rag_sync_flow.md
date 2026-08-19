# RAG Sync Flow

## Knowledge Stores

WooCommerceDomainExpert has two RAG areas:

1. Main domain knowledge collection: `woo_knowledge`
   - Woo REST knowledge
   - PluginHive docs
   - app UI knowledge
   - PDF test cases
   - wiki
   - approved cards

2. Code knowledge collection: `woo_code_knowledge`
   - automation
   - the Multi-Carrier plugin repo (`woo_plugin`)
   - the Shipping Pro repo (`woo_shipping_pro`)

Do not mix the update paths.

## Normal Sync Policy

the Multi-Carrier plugin repo:

- branch: current branch unless QA provides one
- method: `sync_from_git(..., source_type="woo_plugin", branch="<branch or current>")`

the Shipping Pro repo:

- branch: current branch unless QA provides one
- method: `sync_from_git(..., source_type="woo_shipping_pro", branch="<branch or current>")`

Automation:

- branch: QA-selected
- method: `sync_from_git(..., source_type="automation", branch="<selected>")`
- if branch not provided, ask QA

Wiki:

- git pull current branch unless QA says `main`
- delete only source_type `wiki`
- reload with `load_wiki_docs`
- add docs to vectorstore

## Full Reindex Policy

Full reindex for plugin source/automation is okay when QA asks for that scope.

Full main knowledge rebuild through `ingest/run_ingest.py` clears the main collection before rebuilding. Use only when QA explicitly asks for full main RAG rebuild or when the main collection is corrupt/stale globally.

Never use:

```bash
PYTHONPATH=. .venv/bin/python ingest/run_ingest.py --sources wiki
```

for ordinary wiki refresh, because `run_ingest.py` clears the whole main collection first.

## Dirty Repo Check

Before pulling a git repo:

```bash
git status --porcelain
```

If output is not empty, stop and ask QA whether to continue. Do not hide local changes.

## Recommended QA Prompts

When automation branch is missing:

```text
Which automation branch should I sync? Current branch is `<branch>`. Available branches include: ...
```

When full reindex is requested vaguely:

```text
Which scope do you want fully reindexed: automation, the Multi-Carrier plugin repo, the Shipping Pro repo, wiki, or full main knowledge?
```
