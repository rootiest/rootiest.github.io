# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""The home page."""
from .. import config
from ..data import projects, services
from ..html.card import card
from ..html.features import features
from ..html.hero import hero
from ..html.layout import layout
from ..html.section import section

HOW = [
    ("fingerprint", "One account, no passwords",
     'Your <span class="brand-name">RootiestID</span> signs you in to every service with a passkey. '
     "Set it up once and you're in everywhere."),
    ("users-round", "Open where it can be",
     "Public services work with any RootiestID. Member services are unlocked by group, on request "
     'through the <a href="https://support.rootiest.dev/">support desk</a>.'),
    ("server", "Our servers, your data",
     "No ads, no trackers, nothing sold. Services run on servers we manage, are watched around the clock "
     'and backed up encrypted off-site. <a href="/privacy/">How we handle data</a>.'),
]


def build():
    """
    SYNOPSIS
        build() -> {path: html}
    DESCRIPTION
        Build index.html: hero, how it works, featured services and projects.
    EXAMPLE
        pages = home.build()
    """
    svc = {i.name: (i, g.hue) for g in services.GROUPS for i in g.items}
    prj = {i.name: (i, g.hue) for g in projects.GROUPS for i in g.items}
    badge = (f'\n      <a href="{config.STATUS_URL}/" class="status-badge">'
             f'<img src="{config.STATUS_URL}/badge.svg?theme=mocha&amp;style=for-the-badge" '
             'alt="Rootiest Services status" height="28" /></a>')
    main = hero('Rootiest <span class="accent">Solutions</span>',
                "Self-hosted, privacy-respecting services on one sign-in, plus the open-source tools, "
                "configs and plugins we build along the way.",
                [("/services/", "Explore services", True), (config.AUTH_URL + "/", "Create a RootiestID", False),
                 ("/projects/", "Browse projects", False)],
                compact=False, extra=badge)
    main += ('    <section class="section">\n      <div class="section-head">\n        <h2>How it works</h2>\n'
             "      </div>\n" + features(HOW) + "    </section>\n\n")
    main += section("Hosted services", [card(*svc[n]) for n in services.FEATURED],
                    ("/services/", "All services"), hue="red") + "\n"
    main += section("Projects", [card(*prj[n]) for n in projects.FEATURED], ("/projects/", "All projects"),
                    hue="peach")
    return {"index.html": layout(
        "Rootiest Solutions",
        "Self-hosted, privacy-respecting services on one sign-in, plus open-source tools, configs and plugins "
        "for developers and makers.", "/", main, nav="Home")}
