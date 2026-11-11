# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Rounded icon tile used on cards."""
from .glyph import glyph


def tile(icon, badge=False):
    """
    SYNOPSIS
        tile(icon, badge=False) -> str
    DESCRIPTION
        Return the coloured tile holding glyph ICON. BADGE adds the small Rootiest
        mark that tells hosted services apart from projects.
    EXAMPLE
        tile("fingerprint", badge=True)
    """
    b = '<img class="badge" src="/img/icons/logo.svg" alt="" width="16" height="16" />' if badge else ""
    return f'<span class="tile" aria-hidden="true">{glyph(icon)}{b}</span>'
