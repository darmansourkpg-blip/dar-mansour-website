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

## Règles éditoriales du Journal (blog)
Référence complète : `ressources/Dar_Mansour_Editorial_Playbook` + `Dar_Mansour_Journal_Structure`.
Ceci en est la synthèse actionnable. Gabarits prêts à remplir : `ressources/journal-templates/`.

**Raison d'être** : le Journal inspire la curiosité et construit l'autorité (Koh Phangan +
Morocco). Un article doit rester utile **même si le restaurant n'existait pas**. SEO invisible :
la structure sert Google, l'écriture sert le lecteur.

**Voix** : un ami cultivé qui connaît l'île toute l'année et aime le Maroc. Chaleureux, informé,
jamais vendeur ni académique. Phrases courtes/moyennes, rythme varié, paragraphes de 1–3 phrases.
**Montrer, pas déclarer** : au lieu de « the tajine is delicious », écrire « the lamb is tender
enough to separate with a spoon, the sweetness of prunes balanced by toasted almonds ».

**Ne jamais inventer** : prix, horaires, plats, ingrédients, récompenses, citations, faits
historiques, ni fausse expérience à la première personne (« we tried… ») sauf visite réelle de
l'équipe. En cas de doute → vérifier ou l'écrire au conditionnel.

**Mots/tournures à bannir** (le linter du build les signale) : best ever, world-class, incredible,
amazing, breathtaking, unforgettable, hidden gem, must-visit, bucket list, culinary journey,
nestled in, vibrant/rich tapestry, foodies, paradise, game-changer, delve into, boasts, « whether
you're… », « it's not just X, it's Y », « a testament to », « seamlessly blends ».

**SEO par article** : 1 mot-clé principal + variations naturelles (pas de bourrage) · 1 intention
de recherche claire · `seo_title` ~50–60 car. · `description` ~145–160 car. · H2/H3 utiles et
naturels · **≥ 3 liens internes** (anchor text descriptif, jamais « click here ») · FAQ (5–8 vraies
questions, réponses 40–100 mots) sur les guides/piliers. La ligne « année » (…for 2026) seulement
sur les guides restaurants (fraîcheur), **pas** sur les articles culture (intemporels).

**Transparence Dar Mansour** : toujours divulguer que le guide est publié par le restaurant. DM
apparaît naturellement (Moroccan dining, Hin Kong, romantique, occasion, cocktails) mais **ne gagne
jamais toutes les catégories** et n'est pas premier partout. Une seule CTA douce par article.

**Pyramide de contenu** : ~10 % piliers (3 500–5 000 mots) · 40 % standard (1 200–2 000) ·
30 % quick reads (600–900) · 20 % stories (800–1 800). Priorité SEO des 3 premiers mois : contenu
Koh Phangan à forte intention de réservation (Best Restaurants, Romantic Dinner…) avant la culture.
**La qualité prime sur la cadence.**

**Structure standard** (garder seulement les sections utiles au sujet) : H1 → intro qui répond vite
→ How We Selected (si classement) → Quick Picks → sections « Best of » (H2) → chaque lieu en H3
(80–160 mots + Best for / What to order / Price / Location / Good to know) → Best by Experience →
Best by Area → Practical Tips → Final Thoughts → FAQ. Le bloc **« About the Journal » et le sommaire
« In this article » sont générés automatiquement** par `_journal.py` — ne pas les écrire à la main.

**Champs front matter** (voir `_journal.py` / gabarits) : `title`, `seo_title`, `description`,
`date`, `category` (`koh-phangan-guide` | `moroccan-culture` | `journal`), `cover`, `cover_alt`
(décrire la photo, pas de bourrage de mots-clés), `quick_guide` (liste label/value), `faq` (liste
question/answer), `about` (optionnel — sinon signature standard). Après édition :
`cd site && python3 build/build.py` — corriger les ⚠ avertissements éditoriaux affichés.
