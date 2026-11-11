# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Ways to reach Rootiest, in order of preference."""
from .models import Group, Item

CHANNELS = Group("How to reach me", "lavender", (
    Item("Support Desk", "https://support.rootiest.dev/", "life-buoy",
         "Best for anything about a Rootiest service: problems, questions and access requests.",
         ("support.rootiest.dev",)),
    Item("Discord", "/discord/", "message-circle", "Community server for projects, configs and Klipper.",
         ("@Rootiest",)),
    Item("Bluesky", "https://bsky.app/profile/rootiest.com", "at-sign", "Updates and the occasional post.",
         ("@rootiest.com",)),
    Item("Mastodon", "https://fosstodon.org/@rootiest", "rss", "On the fediverse.", ("@rootiest@fosstodon.org",)),
    Item("Lemmy", "https://lemmy.world/u/Rootiest", "users", "Threads and discussion.", ("@Rootiest@lemmy.world",)),
    Item("Matrix", "https://matrix.to/#/@rootiest:matrix.org", "message-square-lock", "Encrypted chat.",
         ("@rootiest:matrix.org",)),
    Item("Email", "mailto:chris@rootiest.com", "mail", "For anything that isn't a support request.",
         ("chris@rootiest.com",)),
))

PGP_FINGERPRINT = "0FD2 5CCB CE46 D16B 8297 DDA2 623C E33E 5CF3 23D5"
PGP_URL = "https://keys.openpgp.org/vks/v1/by-fingerprint/0FD25CCBCE46D16B8297DDA2623CE33E5CF323D5"
