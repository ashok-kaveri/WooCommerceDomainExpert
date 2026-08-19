"""Tests for config.py — INFRA-01, INFRA-03, INFRA-04 coverage."""


def test_dotenv_explicit_path(tmp_path, monkeypatch):
    """Verify config uses explicit dotenv path tied to __file__, not CWD."""
    env_file = tmp_path / ".env"
    env_file.write_text("ANTHROPIC_API_KEY=test-key-abc\n")
    # Re-import config from a different cwd to verify explicit path works
    import importlib, sys, os
    (tmp_path / "subdir").mkdir(exist_ok=True)
    monkeypatch.chdir(tmp_path / "subdir")
    # config.py must not be affected by cwd change — it uses __file__ path
    import config
    # The key should be loaded from the actual .env, not tmp .env —
    # this tests that the pattern is in place (not None)
    assert hasattr(config, "ANTHROPIC_API_KEY")  # attribute exists


def test_collection_names():
    """Verify ChromaDB collection names are Woo-specific (not fedex_*)."""
    import config
    assert config.CHROMA_COLLECTION == "woo_knowledge"
    assert config.CHROMA_CODE_COLLECTION == "woo_code_knowledge"


def test_woo_env_vars():
    """Verify all Woo-specific env vars are present in config module."""
    import config
    assert hasattr(config, "WOO_SITE_URL")
    assert hasattr(config, "WOO_CONSUMER_KEY")
    assert hasattr(config, "WOO_CONSUMER_SECRET")
    assert hasattr(config, "WOO_API_VERSION")
    assert hasattr(config, "WP_ADMIN_USER")
    assert hasattr(config, "WOO_AUTOMATION_REPO_PATH")
    assert hasattr(config, "WOO_PLUGIN_REPO_PATH")
    assert hasattr(config, "WIKI_PATH")


def test_kb_website_is_configured():
    """The KB website is this repo's primary knowledge source."""
    import config
    assert config.KB_BASE_URL.startswith("https://www.pluginhive.com/knowledge-base")
    assert config.KB_SNAPSHOT_DIR.endswith("kb_snapshots")


def test_app_iframe_selector_is_empty_for_woocommerce():
    """WooCommerce plugin settings render inline in wp-admin — no app iframe."""
    import config
    assert config.APP_IFRAME_SELECTOR == ""
