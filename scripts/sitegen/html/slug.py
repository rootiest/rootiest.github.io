# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""URL fragment from a heading."""
import re


def slug(text):
    """
    SYNOPSIS
        slug(text) -> str
    DESCRIPTION
        Lower-case TEXT, drop entities and punctuation, join words with hyphens.
    EXAMPLE
        slug("Files &amp; media")  # "files-media"
    """
    text = re.sub(r"&[a-z]+;", " ", text.lower())
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")
