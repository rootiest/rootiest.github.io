# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Inline reference to a symbol in the Lucide sprite."""


def glyph(name, cls="glyph", size=24):
    """
    SYNOPSIS
        glyph(name, cls="glyph", size=24) -> str
    DESCRIPTION
        Return an <svg> that uses symbol NAME from /assets/icons.svg. Decorative:
        hidden from assistive technology.
    EXAMPLE
        glyph("git-branch")
    """
    return (f'<svg class="{cls}" width="{size}" height="{size}" aria-hidden="true" focusable="false">'
            f'<use href="/assets/icons.svg#{name}"></use></svg>')
