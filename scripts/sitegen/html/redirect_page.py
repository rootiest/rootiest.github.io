# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""A tiny page that sends visitors to another URL without JavaScript."""
from html import escape

from .. import config


def redirect_page(target, title):
    """
    SYNOPSIS
        redirect_page(target, title) -> str
    DESCRIPTION
        Return an HTML document that redirects to TARGET with a meta refresh and
        a visible link. Kept so old URLs (e.g. /services.html, /discord.html)
        work on any host; the server may also redirect them itself.
    EXAMPLE
        redirect_page("/services/", "Rootiest Services")
    """
    t, u = escape(title), escape(target)
    canon = u if target.startswith("http") else config.SITE_URL + u
    return f"""<!DOCTYPE html>
{config.LICENSE_COMMENT}
<html lang="en-US">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{t}</title>
  <meta name="robots" content="noindex" />
  <link rel="canonical" href="{canon}" />
  <meta http-equiv="refresh" content="0; url={u}" />
</head>
<body>
  <p>Redirecting to <a href="{u}">{u}</a>.</p>
</body>
</html>
"""
