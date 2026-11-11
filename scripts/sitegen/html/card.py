# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""A linked card for a service, project or contact."""
from html import escape

from .tile import tile

PILLS = {"public": '<span class="pill">Public</span>', "members": '<span class="pill members">Members</span>'}


def card(item, hue=None, extra=""):
    """
    SYNOPSIS
        card(item, hue=None, extra="") -> str
    DESCRIPTION
        Return the <a class="card"> for ITEM (sitegen.data.models.Item). HUE
        overrides the grid's colour; EXTRA is raw HTML appended to the card body.
        The title and description are escaped; names may carry entities already
        escaped in the data (e.g. &amp;).
    EXAMPLE
        card(Item("Git", "https://git.rootiest.dev", "git-branch", "Code hosting"))
    """
    pill = f" {PILLS[item.access]}" if item.access else ""
    meta = ""
    if item.meta:
        meta = '\n            <span class="meta">' + "".join(f"<span>{escape(m)}</span>" for m in item.meta) + "</span>"
    cls = f"card hue-{hue}" if hue else "card"
    return f"""        <a href="{escape(item.url)}" class="{cls}">
          {tile(item.icon, item.badge)}
          <div class="card-body">
            <h3>{item.name}{pill}</h3>
            <p>{escape(item.desc)}</p>{meta}{extra}
          </div>
        </a>
"""
