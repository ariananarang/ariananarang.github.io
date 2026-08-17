# Images

Drop your image files in this folder using the exact filenames below, then follow
"Swapping in a real image" at the bottom. Every image on the site is currently a
coloured placeholder block showing the filename it expects.

## Filenames the site expects

### Homepage
| File | Where it appears | Recommended size |
|---|---|---|
| `hero.jpg` | Big portrait at the top of the homepage | 1600 × 900 (16:9) |

### Case studies
Each project needs one hero band and up to six gallery shots.

| File pattern | Where | Recommended size |
|---|---|---|
| `<slug>-hero.jpg` | Wide band under the project title | 1800 × 750 (2.4:1) |
| `<slug>-01.jpg` … `-06.jpg` | Gallery grid lower on the page | 1200 × 800 (3:2) |

The slugs are:

```
obstructed-brews      lets-be-real          jbtb-summer
bosch-justaguy        cold-tux              dune-prophecy
essentia-change       black-dont-crack      topochico
accenture-reinvented  chase
```

So a project with placeholders wants `<slug>-hero.jpg`, `<slug>-01.jpg`, and so on.

### Obstructed Brews is already done

Its real assets are in place, and it uses the newer approach described under
"Real images in build.py" below — campaign boards shown full width, plus one
captioned photo. Its files are:

```
obstructed-brews-hero.jpg        the PR key visual
obstructed-brews-board-1.webp    campaign board — press and results
obstructed-brews-board-2.webp    technology board
obstructed-brews-board-3.webp    app flow board
obstructed-brews-board-4.webp    stadium geofencing board
obstructed-brews-clio.jpg        Clio Sports awards photo
```

## Real images in build.py

Rather than hand-editing HTML, add the filenames to the project's entry in
`build.py` and re-run `python3 build.py`. Three optional fields:

| Field | What it does |
|---|---|
| `hero_img=(file, alt)` | Fills the band under the title. A real image keeps its own proportions instead of being cropped to 2.4:1. |
| `boards=[(file, alt), …]` | Full-width, uncropped, stacked. Use for dense layouts like award boards, where cropping would cut the type off. Each one links to the full-size file. |
| `photos=[(file, alt, caption), …]` | A photo at reading width with a caption under it. |

Set `gallery=0` when real images replace the placeholder grid.

## Swapping in a real image

Find the placeholder in the HTML — it looks like this:

```html
<div class="portrait"><span class="ph">Add your portrait — images/hero.jpg</span></div>
```

Replace the inner `<span>` with an `<img>`:

```html
<div class="portrait"><img src="images/hero.jpg" alt="Ariana Narang"></div>
```

On case study pages the path needs `../` because those files live in `work/`:

```html
<div class="hero-band c-blue"><img src="../images/obstructed-brews-hero.jpg" alt="Obstructed Brews"></div>
```

The container handles cropping and aspect ratio, so the image just needs to be
roughly the right shape — it will fill the box without distorting.

## Before you upload

- **Resize.** Nothing needs to be wider than 1800px. A 5MB camera file will make
  the page slow for no visible benefit.
- **Compress.** [Squoosh](https://squoosh.app) is free and runs in the browser —
  aim for under 300KB per image.
- **Use `.jpg` for photos**, `.png` only if you need transparency.

## Getting images out of Squarespace

Do this *before* cancelling — the image URLs stop working when the site goes down.

1. Open each project page on your live site.
2. Right-click each image → "Save image as…"
3. Rename to match the table above.

Squarespace's built-in export (Settings → Import & Export) produces a WordPress
XML file that references images by URL rather than bundling them, so
right-click-saving is more reliable for this.
