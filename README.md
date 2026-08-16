# ariananarang.com

A static portfolio site. No framework, no build step required, no monthly bill.
Three plain HTML pages plus eleven case studies, one stylesheet, and a folder of images.

---

## What's in here

```
index.html          Homepage — portrait, bio, five featured projects
work.html           All eleven projects
contact.html        Bio, areas of expertise, contact details
work/*.html         One page per project (11 files)
assets/style.css    Every style on the site
images/             Your photos go here — see images/README.md
build.py            Optional generator (see "Editing content" below)
CNAME               Tells GitHub Pages your custom domain
404.html            Shown for broken links
.nojekyll           Stops GitHub from reprocessing the files
```

---

## Part 1 — Put it online (about 15 minutes)

You need a free GitHub account: <https://github.com/signup>

### 1. Create the repository

1. Go to <https://github.com/new>
2. **Repository name:** `ariananarang.github.io`
   (this exact name matters — it tells GitHub this is your personal site)
3. Set it to **Public**
4. Don't tick "Add a README"
5. Click **Create repository**

### 2. Upload the files

On the empty repository page, click **uploading an existing file**.

Drag in *everything* from this folder — including the `assets`, `work`, and `images`
folders. Dragging the folders themselves is fine; GitHub preserves the structure.

> **Important:** upload the *contents* of the site folder, not the folder itself.
> `index.html` must sit at the top level of the repository, not inside a subfolder.

Scroll down, click **Commit changes**.

### 3. Turn on Pages

1. In your repository, click **Settings** (top right)
2. **Pages** in the left sidebar
3. Under "Build and deployment" → Source, choose **Deploy from a branch**
4. Branch: **main**, folder: **/ (root)** → **Save**

Wait 2–3 minutes, then visit `https://ariananarang.github.io`. Your site is live and free.

---

## Part 2 — Point ariananarang.com at it

Right now your domain points at Squarespace. **Don't cancel Squarespace yet** — first
check where the domain is actually registered, because that's where you change the DNS.

### If the domain is registered with Squarespace

Squarespace domains can point at an external host, but if you're leaving entirely it's
usually cleaner to **transfer the domain out** to a registrar like Cloudflare or Porkbun
(roughly $10–20/year — the domain itself is the one thing that isn't free).

Squarespace: Settings → Domains → your domain → Transfer Domain, and follow the unlock
and auth-code steps. Transfers take 5–7 days, so start this before cancelling anything.

### If the domain is registered elsewhere (GoDaddy, Namecheap, Google Domains…)

Log in there and edit the DNS records. Delete the existing records pointing at
Squarespace, then add these:

**Four A records** — Host `@`, pointing to:

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

**One CNAME record** — Host `www`, pointing to:

```
ariananarang.github.io
```

### Then, back in GitHub

1. Settings → Pages → **Custom domain**
2. Enter `www.ariananarang.com` → Save
3. Wait for the DNS check to pass (can take up to 24 hours, usually much less)
4. Tick **Enforce HTTPS** once it becomes available

The `CNAME` file in this folder already contains `www.ariananarang.com`, so step 2 may
already be filled in for you.

### Only then, cancel Squarespace

Confirm `https://www.ariananarang.com` loads the new site first. And **make sure you've
saved your images** (see `images/README.md`) — they disappear with the account.

---

## Editing content

### Small changes

Open the relevant `.html` file in any text editor and edit the text. You can even do it
in GitHub's web interface: click the file → pencil icon → edit → Commit. The site
updates within a minute.

### Bigger changes (adding a project, reordering, changing several pages at once)

All the content lives in one place: the `PROJECTS` list at the top of `build.py`.
Edit it, then run:

```bash
python3 build.py
```

That regenerates every page consistently. Useful because a project's title appears in
four places — the homepage card, the work index, its own page, and the prev/next links
on its neighbours — and the generator keeps them in sync.

Each project entry accepts:

| Field | Meaning |
|---|---|
| `slug` | URL and image filename prefix |
| `title`, `client`, `type`, `role`, `year` | Shown in the card tag and the meta bar |
| `color` | `c-blue`, `c-orange`, `c-lime`, `c-pink`, or `c-plum` |
| `feature` | `True` makes it the wide card on the homepage |
| `sub` | One line under the title |
| `blurb` | Text on the homepage/work card |
| `quote` | Optional pull quote at the top of the body |
| `body` | List of paragraphs |
| `results` | Optional list of `(number, label)` pairs |
| `credits` | List of `(role, name)` pairs |
| `awards`, `press` | Optional |
| `gallery` | How many gallery slots to create |

### Changing colours or fonts

Everything is in the `:root` block at the top of `assets/style.css`:

```css
--cream:#FBF3E4;   /* page background */
--ink:#141210;     /* text, borders */
--blue:#2B44F0;    /* the five project colours */
--orange:#FF5A1F;
--lime:#C9F04A;
--pink:#FF3D8A;
--plum:#3B1E5E;
```

Change a value there and it updates everywhere.

---

## Previewing locally before you publish

In this folder, run:

```bash
python3 -m http.server 8000
```

Then open <http://localhost:8000>. Press Ctrl+C to stop.

---

## Running costs

| Item | Cost |
|---|---|
| GitHub Pages hosting | Free |
| SSL certificate | Free, automatic |
| Bandwidth | Free (100GB/month soft limit) |
| Domain registration | ~$10–20/year |

Squarespace was likely $16–23/month, so this is roughly a $200/year saving.
