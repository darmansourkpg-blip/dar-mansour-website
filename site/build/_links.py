# -*- coding: utf-8 -*-
"""Standalone 'link in bio' page for Instagram/Facebook — darmansour.com/links.

A single, mobile-first, tap-friendly page in the Dar Mansour world (brand green,
warm neutrals, a zellige star motif and a lantern divider). Deliberately NOT
wrapped in the site header/footer: visitors arrive from a social bio and want
big buttons, nothing else. Rendered as a self-contained file (its own <style>),
kept out of the sitemap and set to noindex so it doesn't compete with the home
page on brand queries.
"""
import datetime
import _layout as L

WA = L.WA  # https://wa.me/66822767757

# Real, verified destinations (see JSON-LD on the home page).
GMAPS_DIR = "https://www.google.com/maps/dir/?api=1&destination=9.753335,99.968729"
GMAPS_PLACE = "https://share.google/Rp8YllnPe9Z9E9Va0"
INSTAGRAM = "https://instagram.com/darmansour.kohphangan"
FACEBOOK = "https://www.facebook.com/people/Dar-Mansour/"

# Small inline icons (currentColor, 24x24 viewBox).
IC = {
    "whatsapp": '<path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2Zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.6-3.9-4.7-4.1-.1-.2-1.1-1.5-1.1-2.8 0-1.3.7-2 .9-2.2.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5.2.5.7 1.8.8 1.9.1.1.1.3 0 .5-.3.5-.5.7-.7 1-.2.2-.3.4-.1.7.2.3.9 1.5 2 2.4 1.4 1.2 2.5 1.5 2.8 1.7.3.1.5.1.6-.1.2-.2.7-.9.9-1.2.2-.3.4-.2.6-.1.3.1 1.6.8 1.9.9.3.2.5.2.5.3.1.2.1.7-.1 1.3Z"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.5 2.5 15 0 18M12 3c-2.5 2.5-2.5 15 0 18"/>',
    "menu": '<path d="M4 5h16M4 12h16M4 19h10"/>',
    "wine": '<path d="M8 3h8l-.6 6a3.4 3.4 0 0 1-6.8 0L8 3ZM12 15v5M8 21h8"/>',
    "cocktail": '<path d="M4 4h16l-8 8-8-8ZM12 12v7M8 21h8M14 7l4-4"/>',
    "pin": '<path d="M12 21s7-6.3 7-11a7 7 0 1 0-14 0c0 4.7 7 11 7 11Z"/><circle cx="12" cy="10" r="2.5"/>',
    "star": '<path d="M12 3.5l2.6 5.3 5.9.9-4.3 4.1 1 5.8-5.2-2.7-5.2 2.7 1-5.8L4.5 9.7l5.9-.9L12 3.5Z"/>',
    "instagram": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r="1.2" fill="currentColor" stroke="none"/>',
    "facebook": '<path d="M14 8.5V7c0-.8.5-1 1-1h1.5V3H14c-2.2 0-3.5 1.4-3.5 3.6V8.5H8V12h2.5v9H14v-9h2.4l.5-3.5H14Z" fill="currentColor" stroke="none"/>',
}


def _icon(name, filled=False):
    fill = "none" if not filled else "currentColor"
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true">{IC[name]}</svg>')


def _btn(href, label, icon, primary=False, note=None, external=True):
    cls = "lk__btn lk__btn--primary" if primary else "lk__btn"
    rel = ' target="_blank" rel="noopener"' if external else ""
    sub = f'<span class="lk__note">{note}</span>' if note else ""
    return (f'<a class="{cls}" href="{href}"{rel}>'
            f'<span class="lk__ic">{_icon(icon, filled=primary)}</span>'
            f'<span class="lk__lbl">{label}{sub}</span></a>')


# An 8-point Moroccan zellige star (khatam) used as a small brand ornament.
ZELLIGE_STAR = (
    '<svg class="lk__star" viewBox="0 0 100 100" aria-hidden="true">'
    '<path fill="currentColor" d="M50 2 61 24 85 15 76 39 98 50 76 61 85 85 '
    '61 76 50 98 39 76 15 85 24 61 2 50 24 39 15 15 39 24 50 2Z"/></svg>')

# A simple hanging lantern divider.
LANTERN = (
    '<svg class="lk__lantern" viewBox="0 0 40 64" aria-hidden="true" '
    'fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round">'
    '<path d="M20 2v6"/><path d="M13 10h14"/><path d="M20 56v6"/>'
    '<path d="M14 10c-3 3-4 7-4 13s1 10 4 13h12c3-3 4-7 4-13s-1-10-4-13"/>'
    '<path d="M14 36h12"/><path d="M20 14v28"/><path d="M15 22h10M15 30h10"/></svg>')


def render():
    year = datetime.date.today().year
    buttons = "\n".join([
        _btn(WA, "Reserve a Table", "whatsapp", primary=True, note="via WhatsApp"),
        _btn("https://darmansour.com/", "Official Website", "globe", external=False),
        _btn("moroccan-menu-koh-phangan.html", "View Our Menu", "menu", external=False),
        _btn("moroccan-wine-pairing-koh-phangan.html", "Wine Pairing List", "wine", external=False),
        _btn("moroccan-cocktails-koh-phangan.html", "Cocktail Menu", "cocktail", external=False),
        _btn(GMAPS_DIR, "Get Directions", "pin", note="Google Maps"),
        _btn(GMAPS_PLACE, "Reviews", "star"),
        _btn(INSTAGRAM, "Instagram", "instagram"),
        _btn(FACEBOOK, "Facebook", "facebook"),
    ])

    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dar Mansour — Morocco's Kitchen · Links</title>
<meta name="description" content="Reserve a table, explore the menu, get directions and follow Dar Mansour — Moroccan slow food in Koh Phangan.">
<meta name="robots" content="noindex, follow">
<link rel="canonical" href="https://darmansour.com/links">
<link rel="icon" href="assets/logo/dar-mansour-icon.png">
<meta property="og:title" content="Dar Mansour — Morocco's Kitchen">
<meta property="og:description" content="Reserve a table, explore the menu, get directions and follow Dar Mansour — Moroccan slow food in Koh Phangan.">
<meta property="og:image" content="https://darmansour.com/assets/img/moroccan-garden-dining-koh-phangan.jpg">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Mulish:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
  :root{{
    --green:#00837D; --green-deep:#0B403C; --green-darker:#072B29;
    --bone:#FBF8F1; --sand:#F3ECDF; --linen:#EFE7D8; --cream:#FDFBF6;
    --ink:#23302E; --ink-soft:#4C5A57; --line:rgba(11,64,60,.14);
    --serif:'Cormorant Garamond',Georgia,serif; --sans:'Mulish',-apple-system,sans-serif;
    --ease:cubic-bezier(.22,.61,.36,1);
  }}
  *,*::before,*::after{{box-sizing:border-box;margin:0}}
  body{{
    font-family:var(--sans); color:var(--ink); line-height:1.6;
    background:var(--green-deep);
    -webkit-font-smoothing:antialiased; min-height:100vh;
  }}
  a{{color:inherit;text-decoration:none}}
  img{{display:block;max-width:100%;height:auto}}

  /* Deep green ground with a faint zellige star lattice */
  .lk{{
    position:relative; min-height:100vh; overflow:hidden;
    padding:clamp(2.2rem,7vw,3.6rem) 1.25rem clamp(2rem,6vw,3rem);
    display:flex; flex-direction:column; align-items:center;
    background:
      radial-gradient(120% 60% at 50% -10%, rgba(0,131,125,.35), transparent 60%),
      var(--green-deep);
  }}
  .lk__pattern{{
    position:absolute; inset:0; z-index:0; pointer-events:none;
    color:#ffffff; opacity:.05;
    background-image:
      radial-gradient(circle at 25% 25%, currentColor 1.4px, transparent 1.6px),
      radial-gradient(circle at 75% 75%, currentColor 1.4px, transparent 1.6px);
    background-size:38px 38px;
  }}
  /* Card */
  .lk__card{{
    position:relative; z-index:1; width:100%; max-width:440px;
    background:var(--bone); border-radius:20px;
    padding:clamp(1.6rem,5vw,2.4rem) clamp(1.2rem,5vw,2rem) clamp(1.6rem,5vw,2rem);
    box-shadow:0 30px 70px -30px rgba(0,0,0,.6);
    border:1px solid rgba(255,255,255,.6);
    text-align:center;
  }}
  .lk__logo{{height:64px;width:auto;margin:0 auto .9rem}}
  .lk__star{{width:26px;height:26px;color:var(--green);margin:0 auto .5rem;display:block}}
  .lk__eyebrow{{
    font-size:.66rem;font-weight:800;letter-spacing:.28em;text-transform:uppercase;
    color:var(--green);
  }}
  .lk__name{{
    font-family:var(--serif); font-weight:600; color:var(--green-deep);
    font-size:clamp(1.7rem,6.5vw,2.15rem); line-height:1.06; margin:.35rem 0 .15rem;
  }}
  .lk__sub{{font-size:.8rem;color:var(--ink-soft);letter-spacing:.02em}}
  .lk__lantern{{width:24px;height:38px;color:var(--green);opacity:.55;margin:.9rem auto .2rem;display:block}}

  .lk__btns{{display:flex;flex-direction:column;gap:.7rem;margin-top:1.1rem}}
  .lk__btn{{
    display:flex; align-items:center; gap:.85rem; width:100%;
    padding:.95rem 1.15rem; border-radius:12px;
    background:var(--cream); border:1px solid var(--line);
    font-weight:700; font-size:.95rem; color:var(--green-deep);
    text-align:left; transition:transform .25s var(--ease),background .25s var(--ease),border-color .25s var(--ease),box-shadow .25s var(--ease);
  }}
  .lk__btn:hover,.lk__btn:focus-visible{{
    transform:translateY(-2px); background:#fff; border-color:var(--green);
    box-shadow:0 10px 24px -14px rgba(11,64,60,.5);
  }}
  .lk__btn--primary{{
    background:var(--green); color:#fff; border-color:var(--green);
    box-shadow:0 12px 26px -14px rgba(0,131,125,.9);
  }}
  .lk__btn--primary:hover,.lk__btn--primary:focus-visible{{
    background:var(--green-deep); border-color:var(--green-deep);
  }}
  .lk__ic{{flex:0 0 auto;display:grid;place-items:center;width:24px;height:24px}}
  .lk__ic svg{{width:22px;height:22px}}
  .lk__lbl{{display:flex;flex-direction:column;line-height:1.15}}
  .lk__note{{
    font-weight:600;font-size:.72rem;letter-spacing:.02em;opacity:.75;text-transform:none;
  }}
  .lk__btn--primary .lk__note{{opacity:.85}}

  .lk__foot{{
    position:relative; z-index:1; margin-top:1.4rem; text-align:center;
    color:rgba(244,239,228,.7); font-size:.72rem; letter-spacing:.04em;
  }}
  .lk__foot a{{color:rgba(244,239,228,.9);text-decoration:underline;text-underline-offset:2px}}
</style>
</head>
<body>
  <main class="lk">
    <div class="lk__pattern"></div>
    <div class="lk__card">
      <img class="lk__logo" src="assets/logo/dar-mansour-logo-green.png" alt="Dar Mansour — Morocco's Kitchen">
      {ZELLIGE_STAR}
      <p class="lk__eyebrow">Welcome to</p>
      <h1 class="lk__name">Dar Mansour<br>Morocco's Kitchen</h1>
      <p class="lk__sub">Moroccan slow food · Koh Phangan</p>
      {LANTERN}
      <nav class="lk__btns" aria-label="Dar Mansour links">
        {buttons}
      </nav>
    </div>
    <p class="lk__foot">Hin Kong · Sri Thanu, Koh Phangan · Dinner Tue–Sat<br>
      &copy; {year} Dar Mansour — <a href="https://darmansour.com/">darmansour.com</a></p>
  </main>
</body>
</html>
'''
