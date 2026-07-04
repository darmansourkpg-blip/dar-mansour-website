# -*- coding: utf-8 -*-
"""Shared layout: head, header, footer, small helpers. Static-site partials.

Bilingual (EN / FR). The English site lives at the root; the French twin lives
under /fr/. Three module globals drive the current build pass:
  LANG      "en" or "fr"      — set before generating each language's pages
  BASE      "" or "../"       — relative prefix to reach /assets from that depth
  FR_READY  set of filenames  — pages that already have a French version
Untranslated links fall back to English via loc(), so /fr/ never 404s while the
translation is rolled out page by page.
"""

import hashlib
import os

SITE_URL = "https://darmansour.com"

# Pre-launch switch: while True, every page carries a noindex meta and the
# sitemap is not advertised, so search engines keep the site out of results.
# Flip to False (and rebuild) to open the site for indexing at launch.
NOINDEX = False
WA = "https://wa.me/66822767757"

# ---- language state (mutated by build.py before each pass) ----
LANG = "en"
BASE = ""
FR_READY = set()  # filenames (e.g. "index.html") that have a French twin


def _t(en, fr):
    """Pick the string for the current build language."""
    return fr if LANG == "fr" else en


def loc(href):
    """Resolve an internal page link for the current language.
    In French, link to the /fr/ twin when it exists, else fall back to the
    English page one level up. External / asset / anchor links pass through."""
    if LANG != "fr":
        return href
    if href.startswith(("http://", "https://", "mailto:", "tel:", "#", "../")):
        return href
    return href if href in FR_READY else "../" + href


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


def _img(path):
    """Root-relative asset path for the current depth (adds BASE for /fr/)."""
    return BASE + _webp(path)


WA_ICON = ('<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15l-1.3 4.7 '
           '4.8-1.3A10 10 0 1 0 12 2Zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.6-3.9-4.7-4.1-.1-.2-1.1-1.5-1.1-2.8 '
           '0-1.3.7-2 .9-2.2.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5.2.5.7 1.8.8 1.9.1.1.1.3 0 .5-.3.5-.5.7-.7 1-.2.2-.3.4-.1.7.2.3.9 1.5 '
           '2 2.4 1.4 1.2 2.5 1.5 2.8 1.7.3.1.5.1.6-.1.2-.2.7-.9.9-1.2.2-.3.4-.2.6-.1.3.1 1.6.8 1.9.9.3.2.5.2.5.3.1.2.1.7-.1 1.3Z"/></svg>')

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'


def _nav_items():
    return [
        ("index.html", _t("Experience", "Expérience")),
        ("moroccan-menu-koh-phangan.html", _t("Menu", "Carte")),
        ("moroccan-wine-pairing-koh-phangan.html", _t("Wine", "Vins")),
        ("private-dining-koh-phangan.html", _t("Private Dining", "Privatisation")),
        ("moroccan-restaurant-reviews-koh-phangan.html", _t("Reviews", "Avis")),
        ("contact-dar-mansour-koh-phangan.html", _t("Contact", "Contact")),
    ]


def head(title, desc, canonical, og_image="assets/img/moroccan-garden-dining-koh-phangan.jpg", extra=""):
    prefix = "fr/" if LANG == "fr" else ""
    page_id = canonical or "index.html"
    canon_url = f"{SITE_URL}/{prefix}{canonical}"
    alts = ""
    if page_id in FR_READY:
        alts = (f'\n<link rel="alternate" hreflang="en" href="{SITE_URL}/{canonical}">'
                f'\n<link rel="alternate" hreflang="fr" href="{SITE_URL}/fr/{canonical}">'
                f'\n<link rel="alternate" hreflang="x-default" href="{SITE_URL}/{canonical}">')
    return f'''<!DOCTYPE html>
<html lang="{LANG}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
{'<meta name="robots" content="noindex, nofollow">' if NOINDEX else ''}
<link rel="canonical" href="{canon_url}">{alts}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Dar Mansour — Morocco's Kitchen">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE_URL}/{og_image}">
<meta property="og:url" content="{canon_url}">
<meta property="og:locale" content="{'fr_FR' if LANG == 'fr' else 'en_US'}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{BASE}assets/logo/dar-mansour-icon.png">
<link rel="apple-touch-icon" href="{BASE}assets/logo/dar-mansour-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Mulish:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{BASE}assets/css/style.css?v={CSS_V}">
{extra}
</head>
<body>'''


def _mega_groups():
    return [
        (_t("The Restaurant", "Le Restaurant"), [
            ("index.html", _t("The Experience", "L'Expérience")),
            ("moroccan-slow-dining-koh-phangan.html", _t("Concept &amp; Slow Dining", "Concept &amp; Slow Food")),
            ("dar-mansour-founders-vision.html", _t("Founders &amp; Vision", "Fondateurs &amp; Vision")),
            ("moroccan-interior-art-koh-phangan.html", _t("Artistic Direction", "Direction Artistique")),
            ("moroccan-hospitality-values-koh-phangan.html", _t("The Mansour Spirit", "L'Esprit Mansour")),
            ("blog.html", _t("Journal &amp; Stories", "Journal &amp; Récits")),
        ]),
        (_t("Food &amp; Drink", "Table &amp; Cave"), [
            ("moroccan-menu-koh-phangan.html", _t("Our Moroccan Menu", "Notre Carte Marocaine")),
            ("moroccan-wine-pairing-koh-phangan.html", _t("Wine Pairing", "Accords Mets &amp; Vins")),
            ("moroccan-cocktails-koh-phangan.html", _t("The Mansour Bar", "Le Mansour Bar")),
            ("moroccan-pantry-koh-phangan.html", _t("Moroccan Pantry", "Le Garde-Manger Marocain")),
        ]),
        (_t("Visit &amp; Book", "Visite &amp; Réservation"), [
            ("moroccan-restaurant-reservation-koh-phangan.html", _t("Reservation &amp; Pre-order", "Réservation &amp; Précommande")),
            ("private-dining-koh-phangan.html", _t("Private Dining", "Privatisation")),
            ("moroccan-restaurant-reviews-koh-phangan.html", _t("Reviews", "Avis")),
            ("best-moroccan-restaurant-world-press.html", _t("Recognition", "Reconnaissance")),
            ("faq.html", _t("FAQ", "FAQ")),
            ("contact-dar-mansour-koh-phangan.html", _t("Contact &amp; Location", "Contact &amp; Accès")),
        ]),
    ]


def _langswitch(page_id):
    """EN / FR toggle. Links to the twin page, falling back to the home page of
    the other language when the exact twin doesn't exist yet."""
    if LANG == "fr":
        en_href = f"../{page_id}"
        return (f'<div class="langswitch" aria-label="Language">'
                f'<a href="{en_href}" hreflang="en">EN</a>'
                f'<span aria-hidden="true">·</span>'
                f'<span class="is-active" aria-current="true">FR</span></div>')
    fr_href = f"fr/{page_id}" if page_id in FR_READY else "fr/"
    return (f'<div class="langswitch" aria-label="Langue">'
            f'<span class="is-active" aria-current="true">EN</span>'
            f'<span aria-hidden="true">·</span>'
            f'<a href="{fr_href}" hreflang="fr">FR</a></div>')


def header(canonical=""):
    page_id = canonical or "index.html"
    nav = "\n      ".join(f'<a href="{loc(href)}">{label}</a>' for href, label in _nav_items())
    groups = ""
    for title, links in _mega_groups():
        items = "".join(f'<li><a href="{loc(href)}">{label}</a></li>' for href, label in links)
        groups += f'<div class="mega__group"><h4>{title}</h4><ul>{items}</ul></div>'
    return f'''
<header class="header" id="header">
  <div class="wrap header__inner">
    <a class="brand" href="{loc('index.html')}" aria-label="Dar Mansour — Morocco's Kitchen, home">
      <img class="brand__full brand__full--white" src="{BASE}assets/logo/dar-mansour-logo-white.png" alt="Dar Mansour — Morocco's Kitchen" width="1622" height="876">
      <img class="brand__full brand__full--color" src="{BASE}assets/logo/dar-mansour-logo-green.png" alt="" aria-hidden="true" width="1622" height="876">
    </a>
    <nav class="nav" aria-label="Primary">
      {nav}
    </nav>
    <div class="header__cta">
      {_langswitch(page_id)}
      <a class="btn btn--light" href="{WA}" target="_blank" rel="noopener">{_t("Book", "Réserver")}</a>
      <button class="menu-toggle" id="menuToggle" aria-label="{_t("Open full menu", "Ouvrir le menu")}" aria-expanded="false" aria-controls="mega">
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
        <span class="eyebrow">{_t("Reservations", "Réservations")}</span>
        <p><a href="{WA}" target="_blank" rel="noopener">WhatsApp · +66 82 276 7757</a><br>
        <a href="mailto:hello@darmansour.com">hello@darmansour.com</a></p>
      </div>
      <div>
        <span class="eyebrow">{_t("Find us", "Nous trouver")}</span>
        <p>Hin Kong Road, Sri Thanu area<br>Koh Phangan, {_t("Thailand", "Thaïlande")}<br>{_t("Tue–Sat · 7:00–10:30 PM", "Mar–Sam · 19h–22h30")}</p>
      </div>
      <a class="btn btn--primary" href="{WA}" target="_blank" rel="noopener">{WA_ICON} {_t("Book via WhatsApp", "Réserver via WhatsApp")}</a>
    </div>
  </div>
</div>'''


def breadcrumb(*crumbs):
    """crumbs: list of (label, href) ; last one is current (href None)."""
    items = [f'<li><a href="{loc("index.html")}">{_t("Home", "Accueil")}</a></li>']
    for label, href in crumbs:
        items.append('<li class="sep" aria-hidden="true">›</li>')
        if href:
            items.append(f'<li><a href="{loc(href)}">{label}</a></li>')
        else:
            items.append(f'<li aria-current="page">{label}</li>')
    return ('<nav class="wrap breadcrumb" aria-label="Breadcrumb"><ol>'
            + "".join(items) + '</ol></nav>')


def subhero(eyebrow, h1, sub, image, alt, tall=False):
    cls = "subhero subhero--tall" if tall else "subhero"
    return f'''
<section class="{cls}">
  <div class="subhero__media"><img src="{_img(image)}" alt="{alt}" fetchpriority="high"></div>
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
    <span class="eyebrow">{_t("Reservation &amp; Pre-order", "Réservation &amp; Précommande")}</span>
    <h2>{title}</h2>
    <p class="lead">{text}</p>
    <div class="book__actions">
      <a class="btn btn--primary" href="{WA}" target="_blank" rel="noopener">{WA_ICON} {_t("Book &amp; Pre-order via WhatsApp", "Réserver &amp; précommander via WhatsApp")}</a>
      <a class="btn btn--ghost" href="https://share.google/Rp8YllnPe9Z9E9Va0" target="_blank" rel="noopener">{_t("Get Directions", "Itinéraire")}</a>
    </div>
    <p class="book__meta">{_t("Dinner only · Tuesday to Saturday · 7:00 PM – 10:30 PM · Closed Sunday &amp; Monday", "Dîner uniquement · du mardi au samedi · 19h–22h30 · Fermé dimanche &amp; lundi")}</p>
  </div>
</section>'''


def related(*cards):
    """cards: (eyebrow, title, href, image, alt)"""
    inner = "".join(
        f'''<a class="related__card reveal" href="{loc(href)}">
          <img src="{_img(img)}" alt="{alt}" loading="lazy">
          <div><span>{eyebrow}</span><h3>{title}</h3></div>
        </a>''' for eyebrow, title, href, img, alt in cards)
    return f'''
<section class="section" style="padding-top:0;">
  <div class="wrap">
    <div class="center reveal" style="margin-bottom:2.2rem;"><div class="divider"><span>◇◇◇</span></div>
    <h2 style="margin-top:1.3rem;">{_t("Continue the journey", "Poursuivez le voyage")}</h2></div>
    <div class="related">{inner}</div>
  </div>
</section>'''


def _footer_cols():
    return [
        (_t("Explore", "Explorer"), [
            ("index.html", _t("The Experience", "L'Expérience")),
            ("moroccan-slow-dining-koh-phangan.html", _t("Concept", "Concept")),
            ("moroccan-menu-koh-phangan.html", _t("Menu", "La Carte")),
            ("moroccan-wine-pairing-koh-phangan.html", _t("Wine Pairing", "Accords Mets &amp; Vins")),
            ("moroccan-cocktails-koh-phangan.html", _t("The Mansour Bar", "Le Mansour Bar")),
            ("private-dining-koh-phangan.html", _t("Private Dining", "Privatisation")),
        ]),
        (_t("Discover", "Découvrir"), [
            ("dar-mansour-founders-vision.html", _t("Founders &amp; Vision", "Fondateurs &amp; Vision")),
            ("moroccan-interior-art-koh-phangan.html", _t("Artistic Direction", "Direction Artistique")),
            ("moroccan-pantry-koh-phangan.html", _t("Moroccan Pantry", "Garde-Manger Marocain")),
            ("moroccan-hospitality-values-koh-phangan.html", _t("Mansour Spirit", "Esprit Mansour")),
            ("best-moroccan-restaurant-world-press.html", _t("Recognition", "Reconnaissance")),
            ("moroccan-restaurant-reviews-koh-phangan.html", _t("Reviews", "Avis")),
            ("blog.html", _t("Journal &amp; Stories", "Journal &amp; Récits")),
            ("faq.html", _t("FAQ", "FAQ")),
        ]),
    ]


def footer():
    cols = ""
    for heading, links in _footer_cols():
        lis = "".join(f'<li><a href="{loc(href)}">{label}</a></li>' for href, label in links)
        cols += f'<div><h4>{heading}</h4><ul>{lis}</ul></div>'
    return f'''
<footer class="footer" id="contact">
  <div class="wrap">
    <div class="footer__grid">
      <div class="footer__brand">
        <img class="footer__logo" src="{BASE}assets/logo/dar-mansour-logo-white.png" alt="Dar Mansour — Morocco's Kitchen" width="1622" height="876">
        <p class="footer__brand-sub">Koh Phangan · {_t("Thailand", "Thaïlande")}</p>
        <p>{_t("A soulful Moroccan slow food sanctuary on the west coast of Koh Phangan. Rooted in tradition, slow cooked with care.", "Un sanctuaire de slow food marocain, plein d'âme, sur la côte ouest de Koh Phangan. Enraciné dans la tradition, cuisiné lentement avec soin.")}</p>
      </div>
      {cols}
      <div>
        <h4>{_t("Visit &amp; Contact", "Visite &amp; Contact")}</h4>
        <address>
          <p><a href="https://share.google/Rp8YllnPe9Z9E9Va0" target="_blank" rel="noopener">Hin Kong Road, Sri Thanu area<br>Koh Phangan, {_t("Thailand", "Thaïlande")}</a></p>
          <p>{_t("Tue – Sat · 7:00–10:30 PM<br>Closed Sun &amp; Mon", "Mar – Sam · 19h–22h30<br>Fermé dim. &amp; lun.")}</p>
          <p><a href="{WA}" target="_blank" rel="noopener">WhatsApp · +66 82 276 7757</a></p>
          <p><a href="mailto:hello@darmansour.com">hello@darmansour.com</a></p>
        </address>
      </div>
    </div>
    <div class="footer__bottom">
      <span>{_t("All content © Dar Mansour — 2025. No tracking, no ads — just food &amp; soul.", "Tout le contenu © Dar Mansour — 2025. Sans pistage, sans publicité — juste de la cuisine &amp; de l'âme.")}</span>
      <div class="footer__social">
        <a href="https://instagram.com/darmansour.kohphangan" target="_blank" rel="noopener">Instagram</a>
        <a href="https://www.facebook.com/people/Dar-Mansour/" target="_blank" rel="noopener">Facebook</a>
        <a href="https://share.google/Rp8YllnPe9Z9E9Va0" target="_blank" rel="noopener">Google Maps</a>
      </div>
    </div>
  </div>
</footer>
<a class="wa-float" href="{WA}" target="_blank" rel="noopener" aria-label="{_t("Book via WhatsApp", "Réserver via WhatsApp")}">{WA_ICON}</a>
<script src="{BASE}assets/js/main.js?v={JS_V}"></script>
</body>
</html>'''


def page(title, desc, canonical, body, og_image="assets/img/moroccan-garden-dining-koh-phangan.jpg", extra_head=""):
    return head(title, desc, canonical, og_image, extra_head) + header(canonical) + "\n<main id=\"top\">\n" + body + "\n</main>\n" + footer()
