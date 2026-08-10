# -*- coding: utf-8 -*-
"""Shared layout: head, header, footer, small helpers. Static-site partials."""

import hashlib
import json
import os
from urllib.parse import quote, unquote

SITE_URL = "https://darmansour.com"

# Pre-launch switch: while True, every page carries a noindex meta and the
# sitemap is not advertised, so search engines keep the site out of results.
# Flip to False (and rebuild) to open the site for indexing at launch.
NOINDEX = False
WA = "https://wa.me/66822767757"

# --- SEO / Analytics integrations (leave empty to disable) ---
GA4_ID = "G-L2GLFDZHCR"   # Google Analytics 4 Measurement ID
BING_VERIFY = "8ED8A01F43B5C8FE82AE6C2F87241426"   # Bing Webmaster (msvalidate.01)
PINTEREST_VERIFY = "1a3c57976ae153f40f53e3ba2ff91b52"   # Pinterest domain claim (p:domain_verify)

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
    base, ext = os.path.splitext(path)
    if ext.lower() in (".jpg", ".jpeg", ".png"):
        if path.startswith("assets/img/"):
            return base + ".webp"
        if path.startswith("assets/uploads/"):
            # CMS uploads: only switch to WebP if a sibling actually exists
            disk = os.path.join(os.path.dirname(_ASSETS), unquote(base) + ".webp")
            if os.path.exists(disk):
                return base + ".webp"
    return path

import re as _re

# Pages that live in a sub-directory (e.g. /authors/maija-disseau/) cannot use the
# site's relative asset/link paths — they would resolve against the sub-directory.
# This rewrites in-page relative href/src/url() references to root-absolute (/…),
# which work from any depth. Absolute URLs, anchors, mailto/tel and data URIs are
# left untouched. Applied only to sub-directory pages.
_ROOT_SKIP = ("http://", "https://", "//", "/", "#", "mailto:", "tel:", "data:")


def _root_abs(u):
    return u if u.startswith(_ROOT_SKIP) else "/" + u


def to_root_relative(html):
    html = _re.sub(r'\b(href|src)="([^"]*)"',
                   lambda m: f'{m.group(1)}="{_root_abs(m.group(2))}"', html)
    # subhero backdrop uses url(&quot;assets/…&quot;)
    html = _re.sub(r'url\(&quot;([^&]*)&quot;\)',
                   lambda m: f'url(&quot;{_root_abs(m.group(1))}&quot;)', html)
    return html


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

# --- French (fr) UI labels for the bilingual build -------------------------
# Phase 1: French pages live under /fr/ and reuse the same slugs. Only the
# ~10 core "product" pages exist in French; links to not-yet-translated pages
# fall back to their English URL (handled in fr_href()).
NAV_ITEMS_FR = [
    ("index.html", "L'Expérience"),
    ("moroccan-menu-koh-phangan.html", "Menu"),
    ("moroccan-wine-pairing-koh-phangan.html", "Vins"),
    ("private-dining-koh-phangan.html", "Privatisation"),
    ("moroccan-restaurant-reviews-koh-phangan.html", "Avis"),
    ("contact-dar-mansour-koh-phangan.html", "Contact"),
]

# Slugs that have a French version built under /fr/. Links to these get the /fr/
# prefix on French pages; everything else falls back to the English URL.
# Add a slug here only once its French page actually exists (avoids 404s).
FR_PAGES = {
    "index.html",
    "moroccan-slow-dining-koh-phangan.html",
    "moroccan-menu-koh-phangan.html",
    "moroccan-restaurant-reservation-koh-phangan.html",
    "moroccan-wine-pairing-koh-phangan.html",
    "moroccan-cocktails-koh-phangan.html",
    "moroccan-restaurant-reviews-koh-phangan.html",
    "private-dining-koh-phangan.html",
    "faq.html",
    "contact-dar-mansour-koh-phangan.html",
}

UI = {
    "en": {"book": "Book", "menu": "Menu", "lang_other": "FR", "lang_other_full": "Français"},
    "fr": {"book": "Réserver", "menu": "Menu", "lang_other": "EN", "lang_other_full": "English"},
}


def hreflang_links(en_url, fr_url):
    """Reciprocal hreflang tags for a page that exists in both languages.
    en_url / fr_url are site-relative (e.g. 'index.html', 'fr/index.html')."""
    if not fr_url:
        return ""
    return (f'<link rel="alternate" hreflang="en" href="{SITE_URL}/{en_url}">\n'
            f'<link rel="alternate" hreflang="fr" href="{SITE_URL}/{fr_url}">\n'
            f'<link rel="alternate" hreflang="x-default" href="{SITE_URL}/{en_url}">\n')


def head(title, desc, canonical, og_image="assets/img/moroccan-garden-dining-koh-phangan.jpg", extra="", body_class="", lang="en", alt_hreflang=""):
    bodycls = f' class="{body_class}"' if body_class else ''
    analytics = ""
    if BING_VERIFY:
        analytics += f'<meta name="msvalidate.01" content="{BING_VERIFY}">\n'
    if PINTEREST_VERIFY:
        analytics += f'<meta name="p:domain_verify" content="{PINTEREST_VERIFY}">\n'
    if GA4_ID:
        # GA4 is loaded lazily — the gtag stub queues calls into dataLayer
        # immediately (so events fired early, e.g. contact_click, are kept),
        # and the heavy gtag.js is fetched only on first user interaction or
        # after a short timeout. This removes ~180 KB from the initial load
        # (better mobile LCP/FCP) with virtually no measurement loss.
        analytics += (
            "<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}"
            f"gtag('js',new Date());gtag('config','{GA4_ID}');"
            "(function(){var loaded=false;function load(){if(loaded)return;loaded=true;"
            "var s=document.createElement('script');s.async=true;"
            f"s.src='https://www.googletagmanager.com/gtag/js?id={GA4_ID}';"
            "document.head.appendChild(s);}"
            "['scroll','mousemove','touchstart','keydown','click'].forEach(function(e){"
            "window.addEventListener(e,load,{once:true,passive:true});});"
            "setTimeout(load,3500);})();</script>\n"
        )
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
{'<meta name="robots" content="noindex, nofollow">' if NOINDEX else ''}
<link rel="canonical" href="{SITE_URL}/{canonical}">
{alt_hreflang}<meta property="og:locale" content="{'fr_FR' if lang == 'fr' else 'en_US'}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Dar Mansour - Morocco's Kitchen">
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
{analytics}<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Mulish:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500;1,600&display=swap" media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Mulish:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500;1,600&display=swap"></noscript>
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


def _lang_switch(lang, alt_url):
    """Small EN/FR toggle pointing at the current page's other-language URL."""
    if not alt_url:
        return ""
    label = UI[lang]["lang_other"]
    full = UI[lang]["lang_other_full"]
    return (f'<a class="lang-switch" href="{alt_url}" hreflang="{UI[lang]["lang_other"].lower()}" '
            f'aria-label="{full}">{label}</a>')


def header(lang="en", alt_url=""):
    nav_items = NAV_ITEMS_FR if lang == "fr" else NAV_ITEMS
    nav = "\n      ".join(f'<a href="{href}">{label}</a>' for href, label in nav_items)
    groups = ""
    for title, links in MEGA_GROUPS:
        items = "".join(f'<li><a href="{href}">{label}</a></li>' for href, label in links)
        groups += f'<div class="mega__group"><h4>{title}</h4><ul>{items}</ul></div>'
    switch = _lang_switch(lang, alt_url)
    return f'''
<header class="header" id="header">
  <div class="wrap header__inner">
    <a class="brand" href="index.html" aria-label="Dar Mansour - Morocco's Kitchen, home">
      <img class="brand__full brand__full--white" src="assets/logo/dar-mansour-logo-white.png" alt="Dar Mansour - Morocco's Kitchen" width="1622" height="876">
      <img class="brand__full brand__full--color" src="assets/logo/dar-mansour-logo-green.png" alt="" aria-hidden="true" width="1622" height="876">
    </a>
    <nav class="nav" aria-label="Primary">
      {nav}
    </nav>
    <div class="header__cta">
      {switch}
      <a class="btn btn--light" href="{WA}" target="_blank" rel="noopener">{UI[lang]["book"]}</a>
      <button class="menu-toggle" id="menuToggle" aria-label="Open full menu" aria-expanded="false" aria-controls="mega">
        <span class="menu-toggle__lines" aria-hidden="true"><span></span><span></span><span></span></span>
        <span class="menu-toggle__label">{UI[lang]["menu"]}</span>
      </button>
    </div>
  </div>
</header>
<div class="mega" id="mega" aria-label="Full navigation" data-nav>
  <div class="mega__inner">
    <div class="mega__groups">{groups}</div>
    <div class="mega__foot">
      <div>
        <span class="eyebrow">Reservations &amp; Pre-order</span>
        <p><a href="{WA}" target="_blank" rel="noopener">WhatsApp · +66 82 276 7757</a><br>
        <span class="mega__note">For the fastest response and reservations.</span></p>
        <span class="eyebrow" style="margin-top:1.4rem;display:inline-block;">General Enquiries</span>
        <p><a href="mailto:hello@darmansour.com">hello@darmansour.com</a><br>
        <span class="mega__note">Partnerships, private events, media &amp; general enquiries.</span></p>
      </div>
      <div>
        <span class="eyebrow">Find us</span>
        <p>Hin Kong Road, Sri Thanu area<br>Koh Phangan 84280, Thailand<br>Tue–Sat · 7:00–10:30 PM</p>
      </div>
      <a class="btn btn--primary" href="{WA}" target="_blank" rel="noopener">{WA_ICON} Book via WhatsApp</a>
    </div>
  </div>
</div>'''


def breadcrumb(*crumbs, lang="en"):
    """crumbs: list of (label, href) ; last one is current (href None)."""
    home_label = "Accueil" if lang == "fr" else "Home"
    items = [f'<li><a href="index.html">{home_label}</a></li>']
    ld = [{"@type": "ListItem", "position": 1, "name": home_label, "item": f"{SITE_URL}/"}]
    pos = 2
    for label, href in crumbs:
        items.append('<li class="sep" aria-hidden="true">›</li>')
        if href:
            items.append(f'<li><a href="{href}">{label}</a></li>')
            ld.append({"@type": "ListItem", "position": pos, "name": label,
                       "item": f"{SITE_URL}/{href}"})
        else:
            items.append(f'<li aria-current="page">{label}</li>')
            ld.append({"@type": "ListItem", "position": pos, "name": label})
        pos += 1
    crumbs_ld = {"@context": "https://schema.org", "@type": "BreadcrumbList",
                 "itemListElement": ld}
    script = ('<script type="application/ld+json">'
              + json.dumps(crumbs_ld, ensure_ascii=False) + '</script>')
    return ('<nav class="wrap breadcrumb" aria-label="Breadcrumb"><ol>'
            + "".join(items) + '</ol></nav>' + script)


def subhero(eyebrow, h1, sub, image, alt, tall=False, focus=None, variant=None):
    cls = "subhero subhero--tall" if tall else "subhero"
    # focus lets a page steer the crop (object-position) — handy for portrait
    # photos whose subject sits away from the centre.
    if variant:
        cls += f" subhero--{variant}"
    style = f' style="object-position:{focus}"' if focus else ''
    src = _webp(image)
    # A "portrait" variant keeps the mobile cover crop but, on desktop, shows the
    # whole (square/portrait) photo over a soft blurred fill of itself — so it
    # never looks awkwardly zoomed on a wide screen.
    backdrop = f'<div class="subhero__backdrop" style="background-image:url(&quot;{src}&quot;)"></div>' if variant else ''
    return f'''
<section class="{cls}">
  <div class="subhero__media">{backdrop}<img src="{src}" alt="{alt}"{style} fetchpriority="high"></div>
  <div class="wrap subhero__inner">
    <span class="eyebrow">{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="subhero__sub">{sub}</p>
  </div>
</section>'''


_CTA_T = {
    "en": {"eyebrow": "Reservation &amp; Pre-order",
           "btn": "Book &amp; Pre-order via WhatsApp",
           "directions": "Get Directions",
           "meta": "Dinner only · Tuesday to Saturday · 7:00 PM – 10:30 PM · Closed Sunday &amp; Monday"},
    "fr": {"eyebrow": "Réservation &amp; Pré-commande",
           "btn": "Réserver &amp; pré-commander sur WhatsApp",
           "directions": "Itinéraire",
           "meta": "Dîner uniquement · du mardi au samedi · 19h00 – 22h30 · Fermé dimanche &amp; lundi"},
}


def cta_band(title, text, eyebrow=None, btn_label=None, wa_message=None, lang="en"):
    # Optional pre-filled WhatsApp message, so the guest lands on a ready-to-send
    # text (handy for enquiry-led pages like Private Dining).
    t = _CTA_T[lang]
    eyebrow = eyebrow if eyebrow is not None else t["eyebrow"]
    btn_label = btn_label if btn_label is not None else t["btn"]
    href = f"{WA}?text={quote(wa_message)}" if wa_message else WA
    return f'''
<section class="section book">
  <div class="wrap wrap--narrow reveal">
    <span class="eyebrow">{eyebrow}</span>
    <h2>{title}</h2>
    <p class="lead">{text}</p>
    <div class="book__actions">
      <a class="btn btn--primary" href="{href}" target="_blank" rel="noopener">{WA_ICON} {btn_label}</a>
      <a class="btn btn--ghost" href="https://share.google/Rp8YllnPe9Z9E9Va0" target="_blank" rel="noopener">{t["directions"]}</a>
    </div>
    <p class="book__meta">{t["meta"]}</p>
  </div>
</section>'''


def related(*cards, lang="en"):
    """cards: (eyebrow, title, href, image, alt)"""
    heading = "Poursuivez le voyage" if lang == "fr" else "Continue the journey"
    inner = "".join(
        f'''<a class="related__card reveal" href="{href}">
          <img src="{_webp(img)}" alt="{alt}" loading="lazy">
          <div><span>{eyebrow}</span><h3>{title}</h3></div>
        </a>''' for eyebrow, title, href, img, alt in cards)
    return f'''
<section class="section" style="padding-top:0;">
  <div class="wrap">
    <div class="center reveal" style="margin-bottom:2.2rem;"><div class="divider"><span>◇◇◇</span></div>
    <h2 style="margin-top:1.3rem;">{heading}</h2></div>
    <div class="related">{inner}</div>
  </div>
</section>'''


_FOOTER_T = {
    "en": {
        "tagline": "A soulful Moroccan slow food sanctuary on the west coast of Koh Phangan. Rooted in tradition, slow cooked with care.",
        "explore": "Explore", "discover": "Discover", "visit": "Visit &amp; Contact",
        "experience": "The Experience", "concept": "Concept", "menu": "Menu",
        "wine": "Wine Pairing", "bar": "The Mansour Bar", "private": "Private Dining",
        "founders": "Founders &amp; Vision", "art": "Artistic Direction",
        "pantry": "Moroccan Pantry", "spirit": "Mansour Spirit",
        "recognition": "Recognition", "reviews": "Reviews", "journal": "Journal &amp; Stories",
        "team": "Editorial Team", "faq": "FAQ",
        "hours": "Tue – Sat · 7:00–10:30 PM<br>Closed Sun &amp; Mon",
        "rights": "All content © Dar Mansour — 2026. No tracking, no ads — just food &amp; soul.",
    },
    "fr": {
        "tagline": "Un sanctuaire de slow food marocain sur la côte ouest de Koh Phangan. Enraciné dans la tradition, mijoté avec soin.",
        "explore": "Explorer", "discover": "Découvrir", "visit": "Visite &amp; Contact",
        "experience": "L'Expérience", "concept": "Concept", "menu": "Menu",
        "wine": "Accords mets &amp; vins", "bar": "Le Mansour Bar", "private": "Privatisation",
        "founders": "Fondateurs &amp; Vision", "art": "Direction artistique",
        "pantry": "Le Garde-manger marocain", "spirit": "L'Esprit Mansour",
        "recognition": "Reconnaissance", "reviews": "Avis", "journal": "Journal &amp; Récits",
        "team": "Équipe éditoriale", "faq": "FAQ",
        "hours": "Mar – Sam · 19h00–22h30<br>Fermé dim. &amp; lun.",
        "rights": "Tout le contenu © Dar Mansour — 2026. Aucun tracking, aucune pub — juste de la cuisine &amp; de l'âme.",
    },
}


def footer(lang="en"):
    t = _FOOTER_T[lang]
    return f'''
<footer class="footer" id="contact">
  <div class="wrap">
    <div class="footer__grid">
      <div class="footer__brand">
        <img class="footer__logo" src="assets/logo/dar-mansour-logo-white.png" alt="Dar Mansour - Morocco's Kitchen" width="1622" height="876">
        <p class="footer__brand-sub">Koh Phangan · Thailand</p>
        <p>{t["tagline"]}</p>
      </div>
      <div>
        <h3>{t["explore"]}</h3>
        <ul>
          <li><a href="index.html">{t["experience"]}</a></li>
          <li><a href="moroccan-slow-dining-koh-phangan.html">{t["concept"]}</a></li>
          <li><a href="moroccan-menu-koh-phangan.html">{t["menu"]}</a></li>
          <li><a href="moroccan-wine-pairing-koh-phangan.html">{t["wine"]}</a></li>
          <li><a href="moroccan-cocktails-koh-phangan.html">{t["bar"]}</a></li>
          <li><a href="private-dining-koh-phangan.html">{t["private"]}</a></li>
        </ul>
      </div>
      <div>
        <h3>{t["discover"]}</h3>
        <ul>
          <li><a href="dar-mansour-founders-vision.html">{t["founders"]}</a></li>
          <li><a href="moroccan-interior-art-koh-phangan.html">{t["art"]}</a></li>
          <li><a href="moroccan-pantry-koh-phangan.html">{t["pantry"]}</a></li>
          <li><a href="moroccan-hospitality-values-koh-phangan.html">{t["spirit"]}</a></li>
          <li><a href="best-moroccan-restaurant-world-press.html">{t["recognition"]}</a></li>
          <li><a href="moroccan-restaurant-reviews-koh-phangan.html">{t["reviews"]}</a></li>
          <li><a href="blog.html">{t["journal"]}</a></li>
          <li><a href="authors/">{t["team"]}</a></li>
          <li><a href="faq.html">{t["faq"]}</a></li>
        </ul>
      </div>
      <div>
        <h3>{t["visit"]}</h3>
        <address>
          <p><a href="https://share.google/Rp8YllnPe9Z9E9Va0" target="_blank" rel="noopener">Hin Kong Road, Sri Thanu area<br>Koh Phangan 84280, Thailand</a></p>
          <p>{t["hours"]}</p>
          <p><a href="{WA}" target="_blank" rel="noopener">WhatsApp · +66 82 276 7757</a></p>
          <p><a href="mailto:hello@darmansour.com">hello@darmansour.com</a></p>
        </address>
      </div>
    </div>
    <div class="footer__bottom">
      <span>{t["rights"]}</span>
      <div class="footer__social">
        <a href="https://instagram.com/darmansour.kohphangan" target="_blank" rel="noopener">Instagram</a>
        <a href="https://www.facebook.com/p/Dar-Mansour-Koh-Phangan-61574622040198/" target="_blank" rel="noopener">Facebook</a>
        <a href="https://share.google/Rp8YllnPe9Z9E9Va0" target="_blank" rel="noopener">Google Maps</a>
        <a href="https://open.spotify.com/playlist/5A0Qw5uEZiCyLNweh4nQ76" target="_blank" rel="noopener">Spotify</a>
      </div>
    </div>
  </div>
</footer>
<a class="wa-float" href="{WA}" target="_blank" rel="noopener" aria-label="Book via WhatsApp">{WA_ICON}</a>
<script src="assets/js/main.js?v={JS_V}"></script>
</body>
</html>'''


def _fr_localize(html):
    """Rewrite relative asset/page URLs to work from the /fr/ sub-directory.
    Page slugs that have a French version get the /fr/ prefix; others stay English."""
    def repl(m):
        attr, u = m.group(1), m.group(2)
        if u.startswith(_ROOT_SKIP):
            return f'{attr}="{u}"'
        if u.startswith("assets/"):
            return f'{attr}="/{u}"'
        base = u.split("#")[0].split("?")[0]
        if base in FR_PAGES:
            return f'{attr}="/fr/{u}"'
        return f'{attr}="/{u}"'
    html = _re.sub(r'\b(href|src)="([^"]*)"', repl, html)
    html = _re.sub(r'url\(&quot;([^&)]*)&quot;\)',
                   lambda m: (m.group(0) if m.group(1).startswith(_ROOT_SKIP)
                              else f'url(&quot;/{m.group(1)}&quot;)'), html)
    return html


def page(title, desc, canonical, body, og_image="assets/img/moroccan-garden-dining-koh-phangan.jpg",
         extra_head="", body_class="", lang="en", alt_url="", en_url=None, fr_url=None):
    hl = hreflang_links(en_url, fr_url) if (fr_url is not None and en_url is not None) else ""
    html = (head(title, desc, canonical, og_image, extra_head, body_class, lang, hl)
            + header(lang, alt_url) + "\n<main id=\"top\">\n" + body + "\n</main>\n" + footer(lang))
    if lang == "fr":
        html = _fr_localize(html)
    return html


def redirect_page(target, title="Dar Mansour"):
    """Minimal client-side redirect stub for a URL that has moved. Points its
    canonical at the new URL and links to it (so bots follow), stays out of the
    sitemap logic by carrying noindex."""
    url = f"{SITE_URL}/{target}"
    return (f'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">'
            f'<title>{title}</title><meta name="robots" content="noindex,follow">'
            f'<link rel="canonical" href="{url}">'
            f'<meta http-equiv="refresh" content="0; url={url}">'
            f'</head><body><p>This page has moved to '
            f'<a href="{url}">{url}</a>.</p></body></html>')
