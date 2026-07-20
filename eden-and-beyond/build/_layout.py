# -*- coding: utf-8 -*-
"""Eden & Beyond — shared layout: head, header, footer, section helpers.
Static-site partials (no framework, no build step beyond this generator)."""

import hashlib
import os
from urllib.parse import quote

SITE_URL = "https://edenandbeyond.studio"

# Pre-launch switch: while True, every page carries a noindex meta and the
# sitemap is not advertised, so search engines keep the site out of results.
# Flip to False (and rebuild) to open the site for indexing at launch.
NOINDEX = True

# --- Contact / social ---
EMAIL = "hello@edenandbeyond.studio"
INSTAGRAM = "https://instagram.com/edenandbeyond.kpg"
INSTAGRAM_HANDLE = "@edenandbeyond.kpg"

# --- SEO / Analytics integrations (leave empty to disable) ---
GA4_ID = ""          # Google Analytics 4 Measurement ID (add at launch)
BING_VERIFY = ""     # Bing Webmaster (msvalidate.01)

# Cache-busting: short content hash appended to asset URLs so browsers fetch the
# new CSS/JS immediately after a deploy instead of serving a stale cached copy.
_ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")


def _asset_v(rel):
    try:
        with open(os.path.join(_ASSETS, rel), "rb") as f:
            return hashlib.md5(f.read()).hexdigest()[:8]
    except OSError:
        return "1"


CSS_V = _asset_v("css/style.css")
JS_V = _asset_v("js/main.js")

ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
         '<path d="M5 12h14M13 6l6 6-6 6"/></svg>')

# Primary top nav (desktop) — kept short and premium.
NAV_ITEMS = [
    ("studio.html", "Studio"),
    ("projects.html", "Projects"),
    ("collection.html", "Collection"),
    ("journal.html", "Journal"),
    ("contact.html", "Contact"),
]

# Full-screen menu, grouped by cluster.
MEGA_GROUPS = [
    ("The Studio", [
        ("index.html", "Home"),
        ("studio.html", "Studio &amp; Maija"),
        ("projects.html", "Projects"),
        ("journal.html", "Journal"),
        ("contact.html", "Contact"),
    ]),
    ("The Collection", [
        ("collection.html", "All Pieces"),
        ("collection.html#furniture", "Furniture"),
        ("collection.html#lighting", "Lighting"),
        ("collection.html#objects", "Objects"),
        ("collection.html#limited-editions", "Limited Editions"),
    ]),
    ("What We Do", [
        ("hospitality-design.html", "Hospitality Design"),
        ("restaurant-design.html", "Restaurant Design"),
        ("residential-design.html", "Residential Design"),
        ("furniture-object-design.html", "Furniture &amp; Objects"),
        ("creative-direction.html", "Creative Direction"),
    ]),
]


def head(title, desc, canonical, og_image="assets/img/eden-and-beyond-studio.jpg",
         extra="", body_class=""):
    bodycls = f' class="{body_class}"' if body_class else ''
    analytics = ""
    if BING_VERIFY:
        analytics += f'<meta name="msvalidate.01" content="{BING_VERIFY}">\n'
    if GA4_ID:
        analytics += (
            f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>\n'
            "<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}"
            f"gtag('js',new Date());gtag('config','{GA4_ID}');</script>\n"
        )
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
{'<meta name="robots" content="noindex, nofollow">' if NOINDEX else ''}
<link rel="canonical" href="{SITE_URL}/{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Eden &amp; Beyond">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE_URL}/{og_image}">
<meta property="og:url" content="{SITE_URL}/{canonical}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#17150F">
{analytics}<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400;1,9..144,500&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css?v={CSS_V}">
{extra}
</head>
<body{bodycls}>'''


def header():
    nav = "\n      ".join(f'<a href="{href}">{label}</a>' for href, label in NAV_ITEMS)
    groups = ""
    for title, links in MEGA_GROUPS:
        items = "".join(f'<li><a href="{href}">{label}</a></li>' for href, label in links)
        groups += f'<div class="mega__group"><h4>{title}</h4><ul>{items}</ul></div>'
    return f'''
<header class="header" id="header">
  <div class="wrap header__inner">
    <a class="brand" href="index.html" aria-label="Eden &amp; Beyond, home">
      <img class="brand__logo" src="assets/img/eden-and-beyond-logo.png" alt="Eden &amp; Beyond" width="681" height="681">
    </a>
    <nav class="nav" aria-label="Primary">
      {nav}
    </nav>
    <div class="header__cta">
      <a class="btn btn--primary" href="contact.html">Start a Project</a>
      <button class="menu-toggle" id="menuToggle" aria-label="Open full menu" aria-expanded="false" aria-controls="mega">
        <span class="menu-toggle__lines" aria-hidden="true"><span></span><span></span><span></span></span>
        <span class="menu-toggle__label">Menu</span>
      </button>
    </div>
  </div>
</header>
<div class="mega" id="mega" aria-label="Full navigation" data-nav>
  <div class="mega__inner">
    <div class="mega__groups">{groups}</div>
    <div class="mega__foot">
      <div>
        <span class="eyebrow">Start a Project</span>
        <p><a href="mailto:{EMAIL}">{EMAIL}</a><br>
        <span class="mega__note">Hospitality, residential, furniture &amp; creative direction enquiries.</span></p>
      </div>
      <div>
        <span class="eyebrow">Studio</span>
        <p>Working internationally<br>Based in Thailand<br>
        <a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram · {INSTAGRAM_HANDLE}</a></p>
      </div>
      <a class="btn btn--primary" href="contact.html">Start a Project {ARROW}</a>
    </div>
  </div>
</div>'''


def breadcrumb(*crumbs):
    """crumbs: list of (label, href) ; last one is current (href None)."""
    items = ['<li><a href="index.html">Home</a></li>']
    for label, href in crumbs:
        items.append('<li class="sep" aria-hidden="true">›</li>')
        if href:
            items.append(f'<li><a href="{href}">{label}</a></li>')
        else:
            items.append(f'<li aria-current="page">{label}</li>')
    return ('<nav class="wrap breadcrumb" aria-label="Breadcrumb"><ol>'
            + "".join(items) + '</ol></nav>')


def hero(eyebrow, h1_html, sub, actions_html, media_class="hero__media--placeholder",
         media_html=""):
    """Full-screen homepage hero. media_html can hold a <picture>/<video>;
    otherwise a styled placeholder tone is shown (pre-photography)."""
    media = media_html or ''
    return f'''
<section class="hero">
  <div class="hero__media {media_class}">{media}</div>
  <div class="wrap hero__inner">
    <span class="eyebrow">{eyebrow}</span>
    <h1 class="display hero__title">{h1_html}</h1>
    <p class="hero__sub">{sub}</p>
    <div class="hero__actions">{actions_html}</div>
  </div>
  <span class="hero__scroll" aria-hidden="true">Scroll</span>
</section>'''


def subhero(eyebrow, h1, sub, media_class="subhero__media--placeholder",
            media_html="", tall=False):
    cls = "subhero subhero--tall" if tall else "subhero"
    media = media_html or ''
    return f'''
<section class="{cls}">
  <div class="subhero__media {media_class}">{media}</div>
  <div class="wrap subhero__inner">
    <span class="eyebrow">{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="subhero__sub">{sub}</p>
  </div>
</section>'''


def cta_band(title, text, eyebrow="Start a Project", btn_label="Start a Project"):
    return f'''
<section class="section book">
  <div class="wrap wrap--narrow reveal">
    <span class="eyebrow">{eyebrow}</span>
    <h2>{title}</h2>
    <p class="lead">{text}</p>
    <div class="book__actions">
      <a class="btn btn--primary" href="contact.html">{btn_label} {ARROW}</a>
      <a class="btn btn--ghost" href="projects.html">Explore Our Work</a>
    </div>
  </div>
</section>'''


def related(*cards):
    """cards: (eyebrow, title, href)"""
    inner = "".join(
        f'''<a class="related__card reveal" href="{href}">
          <div class="related__card-bg"></div>
          <div><span>{eyebrow}</span><h3>{title}</h3></div>
        </a>''' for eyebrow, title, href in cards)
    return f'''
<section class="section" style="padding-top:0;">
  <div class="wrap">
    <div class="center reveal" style="margin-bottom:2.2rem;"><div class="divider"><span>&#9671;&#9671;&#9671;</span></div>
    <h2 style="margin-top:1.3rem;">Continue exploring</h2></div>
    <div class="related">{inner}</div>
  </div>
</section>'''


def footer():
    return f'''
<footer class="footer" id="contact">
  <div class="wrap">
    <div class="footer__grid">
      <div class="footer__brand">
        <span class="brand__name">Eden &amp; Beyond</span>
        <p class="footer__brand-sub">Creative Studio · Thailand</p>
        <p>A multidisciplinary creative studio designing places, objects &amp; experiences with identity, purpose and lasting impact.</p>
      </div>
      <div>
        <h4>Studio</h4>
        <ul>
          <li><a href="studio.html">Studio</a></li>
          <li><a href="projects.html">Projects</a></li>
          <li><a href="journal.html">Journal</a></li>
          <li><a href="contact.html">Contact</a></li>
          <li><a href="hospitality-design.html">Hospitality Design</a></li>
          <li><a href="residential-design.html">Residential Design</a></li>
          <li><a href="creative-direction.html">Creative Direction</a></li>
        </ul>
      </div>
      <div>
        <h4>The Collection</h4>
        <ul>
          <li><a href="collection.html">All Pieces</a></li>
          <li><a href="collection.html#furniture">Furniture</a></li>
          <li><a href="collection.html#lighting">Lighting</a></li>
          <li><a href="collection.html#objects">Objects</a></li>
          <li><a href="collection.html#limited-editions">Limited Editions</a></li>
        </ul>
      </div>
      <div>
        <h4>Connect</h4>
        <address>
          <p>Working internationally<br>Based in Thailand</p>
          <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
          <p><a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram · {INSTAGRAM_HANDLE}</a></p>
        </address>
      </div>
    </div>
    <div class="footer__bottom">
      <span>&copy; Eden &amp; Beyond — 2026. Designing places, objects &amp; experiences.</span>
      <div class="footer__social">
        <a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a>
        <a href="mailto:{EMAIL}">Email</a>
      </div>
    </div>
  </div>
</footer>
<script src="assets/js/main.js?v={JS_V}"></script>
</body>
</html>'''


def page(title, desc, canonical, body,
         og_image="assets/img/eden-and-beyond-studio.jpg", extra_head="", body_class=""):
    return (head(title, desc, canonical, og_image, extra_head, body_class)
            + header() + "\n<main id=\"top\">\n" + body + "\n</main>\n" + footer())
