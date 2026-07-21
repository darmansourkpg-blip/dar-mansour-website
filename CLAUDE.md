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

## 📸 Règle images (OBLIGATOIRE)
Toute image ajoutée au site (couverture d'article, photo de fiche, visuel de page) **doit être optimisée et SEO** avant intégration :
- **Nom de fichier** : kebab-case descriptif avec mots-clés (ex. `aerial-view-hin-kong-beach-koh-phangan.webp`). Jamais d'espaces, de majuscules, de noms aléatoires (`IMG_1234`, hash CMS) ni de slash initial.
- **Format** : **WebP** de préférence — mais seulement s'il est **plus léger** que l'original (sinon garder JPG/PNG). Viser < ~200 Ko pour une couverture.
- **`alt` descriptif** (décrire la scène + lieu, sans bourrage de mots-clés) et **`cover_alt`** rempli dans le front matter.
- `width`/`height`, `loading="lazy"` et `fetchpriority` sont gérés automatiquement par le template `_journal.py` — ne pas les retirer.
→ Si le client uploade une image via le CMS avec un mauvais nom (espaces/hash), la **renommer** et convertir avant de la référencer.

**Checklist obligatoire avant de référencer une image (ne plus oublier) :**
1. **Nom de fichier** kebab-case, sans espace/majuscule/apostrophe/`%`. Renommer TOUS les fichiers frères (`.jpg` **et** `.webp`) et repointer chaque référence (`build.py`, `_menu.py`, `_drinks.py`, front matter). Vérifier ensuite `grep` = 0 référence à l'ancien nom.
2. **Poids** : couverture < ~200 Ko, autres visuels < ~250 Ko. Compresser (baisser la qualité, redimensionner si > 1700 px) avant commit.
3. **Sibling WebP** : générer un `.webp` à côté de chaque `.jpg/.png` visible (uploads/img) — le template ne sert le WebP que si le frère existe sur le disque.
4. **`alt` toujours rempli** (sauf image purement décorative en `aria-hidden`). Pour les **photos de plats/lieux**, suivre la **convention cross-média** (cohérence Wikimedia Commons / Google, renforce l'entité) :
   `Dar Mansour - Morocco's Kitchen <plat/scène>, Koh Phangan, Thailand`.
5. Les noms de **plats** dans le menu / wine pairing (`_menu.py`, `_drinks.py`) ne sont **pas** des noms de fichiers — ne pas les toucher lors d'un renommage d'image.

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
naturels · **≥ 3 liens internes sortants** (anchor text descriptif, jamais « click here ») · FAQ (5–8 vraies
questions, réponses 40–100 mots) sur les guides/piliers. La ligne « année » (…for 2026) seulement
sur les guides restaurants (fraîcheur), **pas** sur les articles culture (intemporels).
**Maillage entrant (OBLIGATOIRE)** : tout nouvel article doit recevoir **≥ 2 liens entrants** depuis
d'autres articles topiquement proches (idéalement 3+). Après création, **mettre à jour les anciens
articles** pour qu'ils pointent vers le nouveau (le maillage n'est jamais « forward-only »). Le build
le vérifie : `build.py` affiche `⚠ [slug] only X other article(s) link to it` s'il en manque —
corriger avant de publier.

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

**Pattern « by area » (OBLIGATOIRE — SEO local)** : la section géographique de chaque guide suit ce
schéma pour capter les recherches « [type] [village] » :
- **H2** = « Where to [Eat / Have Breakfast / Find Great Coffee / Eat Authentic Thai Food] Around Koh Phangan ».
- **H3 par zone** = « [Type] in [Zone] » → `Restaurants in Sri Thanu`, `Breakfast in Baan Tai`,
  `Cafés in Thong Sala`, `Thai Restaurants in Hin Kong`… (le mot-clé + le village dans le titre).
- Chaque H3 renvoie vers le guide de zone dédié quand il existe (maillage interne).
Ajouter « Authentic » aux H2/FAQ Thai (« authentic Thai food koh phangan » = requête à forte intention).
FAQ : privilégier des questions **localisées** (« best Thai restaurant in Sri Thanu », « breakfast in
Thong Sala ») — plus proches des vraies requêtes que des questions génériques.

**Champs front matter** (voir `_journal.py` / gabarits) : `title`, `seo_title`, `description`,
`date`, `category` (`koh-phangan-guide` | `moroccan-culture` | `journal`), `cover`, `cover_alt`
(décrire la photo, pas de bourrage de mots-clés), `quick_guide` (liste label/value), `faq` (liste
question/answer), `about` (optionnel — sinon signature standard). Après édition :
`cd site && python3 build/build.py` — corriger les ⚠ avertissements éditoriaux affichés.

## Optimisation GEO (moteurs IA) — RÈGLES VALIDÉES (à appliquer à toute parution)
Standards actés avec le client pour être **lu et cité** par les moteurs IA (ChatGPT, Perplexity,
Google AI Overviews, Claude) **et** garder un SEO Google sain. À respecter pour chaque nouvel
article et toute évolution du site.

**1. Lisibilité technique (déjà en place — ne pas casser)**
- **HTML pré-rendu, zéro dépendance JS pour le contenu** (site statique) — les LLMs ne rendent pas le JS.
- **URLs sémantiques** — ne pas renommer les URLs existantes (casse l'indexation).
- **`llms.txt`** à la racine : généré automatiquement par `build.py` (intro marque + pages clés + tous
  les articles). Se met à jour seul → ne pas éditer à la main.
- **`robots.txt`** accueille explicitement les crawlers IA (GPTBot, ClaudeBot, PerplexityBot,
  Google-Extended, CCBot, Applebot-Extended…) — généré par `build.py`.

**2. Answer-First (OBLIGATOIRE sur chaque guide)**
- Juste sous le titre (après le sous-titre), une **phrase-réponse directe** qui nomme les meilleurs
  choix par style/zone/occasion → citable par l'IA + éligible featured snippet Google.
- **Varier la formule** d'un article à l'autre (« Short answer », « In a hurry? », « Quick answer »,
  « Straight to it », « The quick version », « In short »…) — jamais le même boilerplate (Google
  pénalise les patterns identiques). Pour un article **culture**, préférer une phrase-**définition**.
- La `description` (meta) doit elle aussi contenir la réponse synthétique.

**3. Structure en fragments (chaque guide doit cocher les 4)**
- **H2/H3 explicites**, formulés comme des questions ou affirmations directes (« Where to Eat… »,
  « Why You Can Trust This Guide », « How to… »).
- **Listes** à puces **et** numérotées aux moments clés.
- **≥ 1 tableau comparatif** synthétisant plusieurs options (type « Quick Picks »). *(Exception :
  les articles culture/narratifs — ex. Les Dadas — n'en ont pas besoin.)*
- **FAQ** en fin d'article (5–8 questions, anticipe le Query Fan-Out) — ancre `#faq` + schéma
  FAQPage générés automatiquement, et la FAQ apparaît dans le sommaire « In this article ».

**4. Balisage Schema.org / JSON-LD (géré par `_journal.py` / `build.py`)**
- Types : `BlogPosting` (articles), `FAQPage`, `Restaurant` (home + contact), `Organization`, `Person`.
- **Fraîcheur** : `datePublished` + `dateModified`. `dateModified` = **date du dernier commit git**
  du fichier (repli : champ front matter `updated:`, puis date de publication). Ne pas remettre
  `dateModified = datePublished` en dur. Le workflow de déploiement doit garder `fetch-depth: 0`.
- **`sameAs`** (profils officiels) centralisé dans la constante **`SAME_AS`** (`_journal.py`) **et**
  dans le schéma Restaurant (`build.py`) — garder les deux **synchronisés**. Profils actuels :
  Instagram, Facebook, Google (fiche Maps), TripAdvisor, **Wikidata (`Q140585802`)**,
  **Crunchbase** (`/organization/dar-mansour-morocco-s-kitchen`) et **OpenStreetMap**
  (`node/14021567355`, relié en retour via le tag `brand:wikidata=Q140585802`), **Apple Maps**
  et **Bing Places** (URL stable `ss=ypid.YN8178x5570947916035674182` — jamais l'URL de recherche
  avec jeton de session, qui expire). Wikimedia Commons a 8 photos du restaurant sous ce même nom
  (dont une reliée en `image` P18 sur Wikidata) — pas de « profil » unique à ajouter au `sameAs`
  pour une galerie de fichiers, et **Pinterest** (`pinterest.com/darmansourkohphangan`, site
  vérifié via la balise `p:domain_verify` — constante `PINTEREST_VERIFY` dans `_layout.py`).
  **À ajouter quand créé** : LinkedIn.
- **Ne jamais** inventer de `review`/`aggregateRating` (faux avis = risque). Les avis clients réels
  ne sont **jamais** réécrits (ni pour les mots bannis).

**5. Autorité & confiance (E-E-A-T)**
- **Attribuer** les distinctions au lieu d'auto-proclamer : « Featured by Golf du Maroc among the
  world's notable Moroccan restaurants » (PAS « one of the world's best »). Les IA citent l'attribué,
  se méfient du superlatif nu. Transparence : divulguer que le guide est publié par le restaurant.
- **Fait** : Wikidata (`Q140585802`) + Crunchbase + OpenStreetMap (`node/14021567355`) créés et
  reliés au `sameAs` (et dans le schéma Restaurant), **Apple Maps** et **Bing Places** ajoutés.
  Chantier long terme restant : mentions presse sans lien, Wikimedia Commons, présence tierce
  fiable, puis Wikipédia seulement quand la couverture presse indépendante sera suffisante.

**6. Linter mots bannis — étendu aux pages statiques**
- `build.py` passe **toutes** les pages (pas que le blog) au crible des `BANNED_PHRASES`. Exceptions
  whitelistées dans `STATIC_LINT_ALLOW` : citations d'avis clients réels, citation presse, et la
  FAQ SEO « hidden gem » (volontaire — pas une pénalité Google, juste une exception de charte).
  Corriger les ⚠ affichés au build (dans `build.py` / `_menu.py` / `_drinks.py`), ou whitelister
  si c'est une citation.

**7. Page « link in bio » Instagram** : `darmansour.com/links` (générée par `_links.py`) — `noindex`,
hors sitemap, design de marque (losange ◇◇◇, lanterne), 5 boutons max + Instagram/Facebook en icônes.
