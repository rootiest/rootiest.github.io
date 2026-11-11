# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""The page hero: logo, heading, lede and optional actions."""


def hero(h1, lede, actions=(), compact=True, logo=True, extra=""):
    """
    SYNOPSIS
        hero(h1, lede, actions=(), compact=True, logo=True, extra="") -> str
    DESCRIPTION
        Return the hero section. H1 and LEDE are raw HTML. ACTIONS is a list of
        (href, label, primary) buttons; EXTRA raw HTML placed after the lede.
    EXAMPLE
        hero("Contact", "Pick a channel.", [("/discord/", "Discord", False)])
    """
    cls = "hero compact" if compact else "hero"
    size = 72 if compact else 112
    img = (f'      <img src="/img/icons/logo.svg" alt="" class="hero-logo" width="{size}" height="{size}" />\n'
           if logo else "")
    btns = ""
    if actions:
        btns = '\n      <div class="actions">\n' + "\n".join(
            f'        <a href="{h}" class="btn{" primary" if p else ""}">{t}</a>' for h, t, p in actions
        ) + "\n      </div>"
    return f"""    <section class="{cls}">
{img}      <h1>{h1}</h1>
      <p class="lede">{lede}</p>{extra}{btns}
    </section>
"""
