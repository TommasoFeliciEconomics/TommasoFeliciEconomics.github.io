# tommasofelici.com — Quarto site

Built from your CV. Almost everything is filled in already.

## What still needs you

1. **`CHANGE-ME-scholar-url` in `index.qmd`** — your Google Scholar profile link.
   This is the only placeholder left in the whole project. If you do not have a
   Scholar profile, delete that link entirely.
2. **`images/profile.jpg`** — replace the grey silhouette with a real photo.
   Portrait orientation, roughly 800×1000, under 300 KB.
3. **`images/banner.jpg`** — the wide image behind each page title. The one in
   here is generated, not a photograph. Keep the filename. Wide (2000px+), dark
   and low contrast. Free, no attribution: [unsplash.com](https://unsplash.com).
4. **Three PDFs in `files/`** — currently one-line placeholders. Replace with the
   real files, keeping the filenames:
   - `freshwater-consumption.pdf`
   - `animal-food-kuznets-curve.pdf`
   - `economic-exposure.pdf`
5. **`CNAME` and `site-url:` in `_quarto.yml`** — your domain, once you buy it.

`files/cv.pdf` is already your real CV.

## Working on it

```
quarto preview     # live preview, reloads as you save
quarto render      # one-off build into _site/
```

## Publishing

Push to `main`; the workflow in `.github/workflows/publish.yml` does the rest.

```
git add -A
git commit -m "Update research page"
git push
```

## Adding a paper

Copy one `::: {.paper}` block in `research.qmd` and change the fields. Published
articles use a `.journal` line; work in progress uses an `.abstract` line
instead. Both are optional.

## Housekeeping

`make_placeholders.py` regenerates the stand-in banner, photo and paper PDFs. It
does **not** touch `files/cv.pdf`. Delete it once you have replaced everything.
