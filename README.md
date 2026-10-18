# rootiest.github.io

Source for [rootiest.com](https://rootiest.com), deployed by Netlify from `main`.

The pages are plain static HTML, styled by `assets/site.css` (Catppuccin Latte/Mocha) with
icon glyphs from `assets/icons.svg` ([Lucide](https://lucide.dev), ISC License).

## Updating content

Projects, services and contact links live as data in `scripts/build.py`. Edit them there and
regenerate the pages:

```sh
python3 scripts/build.py
```

This rewrites `index.html`, `services.html`, `contact/index.html`, `privacy/index.html` and
`tos/index.html`. The policy wording on the legal pages is read back from each page, so edit
that text directly in the HTML.

## Social preview image

`img/banner.png` (1200×630, used for `og:image`) is rendered from `scripts/banner.html`.
It is always Catppuccin Mocha, since link previews can't follow the viewer's light/dark mode.
The glows are not CSS gradients: `scripts/banner-bg.py` computes them and dithers them into
`scripts/banner-bg.png`, because browser gradients band visibly on dark colours.
After editing either file, re-render with Firefox and numpy installed:

```sh
python3 scripts/render-banner.py
```

When the image changes, bump the `?v=` number on the `og:image` URL in `scripts/build.py` and
rebuild, so Discord and other sites fetch the new one instead of their cached copy.
