#!/usr/bin/env python3
"""
Builds the static site: index.html, work.html, contact.html and one page per project.
Edit PROJECTS below to change content, then re-run:  python3 build.py
"""
import os, html, json

ROOT = os.path.dirname(os.path.abspath(__file__))

EMAIL = "ariananarang@gmail.com"
PHONE = "(630) 765-4885"
PHONE_HREF = "+16307654885"
SOCIAL = [
    ("LinkedIn",  "http://www.linkedin.com/in/ariananarang"),
    ("Instagram", "https://www.instagram.com/ariananarang"),
    ("Medium",    "https://ariananarang.medium.com/"),
    ("Spotify",   "https://open.spotify.com/user/ariananarang?si=7681a12c6faf4e6f"),
]
BIO = [
    "I'm Ariana, an award-winning Interactive and Experiential Producer based in New York and Chicago.",
    "I specialize in bringing bold, engaging ideas to life by merging storytelling, design, and technology to create integrated campaigns that connect with consumers.",
]
CLIENTS = ["Coors Light","HBO Max","Ad Council","Bosch","Accenture","Essentia","J.P. Morgan Chase","Topo Chico"]

# ---------------------------------------------------------------- project data
PROJECTS = [
    dict(
        slug="obstructed-brews", title="Obstructed Brews", client="Coors Light",
        type="AI Activation", role="Lead Producer", year="2025", color="c-blue", feature=True,
        sub="An AI-powered tool that turned blocked stadium views into free beer.",
        blurb="An AI tool that turned blocked stadium views into free beer — geofencing all 30 MLB stadiums and analyzing 1.2M seats. 161M impressions and a Clio Gold.",
        body=[
            "For MLB's Opening Day, Coors Light partnered with the fans nobody designs for: the ones sitting behind a pole. An AI-powered application scanned photos of blocked views and compensated attendees with beer proportional to how bad the obstruction was.",
            "The technology geofenced all 30 MLB stadiums and analyzed obstructions across 1.2 million seats with 0.05% accuracy.",
            "Production captured fan reactions and documented real redemptions at Citi Field in New York and Chase Field in Phoenix on launch day.",
        ],
        results=[("161M","Impressions"),("71","National placements"),("46+","Broadcast segments"),("98%","Completion rate")],
        credits=[("Role","Lead Producer"),("Production Partner","Sounds Fun"),("Videography","Joey Hamburger"),
                 ("Photography","Adobe Firefly in Photoshop"),("Retouching","Accenture Song"),("Post-Production","Oner Studio")],
        awards=["<b>Clio Sports</b> — Gold (Fan Engagement; Gameday Fan Experience), Bronze (Creative Use of Data)",
                "<b>MAD Stars</b> — Gold (Direct, Mobile, Interactive), Silver (Media), Bronze (Brand Experience &amp; Activation), 2× Shortlist",
                "<b>Cannes Lions</b> — 3× Shortlist",
                "<b>The One Show</b> — 5× Merits"],
        press="LBB · AdWeek · Marketing Dive · PR Newswire · Trend Hunter",
        gallery=4,
    ),
    dict(
        slug="lets-be-real", title="Let's Be Real", client="Ad Council Seize the Awkward",
        type="Film", role="Producer", year="2025", color="c-pink",
        sub="Films about being there for a friend, told entirely through body language.",
        blurb="Stripped-back films told entirely through body language — no dialogue.",
        quote="When your friends are struggling with their mental health, they need a real friend to be there for them. To be real with them.",
        body=[
            "The campaign is a set of stripped-back films that depict authentic support through visual storytelling rather than dialogue.",
            "The narrative emerges through body language — hesitations, nervous laughter, eye contact, and the subtle physical shifts that communicate presence and care.",
        ],
        credits=[("Role","Producer"),("Director","Fenn O'Meally"),("Editor","Carla Luffe"),("Colorist","Dante Pasquinelli"),
                 ("Post-Production / Finishing","Preymaker"),("Music","Lil Silva and Sampha"),("Sound Design / Mix","Kevin Koch")],
        gallery=6,
    ),
    dict(
        slug="jbtb-summer", title="Just Bring The Beer Summer", client="Molson Coors",
        type="Campaign Production", role="Lead Producer", year="2025", color="c-lime",
        sub="Five fully custom-fabricated travel objects, one shoot day, a 27-person crew.",
        blurb="Five bespoke travel objects built to spec, shot in a single day in Rumson, NJ.",
        body=[
            "For Molson Coors' summer campaign, the brief called for five fully custom-fabricated pieces of functional travel gear: a cooler disguised as a suitcase, a six-pack carrying personal item, a shower caddy, a fanny pack, and a bottle-opener luggage tag.",
            "As lead producer I managed the production across two specialty vendors, a 27-person crew, and five talent on a single shoot day in Rumson, NJ.",
            "The constraint wasn't necessarily the shoot — it was getting five bespoke physical objects built to spec and camera-ready in time, and then the 1.5 week sprint to retouch, edit and deliver our final assets for campaign launch.",
        ],
        credits=[("Role","Lead Producer"),("Photography","Jamie Pearl"),("Videography","Michael Francis"),
                 ("Fabrication","Leadoff Studio"),("Production Partner","Nem Fisher Inc."),("Post-Production","Accenture Song")],
        press="AdAge · Design Rush · People · LBB · PR Newswire",
        gallery=4,
    ),
    dict(
        slug="bosch-justaguy", title="Just a Guy", client="Bosch",
        type="Creator Campaign", role="Creator / Influencer Manager", year="2026", color="c-orange",
        sub="Guy Fieri's Super Bowl makeover, amplified by 11 creators.",
        blurb="Guy Fieri's Super Bowl makeover, amplified by 11 creators. #1 in AdWeek's rankings.",
        body=[
            "For Super Bowl 2026, Bosch partnered with Guy Fieri on a transformation campaign that extended well beyond the spot itself.",
            "The effort leveraged creator partnerships to amplify the campaign across social platforms, with Guy's makeover going viral through collaborations with 11 influential creators spanning hospitality, comedy, and tools.",
            "I ran the full creator workstream: outreach and briefing, rate and contract negotiations, feedback loops and final approvals across 11 simultaneous partnerships.",
        ],
        results=[("11","Creators"),("25M+","Collective reach"),("#1","AdWeek SB Ranking"),("20+","Outlets covered")],
        credits=[("Role","Creator / Influencer Manager"),("Campaign hashtag","#LikeABosch")],
        press="Complex · The Hollywood Reporter · Page Six · Variety · AdWeek · 20+ more",
        gallery=4,
    ),
    dict(
        slug="cold-tux", title="Cold Tux", client="Coors Light",
        type="Brand Activation", role="Lead Producer", year="2025", color="c-plum",
        sub="A custom AC-cooled tuxedo, shot the morning of a real wedding.",
        blurb="An AC-cooled tuxedo, shot the morning of a real wedding. Seth Meyers noticed.",
        quote="Coors Light wanted to celebrate wedding season with something real — not a campaign that looked like a wedding, but an actual one.",
        body=[
            "The idea: connect with our Groomsmen Film and leverage the theme of weddings to provide people with something chill.",
            "The suit was a full custom engineering feat with built-in AC cooling coils, a cold-gel bow tie, a thermostat, and LED-lit mountains. The challenge was finding the right groom who fit the brief and getting his fiancée plus four groomsmen on board.",
            "As lead producer, I managed the full fabrication process with <em>m ss ng p eces</em> alongside a budget that required creative problem-solving at every turn. Then embedded a lean eight-person crew for a half-day shoot with photographer Jimmy Marble the morning of Ryan's actual wedding in Winter Park, FL, before the ceremony.",
            "The campaign earned widespread press coverage including a mention from Late Night with Seth Meyers. In the end, we gave a piece of the campaign to consumers on the Coors site, where people could buy the cold-gel bowtie for $32 — a nod to freezing temperature in Celsius.",
        ],
        credits=[("Role","Lead Producer"),("Photography","Jimmy Marble"),("Production Partner","m ss ng p eces"),
                 ("Director","Brian Moore"),("Retouching Partner","Apostrophe"),("Post-Production","Oner Studio")],
        press="Late Night with Seth Meyers · AdAge · Breaking &amp; Entering Media · LBB · Parade · Campaign Live",
        gallery=4,
    ),
    dict(
        slug="dune-prophecy", title="Dune Prophecy", client="HBO Max",
        type="Experiential", role="Producer", year="2024", color="c-plum",
        sub="A four-day immersive activation at New York Comic Con. Sold out in minutes.",
        blurb="A four-day immersive activation at NYCC with 100 robed sisters. Sold out in minutes.",
        body=[
            "An interactive activation for HBO's Dune: Prophecy launch at New York Comic Con — a four-day immersive experience set in near-total darkness with 100 robed sisters, leveraging the Bene Gesserit's \"Voice\" as a weapon.",
            "Participants faced high-stakes challenges and, upon completion, were initiated into the Sisterhood and received a replica Reverend Mother ring.",
            "The 100 robed sisters were professional dancers, hired to capture the grace the piece required. Spatial audio design used pinpoint directional speakers with ambient resonance to create disorientation while still guiding participants via the Voice. Participation was deliberately limited to protect the quality of the experience — and sold out in minutes.",
        ],
        credits=[("Role","Producer"),("Design / Direction","The Glue Society"),("Film / Coordination","Biscuit Filmworks"),
                 ("Audio Design","Volvox Labs"),("Fabrication","Misbehavior"),("Director of Photography","Jesse Bronstein")],
        awards=["<b>AdWeek</b> — Best Experiential Activation by a Media Brand",
                "<b>AdWeek</b> — Top 5 TV-Themed Brand Activations at NY Comic Con"],
        press="LBB · Cosmic Book · Vulture · Entertainment Weekly",
        gallery=4,
    ),
    dict(
        slug="essentia-change", title="Change the Equation", client="Essentia Water",
        type="Social Campaign", role="Producer", year="2024", color="c-lime",
        sub="A guerrilla-style NYC takeover of fitness spaces, built for social.",
        blurb="A guerrilla NYC fitness takeover with custom fabrication, shot with a skeleton crew.",
        body=[
            "Essentia's <em>Change the Equation</em> campaign featured a NYC takeover at fitness spaces like Action Black Nomad, plus collaborations with street and fitness influencers to weave the brand into the city's active lifestyle scene.",
            "Fabrication included a custom jacket that held about 20 Essentia water bottles, a branded basketball, a skateboard, an enormous shopping bag, bucket drums, delivery boxes, a newspaper, boxing gloves and a punching bag.",
            "Shot guerrilla-style with a skeleton crew, built specifically for social.",
        ],
        credits=[("Role","Producer"),("Production Partner","OzTech Media"),("Director of Photography","Zach Hetrick"),("Editor","Saki Bergh")],
        press="LBB · AdAge · PR Newswire · Marketing Dive · Media Post",
        gallery=4,
    ),
    dict(
        slug="black-dont-crack", title="Black Don't Crack", client="Ad Council Seize the Awkward",
        type="Film", role="Associate Producer", year="2023", color="c-pink",
        sub="A campaign with Megan Thee Stallion on emotional suppression and mental health.",
        blurb="A film with Megan Thee Stallion on the cost of emotional suppression.",
        body=[
            "Seize the Awkward focuses on normalizing mental health conversations among teens within BIPOC communities.",
            "This campaign used \"Black Don't Crack\" metaphorically, to illustrate the harmful effects of emotional suppression on mental wellbeing.",
        ],
        credits=[("Role","Associate Producer"),("Director","Ewurakua Dawson-Amoah"),("Editor","Sophia Lou | Cartel"),
                 ("VFX","The Mill"),("Tactical","Accenture Song")],
        awards=["<b>Mosaic Awards</b> — Innovative Narrative Award Winner",
                "<b>Anthem Awards</b> — Gold, Best Influencer Collaboration",
                "<b>Anthem Awards</b> — Silver, Film, Video, Television or Show"],
        gallery=4,
    ),
    dict(
        slug="topochico", title="Pawn Shop", client="Topo Chico Hard Seltzer",
        type="Experiential", role="Producer", year="2023", color="c-orange",
        sub="A Cinco de Mayo popup pawn shop trading offensive merch for hard seltzer.",
        blurb="A popup pawn shop in NYC where offensive holiday merch bought you a hard seltzer.",
        quote="Margaritas from a hollowed out watermelon. \"Cinco de Drinko.\" Margaritaville. The margarita has become victim to basic drinking culture.",
        body=[
            "The campaign aimed to position the brand's margarita hard seltzer as the innovative alternative.",
            "A popup pawn shop launched on Cinco de Mayo at 7th St &amp; 1st Ave in NYC, where customers could exchange offensive holiday-themed merchandise for the new product.",
        ],
        credits=[("Role","Producer"),("Photography","Paul McGeiver"),("Production Partner","Lime Media"),
                 ("Prop Rental","ACME Studios"),("Prop Stylist","John Jenkins"),("Microsite","Molson Coors Digital Operations")],
        gallery=4,
    ),
    dict(
        slug="accenture-reinvented", title="Reinvented with Accenture", client="Accenture",
        type="Animation", role="Co-Producer", year="2023", color="c-blue",
        sub="A pointillism-inspired particle system that morphs into any form.",
        blurb="A pointillism-inspired particle system built to shift and morph into any form.",
        quote="Reinvented with Accenture spotlights how Accenture is working with clients to drive some of their most significant business reinventions, including through the transformative power of technologies like generative AI.",
        body=[
            "A pointillism-inspired campaign for Accenture, creating a dynamic particle system capable of shifting and morphing into any form.",
        ],
        credits=[("Role","Co-Producer"),("Production Partner","GRIF Studio"),("Animator","Shane Griffin")],
        gallery=4,
    ),
    dict(
        slug="chase", title="Business Banking", client="J.P. Morgan Chase",
        type="Integrated / Tactical", role="Interactive Producer", year="2023", color="c-plum",
        sub="200+ deliverables across OOH, display, social and print.",
        blurb="200+ deliverables across OOH, display, social and print, on ever-changing timelines.",
        body=[
            "JPM Chase runs a yearly consumer banking campaign that partners with small businesses to feature their Chase Business Banking solutions.",
            "As the lead Producer for tactical, I have managed tight timelines that are ever-changing, and over 200+ deliverables across OOH, Display, Social and Print.",
        ],
        results=[("200+","Deliverables"),("4","Channels")],
        credits=[("Role","Interactive Producer"),("Production Partner","Accenture Song"),
                 ("Mechanicals Designer","Emmanuel Perez"),("Retouching","S'well")],
        gallery=4,
    ),
]

# ---------------------------------------------------------------- partials
HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,800&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}assets/style.css">
</head>
<body>
<a class="sr-only" href="#main">Skip to content</a>
<header>
  <div class="wrap nav">
    <a class="logo" href="{base}index.html">ariana narang<span class="dot">.</span></a>
    <ul>
      <li><a href="{base}work.html"{work_cur}>Work</a></li>
      <li><a class="cta" href="{base}contact.html">Let's talk</a></li>
    </ul>
  </div>
</header>
<main id="main">
"""

def footer(base=""):
    links = "".join(f'<li><a href="{u}">{n}</a></li>' for n, u in SOCIAL)
    return f"""</main>
<footer>
  <div class="wrap">
    <h2 class="disp">Let's make<br>something <span class="y">together</span></h2>
    <a class="mail" href="mailto:{EMAIL}">{EMAIL}</a>
    <ul class="social">{links}</ul>
    <p class="fine">&copy; 2026 Ariana Narang &mdash; New York &amp; Chicago</p>
  </div>
</footer>
</body>
</html>
"""

def marquee():
    run = " ".join(f"{c} <em>&#10022;</em>" for c in CLIENTS)
    return f'<div class="marq"><div class="track"><span>{run}</span><span>{run}</span></div></div>\n'

def ph(text):
    return f'<span class="ph">{text}</span>'

def card(p, base=""):
    feat = " feature" if p.get("feature") else ""
    return f"""      <a class="card{feat} {p['color']}" href="{base}work/{p['slug']}.html">
        <div class="img"><span class="tag">{p['type']}</span>{ph(p['title'])}</div>
        <div class="body">
          <span class="client">{p['client']}</span>
          <h3>{p['title']}</h3>
          <p class="blurb">{p['blurb']}</p>
          <span class="more">Read more <span>&rarr;</span></span>
        </div>
      </a>
"""

# ---------------------------------------------------------------- pages
def build_index():
    cards = "".join(card(p) for p in PROJECTS[:5])
    bio = "".join(f"<p>{b}</p>" for b in BIO)
    out = HEAD.format(title="Ariana Narang — Interactive & Experiential Producer",
                      desc=BIO[0], base="", work_cur="")
    out += f"""<section class="hero">
  <div class="blob b1"></div><div class="blob b2"></div><div class="blob b3"></div>
  <div class="wrap">
    <h1 class="sr-only">Ariana Narang &mdash; Interactive and Experiential Producer</h1>
    <!-- Swap the <span class="ph"> below for: <img src="images/hero.jpg" alt="Ariana Narang"> -->
    <div class="portrait">{ph("Add your portrait &mdash; images/hero.jpg")}</div>
    <div class="hero-bio">{bio}</div>
    <div class="chips">
      <span class="chip">Experiential</span><span class="chip">AI-Powered</span>
      <span class="chip">Integrated</span><span class="chip">Award-Winning</span>
    </div>
  </div>
</section>
{marquee()}<section class="wrap work">
  <div class="sechead"><h2 class="disp">Selected Work</h2></div>
  <div class="grid">
{cards}  </div>
  <p style="margin:44px 0 0"><a class="chip" href="work.html" style="text-decoration:none;padding:12px 24px">See all {len(PROJECTS)} projects &rarr;</a></p>
</section>
"""
    out += footer()
    open(os.path.join(ROOT, "index.html"), "w").write(out)

def build_work():
    cards = "".join(card(p) for p in PROJECTS)
    out = HEAD.format(title="Work — Ariana Narang", desc="Selected work from Ariana Narang.",
                      base="", work_cur=' aria-current="page"')
    out += f"""<section class="wrap work" style="padding-top:64px">
  <div class="sechead"><h1 class="disp">Work</h1><span class="count">{len(PROJECTS)} Projects</span></div>
  <div class="grid">
{cards}  </div>
</section>
"""
    out += footer()
    open(os.path.join(ROOT, "work.html"), "w").write(out)

def build_contact():
    rows = f"""      <div class="row"><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
      <div class="row"><dt>Phone</dt><dd><a href="tel:{PHONE_HREF}">{PHONE}</a></dd></div>
      <div class="row"><dt>Based</dt><dd>New York &amp; Chicago</dd></div>
"""
    social = "".join(f'<div class="row"><dt>{n}</dt><dd><a href="{u}">@ariananarang</a></dd></div>\n' for n, u in SOCIAL)
    out = HEAD.format(title="Contact — Ariana Narang", desc=f"Get in touch with Ariana Narang — {EMAIL}",
                      base="", work_cur="")
    out += f"""<section class="contact-hero">
  <div class="blob b1"></div><div class="blob b2"></div>
  <div class="wrap">
    <span class="badge"><i></i> Open to new work</span>
    <h1 class="disp">Say <span class="b">hi</span></h1>
    <div class="contact-grid">
      <div class="prose">
        <p>My name is Ariana. I may not be famous, but I'm working on it. Ariana Grande just got to it faster.</p>
        <p>I believe passion is the key to all successful people; and, I am passionate about everything I do, whether it be dancing to Rihanna, creating the wildest of integrated ads, or even eating a bowl of Very Berry Cheerios. I like to mix cereals, and I always pour the milk first. Sorry, not sorry! I'm a rebel like that.</p>
        <p style="font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--dim);margin-top:34px">Areas of Expertise</p>
        <ul class="expertise"><li>Production</li><li>Innovation</li><li>Creativity</li><li>Foodie</li></ul>
      </div>
      <dl class="contact-card">
{rows}{social}      </dl>
    </div>
  </div>
</section>
"""
    out += footer()
    open(os.path.join(ROOT, "contact.html"), "w").write(out)

def build_case(i, p):
    prev = PROJECTS[i - 1] if i > 0 else None
    nxt  = PROJECTS[i + 1] if i < len(PROJECTS) - 1 else None
    b = "../"

    quote = f"<blockquote>{p['quote']}</blockquote>\n        " if p.get("quote") else ""
    body = "".join(f"<p>{t}</p>\n        " for t in p["body"])

    results = ""
    if p.get("results"):
        cells = "".join(f"<div><b>{v}</b><span>{l}</span></div>" for v, l in p["results"])
        results = f'  <div class="results">{cells}</div>\n'

    credits = "".join(f"<li><em>{k}</em>{v}</li>" for k, v in p["credits"])
    side = f'      <div class="panel credits"><h2>Credits</h2><ul>{credits}</ul></div>\n'
    if p.get("awards"):
        aw = "".join(f"<li>{a}</li>" for a in p["awards"])
        side += f'      <div class="panel awards"><h2>Awards</h2><ul>{aw}</ul></div>\n'
    if p.get("press"):
        side += f'      <div class="panel press"><h2>Press</h2><p>{p["press"]}</p></div>\n'

    slug = p["slug"]
    shots = "".join(
        '    <div class="shot">{img}</div>\n'.format(
            img=ph("{}-0{}.jpg".format(slug, n + 1)))
        for n in range(p["gallery"]))
    gallery = f'  <div class="gallery">\n{shots}  </div>\n'

    pager = '  <nav class="pager">\n'
    pager += (f'    <a href="{prev["slug"]}.html"><em>&larr; Previous</em><b class="disp">{prev["title"]}</b></a>\n'
              if prev else '    <a class="empty" href="#"></a>\n')
    pager += (f'    <a class="next" href="{nxt["slug"]}.html"><em>Next &rarr;</em><b class="disp">{nxt["title"]}</b></a>\n'
              if nxt else '    <a class="empty next" href="#"></a>\n')
    pager += '  </nav>\n'

    out = HEAD.format(title=f"{p['title']} — Ariana Narang",
                      desc=p["sub"], base=b, work_cur=' aria-current="page"')
    out += f"""<article class="case-hero">
  <div class="blob b1"></div>
  <div class="wrap">
    <a class="back" href="{b}work.html">&larr; All work</a>
    <span class="case-client">{p['client']}</span>
    <h1 class="disp">{p['title']}</h1>
    <p class="case-sub">{p['sub']}</p>

    <dl class="meta">
      <div><dt>Client</dt><dd>{p['client']}</dd></div>
      <div><dt>Type</dt><dd>{p['type']}</dd></div>
      <div><dt>Role</dt><dd>{p['role']}</dd></div>
      <div><dt>Year</dt><dd>{p['year']}</dd></div>
    </dl>

    <div class="hero-band {p['color']}">{ph(f"{p['slug']}-hero.jpg")}</div>

    <div class="case-body">
      <div class="prose">
        {quote}{body}
      </div>
      <aside class="side">
{side}      </aside>
    </div>
{results}{gallery}{pager}  </div>
</article>
"""
    out += footer(b)
    open(os.path.join(ROOT, "work", f"{p['slug']}.html"), "w").write(out)

if __name__ == "__main__":
    os.makedirs(os.path.join(ROOT, "work"), exist_ok=True)
    build_index(); build_work(); build_contact()
    for i, p in enumerate(PROJECTS):
        build_case(i, p)
    print(f"built index.html, work.html, contact.html + {len(PROJECTS)} case studies")
