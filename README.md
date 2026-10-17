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
