# Eden & Beyond — Creative Studio

Static site for **Eden & Beyond** (`edenandbeyond.studio`), a multidisciplinary
creative studio (hospitality / residential / furniture & objects / creative
direction). Same architecture as the Dar Mansour site: HTML/CSS/JS vanilla + a
small Python generator. **No framework, no build step beyond the generator.**

> This scaffold currently lives on a branch of the `dar-mansour-website` repo so
> we could reuse the proven architecture quickly. It is meant to move to its own
> repository (`edenandbeyond`) before deployment — Eden & Beyond and Dar Mansour
> are separate brands and should not share a git history / Pages deployment.

## Structure
```
eden-and-beyond/
├── build/                 # generator (EDIT HERE)
│   ├── build.py           # assembles all pages + sitemap/robots/llms
│   └── _layout.py         # head / header / footer / nav / section helpers
├── assets/                # css / js / img
└── *.html                 # 11 GENERATED pages — do not edit by hand
```

## Build
```bash
cd eden-and-beyond
python3 build/build.py
```

## Preview
```bash
cd eden-and-beyond
python3 -m http.server 8901
# open http://localhost:8901/
```

## Pages (11)
Home · About · Services · Projects · Journal · Contact
SEO landing pages: Hospitality Design · Restaurant Design · Residential Design ·
Furniture & Object Design · Creative Direction.

## Design system
- **Palette**: warm ivory (`--bone`) + charcoal ink (`--ink`) + a single
  terracotta accent (`--clay #B85C38`). Deliberately distinct from Dar Mansour's green.
- **Type**: Fraunces (display) + Inter (body/UI).
- **Hero**: "F*** the Box." (typographied, kept per client decision).

## Status / to-do
- [ ] **Founder bio (Maija)** on About — highest priority for trust / E-E-A-T (placeholder now).
- [ ] Real photography (heroes, project shots, portrait) — placeholders marked in-page show what goes where.
- [ ] Connect the contact form (Formspree / Web3Forms / Cloudflare Worker).
- [ ] Fill the SEO landing pages with deeper, geo-anchored copy (Thailand / Koh Phangan).
- [ ] Write real Journal articles (mirror Dar Mansour's `_journal.py` approach when ready).
- [ ] Add GA4 + Bing IDs in `_layout.py`, add favicons, then flip `NOINDEX = False` at launch.
- [ ] Add JSON-LD (Organization, Person/Maija, CreativeWork for Dar Mansour with `sameAs` → darmansour.com).

**Pre-launch switch**: `NOINDEX = True` in `_layout.py` (robots.txt disallows all,
noindex meta on every page). Flip to `False` and rebuild to open for indexing.
