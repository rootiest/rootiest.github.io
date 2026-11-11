# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""The Terms of Service page: where its body lives and when it last changed.

The privacy notices live in the privacy repository and are served at /privacy/
(config.MOUNTED).

The body is a hand-written HTML fragment in content/legal/. Each <h2> needs an
id; the table of contents is built from them. Update "updated" whenever the
wording changes.
"""

PAGES = (
    {"path": "tos/index.html", "url": "/tos/", "source": "terms.html",
     "title": "Terms of Service - Rootiest", "h1": "Terms of Service",
     "desc": "The terms for using rootiest.com and the services run by Rootiest Solutions.",
     "updated": "November 11, 2026"},
)
