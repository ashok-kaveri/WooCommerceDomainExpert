#!/usr/bin/env python3
"""
WooCommerce Domain Expert — Master Ingestion Pipeline
=====================================================
Ingests knowledge sources into ChromaDB:
  - kb_articles       → woo_knowledge      PluginHive KB mirror in docs/kb_snapshots/
                                           (sync it first: scripts/scrape_woo_kb.py)
  - sheets            → woo_knowledge      QA test-case Google Sheet, all tabs
  - woo_plugin        → woo_code_knowledge multi-carrier-shipping-plugin-for-woocommerce (.php/.js)
  - woo_shipping_pro  → woo_code_knowledge woocommerce-shipping-pro (.php/.js)
  - automation        → woo_code_knowledge ups-woo-automation (.ts/.js/.md)

`wiki` is supported but not part of the default run — this repo's product
knowledge comes from the KB, not an internal wiki. Pass it explicitly if a
WIKI_PATH is configured.

Each doc source: delete_by_source_type() first, then add_documents() (prevents duplicates on re-run).
Each code source: index_codebase(clear_existing=True) (handles delete internally).

Usage:
    python ingest/run_ingest.py                                    # default sources
    python ingest/run_ingest.py --sources kb_articles              # only the KB
    python ingest/run_ingest.py --sources woo_plugin automation
"""
from __future__ import annotations
import argparse
import logging
import sys
import time

import config

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
logger = logging.getLogger(__name__)

# Every source name --sources will accept
_ALL_SOURCES = [
    "kb_articles",
    "sheets",
    "wiki",
    "woo_plugin",
    "woo_shipping_pro",
    "automation",
]

# What a bare `run_ingest.py` does. `wiki` is excluded: this repo has no internal
# wiki, and wiki_loader raises when WIKI_PATH is missing.
_DEFAULT_SOURCES = [
    "kb_articles",
    "sheets",
    "woo_plugin",
    "woo_shipping_pro",
    "automation",
]


def run_ingest(sources: list[str] | None = None) -> None:
    """
    Run ingestion for the specified sources (or all sources if None).

    For document sources (kb_articles, sheets, wiki):
      delete_by_source_type(source_type) → load_*() → add_documents(docs)

    For code sources (woo_plugin, woo_shipping_pro, automation):
      index_codebase(clear_existing=True) which handles deletion internally.

    Args:
        sources: List of source names to ingest. None means all 6 sources.
    """
    from rag.vectorstore import delete_by_source_type, add_documents
    from rag.code_indexer import index_codebase
    from ingest.kb_loader import load_kb_articles
    from ingest.sheets_loader import load_test_cases
    from ingest.wiki_loader import load_wiki_docs

    active = sources if sources is not None else _DEFAULT_SOURCES
    start = time.time()

    print("=" * 60)
    print("WooCommerce Domain Expert — Knowledge Base Ingestion")
    print(f"Sources: {', '.join(active)}")
    print("=" * 60)

    # ── Document sources (→ woo_knowledge) ──────────────────────────────────

    if "kb_articles" in active:
        logger.info("Ingesting KB articles from docs/kb_snapshots/...")
        docs = load_kb_articles()
        logger.info("KB articles: %d chunks loaded", len(docs))
        delete_by_source_type("kb_articles")
        add_documents(docs)
        print(f"  kb_articles: {len(docs)} chunks ingested")

    if "sheets" in active:
        logger.info("Ingesting the QA test-case sheet (Google Sheets)...")
        docs = load_test_cases()
        logger.info("TC sheet: %d chunks loaded", len(docs))
        delete_by_source_type("sheets")
        add_documents(docs)
        print(f"  sheets: {len(docs)} chunks ingested")

    if "wiki" in active:
        logger.info("Ingesting Woo wiki from %s...", config.WIKI_PATH)
        docs = load_wiki_docs()
        logger.info("Wiki: %d chunks loaded", len(docs))
        delete_by_source_type("wiki")
        add_documents(docs)
        print(f"  wiki: {len(docs)} chunks ingested")

    # ── Code sources (→ woo_code_knowledge) ─────────────────────────────────

    if "woo_plugin" in active:
        logger.info("Indexing the Multi-Carrier plugin at %s ...", config.WOO_PLUGIN_REPO_PATH)
        result = index_codebase(
            code_path=config.WOO_PLUGIN_REPO_PATH,
            source_type="woo_plugin",
            extensions=[".php", ".js"],
            clear_existing=True,
        )
        logger.info("woo_plugin: %s", result)
        print(f"  woo_plugin: {result.get('chunks_added', 0)} chunks indexed")

    if "woo_shipping_pro" in active:
        logger.info("Indexing Shipping Pro at %s ...", config.WOO_SHIPPING_PRO_REPO_PATH)
        result = index_codebase(
            code_path=config.WOO_SHIPPING_PRO_REPO_PATH,
            source_type="woo_shipping_pro",
            extensions=[".php", ".js"],
            clear_existing=True,
        )
        logger.info("woo_shipping_pro: %s", result)
        print(f"  woo_shipping_pro: {result.get('chunks_added', 0)} chunks indexed")

    if "automation" in active:
        logger.info("Indexing ups-woo-automation repo (skipping carrier-envs/)...")
        result = index_codebase(
            code_path=config.WOO_AUTOMATION_REPO_PATH,
            source_type="automation",
            extensions=[".ts", ".js", ".md"],
            clear_existing=True,
        )
        logger.info("automation: %s", result)
        print(f"  automation: {result.get('chunks_added', 0)} chunks indexed")

    elapsed = time.time() - start
    print()
    print(f"Done: all sources indexed in {elapsed:.1f}s")
    print("=" * 60)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Rebuild Woo Domain Expert knowledge base",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--sources",
        nargs="*",
        choices=_ALL_SOURCES,
        metavar="SOURCE",
        help=(
            f"Which sources to ingest (default: {' '.join(_DEFAULT_SOURCES)}). "
            f"Choices: {', '.join(_ALL_SOURCES)}"
        ),
    )
    args = parser.parse_args()
    run_ingest(args.sources)
