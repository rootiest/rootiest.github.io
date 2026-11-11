# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Legal pages: where each body lives and when it last changed.

The bodies are hand-written HTML fragments in content/legal/. Each <h2> needs an
id; the table of contents is built from them. Update "updated" whenever the
wording changes.
"""

PAGES = (
    {"path": "privacy/index.html", "url": "/privacy/", "source": "privacy.html",
     "title": "Privacy Policy - Rootiest", "h1": "Privacy Policy",
     "desc": "How Rootiest Solutions handles your information on rootiest.com and every Rootiest service.",
     "updated": "November 10, 2026"},
    {"path": "tos/index.html", "url": "/tos/", "source": "terms.html",
     "title": "Terms of Service - Rootiest", "h1": "Terms of Service",
     "desc": "The terms for using rootiest.com and the services run by Rootiest Solutions.",
     "updated": "November 10, 2026"},
)
