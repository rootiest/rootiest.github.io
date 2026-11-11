# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""The services catalog page."""
from .. import config
from ..data import services
from ..html.card import card
from ..html.hero import hero
from ..html.layout import layout
from ..html.section import section
from ..html.slug import slug
from ..html.steps import steps

START = [
    ("Create your RootiestID.",
     f'Sign up at <a href="{config.AUTH_URL}/">auth.rootiest.dev</a> and add a passkey. '
     "It works with your phone, a security key or your password manager."),
    ("Open a public service.",
     'Anything marked <span class="pill">Public</span> works right away: choose '
     "<em>Sign in with RootiestID</em>."),
    ("Ask for member services.",
     'Services marked <span class="pill members">Members</span> are unlocked by group membership. '
     f'<a href="{config.SUPPORT_URL}/">Open a support ticket</a> saying which ones you need.'),
]


def build():
    """
    SYNOPSIS
        build() -> {path: html}
    DESCRIPTION
        Build services/index.html from sitegen.data.services: getting-started
        steps, a jump list and one section per group.
    EXAMPLE
        pages = services.build()
    """
    jump = " · ".join(f'<a href="#{slug(g.title)}">{g.title}</a>' for g in services.GROUPS)
    main = hero("Rootiest Services",
                'Self-hosted, privacy-respecting services. One <span class="brand-name">RootiestID</span> '
                "signs you in to all of them.",
                extra=f'\n      <p class="jump" aria-label="Jump to">{jump}</p>')
    main += ('    <section class="section">\n      <div class="section-head">\n        <h2>Getting started</h2>\n'
             "      </div>\n" + steps(START) + "    </section>\n\n")
    main += "\n".join(section(g.title, [card(i) for i in g.items], hue=g.hue, blurb=g.blurb, sid=slug(g.title))
                      for g in services.GROUPS)
    main += (f'\n    <p class="note">Every service is watched on the <a href="{config.STATUS_URL}/">status page</a> '
             "and backed up, encrypted, several times a day. Read how we handle your data in the "
             '<a href="/privacy/">privacy policy</a>.</p>\n')
    return {"services/index.html": layout(
        "Rootiest Services", "Self-hosted, privacy-respecting services run by Rootiest Solutions, "
        "all behind one RootiestID sign-in.", "/services/", main, nav="Services")}
