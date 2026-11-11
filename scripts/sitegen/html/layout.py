# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""A whole page: head, header, main content and footer."""
from .footer import footer
from .head import head
from .header import header


def layout(title, desc, path, main, nav=None, robots="index, follow"):
    """
    SYNOPSIS
        layout(title, desc, path, main, nav=None, robots="index, follow") -> str
    DESCRIPTION
        Return a complete HTML document. MAIN is the inner HTML of <main>; NAV
        the header label to mark current.
    EXAMPLE
        layout("Rootiest Services", "...", "/services/", body, nav="Services")
    """
    return (head(title, desc, path, robots) + header(nav)
            + f'\n  <main id="main" class="wrap">\n{main}  </main>\n\n' + footer())
