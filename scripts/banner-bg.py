"""Generate scripts/banner-bg.png: the glow background for the 1200x630 social banner.

The glows are computed in floating point with smooth Gaussian falloffs and dithered with
triangular noise before rounding to 8 bits. Browsers round CSS gradients first, which shows as
banding on dark colours. Needs numpy. Called by render-banner.py; can also be run on its own.
"""
import struct
import zlib
from pathlib import Path

import numpy as np

W, H = 1200, 630
BASE = (30, 30, 46)  # Catppuccin Mocha base #1e1e2e
# (centre x, centre y, sigma px, peak opacity, colour)
GLOWS = [
    (258, 315, 120, 0.26, (255, 0, 76)),  # brand red behind the logo (logo centre)
    (1100, 80, 150, 0.10, (203, 166, 247)),  # Mocha mauve, top right
]
OUT = Path(__file__).resolve().parent / "banner-bg.png"


def render():
    y, x = np.mgrid[0:H, 0:W].astype(np.float64)
    img = np.empty((H, W, 3))
    img[:] = BASE
    for cx, cy, sigma, peak, colour in GLOWS:
        a = peak * np.exp(-((x - cx) ** 2 + (y - cy) ** 2) / (2 * sigma**2))
        img = img * (1 - a[..., None]) + np.array(colour, dtype=np.float64) * a[..., None]
    # Triangular-PDF dither of +-1 level, fixed seed so re-renders are identical
    rng = np.random.default_rng(1200630)
    img += rng.random(img.shape) + rng.random(img.shape) - 1.0
    return np.clip(np.rint(img), 0, 255).astype(np.uint8)


def write_png(path, pixels):
    h, w, _ = pixels.shape
    raw = b"".join(b"\x00" + pixels[row].tobytes() for row in range(h))

    def chunk(kind, data):
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data))

    path.write_bytes(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
                     + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))


if __name__ == "__main__":
    write_png(OUT, render())
    print(f"wrote {OUT.name}")
