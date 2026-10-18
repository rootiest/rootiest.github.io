"""Render scripts/banner.html to img/banner.png (1200x630) with headless Firefox.

Run from anywhere:  python3 scripts/render-banner.py
Needs firefox on PATH and numpy (for the dithered glow background, see banner-bg.py).
The page is served over local HTTP so its SVG <use> references load.
"""
import functools
import runpy
import http.server
import subprocess
import tempfile
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "img" / "banner.png"

runpy.run_path(str(ROOT / "scripts" / "banner-bg.py"), run_name="__main__")

handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT))
server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
threading.Thread(target=server.serve_forever, daemon=True).start()
url = f"http://127.0.0.1:{server.server_address[1]}/scripts/banner.html"

try:
    with tempfile.TemporaryDirectory() as profile:
        subprocess.run(
            ["firefox", "--headless", "--no-remote", "--profile", profile,
             "--window-size=1200,630", "--screenshot", str(OUT), url],
            check=True, timeout=120, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
finally:
    server.shutdown()

print(f"wrote {OUT.relative_to(ROOT)}")
