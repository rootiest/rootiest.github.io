# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Record types for the site's data lists."""
from typing import NamedTuple


class Item(NamedTuple):
    """One card: a service, project or contact.

    access is "public", "members" or "" (no pill). meta is shown in the card's
    monospace footer line; badge adds the small Rootiest mark to the tile.
    """
    name: str
    url: str
    icon: str
    desc: str
    meta: tuple = ()
    access: str = ""
    badge: bool = False


class Group(NamedTuple):
    """A titled grid of cards in one Catppuccin hue."""
    title: str
    hue: str
    items: tuple
    blurb: str = ""
