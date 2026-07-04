# -*- coding: utf-8 -*-
"""Journal (blog) — reads markdown articles authored via Decap CMS and turns
them into full SEO pages + the index listing.

Articles live in  content/journal/*.md  with YAML front matter:

    ---
    title: "..."
    seo_title: "..."        # optional; falls back to title
    description: "..."       # meta description
    date: 2026-07-04
    author: "Dar Mansour"
    cover: "assets/uploads/photo.jpg"
    cover_alt: "..."
    ---
    Markdown body…

Everything technical (canonical, Article JSON-LD, Open Graph, sitemap entry,
breadcrumb, WebP) is generated here — the author only fills the fields above.
"""
import os
import glob
import json
import datetime

import yaml
import markdown as _md

import _layout as L

HERE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(HERE, "..", "content", "journal")
DEFAULT_COVER = "assets/img/moroccan-zellige-wall-art-koh-phangan.jpg"


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


def load_articles():
    """Return a list of article dicts, newest first."""
    articles = []
    for path in sorted(glob.glob(os.path.join(CONTENT, "*.md"))):
        with open(path, encoding="utf-8") as f:
            meta, body = _split_front_matter(f.read())
        slug = os.path.splitext(os.path.basename(path))[0]
        iso, disp = _dates(meta.get("date"))
        cover = (meta.get("cover") or DEFAULT_COVER).lstrip("/")
        title = meta.get("title") or slug.replace("-", " ").title()
        articles.append({
            "slug": slug,
            "title": title,
            "seo_title": meta.get("seo_title") or title,
            "description": (meta.get("description") or "").strip(),
            "date_iso": iso,
            "date_disp": disp,
            "author": meta.get("author") or "Dar Mansour",
            "cover": cover,
            "cover_alt": meta.get("cover_alt") or title,
            "body_html": _md.markdown((body or "").strip(), extensions=["extra", "sane_lists"]),
            "url": f"journal-{slug}.html",
        })
    articles.sort(key=lambda a: a["date_iso"], reverse=True)
    return articles


def _schema(a):
    site = L.SITE_URL
    data = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": a["title"],
        "description": a["description"],
        "image": f'{site}/{a["cover"]}',
        "datePublished": a["date_iso"],
        "dateModified": a["date_iso"],
        "author": {"@type": "Organization", "name": a["author"]},
        "publisher": {
            "@type": "Organization",
            "name": "Dar Mansour — Morocco's Kitchen",
            "logo": {"@type": "ImageObject", "url": f"{site}/assets/logo/dar-mansour-logo-green.png"},
        },
        "mainEntityOfPage": f'{site}/{a["url"]}',
    }
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + '</script>'


def render_article(a):
    body = L.breadcrumb(("Journal", "blog.html"), (a["title"], None)) + L.subhero(
        "Journal", a["title"], a["description"], a["cover"], a["cover_alt"]) + f'''
<section class="section"><div class="wrap prose reveal">
  <p class="article__meta"><time datetime="{a["date_iso"]}">{a["date_disp"]}</time> · {a["author"]}</p>
{a["body_html"]}
</div></section>
''' + L.cta_band("Taste the story around our table",
        "The best chapters are written over a slow Moroccan dinner. Reserve your evening at Dar Mansour.") + L.related(
        ("Journal", "More Stories", "blog.html", "assets/img/moroccan-zellige-wall-art-koh-phangan.jpg", "Zellige wall art"),
        ("Menu", "Our Moroccan Menu", "moroccan-menu-koh-phangan.html", "assets/img/moroccan-couscous-koh-phangan.jpg", "Couscous"),
        ("Founders", "Founders &amp; Vision", "dar-mansour-founders-vision.html", "assets/img/maija-art-direction-koh-phangan.jpg", "Art direction"))
    return L.page(a["seo_title"], a["description"], a["url"], body,
                  og_image=a["cover"], extra_head=_schema(a))


def render_index_cards(articles):
    """Grid of article cards for the Journal index page (empty string if none)."""
    if not articles:
        return ""
    cards = "".join(f'''
      <a class="jcard reveal" href="{a["url"]}">
        <span class="jcard__img"><img src="{L._webp(a["cover"])}" alt="{a["cover_alt"]}" loading="lazy"></span>
        <span class="jcard__body">
          <span class="jcard__date">{a["date_disp"]}</span>
          <span class="jcard__title">{a["title"]}</span>
          <span class="jcard__desc">{a["description"]}</span>
          <span class="textlink">Read the story {L.ARROW}</span>
        </span>
      </a>''' for a in articles)
    return f'''
<section class="section" id="latest" style="padding-top:0;"><div class="wrap">
  <div class="center reveal" style="margin-bottom:clamp(2rem,4vw,3rem);">
    <span class="eyebrow">Latest Stories</span>
    <h2 style="margin-top:1rem;">Fresh from the Journal</h2>
  </div>
  <div class="jgrid">{cards}</div>
</div></section>'''
