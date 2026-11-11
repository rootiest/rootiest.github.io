# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""The document head: metadata, icons and link-preview tags."""
from html import escape

from .. import config


def head(title, desc, path, robots="index, follow"):
    """
    SYNOPSIS
        head(title, desc, path, robots="index, follow") -> str
    DESCRIPTION
        Return everything from <!DOCTYPE html> through <body>. PATH is the page's
        site path ("/contact/"); it becomes the canonical and Open Graph URL. The
        page loads no third-party resources: no analytics, fonts or embeds.
    EXAMPLE
        head("Contact - Rootiest", "Ways to get in touch", "/contact/")
    """
    t, d = escape(title), escape(desc)
    url = config.SITE_URL + path
    return f"""<!DOCTYPE html>
{config.LICENSE_COMMENT}
<html lang="en-US">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{t}</title>
  <meta name="description" content="{d}" />
  <meta name="robots" content="{robots}" />
  <meta name="author" content="Chris Laprade" />
  <meta name="color-scheme" content="light dark" />
  <link rel="canonical" href="{url}" />
  <link rel="stylesheet" href="/assets/site.css" />
  <link rel="icon" type="image/svg+xml" href="/img/icons/logo.svg" />
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
  <link rel="manifest" href="/site.webmanifest" />
  <link rel="mask-icon" href="/safari-pinned-tab.svg" color="#ff004c" />
  <meta name="apple-mobile-web-app-title" content="Rootiest" />
  <meta name="application-name" content="Rootiest" />
  <meta name="msapplication-TileColor" content="#1e1e2e" />
  <meta name="theme-color" content="#eff1f5" media="(prefers-color-scheme: light)" />
  <meta name="theme-color" content="#1e1e2e" media="(prefers-color-scheme: dark)" />

  <meta property="og:site_name" content="Rootiest Solutions" />
  <meta property="og:url" content="{url}" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{t}" />
  <meta property="og:description" content="{d}" />
  <meta property="og:image" content="{config.OG_IMAGE}" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:alt" content="{escape(config.OG_IMAGE_ALT)}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{t}" />
  <meta name="twitter:description" content="{d}" />
  <meta name="twitter:image" content="{config.OG_IMAGE}" />
</head>

<body>
  <a class="skip-link" href="#main">Skip to content</a>
"""
