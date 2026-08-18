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
    "https://www.facebook.com/p/Dar-Mansour-Koh-Phangan-61574622040198/",
    "https://share.google/Rp8YllnPe9Z9E9Va0",
    "https://www.tripadvisor.com/Restaurant_Review-d32851492",
    "https://www.wikidata.org/wiki/Q140585802",
    "https://www.crunchbase.com/organization/dar-mansour-morocco-s-kitchen",
    "https://www.openstreetmap.org/node/14021567355",
    "https://maps.apple.com/place?place-id=I620A58D27664AA56&address=5%2F5+O+Bo+to+Ko+Pa-Ngan+Road%2C+Ko+Pha-Ngan%2C+Ko+Pha-Ngan+District%2C+Surat+Thani+84280%2C+Thailand&coordinate=9.753081%2C99.968740&name=Dar+Mansour+-+Morocco%27s+Kitchen&_provider=9902",
    "https://www.bing.com/maps?ss=ypid.YN8178x5570947916035674182",
    "https://www.pinterest.com/darmansourkohphangan/",
    "https://www.linkedin.com/company/darmansour/",
]

# Editorial signature appended to every article (playbook §19 "About the Journal").
# An article may override it with an `about:` front-matter field.
ABOUT_DEFAULT = (
    "Written by the Dar Mansour team. Living between Koh Phangan and Morocco, "
    "we share carefully researched island guides, cultural stories and culinary "
    "traditions inspired by both worlds. Our articles are regularly reviewed to "
    "keep recommendations useful and up to date.")

# Author / editorial team pages (credibility + SEO / E-E-A-T). Bios are drawn
# from verified copy provided by the founders — do not invent biographical detail.
# Each author has their own page at /authors/<slug>/ ; the hub is /authors/.
AUTHORS_URL = "authors/"

# Recipe (culinary) culture articles get an extra "Recipe reviewed by P'Jae"
# credit; other culture articles (e.g. music) do not.
RECIPE_SLUGS = {
    "what-is-a-tajine", "what-is-couscous",
    "the-dadas-guardians-of-moroccan-recipes",
}

AUTHORS = [
    {
        "slug": "maija-disseau",
        "name": "Maïja Disseau",
        "short": "Maïja Disseau",
        "role": "Co-Founder · Moroccan Culture &amp; Culinary Heritage Specialist",
        "role_short": "Co-Founder · Moroccan Culture &amp; Culinary Heritage",
        # She is the primary writer of the Moroccan-culture universe.
        "category": "moroccan-culture",
        "tagline": ("Some of the world's greatest recipes are never written down. "
                    "They are passed from one generation to the next, around a family table."),
        "photo": "assets/img/maija-art-direction-koh-phangan.jpg",
        "photo_alt": "Maïja Disseau, co-founder of Dar Mansour, and her Moroccan art direction, Koh Phangan",
        "about": [
            ("For more than thirty years, Maïja lived in Morocco, where she built a family "
             "and immersed herself in the country's culture, traditions and way of life. "
             "During those years she was welcomed into Moroccan homes, learned from families "
             "across different regions and discovered that Morocco's greatest treasures are "
             "often passed down through everyday gestures rather than written in books."),
            ("Her understanding of Moroccan culture extends beyond its cuisine. It embraces "
             "hospitality, craftsmanship, architecture, music, rituals and the countless "
             "traditions that shape daily life — a rare perspective on Morocco, not simply as "
             "a visitor, but as someone who experienced it from within."),
            ("After studying psychotherapy and working for twelve years as a psychotherapist, "
             "hypnotherapist and family constellation practitioner, Maïja developed a deep "
             "appreciation for listening, observation and the human stories behind traditions. "
             "These qualities continue to shape her writing, which explores not only what "
             "Morocco is, but why its culture has remained so rich and enduring."),
            ("In 2025, she and her partner Bruno founded Dar Mansour – Morocco's Kitchen in "
             "Koh Phangan, Thailand, a restaurant inspired by the warmth of Moroccan family "
             "hospitality and authentic regional cuisine. Alongside her work with Dar Mansour, "
             "Maïja is the founder and creative force behind Eden &amp; Beyond, where she "
             "creates furniture, lighting and mixed-media artworks inspired by memory, "
             "craftsmanship and the invisible stories carried by objects."),
            ("Today, through The Dar Mansour Journal, Maïja writes about Moroccan cuisine, "
             "traditions, craftsmanship and the country's living heritage, drawing on more "
             "than three decades of personal experience and lifelong curiosity."),
        ],
        "expertise": ["Moroccan Culture", "Family Traditions", "Culinary Heritage",
                      "Craftsmanship", "Architecture &amp; Décor", "Rituals &amp; Storytelling"],
        "philosophy": ("I don't write recipes to teach people how to cook. I write to preserve "
                       "the stories, traditions and people behind Morocco's cuisine."),
    },
    {
        "slug": "pjae",
        "name": "P'Jae",
        "short": "P'Jae",
        "alt_name": "Han P'Jae Min",
        "role": "Partner · Head Chef · Koh Phangan &amp; Thailand Local Expert",
        "role_short": "Partner · Head Chef · Koh Phangan Local Expert",
        # She is the primary writer of the Koh Phangan guide universe.
        "category": "koh-phangan-guide",
        "tagline": ("The best recommendations come from people who truly live a place every day."),
        "photo": "assets/img/moroccan-couscous-koh-phangan.jpg",
        "photo_alt": "Slow-cooked Moroccan couscous from the Dar Mansour kitchen led by Head Chef P'Jae, Koh Phangan",
        "about": [
            ("Born and raised in Thailand, P'Jae has spent her career in hospitality, restaurant "
             "management and professional kitchens before becoming Partner and Head Chef at "
             "Dar Mansour."),
            ("Living and working on Koh Phangan has given her an in-depth understanding of the "
             "island, its food scene and its evolving community. Every week she explores new "
             "restaurants, follows local producers, works with suppliers and welcomes travellers "
             "from around the world."),
            ("Although Dar Mansour celebrates Moroccan cuisine, her role goes far beyond the "
             "kitchen. She helps visitors discover the island itself — its neighbourhoods, cafés, "
             "beaches and restaurants — through first-hand local knowledge gained from daily life "
             "on Koh Phangan."),
            ("As Head Chef, she also works closely with Maïja to faithfully reproduce traditional "
             "Moroccan recipes while adapting them to the realities of sourcing exceptional "
             "ingredients in Thailand."),
        ],
        "expertise": ["Koh Phangan Restaurants", "Koh Phangan Travel", "Thai Hospitality",
                      "Local Food Scene", "Restaurant Operations", "Sustainable Local Sourcing",
                      "Thai Ingredients", "Slow Cooking", "Visitor Experience"],
        "philosophy": ("The best travel advice doesn't come from a list — it comes from living "
                       "somewhere every day. Every recommendation we publish is based on places "
                       "we genuinely know, visit and trust."),
    },
    {
        "slug": "bruno-potier",
        "name": "Bruno Potier",
        "short": "Bruno Potier",
        "role": "Co-Founder · Editorial Director · Hospitality Brand Strategist",
        "role_short": "Co-Founder · Editorial Director",
        # Bruno is the editorial reviewer across the Journal (no primary byline category).
        "category": None,
        "tagline": ("Great hospitality doesn't end when the meal is over. It continues through "
                    "every story people take home."),
        "photo": "assets/uploads/dar-mansour-founders-our-story-koh-phangan.jpg",
        "photo_alt": "Bruno Potier, co-founder of Dar Mansour, with Maïja in Koh Phangan, Thailand",
        "about": [
            ("Bruno Potier is the Co-Founder and Editorial Director of Dar Mansour. For more than "
             "twenty-five years he has built businesses, brands and hospitality concepts across "
             "Europe, Asia and North Africa, combining entrepreneurship, strategy and storytelling "
             "to create lasting customer experiences."),
            ("His journey has taken him from launching one of Shanghai's most talked-about "
             "underground music venues, Club dkd, to founding Jetlag Prod, a Shanghai-based "
             "events and marketing agency specialising in luxury brands, where he produced "
             "events for international names such as Moët &amp; Chandon, Hennessy, Dom Pérignon and Hilton Hotels. "
             "He later led marketing strategies across several European markets before "
             "co-founding Dar Mansour in Koh Phangan, Thailand."),
            ("He also spent twelve years living and working in Morocco, where he developed a deep "
             "appreciation for the country's culture, hospitality and entrepreneurial spirit — an "
             "immersion that helped shape the vision behind Dar Mansour: a brand dedicated to "
             "sharing Moroccan family traditions, craftsmanship and art de vivre with the world."),
            ("As Editorial Director of The Dar Mansour Journal, he oversees the publication's "
             "editorial strategy, ensuring every guide and story combines first-hand experience, "
             "careful research and genuine cultural authenticity. Working alongside Maïja and "
             "P'Jae, he helps turn years of lived experience into content that informs, inspires "
             "and earns readers' trust."),
        ],
        "expertise": ["Hospitality Brand Strategy", "Editorial Strategy &amp; Storytelling",
                      "Customer Experience", "Restaurant Development", "Strategic Partnerships",
                      "International Business Development", "Multicultural Leadership"],
        "philosophy": ("The best travel and food stories don't persuade people to visit a place — "
                       "they help them understand it. Our goal is to create articles that remain "
                       "valuable long after they're published."),
    },
]

# Quick lookup helpers.
AUTHOR_BY_SLUG = {p["slug"]: p for p in AUTHORS}
AUTHOR_BY_CATEGORY = {p["category"]: p for p in AUTHORS if p.get("category")}


def _author_url(p):
    return f"{AUTHORS_URL}{p['slug']}/"

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
        "seo_title": "Koh Phangan Guide — Where to Eat &amp; Secret Spots | Dar Mansour",
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
        "seo_title": "Moroccan Culture &amp; Cuisine — Stories &amp; Traditions | Dar Mansour",
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


def _add_target_blank_to_external_links(html):
    """Add target="_blank" and rel="noopener" to all external links in HTML."""
    def replace_link(match):
        tag = match.group(0)
        href = match.group(1)
        # Skip internal links, anchors, mailto, tel, and links that already have target="_blank"
        if href.startswith(('#', 'mailto:', 'tel:')) or 'target=' in tag:
            return tag
        if href.startswith('http') or href.startswith('//'):
            # Add target="_blank" and rel="noopener" if not present
            if 'target=' not in tag:
                tag = tag.replace('>', ' target="_blank" rel="noopener">', 1)
            return tag
        return tag
    # Match <a ...> tags with href attribute
    return re.sub(r'<a\s+href="([^"]*)"[^>]*>', replace_link, html)


def _render_body(text, has_faq=False):
    """Markdown -> HTML, with an auto clickable table of contents prepended
    when the article has 2+ H2 sub-headings. The FAQ section (rendered later
    as HTML, outside the markdown body) is appended to the TOC when present."""
    _MD.reset()
    html = _MD.convert((text or "").strip())
    # Add target="_blank" to external links to prevent navigating away
    html = _add_target_blank_to_external_links(html)
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


def lint_incoming_links(articles, raw_bodies):
    """Cross-article check: warn about journal articles that few (or no) other
    articles link to. Internal links pass authority between pages, so an
    orphaned article ranks worse. The per-article linter only counts OUTGOING
    links, so this catches the gap it can't see. Aim for >= 2 incoming links
    from other journal articles."""
    for a in articles:
        target = a["url"]  # e.g. journal-best-thai-restaurants-koh-phangan.html
        incoming = sum(1 for other in articles
                       if other["slug"] != a["slug"]
                       and target in (raw_bodies.get(other["slug"]) or ""))
        if incoming < 2:
            print(f"  ⚠ [{a['slug']}] only {incoming} other article(s) link to "
                  f"it — add internal links from related articles (aim for >= 2).")


def load_articles():
    """Return a list of article dicts, newest first."""
    articles = []
    raw_bodies = {}
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
            "hero_scrim": (meta.get("hero_scrim") or "").strip(),
            "quick_guide": _parse_quick_guide(meta.get("quick_guide")),
            "faq": _parse_faq(meta.get("faq")),
            "about": (meta.get("about") or ABOUT_DEFAULT).strip(),
            "body_html": _render_body(body, bool(_parse_faq(meta.get("faq")))),
            "url": f"journal-{slug}.html",
        })
        raw_bodies[slug] = body
        lint_article(articles[-1], body)
    lint_incoming_links(articles, raw_bodies)
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
        # Full ISO 8601 with the local timezone (Thailand, +07:00) so Google
        # doesn't flag a missing-timezone / invalid-datetime warning.
        "datePublished": f'{a["date_iso"]}T09:00:00+07:00',
        "dateModified": f'{a["mod_iso"]}T09:00:00+07:00',
        # Attribute the article to the real writer (a Person with a profile URL)
        # rather than a generic Organization — stronger E-E-A-T. Falls back to
        # the Journal organisation for un-mapped categories.
        "author": (
            {"@type": "Person",
             "name": AUTHOR_BY_CATEGORY[a["category"]]["name"],
             "url": f'{site}/{_author_url(AUTHOR_BY_CATEGORY[a["category"]])}'}
            if a["category"] in AUTHOR_BY_CATEGORY
            else {"@type": "Organization", "name": a["author"], "url": f"{site}/"}
        ),
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
    <p style="margin-top:.6rem;"><a class="ilink" href="{AUTHORS_URL}">Meet our editorial team {L.ARROW}</a></p>
  </aside>
</div></section>'''


def _related_cards(a, all_articles):
    """Prefer other articles in the same universe; top up with evergreen pages."""
    same = [x for x in all_articles if x["category"] == a["category"] and x["url"] != a["url"]][:3]
    cards = [(x["cat"]["label"], x["title"], x["url"], x["cover"], x["cover_alt"]) for x in same]
    fallbacks = [
        ("Menu", "Our Moroccan Menu", "moroccan-menu-koh-phangan.html", "assets/img/moroccan-couscous-koh-phangan.jpg", "Couscous"),
        ("Founders", "Our Story", "dar-mansour-founders-vision.html", "assets/uploads/dar-mansour-founders-our-story-koh-phangan.jpg", "Maïja and Bruno, arm in arm before a Thai temple in Koh Phangan — the founders of Dar Mansour"),
        ("Journal", "More Stories", "blog.html", "assets/uploads/where-to-watch-the-sunset-in-koh-phangan2.jpg", "Aerial view of a turquoise Koh Phangan bay — stories from The Dar Mansour Journal"),
    ]
    i = 0
    while len(cards) < 3 and i < len(fallbacks):
        if fallbacks[i][2] != a["url"]:
            cards.append(fallbacks[i])
        i += 1
    return cards[:3]


def byline(a):
    """Rich editorial byline (writer + reviewers), reflecting the real team
    workflow — a strong E-E-A-T / GEO signal. Writer is derived from the
    article's category (Moroccan culture → Maïja, Koh Phangan → P'Jae), unless
    a front-matter `author` name overrides the display."""
    writer = AUTHOR_BY_CATEGORY.get(a["category"])
    bruno = AUTHOR_BY_SLUG.get("bruno-potier")
    pjae = AUTHOR_BY_SLUG.get("pjae")

    def link(p):
        return f'<a class="ilink" href="{_author_url(p)}">{p["short"]}</a>'

    # Writer line. If no mapped author (generic journal post), fall back to the
    # front-matter author name linking to the team hub.
    if writer:
        written = f'Written by {link(writer)} · <span class="byline__role">{writer["role_short"]}</span>'
    else:
        written = f'Written by <a class="ilink" href="{AUTHORS_URL}">{a["author"]}</a>'

    creds = []
    # Recipe review by P'Jae on culinary culture pieces (she is already the
    # writer on Koh Phangan guides, so no double credit there).
    if writer and writer["slug"] != "pjae" and a["slug"] in RECIPE_SLUGS and pjae:
        creds.append(f'Recipe reviewed by {link(pjae)}')
    # Editorial direction by Bruno across the Journal.
    if writer and bruno:
        creds.append(f'Editorial review by {link(bruno)}')
    creds_html = (f'<p class="article__credits">{" · ".join(creds)}</p>' if creds else "")

    return (f'<p class="article__meta"><time datetime="{a["date_iso"]}">{a["date_disp"]}</time>'
            f' · {written} · <a class="ilink" href="{a["cat"]["url"]}">{a["cat"]["label"]}</a></p>'
            + creds_html)


def render_article(a, all_articles):
    cat = a["cat"]
    body = L.breadcrumb(("Journal", "blog.html"), (a["title"], None)) + L.subhero(
        cat["label"], a["title"], a["description"], a["cover"], a["cover_alt"],
        tall=(a.get("cover_fit") == "portrait"),
        variant=("portrait" if a.get("cover_fit") == "portrait" else None),
        scrim=a.get("hero_scrim")) + f'''
<section class="section"><div class="wrap prose reveal">
  {byline(a)}
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
        ("Journal", "All Stories", "blog.html", "assets/uploads/where-to-watch-the-sunset-in-koh-phangan2.jpg", "Aerial view of a turquoise Koh Phangan bay — stories from The Dar Mansour Journal"),
        ("Menu", "Our Moroccan Menu", "moroccan-menu-koh-phangan.html", "assets/img/moroccan-couscous-koh-phangan.jpg", "Couscous"),
        ("Experience", "The Experience", "index.html", "assets/img/moroccan-garden-dining-koh-phangan.jpg", "Garden dining"))
    return L.page(cat.get("seo_title") or cat["title"],
                  cat.get("seo_desc") or cat["intro"],
                  cat["url"], body, og_image=cat["hero"], body_class="journal")


def _strip(text):
    """Plain text (no HTML entities) for JSON-LD descriptions."""
    import html as _h
    return _h.unescape(text)


def _person_schema(p, all_articles=None):
    site = L.SITE_URL
    data = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": p["name"],
        "jobTitle": _strip(p["role"]),
        "image": f'{site}/{p["photo"]}',
        **({"alternateName": p["alt_name"]} if p.get("alt_name") else {}),
        "description": _strip(" ".join(p["about"])),
        "url": f'{site}/{_author_url(p)}',
        "knowsAbout": [_strip(x) for x in p["expertise"]],
        "worksFor": {"@type": "Organization",
                     "name": "Dar Mansour - Morocco's Kitchen", "url": site + "/"},
        "sameAs": SAME_AS,
    }
    return data


def _authors_hub_schema(all_articles):
    return "\n".join(
        '<script type="application/ld+json">'
        + json.dumps(_person_schema(p, all_articles), ensure_ascii=False) + '</script>'
        for p in AUTHORS)


def _team_cards():
    """Three linked cards for the editorial-team hub."""
    return "".join(f'''
    <a class="author author--card reveal" href="{_author_url(p)}">
      <div class="author__img"><img src="{L._webp(p["photo"])}" alt="{p["photo_alt"]}" loading="lazy"></div>
      <div class="author__body">
        <h2 class="author__name">{p["name"]}</h2>
        <p class="author__role">{p["role"]}</p>
        <p>{p["about"][0]}</p>
        <span class="textlink">Read full profile {L.ARROW}</span>
      </div>
    </a>''' for p in AUTHORS)


def render_authors(all_articles):
    """Editorial-team hub (/authors/) — credibility and E-E-A-T for the Journal."""
    intro = ("The Dar Mansour Journal is written by the team behind the restaurant, living "
             "between Koh Phangan and Morocco. Every guide and story draws on real local "
             "knowledge and a lifelong connection to Moroccan cooking — written by the person "
             "closest to the subject and reviewed by the rest of the team to stay useful, "
             "accurate and genuinely helpful.")
    body = L.breadcrumb(("Journal", "blog.html"), ("Editorial Team", None)) + L.subhero(
        "The Dar Mansour Journal", "Meet our editorial team", intro,
        "assets/img/maija-art-direction-koh-phangan.jpg",
        "Maïja's art direction and Moroccan décor at Dar Mansour, Koh Phangan") + f'''
<section class="section"><div class="wrap authors">{_team_cards()}</div></section>
''' + L.cta_band(
        "Taste the story around our table",
        "The best chapters are written over a slow Moroccan dinner. Reserve your evening at Dar Mansour.") + L.related(
        ("Journal", "All Stories", "blog.html", "assets/uploads/where-to-watch-the-sunset-in-koh-phangan2.jpg", "Aerial view of a turquoise Koh Phangan bay — stories from The Dar Mansour Journal"),
        ("Founders", "Our Story", "dar-mansour-founders-vision.html", "assets/uploads/dar-mansour-founders-our-story-koh-phangan.jpg", "Maïja and Bruno, founders of Dar Mansour"),
        ("Menu", "Our Moroccan Menu", "moroccan-menu-koh-phangan.html", "assets/img/moroccan-couscous-koh-phangan.jpg", "Couscous"))
    html = L.page(
        "Meet Our Editorial Team — The Dar Mansour Journal",
        "The editorial team behind the Dar Mansour Journal: Maïja Disseau (Moroccan culture), P'Jae (Koh Phangan local expert) and Bruno Potier (editorial director).",
        AUTHORS_URL, body, og_image="assets/img/maija-art-direction-koh-phangan.jpg",
        extra_head=_authors_hub_schema(all_articles), body_class="journal")
    return L.to_root_relative(html)


def _author_articles(p, all_articles):
    """Articles this author is the primary writer of — only real, published ones
    (never invent titles for pages that do not exist)."""
    if not p.get("category"):
        return []
    return [a for a in all_articles if a["category"] == p["category"]]


def render_author(p, all_articles):
    """Individual author profile page (/authors/<slug>/)."""
    about = "".join(f"<p>{para}</p>" for para in p["about"])
    expertise = "".join(f"<li>{x}</li>" for x in p["expertise"])
    arts = _author_articles(p, all_articles)
    if arts:
        art_items = "".join(
            f'<li><a class="ilink" href="{a["url"]}">{a["title"]}</a></li>' for a in arts)
        articles_block = f'''
    <h2>Articles by {p["short"]}</h2>
    <ul class="author__articles">{art_items}</ul>'''
    elif p["slug"] == "bruno-potier":
        articles_block = ('\n    <h2>At the Journal</h2>\n    <p>As Editorial Director, Bruno '
                          'oversees the editorial direction and review of every guide and story '
                          'in <a class="ilink" href="blog.html">The Dar Mansour Journal</a>, '
                          'working alongside Maïja and P\'Jae.</p>')
    else:
        articles_block = ""

    other = "".join(
        f'<a class="ilink" href="{_author_url(o)}">{o["name"]}</a>'
        + (" · " if i < len(AUTHORS) - 2 else "")
        for i, o in enumerate([x for x in AUTHORS if x["slug"] != p["slug"]]))

    body = L.breadcrumb(("Journal", "blog.html"), ("Editorial Team", AUTHORS_URL),
                        (p["name"], None)) + L.subhero(
        p["role"], p["name"], p["tagline"], p["photo"], p["photo_alt"]) + f'''
<section class="section"><div class="wrap prose reveal">
    <h2>About {p["short"]}</h2>
    {about}
    <h2>Areas of Expertise</h2>
    <ul class="author__expertise">{expertise}</ul>
    {articles_block}
    <blockquote class="author__quote">“{p["philosophy"]}”</blockquote>
    <p class="author__meet">Meet the rest of the team: {other} · <a class="ilink" href="{AUTHORS_URL}">Editorial Team</a></p>
</div></section>
''' + L.cta_band(
        "Taste the story around our table",
        "The best chapters are written over a slow Moroccan dinner. Reserve your evening at Dar Mansour.") + L.related(
        ("Journal", "All Stories", "blog.html", "assets/uploads/where-to-watch-the-sunset-in-koh-phangan2.jpg", "Aerial view of a turquoise Koh Phangan bay — stories from The Dar Mansour Journal"),
        ("Founders", "Our Story", "dar-mansour-founders-vision.html", "assets/uploads/dar-mansour-founders-our-story-koh-phangan.jpg", "Maïja and Bruno, founders of Dar Mansour"),
        ("Menu", "Our Moroccan Menu", "moroccan-menu-koh-phangan.html", "assets/img/moroccan-couscous-koh-phangan.jpg", "Couscous"))
    seo_title = f'{p["name"]} — {_strip(p["role_short"])} · Dar Mansour Journal'
    seo_desc = _strip(p["about"][0])
    if len(seo_desc) > 158:
        seo_desc = seo_desc[:155].rsplit(" ", 1)[0] + "…"
    html = L.page(
        seo_title[:70], seo_desc, _author_url(p), body,
        og_image=p["photo"],
        extra_head='<script type="application/ld+json">'
                   + json.dumps(_person_schema(p, all_articles), ensure_ascii=False) + '</script>',
        body_class="journal")
    return L.to_root_relative(html)
