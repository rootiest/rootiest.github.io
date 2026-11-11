# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""The hosted services catalog.

Source of truth for hostnames and access: the rootiest-infra services map
(infra skill, reference/services.md). "public" = any RootiestID account (or no
account at all for pages without a login); "members" = unlocked by membership
in the service's RootiestID group.
"""
from .models import Group, Item

# ╭──────────────────────────────────────────────────────────╮
# │                        Start here                        │
# ╰──────────────────────────────────────────────────────────╯
START = Group("Start here", "red", (
    Item("RootiestID", "https://auth.rootiest.dev", "fingerprint",
         "One account and a passkey sign you in to every Rootiest service.",
         ("auth.rootiest.dev",), "public", True),
    Item("Status", "https://status.rootiest.dev", "activity",
         "Live health of every service and server, with push alerts and uptime history.",
         ("status.rootiest.dev",), "public", True),
    Item("Support Desk", "https://support.rootiest.dev", "life-buoy",
         "Report a problem, ask a question or request access, and follow your tickets.",
         ("support.rootiest.dev",), "public", True),
    Item("Status for Android", "https://git.rootiest.dev/rootiest/rootiest-status-android", "smartphone",
         "Native app for the status page, with a home-screen widget and outage notifications.",
         ("Android app",), "public", True),
))

# ╭──────────────────────────────────────────────────────────╮
# │                      Communication                       │
# ╰──────────────────────────────────────────────────────────╯
COMMUNICATION = Group("Communication &amp; AI", "mauve", (
    Item("Chat", "https://chat.rootiest.dev", "messages-square",
         "Team chat with channels, threads, file sharing and mobile apps, powered by Mattermost.",
         ("chat.rootiest.dev",), "members", True),
    Item("Rootiest AI", "https://ai.rootiest.dev", "sparkles",
         "One workspace for models from OpenAI, Anthropic and Google, with file search and web search.",
         ("ai.rootiest.dev",), "members", True),
    Item("Push Notifications", "https://ntfy.rootiest.dev", "bell",
         "Send notifications to your phone or desktop with a simple HTTP request, powered by ntfy.",
         ("ntfy.rootiest.dev",), "members", True),
    Item("MollySocket", "https://molly.rootiest.dev", "message-square-lock",
         "UnifiedPush notifications for the Molly Signal client, without Google services.",
         ("molly.rootiest.dev",), "members", True),
    Item("Bluesky PDS", "https://pds.rootiest.dev", "at-sign",
         "A Rootiest home for your Bluesky account on the AT Protocol network.",
         ("pds.rootiest.dev",), "members", True),
))

# ╭──────────────────────────────────────────────────────────╮
# │                    Notes and knowledge                   │
# ╰──────────────────────────────────────────────────────────╯
NOTES = Group("Notes &amp; knowledge", "yellow", (
    Item("Notes", "https://notes.rootiest.com", "notebook-pen",
         "Quick notes and memos you can keep private or share, powered by Memos.",
         ("notes.rootiest.com",), "public", True),
    Item("Joplin Sync", "https://joplin.rootiest.com", "notebook",
         "Sync server for the Joplin note-taking apps on every device.",
         ("joplin.rootiest.com",), "members", True),
    Item("Obsidian LiveSync", "https://livesync.rootiest.dev", "gem",
         "Real-time Obsidian vault sync, replicated across two servers.",
         ("livesync.rootiest.dev",), "members", True),
))

# ╭──────────────────────────────────────────────────────────╮
# │                      Files and media                     │
# ╰──────────────────────────────────────────────────────────╯
FILES = Group("Files &amp; media", "blue", (
    Item("Photos", "https://photos.rootiest.com", "image",
         "Private photo and video library with search, faces and albums, powered by Immich.",
         ("photos.rootiest.com",), "members", True),
    Item("Files", "https://files.rootiest.com", "folder-open",
         "File storage and sharing over the web and SFTP, with share links, powered by SFTPGo.",
         ("files.rootiest.com",), "members", True),
    Item("Drive", "https://drive.rootiest.dev", "hard-drive",
         "Fast file server with uploads, media playback and sharing, powered by copyparty.",
         ("drive.rootiest.dev",), "members", True),
    Item("Pages", "https://pages.rootiest.fyi", "globe",
         "Static sites, cheatsheets and published docs for Rootiest projects.",
         ("pages.rootiest.fyi",), "public", True),
))

# ╭──────────────────────────────────────────────────────────╮
# │                      Developer tools                     │
# ╰──────────────────────────────────────────────────────────╯
DEV = Group("Developer tools", "green", (
    Item("Git", "https://git.rootiest.dev", "git-branch",
         "Gitea code hosting with CI runners, packages and SSH access.",
         ("git.rootiest.dev",), "public", True),
    Item("Git over SSH", "https://git.rootiest.fyi", "key-round",
         "How to add a key, verify the host and clone from Rootiest Git over SSH.",
         ("git.rootiest.fyi",), "public", True),
    Item("Gists", "https://gists.rootiest.dev", "code",
         "Share code snippets and pastes, powered by Opengist.",
         ("gists.rootiest.dev",), "public", True),
    Item("Short Links", "https://rootiest.link", "link",
         "Privacy-respecting, ad-free URL shortener with link stats, powered by Kutt.",
         ("rootiest.link",), "public", True),
    Item("Coding Stats", "https://wakatime.rootiest.dev", "timer",
         "Track your coding time with WakaTime-compatible editor plugins, powered by Wakapi.",
         ("wakatime.rootiest.dev",), "public", True),
))

# ╭──────────────────────────────────────────────────────────╮
# │                         Security                         │
# ╰──────────────────────────────────────────────────────────╯
SECURITY = Group("Security", "peach", (
    Item("Password Vault", "https://vault.rootiest.dev", "lock-keyhole",
         "End-to-end encrypted, Bitwarden-compatible password manager with autofill and TOTP.",
         ("vault.rootiest.dev",), "public", True),
))

GROUPS = (START, COMMUNICATION, NOTES, FILES, DEV, SECURITY)

# Shown on the home page, in this order.
FEATURED = ("Photos", "Chat", "Password Vault", "Gists", "Git", "Notes")
