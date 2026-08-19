import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(__file__).parent / ".env", override=True)

BASE_DIR = Path(__file__).parent

# Anthropic / Claude
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
# Primary model — deep reasoning, code gen, visual exploration
CLAUDE_SONNET_MODEL = os.getenv("CLAUDE_SONNET_MODEL", "claude-sonnet-4-6")
# Fast/cheap model — card processing, feature detection, lightweight tasks
CLAUDE_HAIKU_MODEL = os.getenv("CLAUDE_HAIKU_MODEL", "claude-haiku-4-5-20251001")
# Default model used by the domain expert chat
DOMAIN_EXPERT_MODEL = os.getenv("DOMAIN_EXPERT_MODEL", CLAUDE_SONNET_MODEL)

# Ollama — kept ONLY for embeddings (Anthropic has no embedding model)
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "nomic-embed-text")

# ChromaDB
CHROMA_PATH = str(BASE_DIR / "data" / "chroma_db")
CHROMA_COLLECTION = "woo_knowledge"
# Separate collection for source code (plugin PHP + automation TS)
CHROMA_CODE_COLLECTION = "woo_code_knowledge"

# ── WooCommerce store ───────────────────────────────────────────────
# The QA WordPress/WooCommerce site the plugins are installed on.
# WOO_SITE_URL is the site origin, e.g. https://qa-ups.pluginhive.com
WOO_SITE_URL = os.getenv("WOO_SITE_URL", os.getenv("site_url", ""))
# WooCommerce REST API credentials (WooCommerce > Settings > Advanced > REST API)
WOO_CONSUMER_KEY = os.getenv("WOO_CONSUMER_KEY", os.getenv("CONSUMER_KEY", ""))
WOO_CONSUMER_SECRET = os.getenv("WOO_CONSUMER_SECRET", os.getenv("CONSUMER_SECRET", ""))
WOO_API_VERSION = os.getenv("WOO_API_VERSION", "wc/v3")
# WP admin credentials — used by Playwright/browser flows, not by the REST API
WP_ADMIN_USER = os.getenv("WP_ADMIN_USER", os.getenv("userName", ""))
WP_ADMIN_PASSWORD = os.getenv("WP_ADMIN_PASSWORD", os.getenv("pass", ""))
# WP admin path — plugin settings screens hang off this
WP_ADMIN_PATH = os.getenv("WP_ADMIN_PATH", "/wp-admin/")

# Legacy alias — a few carrier-env writers and older pipeline call sites still
# read `STORE`. It maps onto the WooCommerce site URL, which is this platform's
# equivalent of a store identity.
STORE = WOO_SITE_URL

# ── Woo knowledge sources ───────────────────────────────────────────
# Playwright automation repo for the WooCommerce plugins
WOO_AUTOMATION_REPO_PATH = os.getenv(
    "WOO_AUTOMATION_REPO_PATH",
    str(Path.home() / "Documents" / "Pluginhive" / "plugins" / "automation" / "ups-woo-automation"),
)

WOO_CHROME_AUTH_PATH = os.getenv(
    "WOO_CHROME_AUTH_PATH",
    str(Path(WOO_AUTOMATION_REPO_PATH) / "auth-chrome.json"),
)

WIKI_PATH = os.getenv(
    "WIKI_PATH",
    str(Path.home() / "Documents" / "Pluginhive" / "wiki"),
)

# ── WooCommerce plugin source repos ─────────────────────────────────
# The Woo equivalent of MCSL's plugin source split: the multi-carrier
# plugin is the "server" side of the domain, woocommerce-shipping-pro the
# shared/base shipping layer.
WOO_PLUGIN_REPO_PATH = os.getenv(
    "WOO_PLUGIN_REPO_PATH",
    str(Path.home() / "Documents" / "Pluginhive" / "plugins"
        / "multi-carrier-shipping-plugin-for-woocommerce"),
)
WOO_SHIPPING_PRO_REPO_PATH = os.getenv(
    "WOO_SHIPPING_PRO_REPO_PATH",
    str(Path.home() / "Documents" / "Pluginhive" / "plugins" / "woocommerce-shipping-pro"),
)

# Aliases used by the ingest pipeline (match --sources argument names).
# "server" = plugin PHP source, "client" = shipping-pro shared layer.
WOO_PLUGIN_REPO_PATH = WOO_PLUGIN_REPO_PATH
WOO_PLUGIN_REPO_PATH = WOO_PLUGIN_REPO_PATH
WOO_SHIPPING_PRO_REPO_PATH = WOO_SHIPPING_PRO_REPO_PATH

# ── Knowledge base website ──────────────────────────────────────────
# Primary knowledge source for this repo: the public PluginHive KB.
KB_BASE_URL = os.getenv("KB_BASE_URL", "https://www.pluginhive.com/knowledge-base/")
KB_SITEMAP_URL = os.getenv("KB_SITEMAP_URL", "https://www.pluginhive.com/kb_sitemap.xml")
KB_SNAPSHOT_DIR = str(BASE_DIR / "docs" / "kb_snapshots")

# File extensions to index from source code directories
CODE_FILE_EXTENSIONS = [".php", ".ts", ".tsx", ".js", ".jsx", ".py", ".java", ".go", ".rb", ".cs"]

# Google Sheets
GOOGLE_SHEETS_ID = os.getenv(
    "GOOGLE_SHEETS_ID", "1oVtOaM2PesVR_TkuVaBKpbp_qQdmq4FQnN43Xew0FuY"
)
GOOGLE_CREDENTIALS_PATH = os.getenv(
    "GOOGLE_CREDENTIALS_PATH", str(BASE_DIR / "credentials.json")
)

# RAG settings
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
TOP_K_RESULTS = 8
MEMORY_WINDOW = 10

# WooCommerce plugin settings render inline in wp-admin — there is no app
# iframe the way the WooCommerce MCSL app has one. Kept as an empty-string constant
# so shared browser helpers can branch on "no iframe" instead of crashing.
APP_IFRAME_SELECTOR = ""
