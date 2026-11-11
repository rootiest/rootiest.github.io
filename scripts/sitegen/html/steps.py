# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""A numbered list of steps."""


def steps(items):
    """
    SYNOPSIS
        steps(items) -> str
    DESCRIPTION
        Return an ordered list styled as numbered steps. ITEMS is a list of
        (title, html) pairs; the html is inserted unescaped.
    EXAMPLE
        steps([("Create a RootiestID", "Go to auth.rootiest.dev.")])
    """
    lis = "".join(f'        <li><strong>{t}</strong> <span>{body}</span></li>\n' for t, body in items)
    return f'      <ol class="steps">\n{lis}      </ol>\n'
