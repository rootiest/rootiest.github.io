#!/usr/bin/env python3
# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Check the built site in site/.

Usage: python3 scripts/check.py

Fails (exit 1) when:
  - site/ is not what scripts/build.py generates (someone edited output by hand,
    or forgot to rebuild after changing data or content);
  - an internal link, image, stylesheet or icon reference points at nothing;
  - a page loads a script, stylesheet, frame or font from another site;
  - a page lacks lang, <title>, a meta description or a canonical link
    (redirect pages need only a title and canonical);
  - an in-page #fragment has no matching id.
"""
import filecmp
import re
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"


class Page(HTMLParser):
    """Collects references, ids and head metadata from one HTML document."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.refs, self.ids, self.meta = [], set(), {}
        self.title = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "html":
            self.meta["lang"] = a.get("lang")
        if tag == "title":
            self.title = True
        if tag == "meta" and a.get("name") == "description":
            self.meta["description"] = a.get("content")
        if tag == "meta" and a.get("http-equiv") == "refresh":
            self.meta["refresh"] = True
        if tag == "link" and a.get("rel") == "canonical":
            self.meta["canonical"] = a.get("href")
        for attr in ("href", "src"):
            if a.get(attr):
                self.refs.append((tag, attr, a[attr], a.get("rel")))
        if a.get("srcset"):
            self.refs.extend((tag, "srcset", s.split()[0], None) for s in str(a["srcset"]).split(","))


def target(ref, page):
    """Map a site-relative reference to the file that must exist, or None if external."""
    u = urlsplit(ref)
    if u.scheme or ref.startswith(("//", "mailto:", "bitcoin:")):
        return None
    path = unquote(u.path)
    if not path:
        return page
    base = SITE if path.startswith("/") else page.parent
    f = (base / path.lstrip("/")).resolve()
    if path.endswith("/") or f.is_dir():
        f = f / "index.html"
    return f


def main():
    """Run every check and print problems; exit 1 if there are any."""
    problems = []

    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([sys.executable, str(ROOT / "scripts" / "build.py"), tmp], check=True,
                       stdout=subprocess.DEVNULL)
        for f in Path(tmp).rglob("*"):
            if f.is_file():
                live = SITE / f.relative_to(tmp)
                if not live.exists() or not filecmp.cmp(f, live, shallow=False):
                    problems.append(f"{live.relative_to(ROOT)}: out of date, run scripts/build.py")

    pages = {p: Page() for p in SITE.rglob("*.html")}
    for p, parser in pages.items():
        parser.feed(p.read_text())

    for p, parser in pages.items():
        rel = p.relative_to(ROOT)
        m = parser.meta
        if not parser.title or not m.get("canonical"):
            problems.append(f"{rel}: missing <title> or canonical link")
        if not m.get("refresh") and (not m.get("lang") or not m.get("description")):
            problems.append(f"{rel}: missing lang or meta description")
        for tag, attr, ref, rel_attr in parser.refs:
            external = urlsplit(ref).scheme in ("http", "https") or ref.startswith("//")
            loads = tag in ("script", "iframe") or (tag == "link" and rel_attr in ("stylesheet", "preload", "modulepreload"))
            if external and loads:
                problems.append(f"{rel}: third-party {tag} {ref}")
            if tag == "link" and rel_attr == "canonical":
                continue
            f = target(ref, p)
            if f is None:
                continue
            if not f.exists():
                problems.append(f"{rel}: broken {attr} {ref}")
                continue
            frag = urlsplit(ref).fragment
            if frag and f.suffix == ".html" and f in pages and frag not in pages[f].ids:
                problems.append(f"{rel}: no #{frag} in {f.relative_to(ROOT)}")
            if frag and f.suffix == ".svg" and f'id="{frag}"' not in f.read_text():
                problems.append(f"{rel}: no symbol #{frag} in {f.relative_to(ROOT)}")

    css = (SITE / "assets" / "site.css").read_text()
    for ref in re.findall(r"url\(([^)]+)\)", css):
        ref = ref.strip("'\"")
        if ref.startswith(("http", "//")):
            problems.append(f"site/assets/site.css: third-party url({ref})")

    for line in problems:
        print(line)
    print(f"{len(pages)} pages checked, {len(problems)} problem(s)")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
