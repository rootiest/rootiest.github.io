# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""A labelled row of plain text links (private helper for the footer)."""


def _link_row(links, label):
    """
    SYNOPSIS
        _link_row(links, label) -> str
    DESCRIPTION
        Return a <nav class="footer-links"> named LABEL holding LINKS, a list of
        (href, text) pairs.
    EXAMPLE
        _link_row([("/privacy/", "Privacy")], "Footer")
    """
    return (f'      <nav class="footer-links" aria-label="{label}">\n'
            + "\n".join(f'        <a href="{h}">{t}</a>' for h, t in links) + "\n      </nav>\n")
