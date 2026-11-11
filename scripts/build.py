#!/usr/bin/env python3
# Copyright (C) 2026 Chris Laprade (chris@rootiest.com)
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Generate the rootiest.com pages into site/ (or the directory given).

Usage: python3 scripts/build.py [OUTPUT_DIR]

Content lives in scripts/sitegen/data/ (services, projects, contacts) and
content/legal/ (policy text). Never edit the generated .html files in site/.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from sitegen.pages import contact, home, legal, not_found, projects, redirects, services, sitemap  # noqa: E402

GENERATED = (home, services, projects, contact, legal, not_found, redirects, sitemap)


def main():
    """Write every generated page and print how many were written."""
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "site"
    count = 0
    for module in GENERATED:
        for rel, text in module.build().items():
            dest = out / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(text)
            count += 1
    print(f"wrote {count} files to {out}")


if __name__ == "__main__":
    main()
