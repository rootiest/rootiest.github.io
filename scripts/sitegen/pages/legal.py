# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""The privacy policy and terms of service pages."""
import re
from pathlib import Path

from ..data import legal
from ..html.hero import hero
from ..html.layout import layout

CONTENT = Path(__file__).resolve().parents[3] / "content" / "legal"


def build():
    """
    SYNOPSIS
        build() -> {path: html}
    DESCRIPTION
        Wrap each fragment in content/legal/ in the site layout, with a "last
        updated" line and a table of contents built from its <h2 id> headings.
    EXAMPLE
        pages = legal.build()
    """
    out = {}
    for p in legal.PAGES:
        body = (CONTENT / p["source"]).read_text().strip("\n")
        heads = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body)
        toc = "".join(f'          <li><a href="#{i}">{t}</a></li>\n' for i, t in heads)
        main = hero(p["h1"], f'Last updated {p["updated"]}', logo=False)
        main += f"""
    <div class="legal-layout">
      <nav class="toc" aria-label="Contents">
        <h2>Contents</h2>
        <ol>
{toc}        </ol>
      </nav>
      <article class="legal">
{body}
      </article>
    </div>
"""
        out[p["path"]] = layout(p["title"], p["desc"], p["url"], main)
    return out
