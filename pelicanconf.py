#!/usr/bin/env python
from __future__ import annotations

from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()

AUTHOR = "Taku Sewo"
SITENAME = "Cloud Diaries: Azure Edition"
SITEURL = ""

PATH = "content"
TIMEZONE = "Asia/Tokyo"
DEFAULT_LANG = "en"

# Theme settings
THEME = str(BASE_DIR / "themes" / "my-blog-template")
HERO_INTRO = "Defend proactively with intelligence-driven Azure guidance."
FOOTER_TEXT = "Insights and resources to help you secure your cloud estate."
COPYRIGHT_YEAR = "2025"

# Content paths
ARTICLE_URL = "posts/{slug}/"
ARTICLE_SAVE_AS = "posts/{slug}/index.html"
PAGE_URL = "pages/{slug}/"
PAGE_SAVE_AS = "pages/{slug}/index.html"

# Feed generation disabled in development
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Pagination and display
DEFAULT_PAGINATION = 10
RELATIVE_URLS = True

# Static assets
STATIC_PATHS = ["images"]
EXTRA_PATH_METADATA: dict[str, dict[str, str]] = {}

# Markdown and syntax highlighting
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight", "guess_lang": False},
        "markdown.extensions.extra": {},
        "markdown.extensions.toc": {"permalink": True},
    },
    "output_format": "html5",
}
PYGMENTS_STYLE = "dracula"

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = []

# Metadata defaults
DEFAULT_METADATA = {"status": "published"}
