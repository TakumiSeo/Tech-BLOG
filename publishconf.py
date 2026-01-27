#!/usr/bin/env python
from __future__ import annotations

import os
from pathlib import Path

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

from pelicanconf import *  # noqa: F401,F403

SITEURL = os.environ.get("SITEURL", "")
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DELETE_OUTPUT_DIRECTORY = True

# Output path for Azure Static Web Apps
OUTPUT_PATH = Path("output")
