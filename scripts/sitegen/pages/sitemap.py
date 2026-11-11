# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""sitemap.xml for search engines."""
from .. import config

URLS = ("/", "/services/", "/projects/", "/contact/", "/privacy/", "/tos/")


def build():
    """
    SYNOPSIS
        build() -> {path: text}
    DESCRIPTION
        Build sitemap.xml listing the canonical page URLs.
    EXAMPLE
        pages = sitemap.build()
    """
    locs = "".join(f"  <url><loc>{config.SITE_URL}{u}</loc></url>\n" for u in URLS)
    return {"sitemap.xml": '<?xml version="1.0" encoding="UTF-8"?>\n'
                           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + locs + "</urlset>\n"}
