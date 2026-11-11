# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""The contact page."""
from .. import config
from ..data import contacts
from ..data.models import Item
from ..html.card import card
from ..html.hero import hero
from ..html.layout import layout
from ..html.section import section


def build():
    """
    SYNOPSIS
        build() -> {path: html}
    DESCRIPTION
        Build contact/index.html: channels, the Discord banner and the PGP key.
    EXAMPLE
        pages = contact.build()
    """
    g = contacts.CHANNELS
    main = hero("Contact",
                "Need help with a Rootiest service? The support desk is the fastest way. "
                "For anything else, pick a channel below.",
                [(config.SUPPORT_URL + "/", "Open a ticket", True), ("/discord/", "Join the Discord", False)])
    main += section(g.title, [card(i) for i in g.items], hue=g.hue)
    main += """
    <section class="section">
      <div class="section-head">
        <h2>Community</h2>
      </div>
      <a href="/discord/" class="discord-banner">
        <img src="/img/discord-banner.webp" alt="Rootiest Discord server banner" width="300" height="50" loading="lazy" />
      </a>
    </section>
"""
    key = Item("GPG public key", contacts.PGP_URL, "key-round", "", ("keys.openpgp.org", "also at /keys/rootiest.asc"))
    pgp = card(key).replace("<p></p>", f'<p class="fingerprint">{contacts.PGP_FINGERPRINT}</p>')
    main += section("Verify my identity", [pgp], hue="green")
    return {"contact/index.html": layout(
        "Contact - Rootiest", "Ways to get in touch with Rootiest Solutions: support desk, Discord, Bluesky, "
        "Mastodon, Matrix and email.", "/contact/", main, nav="Contact")}
