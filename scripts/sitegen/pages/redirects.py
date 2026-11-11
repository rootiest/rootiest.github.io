# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Old and short URLs that point somewhere else."""
from .. import config
from ..html.redirect_page import redirect_page

# path -> (target, title)
REDIRECTS = {
    "services.html": ("/services/", "Rootiest Services"),
    "terms/index.html": ("/tos/", "Terms of Service"),
    "discord.html": (config.DISCORD_INVITE, "Rootiest Discord invite"),
    "discord/index.html": (config.DISCORD_INVITE, "Rootiest Discord invite"),
}


def build():
    """
    SYNOPSIS
        build() -> {path: html}
    DESCRIPTION
        Build one meta-refresh page per entry in REDIRECTS, so old links keep
        working on any host.
    EXAMPLE
        pages = redirects.build()
    """
    return {path: redirect_page(target, title) for path, (target, title) in REDIRECTS.items()}
