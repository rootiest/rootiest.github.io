# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""The site footer: page links, social links, donations and copyright."""
from .. import config
from ._link_row import _link_row


def footer():
    """
    SYNOPSIS
        footer() -> str
    DESCRIPTION
        Return the footer and close the document (</body></html>). Every link is
        plain text: no badges or images from other sites.
    EXAMPLE
        page = head(...) + header("Home") + main + footer()
    """
    donate = " · ".join(f'<a href="{h}">{t}</a>' for h, t in config.FOOTER_DONATE)
    return f"""  <footer class="site-footer">
    <div class="wrap">
{_link_row(config.FOOTER_LINKS, "Footer")}{_link_row(config.FOOTER_SOCIAL, "Elsewhere")}      <p class="footer-donate">Like what we run? Chip in on {donate}.</p>
      <p>© {config.YEAR} {config.ENTITY}. No ads, no trackers.</p>
    </div>
  </footer>
</body>
</html>
"""
