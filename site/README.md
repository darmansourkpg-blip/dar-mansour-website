# Dar Mansour — Official Website

Contemporary Moroccan *Art de Vivre* — a boutique slow food restaurant in Koh Phangan.
Static site (HTML / CSS / vanilla JS), no build step, no dependencies.

## Preview locally
```bash
cd site
python3 -m http.server 8899
# open http://localhost:8899/
```

## Design system
- **Colour**: brand green `#00837D` + warm neutrals (bone `#FBF8F1`, sand `#F3ECDF`), deep forest `#0B403C`. Green only (no bordeaux), per brief.
- **Type**: Cormorant Garamond (editorial display serif) + Mulish (humanist sans, close to the brand's Espuma Pro).
- **Brand elements**: Moroccan arch (logo), ◇◇◇ diamond divider.

## Structure
```
site/
├── *.html                # 15 generated pages (do NOT edit by hand — see build/)
├── build/                # Static generator — edit here, then re-run
│   ├── build.py          # Assembles every page; run: python3 build/build.py
│   ├── _layout.py        # Shared head / header / footer / helpers (partials)
│   ├── _menu.py          # Full menu data + renderer
│   └── _drinks.py        # Wine list + cocktail list data + renderers
├── assets/
│   ├── css/style.css     # Full design system + components
│   ├── js/main.js        # Header, mobile nav, scroll reveal
│   ├── img/              # SEO-named photography
│   ├── logo/             # Brand logos
│   └── video/            # Ambience clips (available for future use)
```

## Editing / rebuilding
Pages are generated. **Edit content in `build/` then run `python3 build/build.py`** from `site/`.
Header, footer and navigation live once in `build/_layout.py`.

## Pages (all from the verbatim content brief)
Home · Concept · Menu · Reservation · Wine Pairing · Mansour Bar · Artistic Direction ·
Recognition · Reviews · Moroccan Pantry · Mansour Spirit · Founders · Private Dining · FAQ · Contact.
The full menu (tajines, tanjia, couscous, chiiwats, m'semen, sides, tea) is integrated from `Menu Dar Mansour.pdf`.

## Content & facts (verbatim from brief)
- Reservation only · pre-order before 2 pm via WhatsApp · max 40 guests/night
- WhatsApp: +66 82 276 7757 · hello@darmansour.com
- Hin Kong Road, Sri Thanu area, Koh Phangan · Tue–Sat 7:00–10:30 PM (closed Sun & Mon)
- Instagram @darmansour.kohphangan

## To do next
- Full menu (client to provide) → dedicated Menu page
- Remaining pages: Concept, Reservation, Wine Pairing, Bar, Artistic Direction, Recognition, Reviews, Pantry, Mansour Spirit, Founders, Private Dining, FAQ, Contact
- Convert images to WebP + generate favicons
- Deploy (Netlify / Vercel)
