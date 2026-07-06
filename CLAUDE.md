# Dar Mansour — Official Website

Contexte projet pour Claude Code (lu automatiquement au démarrage). **Note de passation** : ce
fichier remplace la mémoire locale du poste d'origine — tout le contexte utile est ici.

## Le projet
Site vitrine du restaurant **Dar Mansour — Morocco's Kitchen**, cuisine marocaine slow food à
Koh Phangan (Thaïlande). Positionnement **luxe éditorial** (références : Aman, Kinfolk, Hermès),
surtout **pas** un site de resto classique. Contenu en **anglais**.

## Décisions clés
- **Stack : site statique** (HTML/CSS/JS vanilla) — pas de WordPress, pas de framework, pas de build lourd.
- **Générateur maison** en Python dans `site/build/` : header/footer/nav définis **une seule fois**.
  → **Ne jamais éditer les `.html` à la racine de `site/`** (ils sont régénérés/écrasés).
  → Éditer dans `site/build/`, puis lancer : `cd site && python3 build/build.py`
- **Couleur : vert uniquement** — vert marque `#00837D` + neutres chauds (sable/os). Le bordeaux
  `#482C3D` de la charte n'est **pas** utilisé (choix du client).
- **Typo** : Cormorant Garamond (titres) + Mulish (corps) — proche de la police de marque « Espuma Pro ».

## Structure
```
dar_mansour/
├── CLAUDE.md                 # ce fichier
├── ressources/               # sources : PRD (6 vol.), contenu verbatim, FAQ, blog, charte, menu PDF, photos
└── site/                     # le site
    ├── *.html                # 16 pages GÉNÉRÉES — ne pas éditer à la main
    ├── build/                # générateur (à éditer)
    │   ├── build.py          # assemble toutes les pages
    │   ├── _layout.py        # head / header / footer / nav / helpers
    │   ├── _menu.py          # données + rendu du menu
    │   └── _drinks.py        # vins + cocktails
    └── assets/               # css/ js/ img/ logo/ video/
```

## Prévisualiser
```bash
cd site
python3 -m http.server 8899
# ouvrir http://localhost:8899/
```

## Mise en ligne (déjà en place)
- **Hébergement : GitHub Pages** — le site est **en ligne sur https://darmansour.com** (fichier
  `site/CNAME`, HTTPS automatique). Choix final : GitHub Pages (et **non** Netlify/Vercel).
- **Déploiement automatique** : à chaque push sur `main`, le workflow
  `.github/workflows/deploy-pages.yml` **régénère le site** (`python3 site/build/build.py`) puis
  publie le dossier `site/`. → Pour mettre une modif en ligne : la faire arriver sur `main`.
- **Après déploiement** : ping **IndexNow** automatique (Bing/Yandex re-crawlent en minutes).
- **Back-office articles (CMS)** : **Decap CMS** sur `/admin` (`site/admin/config.yml`). Le client
  écrit/publie ses articles depuis une interface web ; ça commite du Markdown dans
  `site/content/journal/` et le workflow le transforme en vraie page HTML SEO. Auth via un
  Cloudflare Worker (`dar-mansour-auth.darmansour-kpg.workers.dev`).
- **SEO branché** : GA4 `G-L2GLFDZHCR`, Bing Webmaster, `sitemap.xml`, `robots.txt`.

## Les 16 pages
Home (Experience) · Concept · Menu · Réservation · Wine Pairing · Mansour Bar · Artistic Direction ·
Recognition · Reviews · Moroccan Pantry · Mansour Spirit · Founders · Private Dining · FAQ · Contact · Journal (blog).

Nav : menu ☰ plein écran (toutes les pages, tous écrans) + nav rapide desktop + footer complet.
Chaque page finit par un CTA WhatsApp + un bloc « Continue the journey » (maillage interne).

## Infos établissement (verbatim — ne pas inventer)
- Réservation **vivement recommandée** (walk-ins bienvenus selon disponibilité) · pré-commande via WhatsApp **idéalement 5h à l'avance** · max 40 couverts/soir
- WhatsApp **+66 82 276 7757** · hello@darmansour.com · Instagram @darmansour.kohphangan
- Hin Kong Road (zone Sri Thanu), Koh Phangan, Thaïlande
- Dîner uniquement, mar–sam 19h–22h30 (fermé dim & lun) · Fondateurs : Maïja & Bruno

## ⚠️ Piège sur les images
Plusieurs fichiers de `ressources/Pix/` sont des **visuels marketing**, pas des photos brutes :
- `dar-mansour-groove-*` = **pochette d'album de musique** (à ne pas utiliser comme photo d'ambiance).
- Les photos de plats (tajines, couscous, pastilla…) sont des **posts Instagram** (cadre turquoise +
  nom + logo incrustés) : OK en **vignettes/cartes**, à éviter en **hero plein écran**.
- Photos « propres » utilisables partout : garden-dining, central-room, round-table, arty-table,
  entrance, front, street-view, maija-art-direction, interior-decor, pastries-mint-tea.
- **À demander au client** : des photos de plats en haute résolution, sans cadre ni texte.

## Reste à faire
- Intégrer de vraies photos de plats « propres » en haute résolution (sans cadre ni texte)
- Écrire de vrais articles de blog (via le CMS `/admin` ou en Markdown dans `site/content/journal/`)

_Déjà fait : mise en ligne (GitHub Pages sur darmansour.com), déploiement auto, favicons,
conversion WebP des heros._

## Règles de contenu
Contenu verbatim des docs dans `ressources/` — **ne jamais inventer** de plats, prix ou infos.
Améliorer seulement la hiérarchie, l'accessibilité, le SEO et la technique. Ton : chaleureux,
élégant, authentique, jamais « vendeur ».
