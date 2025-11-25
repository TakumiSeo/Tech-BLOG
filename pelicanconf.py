#!/usr/bin/env python
from __future__ import annotations

from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()

AUTHOR = "Taku Sewo"
SITENAME = "Cloud Diaries: Azure Edition"
SITEURL = ""

PATH = "content"
ARTICLE_PATHS = [
    "posts/en-us",
    "posts/ja-jp",
]
TIMEZONE = "Asia/Tokyo"
DEFAULT_LANG = "en-us"
PRIMARY_LANG_ROOT = DEFAULT_LANG
I18N_TEMPLATES_LANG = DEFAULT_LANG
LOCALE = ("en_US",)

# Multilingual support
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}
PLUGINS = ["pelican.plugins.i18n_subsites"]
LANGUAGE_SWITCHER = (
    ("en-us", "English"),
    ("ja-jp", "Japanese"),
)
I18N_SUBSITES = {
    "ja-jp": {
        "SITENAME": "カモメとクラウドブログ",
        "SITESUBTITLE": "Azureの実験ノート",
        "LOCALE": "ja_JP",
        "LANGUAGE_SWITCHER": LANGUAGE_SWITCHER,
        "SITEURL": "/ja-jp",
        "ARTICLE_URL": "{slug}.html",
        "ARTICLE_SAVE_AS": "{slug}.html",
        "PAGE_URL": "pages/{slug}.html",
        "PAGE_SAVE_AS": "pages/{slug}.html",
        "CATEGORY_URL": "category/{slug}.html",
        "CATEGORY_SAVE_AS": "category/{slug}.html",
        "TAG_URL": "tag/{slug}.html",
        "TAG_SAVE_AS": "tag/{slug}.html",
        "AUTHOR_URL": "author/{slug}.html",
        "AUTHOR_SAVE_AS": "author/{slug}.html",
        "INDEX_SAVE_AS": "index.html",
        "ARCHIVES_SAVE_AS": "archives.html",
        "CATEGORIES_SAVE_AS": "categories.html",
        "TAGS_SAVE_AS": "tags.html",
        "AUTHORS_SAVE_AS": "authors.html",
    }
}

# Theme settings
THEME = str(BASE_DIR / "themes" / "my-blog-template")
HERO_INTRO = "Defend proactively with intelligence-driven Azure guidance."
FOOTER_TEXT = "Insights and resources to help you secure your cloud estate."
COPYRIGHT_YEAR = "2025"

# Content paths
ARTICLE_URL = f"{PRIMARY_LANG_ROOT}/{{slug}}.html"
ARTICLE_SAVE_AS = ARTICLE_URL
ARTICLE_LANG_URL = "{lang}/{slug}.html"
ARTICLE_LANG_SAVE_AS = ARTICLE_LANG_URL

PAGE_URL = f"{PRIMARY_LANG_ROOT}/pages/{{slug}}.html"
PAGE_SAVE_AS = PAGE_URL
PAGE_LANG_URL = "{lang}/pages/{slug}.html"
PAGE_LANG_SAVE_AS = PAGE_LANG_URL

CATEGORY_URL = f"{PRIMARY_LANG_ROOT}/category/{{slug}}.html"
CATEGORY_SAVE_AS = CATEGORY_URL
CATEGORY_LANG_URL = "{lang}/category/{slug}.html"
CATEGORY_LANG_SAVE_AS = CATEGORY_LANG_URL

TAG_URL = f"{PRIMARY_LANG_ROOT}/tag/{{slug}}.html"
TAG_SAVE_AS = TAG_URL
TAG_LANG_URL = "{lang}/tag/{slug}.html"
TAG_LANG_SAVE_AS = TAG_LANG_URL

AUTHOR_URL = f"{PRIMARY_LANG_ROOT}/author/{{slug}}.html"
AUTHOR_SAVE_AS = AUTHOR_URL
AUTHOR_LANG_URL = "{lang}/author/{slug}.html"
AUTHOR_LANG_SAVE_AS = AUTHOR_LANG_URL

INDEX_SAVE_AS = f"{PRIMARY_LANG_ROOT}/index.html"
ARCHIVES_SAVE_AS = f"{PRIMARY_LANG_ROOT}/archives.html"
CATEGORIES_SAVE_AS = f"{PRIMARY_LANG_ROOT}/categories.html"
TAGS_SAVE_AS = f"{PRIMARY_LANG_ROOT}/tags.html"
AUTHORS_SAVE_AS = f"{PRIMARY_LANG_ROOT}/authors.html"
DIRECT_TEMPLATES = ["index", "categories", "archives", "authors", "tags"]

# Feed generation disabled in development
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Pagination and display
DEFAULT_PAGINATION = 10
RELATIVE_URLS = False

# Static assets
STATIC_PATHS = ["images", "extra"]
EXTRA_PATH_METADATA: dict[str, dict[str, str]] = {
    "extra/root-index.html": {"path": "index.html"},
}

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

# Plugins (legacy plugin folder support for local experiments)
PLUGIN_PATHS = ["plugins"]

# Metadata defaults
DEFAULT_METADATA = {"status": "published"}
