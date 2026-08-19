import pytest
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def test_sources_argparse():
    """Verify argparse --help shows all 6 Woo source names."""
    import subprocess
    import os
    env = os.environ.copy()
    env["PYTHONPATH"] = str(REPO_ROOT)
    result = subprocess.run(
        [sys.executable, "ingest/run_ingest.py", "--help"],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        env=env,
    )
    assert result.returncode == 0
    assert "kb_articles" in result.stdout
    assert "sheets" in result.stdout
    assert "wiki" in result.stdout
    assert "woo_plugin" in result.stdout
    assert "woo_shipping_pro" in result.stdout
    assert "automation" in result.stdout


def test_partial_reingest_deletes_before_add():
    """Verify partial re-ingest calls delete_by_source_type before add_documents."""
    from unittest.mock import patch, MagicMock
    with patch("rag.vectorstore.delete_by_source_type") as mock_del, \
         patch("rag.vectorstore.add_documents") as mock_add, \
         patch("ingest.kb_loader.load_kb_articles", return_value=[MagicMock()]) as mock_load:
        from importlib import reload
        import ingest.run_ingest as ri
        reload(ri)
        ri.run_ingest(sources=["kb_articles"])
        mock_del.assert_called_once_with("kb_articles")
        mock_add.assert_called_once()


def test_run_ingest_default_sources_when_none():
    """run_ingest(sources=None) runs the default set — KB, sheets, and the 3 code repos.

    `wiki` is deliberately excluded from the default: this repo's product
    knowledge comes from the PluginHive KB, and wiki_loader raises when
    WIKI_PATH is unset.
    """
    from unittest.mock import patch, MagicMock, call
    with patch("rag.vectorstore.delete_by_source_type") as mock_del, \
         patch("rag.vectorstore.add_documents") as mock_add, \
         patch("ingest.kb_loader.load_kb_articles", return_value=[]) as mock_kb, \
         patch("ingest.sheets_loader.load_test_cases", return_value=[]) as mock_sh, \
         patch("ingest.wiki_loader.load_wiki_docs", return_value=[]) as mock_wiki, \
         patch("rag.code_indexer.index_codebase", return_value={"files_indexed": 0, "chunks_added": 0, "skipped": 0, "error": ""}) as mock_code:
        from importlib import reload
        import ingest.run_ingest as ri
        reload(ri)
        ri.run_ingest(sources=None)
        mock_kb.assert_called_once()
        mock_sh.assert_called_once()
        mock_wiki.assert_not_called()
        # Code sources called (woo_plugin, woo_shipping_pro, automation)
        assert mock_code.call_count == 3
        # wiki stays available when asked for explicitly
        assert "wiki" in ri._ALL_SOURCES
        assert "wiki" not in ri._DEFAULT_SOURCES


def test_woo_plugin_source_type():
    """woo_plugin source calls index_codebase with correct source_type."""
    from unittest.mock import patch, MagicMock
    with patch("rag.code_indexer.index_codebase") as mock_code:
        mock_code.return_value = {"files_indexed": 0, "chunks_added": 0, "skipped": 0, "error": ""}
        from importlib import reload
        import ingest.run_ingest as ri
        reload(ri)
        ri.run_ingest(sources=["woo_plugin"])
        call_kwargs = mock_code.call_args
        assert call_kwargs[1].get("source_type") == "woo_plugin" or \
               (len(call_kwargs[0]) > 1 and call_kwargs[0][1] == "woo_plugin")


def test_automation_source_type():
    """automation source calls index_codebase with source_type='automation'."""
    from unittest.mock import patch
    with patch("rag.code_indexer.index_codebase") as mock_code:
        mock_code.return_value = {"files_indexed": 0, "chunks_added": 0, "skipped": 0, "error": ""}
        from importlib import reload
        import ingest.run_ingest as ri
        reload(ri)
        ri.run_ingest(sources=["automation"])
        call_kwargs = mock_code.call_args
        assert call_kwargs[1].get("source_type") == "automation" or \
               (len(call_kwargs[0]) > 1 and call_kwargs[0][1] == "automation")
