# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""A titled section holding a grid of cards."""


def section(title, cards, more=None, hue="red", blurb="", sid=None):
    """
    SYNOPSIS
        section(title, cards, more=None, hue="red", blurb="", sid=None) -> str
    DESCRIPTION
        Return a <section> with heading TITLE and a card grid in HUE. MORE is an
        optional (href, label) link beside the heading; BLURB a short paragraph
        under it; SID the section's id for in-page links.
    EXAMPLE
        section("Projects", [card(p) for p in items], ("/projects/", "All projects"))
    """
    extra = f'\n        <a href="{more[0]}">{more[1]} <span aria-hidden="true">→</span></a>' if more else ""
    note = f'\n      <p class="section-blurb">{blurb}</p>' if blurb else ""
    ident = f' id="{sid}"' if sid else ""
    return f"""    <section class="section"{ident}>
      <div class="section-head">
        <h2>{title}</h2>{extra}
      </div>{note}
      <div class="grid hue-{hue}">
{"".join(cards)}      </div>
    </section>
"""
