# -*- coding: utf-8 -*-
"""Shared layout: head, header, footer, small helpers. Static-site partials."""

import hashlib
import os

SITE_URL = "https://darmansour.com"

# Pre-launch switch: while True, every page carries a noindex meta and the
# sitemap is not advertised, so search engines keep the site out of results.
# Flip to False (and rebuild) to open the site for indexing at launch.
NOINDEX = False
WA = "https://wa.me/66822767757"

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


def _webp(path):
    """Serve visible photos as WebP. og:image / schema keep their JPG paths
    (better handled by social scrapers) — those never pass through here."""
    if path.startswith("assets/img/"):
        base, ext = os.path.splitext(path)
        if ext.lower() in (".jpg", ".jpeg", ".png"):
            return base + ".webp"
    return path

WA_ICON = ('<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15l-1.3 4.7 '
           '4.8-1.3A10 10 0 1 0 12 2Zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.6-3.9-4.7-4.1-.1-.2-1.1-1.5-1.1-2.8 '
           '0-1.3.7-2 .9-2.2.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5.2.5.7 1.8.8 1.9.1.1.1.3 0 .5-.3.5-.5.7-.7 1-.2.2-.3.4-.1.7.2.3.9 1.5 '
           '2 2.4 1.4 1.2 2.5 1.5 2.8 1.7.3.1.5.1.6-.1.2-.2.7-.9.9-1.2.2-.3.4-.2.6-.1.3.1 1.6.8 1.9.9.3.2.5.2.5.3.1.2.1.7-.1 1.3Z"/></svg>')

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

NAV_ITEMS = [
    ("index.html", "Experience"),
    ("moroccan-menu-koh-phangan.html", "Menu"),
    ("moroccan-wine-pairing-koh-phangan.html", "Wine"),
    ("private-dining-koh-phangan.html", "Private Dining"),
    ("moroccan-restaurant-reviews-koh-phangan.html", "Reviews"),
    ("contact-dar-mansour-koh-phangan.html", "Contact"),
]


def head(title, desc, canonical, og_image="assets/img/moroccan-garden-dining-koh-phangan.jpg", extra="", body_class=""):
    bodycls = f' class="{body_class}"' if body_class else ''
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
<meta property="og:site_name" content="Dar Mansour — Morocco's Kitchen">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE_URL}/{og_image}">
<meta property="og:url" content="{SITE_URL}/{canonical}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="/favicon-32.png" sizes="32x32">
<link rel="icon" type="image/png" href="/favicon-192.png" sizes="192x192">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#00837D">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Mulish:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css?v={CSS_V}">
{extra}
</head>
<body{bodycls}>'''



# Full-menu groups (every page, grouped by cluster)
MEGA_GROUPS = [
    ("The Restaurant", [
        ("index.html", "The Experience"),
        ("moroccan-slow-dining-koh-phangan.html", "Concept &amp; Slow Dining"),
        ("dar-mansour-founders-vision.html", "Founders &amp; Vision"),
        ("moroccan-interior-art-koh-phangan.html", "Artistic Direction"),
        ("moroccan-hospitality-values-koh-phangan.html", "The Mansour Spirit"),
        ("blog.html", "Journal &amp; Stories"),
    ]),
    ("Food &amp; Drink", [
        ("moroccan-menu-koh-phangan.html", "Our Moroccan Menu"),
        ("moroccan-wine-pairing-koh-phangan.html", "Wine Pairing"),
        ("moroccan-cocktails-koh-phangan.html", "The Mansour Bar"),
        ("moroccan-pantry-koh-phangan.html", "Moroccan Pantry"),
    ]),
    ("Visit &amp; Book", [
        ("moroccan-restaurant-reservation-koh-phangan.html", "Reservation &amp; Pre-order"),
        ("private-dining-koh-phangan.html", "Private Dining"),
        ("moroccan-restaurant-reviews-koh-phangan.html", "Reviews"),
        ("best-moroccan-restaurant-world-press.html", "Recognition"),
        ("faq.html", "FAQ"),
        ("contact-dar-mansour-koh-phangan.html", "Contact &amp; Location"),
    ]),
]


def header():
    nav = "\n      ".join(f'<a href="{href}">{label}</a>' for href, label in NAV_ITEMS)
    groups = ""
    for title, links in MEGA_GROUPS:
        items = "".join(f'<li><a href="{href}">{label}</a></li>' for href, label in links)
        groups += f'<div class="mega__group"><h4>{title}</h4><ul>{items}</ul></div>'
    return f'''
<header class="header" id="header">
  <div class="wrap header__inner">
    <a class="brand" href="index.html" aria-label="Dar Mansour — Morocco's Kitchen, home">
      <img class="brand__full brand__full--white" src="assets/logo/dar-mansour-logo-white.png" alt="Dar Mansour — Morocco's Kitchen" width="1622" height="876">
      <img class="brand__full brand__full--color" src="assets/logo/dar-mansour-logo-green.png" alt="" aria-hidden="true" width="1622" height="876">
    </a>
    <nav class="nav" aria-label="Primary">
      {nav}
    </nav>
    <div class="header__cta">
      <a class="btn btn--light" href="{WA}" target="_blank" rel="noopener">Book</a>
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
        <span class="eyebrow">Reservations</span>
        <p><a href="{WA}" target="_blank" rel="noopener">WhatsApp · +66 82 276 7757</a><br>
        <a href="mailto:hello@darmansour.com">hello@darmansour.com</a></p>
      </div>
      <div>
        <span class="eyebrow">Find us</span>
        <p>Hin Kong Road, Sri Thanu area<br>Koh Phangan, Thailand<br>Tue–Sat · 7:00–10:30 PM</p>
      </div>
      <a class="btn btn--primary" href="{WA}" target="_blank" rel="noopener">{WA_ICON} Book via WhatsApp</a>
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


def subhero(eyebrow, h1, sub, image, alt, tall=False):
    cls = "subhero subhero--tall" if tall else "subhero"
    return f'''
<section class="{cls}">
  <div class="subhero__media"><img src="{_webp(image)}" alt="{alt}" fetchpriority="high"></div>
  <div class="wrap subhero__inner">
    <span class="eyebrow">{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="subhero__sub">{sub}</p>
  </div>
</section>'''


def cta_band(title, text):
    return f'''
<section class="section book">
  <div class="wrap wrap--narrow reveal">
    <span class="eyebrow">Reservation &amp; Pre-order</span>
    <h2>{title}</h2>
    <p class="lead">{text}</p>
    <div class="book__actions">
      <a class="btn btn--primary" href="{WA}" target="_blank" rel="noopener">{WA_ICON} Book &amp; Pre-order via WhatsApp</a>
      <a class="btn btn--ghost" href="https://share.google/Rp8YllnPe9Z9E9Va0" target="_blank" rel="noopener">Get Directions</a>
    </div>
    <p class="book__meta">Dinner only · Tuesday to Saturday · 7:00 PM – 10:30 PM · Closed Sunday &amp; Monday</p>
  </div>
</section>'''


def related(*cards):
    """cards: (eyebrow, title, href, image, alt)"""
    inner = "".join(
        f'''<a class="related__card reveal" href="{href}">
          <img src="{_webp(img)}" alt="{alt}" loading="lazy">
          <div><span>{eyebrow}</span><h3>{title}</h3></div>
        </a>''' for eyebrow, title, href, img, alt in cards)
    return f'''
<section class="section" style="padding-top:0;">
  <div class="wrap">
    <div class="center reveal" style="margin-bottom:2.2rem;"><div class="divider"><span>◇◇◇</span></div>
    <h2 style="margin-top:1.3rem;">Continue the journey</h2></div>
    <div class="related">{inner}</div>
  </div>
</section>'''


def footer():
    return f'''
<footer class="footer" id="contact">
  <div class="wrap">
    <div class="footer__grid">
      <div class="footer__brand">
        <img class="footer__logo" src="assets/logo/dar-mansour-logo-white.png" alt="Dar Mansour — Morocco's Kitchen" width="1622" height="876">
        <p class="footer__brand-sub">Koh Phangan · Thailand</p>
        <p>A soulful Moroccan slow food sanctuary on the west coast of Koh Phangan. Rooted in tradition, slow cooked with care.</p>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="index.html">The Experience</a></li>
          <li><a href="moroccan-slow-dining-koh-phangan.html">Concept</a></li>
          <li><a href="moroccan-menu-koh-phangan.html">Menu</a></li>
          <li><a href="moroccan-wine-pairing-koh-phangan.html">Wine Pairing</a></li>
          <li><a href="moroccan-cocktails-koh-phangan.html">The Mansour Bar</a></li>
          <li><a href="private-dining-koh-phangan.html">Private Dining</a></li>
        </ul>
      </div>
      <div>
        <h4>Discover</h4>
        <ul>
          <li><a href="dar-mansour-founders-vision.html">Founders &amp; Vision</a></li>
          <li><a href="moroccan-interior-art-koh-phangan.html">Artistic Direction</a></li>
          <li><a href="moroccan-pantry-koh-phangan.html">Moroccan Pantry</a></li>
          <li><a href="moroccan-hospitality-values-koh-phangan.html">Mansour Spirit</a></li>
          <li><a href="best-moroccan-restaurant-world-press.html">Recognition</a></li>
          <li><a href="moroccan-restaurant-reviews-koh-phangan.html">Reviews</a></li>
          <li><a href="blog.html">Journal &amp; Stories</a></li>
          <li><a href="faq.html">FAQ</a></li>
        </ul>
      </div>
      <div>
        <h4>Visit &amp; Contact</h4>
        <address>
          <p><a href="https://share.google/Rp8YllnPe9Z9E9Va0" target="_blank" rel="noopener">Hin Kong Road, Sri Thanu area<br>Koh Phangan, Thailand</a></p>
          <p>Tue – Sat · 7:00–10:30 PM<br>Closed Sun &amp; Mon</p>
          <p><a href="{WA}" target="_blank" rel="noopener">WhatsApp · +66 82 276 7757</a></p>
          <p><a href="mailto:hello@darmansour.com">hello@darmansour.com</a></p>
        </address>
      </div>
    </div>
    <div class="footer__bottom">
      <span>All content © Dar Mansour — 2025. No tracking, no ads — just food &amp; soul.</span>
      <div class="footer__social">
        <a href="https://instagram.com/darmansour.kohphangan" target="_blank" rel="noopener">Instagram</a>
        <a href="https://www.facebook.com/people/Dar-Mansour/" target="_blank" rel="noopener">Facebook</a>
        <a href="https://share.google/Rp8YllnPe9Z9E9Va0" target="_blank" rel="noopener">Google Maps</a>
      </div>
    </div>
  </div>
</footer>
<a class="wa-float" href="{WA}" target="_blank" rel="noopener" aria-label="Book via WhatsApp">{WA_ICON}</a>
<script src="assets/js/main.js?v={JS_V}"></script>
</body>
</html>'''


def page(title, desc, canonical, body, og_image="assets/img/moroccan-garden-dining-koh-phangan.jpg", extra_head="", body_class=""):
    return head(title, desc, canonical, og_image, extra_head, body_class) + header() + "\n<main id=\"top\">\n" + body + "\n</main>\n" + footer()
