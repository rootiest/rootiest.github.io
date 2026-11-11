# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""A row of short feature blurbs with icons."""
from .glyph import glyph


def features(items, hue="red"):
    """
    SYNOPSIS
        features(items, hue="red") -> str
    DESCRIPTION
        Return a grid of feature blurbs. ITEMS is a list of (icon, title, html)
        tuples; the html is inserted unescaped.
    EXAMPLE
        features([("fingerprint", "One account", "Sign in with a passkey.")])
    """
    blocks = "".join(f"""        <div class="feature">
          <span class="tile" aria-hidden="true">{glyph(i)}</span>
          <h3>{t}</h3>
          <p>{body}</p>
        </div>
""" for i, t, body in items)
    return f'      <div class="features hue-{hue}">\n{blocks}      </div>\n'
