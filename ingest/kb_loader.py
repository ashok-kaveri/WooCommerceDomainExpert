"""
KB Loader
=========
Reads all Markdown files from docs/kb_snapshots/ and returns chunked
LangChain Documents ready for indexing into ChromaDB (woo_knowledge).

Each article becomes one or more chunks tagged with:
  source_type : "kb_articles"
  source      : "kb_articles:{filename}"
  source_url  : the live https://www.pluginhive.com/knowledge-base/... URL
  plugin      : ups | fedex | bookings | table-rate | ... | general
  title       : the article H1
  file_name   : original .md filename
  chunk_index : 0, 1, 2, ...

Snapshots are produced by `scripts/scrape_woo_kb.py`, which writes a small
metadata header at the top of every file. This loader parses that header so
answers can cite the live KB URL instead of a local filename.
"""
from __future__ import annotations
import logging
import re
from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

import config

logger = logging.getLogger(__name__)


_TITLE_RE = re.compile(r"^#\s+(.+?)\s*$", re.M)
_SOURCE_RE = re.compile(r"^\*\*Source:\*\*\s*(\S+)\s*$", re.M)
_PLUGIN_RE = re.compile(r"^\*\*Plugin:\*\*\s*(.+?)\s*$", re.M)


def _parse_header(text: str) -> dict[str, str]:
    """Pull title / source URL / plugin out of a snapshot's metadata header."""
    head = text[:1500]
    title = _TITLE_RE.search(head)
    source = _SOURCE_RE.search(head)
    plugin = _PLUGIN_RE.search(head)
    return {
        "title": title.group(1).strip() if title else "",
        "source_url": source.group(1).strip() if source else "",
        "plugin": plugin.group(1).strip() if plugin else "general",
    }


def load_kb_articles(kb_dir: str | Path | None = None) -> list[Document]:
    """
    Walk the KB snapshot directory, read every .md file, chunk the content,
    and return LangChain Documents tagged with source_type='kb_articles'.

    Returns an empty list (with a warning) if the directory doesn't exist.
    Skips files with fewer than 50 characters of content.
    """
    # Derived from config.BASE_DIR (same value as config.KB_SNAPSHOT_DIR) so
    # tests can point the loader at a temp directory.
    kb_dir = Path(kb_dir) if kb_dir else Path(config.BASE_DIR) / "docs" / "kb_snapshots"
    if not kb_dir.exists():
        logger.warning("KB snapshots dir not found: %s — skipping kb_articles ingestion", kb_dir)
        return []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,
    )

    documents: list[Document] = []
    files_read = 0
    files_skipped = 0

    for md_file in sorted(kb_dir.glob("*.md")):
        if md_file.name.startswith("_"):
            continue
        try:
            text = md_file.read_text(encoding="utf-8", errors="replace").strip()
        except Exception as e:
            logger.warning("Could not read KB file %s: %s", md_file, e)
            continue

        if len(text) < 50:
            files_skipped += 1
            continue

        header = _parse_header(text)
        chunks = splitter.split_text(text)
        for i, chunk in enumerate(chunks):
            documents.append(Document(
                page_content=chunk,
                metadata={
                    "source":      f"kb_articles:{md_file.name}",
                    # Cite the live KB article when the snapshot recorded one.
                    "source_url":  header["source_url"] or f"kb_articles:{md_file.name}",
                    "source_type": "kb_articles",
                    "title":       header["title"] or md_file.stem,
                    "plugin":      header["plugin"],
                    "platform":    "woocommerce",
                    "file_name":   md_file.name,
                    "chunk_index": i,
                },
            ))

        files_read += 1
        logger.debug("KB: %s → %d chunks", md_file.name, len(chunks))

    logger.info(
        "KB loader: %d files read, %d files skipped → %d total chunks",
        files_read, files_skipped, len(documents),
    )
    return documents
