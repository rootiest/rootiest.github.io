# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""The sticky site header with the main navigation."""
from .. import config


def header(current):
    """
    SYNOPSIS
        header(current) -> str
    DESCRIPTION
        Return the site header. The nav entry whose label equals CURRENT gets
        aria-current="page"; pass None on pages that are not in the nav.
    EXAMPLE
        header("Services")
    """
    links = "\n".join(
        f'        <a href="{h}"{" aria-current=\"page\"" if label == current else ""}>{label}</a>'
        for h, label in config.NAV)
    return f"""  <header class="site-header">
    <div class="wrap">
      <a href="/" class="brand"><img src="/img/icons/logo.svg" alt="" width="28" height="28" />Rootiest</a>
      <nav class="nav" aria-label="Main">
{links}
      </nav>
    </div>
  </header>
"""
