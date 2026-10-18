"""Generate the rootiest.com pages from the data in this file.

Builds index.html, services.html, contact/index.html, privacy/index.html and tos/index.html.
Edit the PROJECTS, KLIPPER, SERVICES or CONTACTS lists (or the page templates) here, then run:

    python3 scripts/build.py

The legal pages keep their text: it is read back from each page's <article class="legal"> block,
so edit the policy wording directly in privacy/index.html or tos/index.html.
Glyph names refer to symbols in assets/icons.svg (Lucide icons).
"""
import sys
from html import escape
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent

LICENSE = """<!--
 Copyright (C) 2026 Chris Laprade (chris@rootiest.com)

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU Affero General Public License as
 published by the Free Software Foundation, either version 3 of the
 License, or (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU Affero General Public License for more details.

 You should have received a copy of the GNU Affero General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
-->"""

GTAG = """  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-GMX96HJQ8Z"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-GMX96HJQ8Z');
  </script>
"""


def head(title, desc, url, gtag=True):
    t, d = escape(title), escape(desc)
    return f"""<!DOCTYPE html>
{LICENSE}
<html lang="en-US">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{t}</title>
  <meta name="description" content="{d}" />
  <meta name="robots" content="index, follow" />
  <meta name="author" content="Chris Laprade" />
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
  <meta name="theme-color" content="#ff004c" />

  <!-- Open Graph -->
  <meta property="og:url" content="{url}" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{t}" />
  <meta property="og:description" content="{d}" />
  <meta property="og:image" content="https://www.rootiest.com/img/banner.png?v=2" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:alt" content="Rootiest Solutions: self-hosted, privacy-respecting services and open-source tools" />

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta property="twitter:domain" content="rootiest.com" />
  <meta property="twitter:url" content="{url}" />
  <meta name="twitter:title" content="{t}" />
  <meta name="twitter:description" content="{d}" />
  <meta name="twitter:image" content="https://www.rootiest.com/img/banner.png?v=2" />
</head>

<body>
{GTAG if gtag else ""}"""


def header(current):
    links = [("/", "Home"), ("/services.html", "Services"), ("https://status.rootiest.dev/", "Status"),
             ("https://support.rootiest.dev/", "Support"), ("/contact/", "Contact")]
    nav = "\n".join(
        f'        <a href="{h}"{" aria-current=\"page\"" if l == current else ""}>{l}</a>' for h, l in links)
    return f"""  <header class="site-header">
    <div class="wrap">
      <a href="/" class="brand"><img src="/img/icons/logo.svg" alt="" width="28" height="28" />Rootiest</a>
      <nav class="nav" aria-label="Main">
{nav}
      </nav>
    </div>
  </header>
"""


def tile(icon, badge=False):
    b = '<img class="badge" src="/img/icons/logo.svg" alt="" width="16" height="16" />' if badge else ""
    return (f'<span class="tile" aria-hidden="true"><svg class="glyph" width="24" height="24">'
            f'<use href="/assets/icons.svg#{icon}"></use></svg>{b}</span>')


def card(href, icon, title, desc, meta=(), public=False, badge=False, hue=None):
    pill = ' <span class="pill">Public</span>' if public else ""
    m = ""
    if meta:
        m = '\n            <span class="meta">' + "".join(f"<span>{escape(x)}</span>" for x in meta) + "</span>"
    return f"""        <a href="{href}" class="card{f' hue-{hue}' if hue else ''}">
          {tile(icon, badge)}
          <div class="card-body">
            <h3>{escape(title)}{pill}</h3>
            <p>{escape(desc)}</p>{m}
          </div>
        </a>
"""


def section(title, cards, more=None, hue="red"):
    extra = f'\n        <a href="{more[0]}">{more[1]}</a>' if more else ""
    return f"""    <section class="section">
      <div class="section-head">
        <h2>{title}</h2>{extra}
      </div>
      <div class="grid hue-{hue}">
{"".join(cards)}      </div>
    </section>
"""


def footer(badges=True):
    b = ""
    if badges:
        b = """      <div class="badges">
        <a href="/discord.html"><img src="https://img.shields.io/discord/1058478355973939220?color=7289da&amp;label=Discord&amp;logo=discord&amp;logoColor=white&amp;style=for-the-badge" alt="Discord server" /></a>
        <a href="https://twitter.com/RootiestSolves"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&amp;logo=twitter&amp;logoColor=white" alt="Twitter" /></a>
        <a href="https://github.com/rootiest"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&amp;logo=github&amp;logoColor=white" alt="GitHub" /></a>
        <a href="https://git.rootiest.dev/rootiest"><img src="https://img.shields.io/badge/Gitea-609926?style=for-the-badge&amp;logo=gitea&amp;logoColor=white" alt="Gitea" /></a>
        <a href="https://www.paypal.me/rootiest/"><img src="https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&amp;logo=paypal&amp;logoColor=white" alt="PayPal" /></a>
      </div>
      <div class="badges small">
        <a href="https://app.netlify.com/projects/charming-crumble-efcb4a/deploys"><img src="https://api.netlify.com/api/v1/badges/fa49e4b0-c380-431d-a4f0-ab714e504786/deploy-status" alt="Netlify Status" /></a>
        <a href="https://keys.openpgp.org/vks/v1/by-fingerprint/0FD25CCBCE46D16B8297DDA2623CE33E5CF323D5"><img src="https://img.shields.io/badge/PGP-623CE33E5CF323D5-green?style=flat-square" alt="PGP Key" /></a>
        <a href="bitcoin:3CmkzM7nPKWCeEc9y9KF5Gw2KQdbDLC77P"><img src="https://img.shields.io/keybase/btc/rootiest?style=flat-square" alt="Bitcoin" /></a>
      </div>
"""
    return f"""  <footer class="site-footer">
    <div class="wrap">
{b}      <nav class="footer-links" aria-label="Footer">
        <a href="/contact/">Contact</a>
        <a href="/privacy/">Privacy</a>
        <a href="/tos/">Terms</a>
        <a href="https://status.rootiest.dev/">Status</a>
      </nav>
      <p>© 2026 Rootiest Solutions</p>
    </div>
  </footer>
"""


GH, GT = "https://github.com/rootiest/", "https://git.rootiest.dev/rootiest/"

PROJECTS = [
    (GT + "fish-config", "fish", "Fish Config",
     "A modular, guard-railed Fish shell configuration with full documentation.", ("Shell config", "Gitea")),
    (GT + "neovim-config", "square-terminal", "Neovim Config",
     "The Rootiest Neovim setup, tuned for everyday development.", ("Editor config", "Gitea")),
    (GH + "obsidian-ai-image-ocr", "scan-text", "Obsidian AI Image OCR",
     "Obsidian plugin for AI-powered text extraction from images.", ("Obsidian plugin", "GitHub")),
    (GT + "rootiest-ai", "sparkles", "Rootiest AI",
     "Agent plugins and skills for Claude Code and other AI coding agents.", ("Agent plugins", "Gitea")),
    (GT + "claude-tokenization-proxy", "shield-check", "Claude Tokenization Proxy",
     "Masks secrets locally before they reach the Claude API, then restores them in replies.", ("Tool", "Gitea")),
    (GT + "rootiest-iosevka", "type", "Rootiest Iosevka",
     "A custom Iosevka font variant built for terminals and editors.", ("Font", "Gitea")),
    (GT + "tmux-config", "panels-top-left", "Tmux Config", "The Rootiest tmux configuration.", ("Terminal config", "Gitea")),
    (GT + "kitty-config", "cat", "Kitty Config", "The Rootiest kitty terminal configuration.", ("Terminal config", "Gitea")),
    (GH + "nvim-updater.nvim", "refresh-cw", "nvim-updater.nvim",
     "Build and update Neovim from source, from inside Neovim.", ("Neovim plugin", "GitHub")),
    (GH + "neoterm", "terminal", "NeoTerm", "Use Neovide as a traditional terminal emulator.", ("Tool", "GitHub")),
]

KLIPPER = [
    (GH + "printcfg", "settings", "PrintCFG", "A suite of macros to enhance the Klipper experience.", ("Klipper macros", "GitHub")),
    (GH + "zippy-klipper_config", "printer", "Zippy Klipper Config", "Klipper configurations, macros and tuning.",
     ("Klipper config", "GitHub")),
    (GH + "zippy_guides", "book-open", "Zippy Guides", "Guides for all things Klipper.", ("Docs", "GitHub")),
    (GH + "klipper-scripts", "scroll-text", "Klipper Scripts", "Scripts that simplify userspace modification of Klipper.",
     ("Scripts", "GitHub")),
    (GH + "CANburner", "cpu", "CANBurner", "A CAN bus adapter PCB for 3D printers.", ("Hardware", "GitHub")),
]

# (url, icon, name, description, public)
SERVICES = [
    ("Start here", [
        ("https://auth.rootiest.dev", "fingerprint", "RootiestID",
         "Single sign-on for every Rootiest service, with passkey support.", True),
        ("https://status.rootiest.dev", "activity", "Status Page",
         "Live health of every service and server, with push alerts.", True),
        ("https://support.rootiest.dev", "life-buoy", "Support Desk",
         "Open and track support tickets for any Rootiest service.", True),
    ]),
    ("Notes &amp; knowledge", [
        ("https://notes.rootiest.com", "notebook-pen", "Notes",
         "Quick notes and memos on a private Memos instance.", True),
        ("https://joplin.rootiest.com", "notebook", "Joplin Sync",
         "Sync server for the Joplin note-taking apps.", False),
        ("https://livesync.rootiest.dev", "gem", "Obsidian LiveSync",
         "Real-time Obsidian vault sync, replicated across two servers.", False),
    ]),
    ("Files &amp; media", [
        ("https://photos.rootiest.com", "image", "Photos",
         "Private photo and video library with search and ML features, powered by Immich.", False),
        ("https://files.rootiest.com", "folder-open", "Files",
         "File storage and sharing over the web and SFTP, powered by SFTPGo.", False),
        ("https://disk.rootiest.dev", "hard-drive", "Disk",
         "Fast file server with uploads, media playback and sharing, powered by copyparty.", False),
        ("https://pages.rootiest.fyi", "globe", "Pages",
         "Static sites and published docs for Rootiest projects.", True),
    ]),
    ("Developer tools", [
        ("https://git.rootiest.dev", "git-branch", "Git",
         "Gitea code hosting with CI runners, packages and SSH access.", True),
        ("https://gists.rootiest.dev", "code", "Gists",
         "Share code snippets and pastes, powered by Opengist.", True),
        ("https://rootiest.link", "link", "Short Links",
         "Privacy-respecting, ad-free URL shortener with stats.", True),
        ("https://wakatime.rootiest.dev", "timer", "Coding Stats",
         "Track your coding time with WakaTime-compatible plugins, powered by Wakapi.", True),
    ]),
    ("Privacy &amp; communication", [
        ("https://vault.rootiest.dev", "lock-keyhole", "Password Vault",
         "Bitwarden-compatible password manager with autofill and TOTP.", False),
        ("https://chat.rootiest.com", "bot", "AI Chat",
         "LibreChat workspace for many AI models, with file search.", False),
        ("https://ntfy.rootiest.dev", "bell", "Push Notifications",
         "Send push notifications to your phone or desktop over HTTP, powered by ntfy.", False),
        ("https://molly.rootiest.dev", "message-square-lock", "MollySocket",
         "UnifiedPush notifications for the Molly Signal client, without Google services.", False),
        ("https://pds.rootiest.dev", "at-sign", "Bluesky PDS",
         "A self-hosted Bluesky personal data server for AT Protocol accounts.", False),
    ]),
]


def svc_card(s, hue=None):
    url, icon, name, desc, public = s
    return card(url, icon, name, desc, (url.removeprefix("https://"),), public, badge=True, hue=hue)


HUES = {"Start here": "red", "Notes &amp; knowledge": "yellow", "Files &amp; media": "blue",
        "Developer tools": "green", "Privacy &amp; communication": "mauve"}
ALL = {s[2]: s for _, group in SERVICES for s in group}
CAT = {s[2]: HUES[title] for title, group in SERVICES for s in group}
FEATURED = ["Photos", "Notes", "Password Vault", "Git", "Files", "AI Chat"]

# ---------------------------------------------------------------- index.html
index = head("Rootiest Solutions",
             "Rootiest Solutions: self-hosted, privacy-respecting services and open-source tools, configs and "
             "plugins for developers and makers.", "https://rootiest.com")
index += header("Home")
index += f"""
  <main class="wrap">
    <section class="hero">
      <img src="/img/icons/logo.svg" alt="Rootiest logo" class="hero-logo" width="112" height="112" />
      <h1>Rootiest <span class="accent">Solutions</span></h1>
      <p class="lede">Self-hosted, privacy-respecting services and open-source tools for developers and makers.</p>
      <a href="https://status.rootiest.dev/" class="status-badge">
        <img src="https://status.rootiest.dev/badge.svg?theme=mocha&amp;style=for-the-badge" alt="Rootiest Services status" />
      </a>
      <div class="actions">
        <a href="/services.html" class="btn primary">Explore services</a>
        <a href="https://github.com/rootiest" class="btn">GitHub</a>
        <a href="https://git.rootiest.dev/rootiest" class="btn">Gitea</a>
      </div>
    </section>

{section("Hosted services", [svc_card(ALL[n], CAT[n]) for n in FEATURED], ("/services.html", "All services →"))}
{section("Projects", [card(*p) for p in PROJECTS], ("https://github.com/rootiest?tab=repositories", "All repositories →"), hue="peach")}
{section("Klipper &amp; 3D printing", [card(*p) for p in KLIPPER], hue="sky")}
    <section class="section">
      <div class="section-head">
        <h2>Activity</h2>
      </div>
      <a href="https://github.com/rootiest" class="snake">
        <picture>
          <source srcset="/img/github-snake-dark.svg" media="(prefers-color-scheme: dark)" />
          <img src="/img/github-snake.svg" alt="Animated snake eating the GitHub contribution graph" loading="lazy" width="880" height="192" />
        </picture>
      </a>
    </section>
  </main>

"""
index += footer()
index += """
  <script src="https://storage.ko-fi.com/cdn/scripts/overlay-widget.js"></script>
  <script>
    kofiWidgetOverlay.draw('rootiest', {
      'type': 'floating-chat',
      'floating-chat.donateButton.text': 'Support me',
      'floating-chat.donateButton.background-color': '#ff004c',
      'floating-chat.donateButton.text-color': '#fff'
    });
  </script>
  <script src="https://cdn.jsdelivr.net/npm/@widgetbot/crate@3" async defer>
    new Crate({
      server: '1058478355973939220',
      channel: '1115928968101634082'
    })
  </script>
</body>
</html>
"""

# ------------------------------------------------------------- services.html
svc = head("Rootiest Services", "Self-hosted, privacy-respecting services run by Rootiest Solutions",
           "https://rootiest.com/services.html")
svc += header("Services")
svc += """
  <main class="wrap">
    <section class="hero compact">
      <img src="/img/icons/logo.svg" alt="" class="hero-logo" width="72" height="72" />
      <h1>Rootiest Services</h1>
      <p class="lede">Self-hosted, privacy-respecting services. One RootiestID account signs you in to all of them.</p>
      <p class="note">
        Services marked <span class="pill">Public</span> are open to everyone. The rest are for members:
        a RootiestID account alone doesn't unlock them, because each one is enabled by membership in its
        RootiestID group. To request access, <a href="https://support.rootiest.dev/">open a support ticket</a>.
      </p>
    </section>

"""
svc += "\n".join(section(title, [svc_card(s) for s in group], hue=HUES[title]) for title, group in SERVICES)
svc += "  </main>\n\n" + footer(badges=False) + "</body>\n</html>\n"

# --------------------------------------------------------- contact/index.html
CONTACTS = [
    ("https://support.rootiest.dev/", "life-buoy", "Support Desk", "support.rootiest.dev"),
    ("/discord.html", "message-circle", "Discord", "@Rootiest"),
    ("https://bsky.app/profile/rootiest.com", "at-sign", "Bluesky", "@rootiest.com"),
    ("https://fosstodon.org/@rootiest", "rss", "Mastodon", "@rootiest@fosstodon.org"),
    ("https://lemmy.world/u/Rootiest", "users", "Lemmy", "@Rootiest@lemmy.world"),
    ("https://matrix.to/#/@rootiest:matrix.org", "message-square-lock", "Matrix", "@rootiest:matrix.org"),
    ("mailto:chris@rootiest.com", "mail", "Email", "chris@rootiest.com"),
]
contact = head("Rootiest Solutions: Contact", "Ways to get in touch with Rootiest Solutions",
               "https://rootiest.com/contact", gtag=False)
contact += header("Contact")
contact += f"""
  <main class="wrap">
    <section class="hero compact">
      <img src="/img/icons/logo.svg" alt="" class="hero-logo" width="72" height="72" />
      <h1>Contact</h1>
      <p class="lede">Need help with a Rootiest service? The support desk is the fastest way. For anything else, pick a channel below.</p>
      <div class="actions">
        <a href="https://support.rootiest.dev/" class="btn primary">Open a ticket</a>
        <a href="/discord.html" class="btn">Join the Discord</a>
      </div>
    </section>

{section("How to reach me", [card(h, i, t, d) for h, i, t, d in CONTACTS], hue="lavender")}
    <section class="section">
      <div class="section-head">
        <h2>Community</h2>
      </div>
      <a href="/discord.html" class="discord-banner">
        <img src="/img/discord-banner.png" alt="Rootiest Discord server banner" />
      </a>
    </section>

    <section class="section">
      <div class="section-head">
        <h2>Verify my identity</h2>
      </div>
      <div class="grid hue-green">
        <a href="https://keys.openpgp.org/vks/v1/by-fingerprint/0FD25CCBCE46D16B8297DDA2623CE33E5CF323D5" class="card">
          {tile("key-round")}
          <div class="card-body">
            <h3>GPG public key</h3>
            <p class="fingerprint">0FD2 5CCB CE46 D16B 8297 DDA2 623C E33E 5CF3 23D5</p>
            <span class="meta"><span>keys.openpgp.org</span><span>also at /keys/rootiest.asc</span></span>
          </div>
        </a>
      </div>
    </section>
  </main>

"""
contact += footer(badges=False) + "</body>\n</html>\n"

(ROOT / "index.html").write_text(index)
(ROOT / "services.html").write_text(svc)
(ROOT / "contact" / "index.html").write_text(contact)
print("ok")


# ------------------------------------------------------------ legal pages
def legal_body(path, start, end):
    """Return the legal text. Re-runs read it back from the <article> wrapper."""
    s = (ROOT / path).read_text()
    if '<article class="legal">' in s:
        a = s.index('<article class="legal">') + len('<article class="legal">')
        return s[a:s.rindex("</article>")].strip("\n").rstrip()
    return s[s.index(start):s.index(end)].rstrip()


def legal_page(path, title, desc, url, h1, lede, body, credit=""):
    page = head(title, desc, url, gtag=False) + header(None)
    page += f"""
  <main class="wrap">
    <section class="hero compact">
      <h1>{h1}</h1>
      <p class="lede">{lede}</p>
    </section>

    <article class="legal">
{body}
    </article>
{credit}  </main>

"""
    page += footer(badges=False) + "</body>\n</html>\n"
    (ROOT / path).write_text(page)


privacy_body = legal_body("privacy/index.html", '<div data-custom-class="body">',
                          '\n        <div style="color: #595959;font-size: 14px;font-family: Arial;padding-top:16px;">')
legal_page("privacy/index.html", "Privacy Policy - Rootiest", "Privacy Policy for Rootiest Solutions LLC",
           "https://rootiest.com/privacy", "Privacy Policy", "How Rootiest Solutions handles your information.",
           privacy_body,
           '    <p class="legal-credit">This privacy policy was created using Termly\'s '
           '<a href="https://termly.io/products/privacy-policy-generator/">Privacy Policy Generator</a>.</p>\n')

tos_body = legal_body("tos/index.html", '<p class="intro">', "\n      </div>\n    </div>\n  </section>")
legal_page("tos/index.html", "Rootiest Solutions: Terms of Service",
           "Outlines the terms of service for Rootiest Solutions", "https://rootiest.com/tos",
           "Terms of Service", "Last updated: July 24, 2026", tos_body)
print("legal ok")
