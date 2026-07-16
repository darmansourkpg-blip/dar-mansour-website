# -*- coding: utf-8 -*-
"""Journal (blog) — reads markdown articles authored via Decap CMS and turns
them into full SEO pages, category (editorial universe) hubs and the index.

Articles live in  content/journal/*.md  with YAML front matter:

    ---
    title: "..."
    seo_title: "..."        # optional; falls back to title
    description: "..."       # meta description
    date: 2026-07-04
    author: "Dar Mansour"
    category: "moroccan-culture"   # editorial universe (see CATEGORIES)
    cover: "assets/uploads/photo.jpg"
    cover_alt: "..."
    faq:                     # optional — renders an FAQ block + FAQ schema
      - question: "..."
        answer: "..."
    ---
    Markdown body…

Everything technical (canonical, Article + FAQ JSON-LD, Open Graph, sitemap,
breadcrumb, table of contents, WebP, cluster linking) is generated here — the
author only fills the fields above.
"""
import os
import re
import glob
import json
import datetime

import yaml
import markdown as _md

import _layout as L

HERE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(HERE, "..", "content", "journal")
DEFAULT_COVER = "assets/img/moroccan-zellige-wall-art-koh-phangan.jpg"

# Official brand profiles (Schema.org sameAs) — kept in sync with the Restaurant
# schema on the home page. Add Wikidata / others here when created.
SAME_AS = [
    "https://instagram.com/darmansour.kohphangan",
    "https://www.facebook.com/people/Dar-Mansour/",
    "https://share.google/Rp8YllnPe9Z9E9Va0",
    "https://www.tripadvisor.com/Restaurant_Review-d32851492",
]

# Editorial signature appended to every article (playbook §19 "About the Journal").
# An article may override it with an `about:` front-matter field.
ABOUT_DEFAULT = (
    "Written by the Dar Mansour team. Living between Koh Phangan and Morocco, "
    "we share carefully researched island guides, cultural stories and culinary "
    "traditions inspired by both worlds. Our articles are regularly reviewed to "
    "keep recommendations useful and up to date.")

# Author / editorial team page (credibility + SEO / E-E-A-T). Bios are drawn
# from existing verified site copy — do not invent biographical detail.
AUTHORS_URL = "journal-authors.html"
AUTHORS = [
    {
        "name": "Maïja",
        "role": "Co-Founder & Creative Director",
        "photo": "assets/img/maija-art-direction-koh-phangan.jpg",
        "photo_alt": "Maïja, co-founder and creative director of Dar Mansour, Koh Phangan",
        "bio": ("A creative spirit who has spent more than 30 years immersed in "
                "Moroccan culture, Maïja co-founded Dar Mansour and shapes its "
                "world of food, design and hospitality. Through her interior and "
                "creative studio, Eden & Beyond, she designed the restaurant's "
                "spaces — and it is the wisdom of the Dadas, the women who carried "
                "Morocco's family recipes across generations, that guides the "
                "kitchen's slow-cooked philosophy."),
    },
    {
        "name": "P'Jae",
        "role": "Head of Kitchen",
        "photo": "assets/img/moroccan-couscous-koh-phangan.jpg",
        "photo_alt": "Slow-cooked Moroccan couscous from the Dar Mansour kitchen led by P'Jae",
        "bio": ("Dar Mansour's local partner and Head of Kitchen, P'Jae brings "
                "daily hands-on expertise to the restaurant, translating Moroccan "
                "traditions into refined, slow-cooked dishes prepared with patience "
                "and care — rooted in respect for sacred cooking and island "
                "hospitality."),
    },
]

# --- Editorial linter -------------------------------------------------------
# Non-blocking warnings printed at build time, enforcing the Editorial Playbook
# (style guide, SEO rules, internal-linking rules). Nothing here changes output;
# it only flags articles that drift from the guidelines so they can be fixed.
BANNED_PHRASES = [
    "best ever", "world-class", "world class", "incredible", "amazing",
    "breathtaking", "unforgettable", "hidden secret", "hidden gem", "must-do",
    "must do", "must-visit", "must visit", "bucket list", "game-changer",
    "game changer", "ultimate experience", "authentic experience",
    "something for everyone", "nestled in", "culinary journey",
    "tantalise your taste buds", "tantalize your taste buds", "vibrant tapestry",
    "rich tapestry", "foodies", "paradise", "delve into", "boasts",
    "offers a plethora", "a testament to", "seamlessly blend", "more than just",
    "leaves a lasting impression", "in today's fast-paced world",
]


def lint_article(a, raw_body):
    """Print gentle warnings when an article drifts from the Playbook. Never
    raises — the build always succeeds; the author just sees what to improve."""
    warn = lambda msg: print(f"  ⚠ [{a['slug']}] {msg}")
    d = a["description"]
    if not d:
        warn("missing meta description (playbook: ~145–160 characters).")
    elif len(d) < 120:
        warn(f"meta description is short ({len(d)} chars) — aim for ~145–160.")
    elif len(d) > 165:
        warn(f"meta description is long ({len(d)} chars) — aim for ~145–160, it may be truncated by Google.")
    if len(a["seo_title"]) > 62:
        warn(f"SEO title is {len(a['seo_title'])} chars — aim for ~50–60.")
    if not a["cover_alt"] or a["cover_alt"] == a["title"]:
        warn("cover image has no descriptive alt text (avoid keyword stuffing; describe the photo).")
    # Internal linking: playbook asks for at least 3 links to other Dar Mansour
    # pages. Count both HTML (href="x.html") and Markdown ([text](x.html)) links.
    body = raw_body or ""
    internal = (re.findall(r'href="(?!https?:|#|mailto:|tel:)[^"]+\.html', body)
                + re.findall(r'\]\((?!https?:|#|mailto:|tel:)[^)]+\.html', body))
    if len(internal) < 3:
        warn(f"only {len(internal)} internal link(s) in the body — playbook asks for at least 3.")
    # FAQ is expected on guide/pillar articles (rough proxy: long body).
    words = len(re.findall(r"\w+", raw_body or ""))
    if words >= 1200 and not a["faq"]:
        warn("long article with no FAQ — guide/pillar articles should include 5–8 real questions.")
    # Banned / empty marketing vocabulary (whole-word/phrase match so words like
    # "best everyday" don't trip the "best ever" rule).
    low = (raw_body or "").lower()
    hits = sorted({p for p in BANNED_PHRASES
                   if re.search(r"\b" + re.escape(p) + r"\b", low)})
    if hits:
        warn("avoid empty/AI marketing words — found: " + ", ".join(hits))

# Editorial universes (the playbook's clusters). Each gets a hub page listing
# its articles; articles link back to their hub for topical authority.
CATEGORIES = {
    "koh-phangan-guide": {
        "label": "Koh Phangan Guide",
        "title": "Koh Phangan Guide",
        "tagline": "Your insider guide to the island",
        "intro": "Where to eat, the best beaches, hidden sunset spots and slow island living — an evolving guide to discovering Koh Phangan with intention.",
        "hero": "assets/uploads/koh-phangan-day.webp",
        "hero_alt": "Turquoise bay and white-sand beach on the west coast of Koh Phangan",
        "url": "koh-phangan-guide.html",
        "seo_title": "Koh Phangan Guide — Where to Eat, Beaches &amp; Secret Spots | Dar Mansour",
        "seo_desc": "An insider's guide to Koh Phangan by Dar Mansour: where to eat, the best beaches, sunset spots, local secrets and slow island living.",
        "hub": True,
    },
    "moroccan-culture": {
        "label": "Moroccan Culture",
        "title": "Moroccan Culture &amp; Cuisine",
        "tagline": "Beyond the recipes",
        "intro": "Tajines, spices, mint tea, riads, music and craftsmanship — stories that carry the soul of Morocco far beyond the plate.",
        "hero": "assets/uploads/moroccan-culture-card.webp",
        "hero_alt": "Moroccan culture and cuisine — Dar Mansour",
        "url": "moroccan-culture-cuisine.html",
        "seo_title": "Moroccan Culture &amp; Cuisine — Stories, Traditions &amp; Food | Dar Mansour",
        "seo_desc": "Explore Moroccan culture and cuisine with Dar Mansour: tajines, spices, mint tea, riads, music and craftsmanship — the soul of Morocco beyond the plate.",
        "hub": True,
    },
    "journal": {
        "label": "Journal",
        "title": "The Dar Mansour Journal",
        "tagline": "Behind the scenes",
        "intro": "Design, interviews, events and the people behind Dar Mansour.",
        "hero": "assets/img/maija-art-direction-koh-phangan.jpg",
        "hero_alt": "Art direction and décor at Dar Mansour",
        "url": "blog.html",       # the main Journal index acts as this hub
        "hub": False,
    },
}
DEFAULT_CATEGORY = "journal"


def _split_front_matter(raw):
    if raw.startswith("---"):
        parts = raw.split("---", 2)
        if len(parts) >= 3:
            meta = yaml.safe_load(parts[1]) or {}
            return meta, parts[2]
    return {}, raw


def _dates(value):
    if isinstance(value, (datetime.datetime, datetime.date)):
        dt = value
    else:
        try:
            dt = datetime.date.fromisoformat(str(value)[:10])
        except (ValueError, TypeError):
            dt = datetime.date.today()
    iso = dt.isoformat()[:10]
    disp = datetime.date.fromisoformat(iso).strftime("%-d %B %Y")
    return iso, disp


# Markdown renderer with the 'toc' extension: it slugs every heading into an id
# (so anchors work) and exposes the heading tree via .toc_tokens.
_MD = _md.Markdown(extensions=["extra", "sane_lists", "toc"],
                   extension_configs={"toc": {"toc_depth": "2-3"}})


def _render_body(text, has_faq=False):
    """Markdown -> HTML, with an auto clickable table of contents prepended
    when the article has 2+ H2 sub-headings. The FAQ section (rendered later
    as HTML, outside the markdown body) is appended to the TOC when present."""
    _MD.reset()
    html = _MD.convert((text or "").strip())
    h2s = [t for t in _MD.toc_tokens if t.get("level") == 2]
    if len(h2s) < 2:
        return html
    items = "".join(f'<li><a href="#{t["id"]}">{t["name"]}</a></li>' for t in h2s)
    if has_faq:
        items += '<li><a href="#faq">Frequently asked questions</a></li>'
    toc = (f'<nav class="toc" aria-label="In this article">'
           f'<p class="toc__title">In this article</p><ol>{items}</ol></nav>')
    return toc + html


def _parse_quick_guide(raw):
    """raw: list of {label, value} -> cleaned key/value rows."""
    out = []
    for item in raw or []:
        label = (str(item.get("label", "")) or "").strip()
        value = (str(item.get("value", "")) or "").strip()
        if label and value:
            out.append({"label": label, "value": value})
    return out


def _parse_faq(raw):
    """raw: list of {question, answer}. Returns display-ready + plain-text."""
    faq = []
    for item in raw or []:
        q = (str(item.get("question", "")) or "").strip()
        a = (str(item.get("answer", "")) or "").strip()
        if not q or not a:
            continue
        a_html = _md.markdown(a, extensions=["extra"])
        a_text = re.sub(r"<[^>]+>", "", a_html).strip()
        faq.append({"q": q, "a_html": a_html, "a_text": a_text})
    return faq


def _git_mod_date(path):
    """Last git commit date (YYYY-MM-DD) for a file, or None if unavailable
    (no git, shallow checkout with no history, or file not yet committed)."""
    try:
        import subprocess
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", path],
            cwd=os.path.dirname(os.path.abspath(path)),
            capture_output=True, text=True, timeout=10)
        d = out.stdout.strip()
        return d if re.match(r"^\d{4}-\d{2}-\d{2}$", d) else None
    except Exception:
        return None


def load_articles():
    """Return a list of article dicts, newest first."""
    articles = []
    for path in sorted(glob.glob(os.path.join(CONTENT, "*.md"))):
        with open(path, encoding="utf-8") as f:
            meta, body = _split_front_matter(f.read())
        slug = os.path.splitext(os.path.basename(path))[0]
        iso, disp = _dates(meta.get("date"))
        # Freshness signal (JSON-LD dateModified): explicit `updated:` field wins,
        # else the file's last git-commit date, else the published date. Never
        # earlier than the published date.
        upd, _ = _dates(meta.get("updated")) if meta.get("updated") else (None, None)
        mod_iso = upd or _git_mod_date(path) or iso
        if mod_iso < iso:
            mod_iso = iso
        cover = (meta.get("cover") or DEFAULT_COVER).lstrip("/")
        title = meta.get("title") or slug.replace("-", " ").title()
        cat_key = meta.get("category") if meta.get("category") in CATEGORIES else DEFAULT_CATEGORY
        articles.append({
            "slug": slug,
            "title": title,
            "seo_title": meta.get("seo_title") or title,
            "description": (meta.get("description") or "").strip(),
            "date_iso": iso,
            "date_disp": disp,
            "mod_iso": mod_iso,
            "author": meta.get("author") or "Dar Mansour",
            "category": cat_key,
            "cat": CATEGORIES[cat_key],
            "cover": cover,
            "cover_alt": meta.get("cover_alt") or title,
            "cover_fit": (meta.get("cover_fit") or "").strip(),
            "quick_guide": _parse_quick_guide(meta.get("quick_guide")),
            "faq": _parse_faq(meta.get("faq")),
            "about": (meta.get("about") or ABOUT_DEFAULT).strip(),
            "body_html": _render_body(body, bool(_parse_faq(meta.get("faq")))),
            "url": f"journal-{slug}.html",
        })
        lint_article(articles[-1], body)
    articles.sort(key=lambda a: a["date_iso"], reverse=True)
    return articles


def _blog_schema(a):
    site = L.SITE_URL
    return {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": a["title"],
        "description": a["description"],
        "image": f'{site}/{a["cover"]}',
        "datePublished": a["date_iso"],
        "dateModified": a["mod_iso"],
        "author": {"@type": "Organization", "name": a["author"]},
        "publisher": {
            "@type": "Organization",
            "name": "Dar Mansour - Morocco's Kitchen",
            "url": f"{site}/",
            "logo": {"@type": "ImageObject", "url": f"{site}/assets/logo/dar-mansour-logo-green.png"},
            # Official profiles — same list as the Restaurant schema, so every
            # article ties the brand to its verified entities (Google/AI).
            "sameAs": SAME_AS,
        },
        "mainEntityOfPage": f'{site}/{a["url"]}',
        "articleSection": a["cat"]["label"],
    }


def _faq_schema(a):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": f["q"],
             "acceptedAnswer": {"@type": "Answer", "text": f["a_text"]}}
            for f in a["faq"]
        ],
    }


def _schema_head(a):
    scripts = ['<script type="application/ld+json">' + json.dumps(_blog_schema(a), ensure_ascii=False) + '</script>']
    if a["faq"]:
        scripts.append('<script type="application/ld+json">' + json.dumps(_faq_schema(a), ensure_ascii=False) + '</script>')
    return "\n".join(scripts)


def _quick_guide(a):
    """A 'Quick Guide' key-facts box shown near the top of the article."""
    qg = a["quick_guide"]
    if not qg:
        return ""
    rows = "".join(f'<div><dt>{r["label"]}</dt><dd>{r["value"]}</dd></div>' for r in qg)
    return f'<aside class="qguide"><p class="qguide__title">Quick Guide</p><dl>{rows}</dl></aside>'


def _faq_section(a):
    if not a["faq"]:
        return ""
    items = "".join(
        f'<details class="faq__item"><summary>{f["q"]}</summary>'
        f'<div class="faq__answer">{f["a_html"]}</div></details>'
        for f in a["faq"])
    return f'''
<section class="section" id="faq" style="padding-top:0;"><div class="wrap">
  <div class="center" style="margin-bottom:2rem;">
    <span class="eyebrow">Good to know</span>
    <h2 style="margin-top:.7rem;">Frequently asked questions</h2>
  </div>
  <div class="faq">{items}</div>
</div></section>'''


def _about_section(a):
    """Short editorial signature closing every article (playbook §19)."""
    return f'''
<section class="section" style="padding-top:0;"><div class="wrap">
  <aside class="about-journal">
    <p class="about-journal__title">About the Dar Mansour Journal</p>
    <p>{a["about"]}</p>
    <p style="margin-top:.6rem;"><a class="ilink" href="{AUTHORS_URL}">Meet the team behind the Journal — Maïja &amp; P'Jae {L.ARROW}</a></p>
  </aside>
</div></section>'''


def _related_cards(a, all_articles):
    """Prefer other articles in the same universe; top up with evergreen pages."""
    same = [x for x in all_articles if x["category"] == a["category"] and x["url"] != a["url"]][:3]
    cards = [(x["cat"]["label"], x["title"], x["url"], x["cover"], x["cover_alt"]) for x in same]
    fallbacks = [
        ("Menu", "Our Moroccan Menu", "moroccan-menu-koh-phangan.html", "assets/img/moroccan-couscous-koh-phangan.jpg", "Couscous"),
        ("Founders", "Our Story", "dar-mansour-founders-vision.html", "assets/uploads/Founders%20-%20Our%20Story%20-Dar-Mansour-1.jpg", "Maïja and Bruno, arm in arm before a Thai temple in Koh Phangan — the founders of Dar Mansour"),
        ("Journal", "More Stories", "blog.html", "assets/img/moroccan-zellige-wall-art-koh-phangan.jpg", "Zellige wall art"),
    ]
    i = 0
    while len(cards) < 3 and i < len(fallbacks):
        if fallbacks[i][2] != a["url"]:
            cards.append(fallbacks[i])
        i += 1
    return cards[:3]


def render_article(a, all_articles):
    cat = a["cat"]
    body = L.breadcrumb(("Journal", "blog.html"), (a["title"], None)) + L.subhero(
        cat["label"], a["title"], a["description"], a["cover"], a["cover_alt"],
        tall=(a.get("cover_fit") == "portrait"),
        variant=("portrait" if a.get("cover_fit") == "portrait" else None)) + f'''
<section class="section"><div class="wrap prose reveal">
  <p class="article__meta"><time datetime="{a["date_iso"]}">{a["date_disp"]}</time> · <a class="ilink" href="{AUTHORS_URL}">{a["author"]}</a> · <a class="ilink" href="{cat["url"]}">{cat["label"]}</a></p>
{_quick_guide(a)}
{a["body_html"]}
</div></section>
''' + _faq_section(a) + _about_section(a) + L.cta_band("Taste the story around our table",
        "The best chapters are written over a slow Moroccan dinner. Reserve your evening at Dar Mansour.") + L.related(*_related_cards(a, all_articles))
    return L.page(a["seo_title"], a["description"], a["url"], body,
                  og_image=a["cover"], extra_head=_schema_head(a), body_class="journal")


def render_index_cards(articles, eyebrow="Latest Stories", heading="Fresh from the Journal", show_header=True):
    """Grid of article cards (empty string if none)."""
    if not articles:
        return ""
    cards = "".join(f'''
      <a class="jcard reveal" href="{a["url"]}">
        <span class="jcard__img"><img src="{L._webp(a["cover"])}" alt="{a["cover_alt"]}" loading="lazy"><span class="jcard__cat">{a["cat"]["label"]}</span></span>
        <span class="jcard__body">
          <span class="jcard__date">{a["date_disp"]}</span>
          <span class="jcard__title">{a["title"]}</span>
          <span class="jcard__desc">{a["description"]}</span>
          <span class="textlink">Read the story {L.ARROW}</span>
        </span>
      </a>''' for a in articles)
    header = ""
    if show_header:
        header = (f'<div class="center reveal" style="margin-bottom:clamp(2rem,4vw,3rem);">'
                  f'<span class="eyebrow">{eyebrow}</span>'
                  f'<h2 style="margin-top:1rem;">{heading}</h2></div>')
    return f'''
<section class="section" id="latest" style="padding-top:0;"><div class="wrap">
  {header}
  <div class="jgrid">{cards}</div>
</div></section>'''


def universe_hubs(articles):
    """(cat_key, cat, [articles]) for each hub universe that has articles."""
    out = []
    for key, cat in CATEGORIES.items():
        if not cat.get("hub"):
            continue
        arts = [a for a in articles if a["category"] == key]
        if arts:
            out.append((key, cat, arts))
    return out


def render_universe_nav(articles):
    """Section on the Journal index linking to each editorial universe hub."""
    hubs = universe_hubs(articles)
    if not hubs:
        return ""
    cards = "".join(f'''
      <a class="uni reveal" href="{cat["url"]}">
        <span class="uni__img"><img src="{L._webp(cat["hero"])}" alt="{cat["hero_alt"]}" loading="lazy"></span>
        <span class="uni__body"><span class="eyebrow">{cat["tagline"]}</span>
        <span class="uni__title">{cat["title"]}</span>
        <span class="uni__count">{len(arts)} article{"s" if len(arts) != 1 else ""}</span></span>
      </a>''' for _key, cat, arts in hubs)
    return f'''
<section class="section" style="background:var(--sand);"><div class="wrap">
  <div class="center reveal" style="max-width:640px;margin:0 auto clamp(2rem,4vw,3rem);">
    <span class="eyebrow">Editorial Universes</span>
    <h2 style="margin-top:1rem;">Explore by world</h2>
  </div>
  <div class="unigrid">{cards}</div>
</div></section>'''


def render_category(cat, arts):
    body = L.breadcrumb(("Journal", "blog.html"), (cat["title"], None)) + L.subhero(
        cat["tagline"], cat["title"], cat["intro"], cat["hero"], cat["hero_alt"]) + render_index_cards(
        arts, show_header=False) + L.cta_band(
        "Come and live the story",
        "The best chapters are written over a slow Moroccan dinner. Reserve your evening at Dar Mansour.") + L.related(
        ("Journal", "All Stories", "blog.html", "assets/img/moroccan-zellige-wall-art-koh-phangan.jpg", "Zellige wall art"),
        ("Menu", "Our Moroccan Menu", "moroccan-menu-koh-phangan.html", "assets/img/moroccan-couscous-koh-phangan.jpg", "Couscous"),
        ("Experience", "The Experience", "index.html", "assets/img/moroccan-garden-dining-koh-phangan.jpg", "Garden dining"))
    return L.page(cat.get("seo_title") or cat["title"],
                  cat.get("seo_desc") or cat["intro"],
                  cat["url"], body, og_image=cat["hero"], body_class="journal")


def _authors_schema():
    site = L.SITE_URL
    people = [{
        "@context": "https://schema.org",
        "@type": "Person",
        "name": p["name"],
        "jobTitle": p["role"],
        "image": f'{site}/{p["photo"]}',
        "description": p["bio"],
        "url": f"{site}/{AUTHORS_URL}",
        "worksFor": {"@type": "Organization", "name": "Dar Mansour - Morocco's Kitchen",
                     "url": site + "/"},
    } for p in AUTHORS]
    return "\n".join('<script type="application/ld+json">' + json.dumps(p, ensure_ascii=False) + '</script>'
                     for p in people)


def render_authors():
    """Editorial team / author page — credibility and E-E-A-T for the Journal."""
    cards = "".join(f'''
    <article class="author reveal">
      <div class="author__img"><img src="{L._webp(p["photo"])}" alt="{p["photo_alt"]}" loading="lazy"></div>
      <div class="author__body">
        <h2 class="author__name">{p["name"]}</h2>
        <p class="author__role">{p["role"]}</p>
        <p>{p["bio"]}</p>
      </div>
    </article>''' for p in AUTHORS)
    intro = ("The Dar Mansour Journal is written by the team behind the restaurant, living "
             "between Koh Phangan and Morocco. Our island guides and cultural stories are "
             "shaped by real local knowledge and a lifelong connection to Moroccan cooking, "
             "and reviewed regularly to stay useful and accurate.")
    body = L.breadcrumb(("Journal", "blog.html"), ("Authors", None)) + L.subhero(
        "The Dar Mansour Journal", "The team behind the Journal", intro,
        "assets/img/maija-art-direction-koh-phangan.jpg",
        "Maïja's art direction and Moroccan décor at Dar Mansour, Koh Phangan") + f'''
<section class="section"><div class="wrap authors">{cards}</div></section>
''' + L.cta_band(
        "Taste the story around our table",
        "The best chapters are written over a slow Moroccan dinner. Reserve your evening at Dar Mansour.") + L.related(
        ("Journal", "All Stories", "blog.html", "assets/img/moroccan-zellige-wall-art-koh-phangan.jpg", "Zellige wall art"),
        ("Founders", "Our Story", "dar-mansour-founders-vision.html", "assets/uploads/Founders%20-%20Our%20Story%20-Dar-Mansour-1.jpg", "Maïja and Bruno, founders of Dar Mansour"),
        ("Menu", "Our Moroccan Menu", "moroccan-menu-koh-phangan.html", "assets/img/moroccan-couscous-koh-phangan.jpg", "Couscous"))
    return L.page(
        "The Dar Mansour Journal — Meet the Team (Maïja &amp; P'Jae)",
        "Meet the team behind the Dar Mansour Journal: Maïja, co-founder and creative director, and P'Jae, head of kitchen — the people behind our Koh Phangan and Moroccan guides.",
        AUTHORS_URL, body, og_image="assets/img/maija-art-direction-koh-phangan.jpg",
        extra_head=_authors_schema(), body_class="journal")
