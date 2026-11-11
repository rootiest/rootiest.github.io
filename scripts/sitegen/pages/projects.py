# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""The projects page."""
from ..data import projects
from ..html.card import card
from ..html.hero import hero
from ..html.layout import layout
from ..html.section import section
from ..html.slug import slug


def build():
    """
    SYNOPSIS
        build() -> {path: html}
    DESCRIPTION
        Build projects/index.html, one section per group in sitegen.data.projects.
    EXAMPLE
        pages = projects.build()
    """
    main = hero("Projects",
                "Open-source configs, tools and plugins. Most live on Rootiest Git and are mirrored to GitHub.",
                [("https://git.rootiest.dev/rootiest", "Rootiest Git", True),
                 ("https://github.com/rootiest", "GitHub", False)])
    main += "\n".join(section(g.title, [card(i) for i in g.items], hue=g.hue, blurb=g.blurb, sid=slug(g.title))
                      for g in projects.GROUPS)
    return {"projects/index.html": layout(
        "Rootiest Projects", "Open-source configs, tools and plugins from Rootiest: shell, editor and terminal "
        "setups, AI agent plugins, keyboards and Klipper.", "/projects/", main, nav="Projects")}
