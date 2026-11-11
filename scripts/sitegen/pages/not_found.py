# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""The 404 page."""
from .. import config
from ..html.hero import hero
from ..html.layout import layout


def build():
    """
    SYNOPSIS
        build() -> {path: html}
    DESCRIPTION
        Build 404.html, served by the web server for unknown paths.
    EXAMPLE
        pages = not_found.build()
    """
    main = hero("Page not found",
                "That page doesn't exist, or it moved when the site was rebuilt.",
                [("/", "Home", True), ("/services/", "Services", False), (config.SUPPORT_URL + "/", "Support", False)])
    return {"404.html": layout("Page not found - Rootiest", "This page does not exist.", "/404.html", main,
                               robots="noindex")}
