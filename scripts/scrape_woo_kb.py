"""
Scrape the PluginHive knowledge base for WooCommerce plugin articles.

This is the primary knowledge source for WooCommerceDomainExpert. Unlike the
MCSL scraper (which worked off a hand-maintained URL list), this one discovers
articles from the site's own KB sitemap, so newly published articles are picked
up automatically.

Usage:
    python3 scripts/scrape_woo_kb.py                   # full sync
    python3 scripts/scrape_woo_kb.py --plugin ups      # only UPS articles
    python3 scripts/scrape_woo_kb.py --limit 20        # smoke run
    python3 scripts/scrape_woo_kb.py --list            # discover only, no fetch
    python3 scripts/scrape_woo_kb.py --force           # re-fetch unchanged pages

Output: docs/kb_snapshots/<slug>.md  (one file per article, with a metadata
header used later by ingest/kb_loader.py).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path

import requests
import html2text
from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import config  # noqa: E402

SITEMAP_INDEX = "https://www.pluginhive.com/sitemap_index.xml"
KB_PREFIX = "https://www.pluginhive.com/knowledge-base/"

OUTPUT_DIR = Path(config.KB_SNAPSHOT_DIR)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
STATE_FILE = OUTPUT_DIR / "_kb_sync_state.json"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

# Slugs mentioning these platforms are NOT WooCommerce articles.
FOREIGN_PLATFORMS = (
    "shopify", "magento", "prestashop", "bigcommerce", "opencart", "ebay", "etsy",
)

# Plugin classification — first match wins, so order is most-specific first.
PLUGIN_PATTERNS = [
    ("multi-carrier", ("multi-carrier", "multi-vendor-shipping", "multicarrier")),
    ("shipment-tracking", ("shipment-tracking", "tracking-pro", "track-order", "order-tracking")),
    ("estimated-delivery", ("estimated-delivery", "delivery-date", "delivery-estimate",
                            "estimated-shipping-date", "delivery-day")),
    ("bookings", ("booking", "appointment")),
    ("table-rate", ("table-rate", "shipping-pro")),
    ("ups", ("ups",)),
    ("fedex", ("fedex",)),
    ("canada-post", ("canada-post", "canadapost")),
    ("royal-mail", ("royal-mail", "royalmail")),
    ("australia-post", ("australia-post", "auspost")),
    ("usps", ("usps", "stamps", "easypost", "endicia")),
    ("dhl", ("dhl",)),
    ("aramex", ("aramex",)),
    ("postnord", ("postnord",)),
    ("purolator", ("purolator",)),
    ("amazon-shipping", ("amazon-shipping",)),
]

ARTICLE_SELECTORS = [
    "#eckb-article-content",
    ".eckb-article-content",
    ".epkb-article__content",
    ".epkb-article-content",
    ".entry-content",
    "article .content",
    "article",
    ".post-content",
    "main article",
]

NOISE_SELECTORS = [
    "nav", "header", "footer",
    ".eckb-article-navigation", ".epkb-navigation",
    ".eckb-sidebar", ".epkb-sidebar",
    ".eckb-breadcrumb", ".epkb-breadcrumb",
    ".eckb-search", ".epkb-search",
    ".eckb-categories", ".epkb-categories",
    ".eckb-article-list", ".epkb-article-list",
    ".widget", ".sidebar",
    "#comments", ".comments",
    ".related-posts", ".wp-block-related-posts",
    "script", "style", "noscript",
    ".cookie-notice", ".gdpr", ".cky-consent-container",
]

h = html2text.HTML2Text()
h.ignore_links = False
h.ignore_images = True
h.ignore_emphasis = False
h.body_width = 0
h.protect_links = False


# ── discovery ───────────────────────────────────────────────────────

def _fetch(url: str, timeout: int = 40) -> str:
    resp = requests.get(url, headers=HEADERS, timeout=timeout)
    resp.raise_for_status()
    return resp.text


def _locs(xml_text: str) -> list[str]:
    root = ET.fromstring(xml_text.encode("utf-8"))
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [el.text.strip() for el in root.findall(".//s:loc", ns) if el.text]


def discover_kb_urls() -> list[str]:
    """Every knowledge-base article URL, from the site's own sitemap index."""
    sub_sitemaps = [u for u in _locs(_fetch(SITEMAP_INDEX)) if "epkb" in u]
    urls: set[str] = set()
    for sm in sub_sitemaps:
        urls.update(u for u in _locs(_fetch(sm)) if u.startswith(KB_PREFIX))
    return sorted(urls)


def is_woocommerce_article(url: str) -> bool:
    """
    WooCommerce is PluginHive's primary platform, so an article counts unless
    its slug names a different platform. That keeps platform-neutral support
    FAQs (error codes, box packing, carrier credentials) in scope.
    """
    slug = url.lower()
    if "woocommerce" in slug or "-woo-" in slug or slug.rstrip("/").endswith("-woo"):
        return True
    return not any(p in slug for p in FOREIGN_PLATFORMS)


def classify_plugin(url: str) -> str:
    slug = url.rstrip("/").split("/")[-1].lower()
    for name, needles in PLUGIN_PATTERNS:
        if any(n in slug for n in needles):
            return name
    return "general"


# ── extraction ──────────────────────────────────────────────────────

def url_to_filename(url: str) -> str:
    slug = url.rstrip("/").split("/")[-1]
    slug = re.sub(r"[^a-z0-9-]", "-", slug.lower())
    slug = re.sub(r"-+", "-", slug).strip("-")
    return f"{slug}.md"


def extract_article_content(soup: BeautifulSoup) -> str:
    for sel in NOISE_SELECTORS:
        for el in soup.select(sel):
            el.decompose()
    for sel in ARTICLE_SELECTORS:
        article = soup.select_one(sel)
        if article and len(article.get_text(strip=True)) > 200:
            return str(article)
    main = soup.find("main") or soup.find("body")
    return str(main) if main else ""


def scrape_url(url: str) -> tuple[str, str]:
    """Return (title, markdown_content)."""
    soup = BeautifulSoup(_fetch(url, timeout=30), "html.parser")
    title_tag = soup.find("h1") or soup.find("title")
    title = title_tag.get_text(strip=True) if title_tag else url.rstrip("/").split("/")[-1]
    markdown = h.handle(extract_article_content(soup))
    return title, re.sub(r"\n{3,}", "\n\n", markdown).strip()


def build_file_content(url: str, title: str, plugin: str, markdown: str) -> str:
    return f"""# {title}

**Source:** {url}
**Platform:** WooCommerce (WordPress)
**Plugin:** {plugin}
**Note:** Screenshots may show an older plugin UI — text content is current.

---

{markdown}
"""


# ── main ────────────────────────────────────────────────────────────

def load_state() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except json.JSONDecodeError:
            return {}
    return {}


def main() -> int:
    ap = argparse.ArgumentParser(description="Sync PluginHive WooCommerce KB articles.")
    ap.add_argument("--plugin", help="only articles classified under this plugin (e.g. ups, fedex, bookings)")
    ap.add_argument("--limit", type=int, help="stop after N articles")
    ap.add_argument("--list", action="store_true", help="discover and print URLs, do not fetch")
    ap.add_argument("--force", action="store_true", help="re-write even if content is unchanged")
    ap.add_argument("--delay", type=float, default=0.8, help="polite delay between fetches")
    args = ap.parse_args()

    print(f"Discovering KB articles from {SITEMAP_INDEX} ...")
    all_urls = discover_kb_urls()
    woo_urls = [u for u in all_urls if is_woocommerce_article(u)]
    print(f"  {len(all_urls)} KB articles, {len(woo_urls)} in WooCommerce scope")

    tagged = [(u, classify_plugin(u)) for u in woo_urls]
    if args.plugin:
        tagged = [(u, p) for u, p in tagged if p == args.plugin]
        print(f"  filtered to plugin='{args.plugin}': {len(tagged)}")
    if args.limit:
        tagged = tagged[: args.limit]

    if args.list:
        for u, p in tagged:
            print(f"  [{p}] {u}")
        return 0

    state = load_state()
    ok = short = err = skipped = 0

    for i, (url, plugin) in enumerate(tagged, 1):
        slug = url_to_filename(url)
        print(f"[{i}/{len(tagged)}] ({plugin}) {slug}")
        try:
            title, markdown = scrape_url(url)
        except Exception as exc:  # network / parse failures should not abort the sync
            print(f"    ERROR: {exc}")
            err += 1
            continue

        digest = hashlib.sha256(markdown.encode("utf-8")).hexdigest()
        out_path = OUTPUT_DIR / slug
        if not args.force and state.get(slug, {}).get("sha256") == digest and out_path.exists():
            skipped += 1
            time.sleep(args.delay)
            continue

        out_path.write_text(build_file_content(url, title, plugin, markdown), encoding="utf-8")
        state[slug] = {"url": url, "plugin": plugin, "title": title, "sha256": digest}

        if len(markdown) < 100:
            print(f"    WARNING: very short ({len(markdown)} chars) — may be JS-rendered")
            short += 1
        else:
            ok += 1
        time.sleep(args.delay)

    STATE_FILE.write_text(json.dumps(state, indent=2, sort_keys=True))
    print(f"\nDone. {ok} written, {skipped} unchanged, {short} short, {err} errors -> {OUTPUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
