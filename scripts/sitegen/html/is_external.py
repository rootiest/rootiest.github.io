# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Whether a link leaves rootiest.com."""


def is_external(href):
    """
    SYNOPSIS
        is_external(href) -> bool
    DESCRIPTION
        True for absolute http(s) URLs; False for site-relative paths, mailto and
        anchors.
    EXAMPLE
        is_external("https://git.rootiest.dev")  # True
    """
    return href.startswith(("http://", "https://"))
