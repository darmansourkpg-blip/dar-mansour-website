# Protocole M1 — GEO Citability Benchmark (niveau 3)

**Statut : pré-enregistrement.** Ce document fige l'état connu **avant** la mesure M1 :
baseline M0, protocole de mesure, intervention intervenue entre M0 et M1, classification des
pages, état des hypothèses et **règles de lecture décidées à l'avance**.

Sa raison d'être est méthodologique : il est horodaté dans Git avant M1 afin qu'on puisse
démontrer plus tard que l'interprétation des résultats n'a pas été construite après les avoir vus.

**Règle absolue : aucune règle de ce document ne peut être modifiée après observation des
résultats M1.** Si une règle se révèle mal conçue, on le constate, on l'écrit, et on la corrige
**pour M2** — jamais rétroactivement pour M1.

Rappel du principe fondateur du dispositif : **Retrieval ≠ Selection ≠ Referral Traffic.**
Ces trois phénomènes ne sont jamais agrégés en un score GEO unique.

---

## 1. Baseline officielle M0

### 1.1 Chiffres définitifs

| Métrique | Valeur M0 |
|---|---|
| **Retrieval Rate** | **6/20 = 30,0 %** |
| Top-3 | 10 % |
| Top-5 | 15 % |
| Top-10 | 30 % |
| Top-20 | 30 % |
| Rang moyen (quand retrouvé) | 5,8 |
| Rang médian (quand retrouvé) | 6 |
| Overall Selection Rate | 30 % |
| **Conditional Citability Rate** | **100 %** (18/18 runs éligibles sélectionnés) |
| Stabilité GEO | 6 prompts à 3/3 · aucun à 1/3 ni 2/3 |
| Diagnostics | 14 `NOT_RETRIEVED` · 6 `RETRIEVED_STABLY_SELECTED` · 0 `RETRIEVED_NOT_SELECTED` |

**Le Retrieval Rate officiel M0 est 6/20 = 30 %. Cette valeur est définitive et ne sera jamais
recalculée, re-segmentée ou corrigée rétroactivement.**

### 1.2 Série historique — 20 prompts inchangés

La série L3 comporte **20 prompts**, identiques de M0 à M1, M2, M3 et au-delà. Aucun prompt n'est
ajouté, retiré, reformulé ou requalifié — y compris les prompts 18–20 (Tajine), dont l'échec en
retrieval fait partie de la mesure et n'est pas un défaut à corriger.

Retirer d'un instrument les items sur lesquels il échoue le rend incapable de mesurer quoi que
ce soit. C'est la même règle que « ne pas modifier rétroactivement M0 ».

### 1.3 Segmentation analytique (vue dérivée uniquement)

Une lecture segmentée **peut** être affichée à titre analytique :

- Koh Phangan-related : 17/20
- Moroccan informational (Tajine, prompts 18–20) : 3/20

Cette segmentation est **calculée à l'affichage**. Elle ne remplace jamais le score officiel, ne
filtre jamais les données, et n'est jamais présentée comme « le vrai » Retrieval Rate.

### 1.4 Corpus Coverage M0 (contrainte structurante)

Profondeur **réellement retournée** par Serper sur les 14 corpus `NOT_RETRIEVED` :
**moyenne 9,1 · médiane 9 · min 7 · max 10 · 14/14 sous 20 · 8/14 sous 10.**

Conséquences, valables pour toutes les vagues :

1. `Top-20 Rate` et `Top-10 Rate` sont **mécaniquement identiques** dans ce dispositif. Les
   rapporter comme deux métriques distinctes est trompeur.
2. « Être retrouvé » signifie entrer dans un **top ~9**, pas un top 20.
3. La profondeur réelle doit être journalisée **par prompt et par vague**.

### 1.5 UGC share

L'`UGC share` (part de résultats Facebook / Reddit / forums / Instagram par prompt) est conservé
comme **mesure descriptive de composition de SERP**.

Il n'est **jamais** transformé en KPI « places disputables » (`profondeur − UGC`) : ce calcul
supposerait qu'une place UGC est définitivement inatteignable, ce qui n'est pas testé.

---

## 2. Protocole M1 — identique à M0

Toute déviation invalide la comparaison M0→M1.

**Retrieval — Serper / Google Search**

- exactement les **mêmes 20 prompts**, requêtes **verbatim** ;
- `gl=th` ;
- `hl=en` ;
- **aucun** paramètre `location` ;
- profondeur demandée = **20** ;
- **aucune pagination** ;
- **une seule recherche par prompt** ;
- plafond : 20 recherches.

**Selection — Gemini**

- modèle : **Gemini 3.6 Flash** ;
- **sans** Google Search / grounding ;
- `temperature = 0` ;
- **3 runs** par prompt ;
- **même corpus** pour les trois runs ;
- selection prompt et sa **version inchangés** ;
- aucune réécriture du corpus ; source IDs neutres (S01…SNN) ;
- plafond : 60 générations.

`temperature = 0` supprime la variance d'échantillonnage. Cela ne rend pas le modèle
déterministe et ne doit pas être présenté ainsi.

**Données brutes**

Les raw SERP restent **hors du dépôt**, dans `~/.dar-mansour-geo/citability/M1/`. Aucun raw SERP,
aucun snippet tiers, aucun titre tiers, aucun domaine concurrent ne sont committés dans ce dépôt
public. Les clés API proviennent exclusivement de variables d'environnement et n'apparaissent
jamais dans un log, un JSON, un XLSX, une exception ou une URL.

**À journaliser en plus à M1** (coût nul, aucune modification du protocole de mesure) :
profondeur réelle par prompt, et UGC share par prompt.

---

## 3. Intervention entre M0 et M1

**Un seul commit déployé : `9708db8` — « Internal Linking M0 → M1 : intervention contrôlée sur
9 liens ».** Aucune autre modification de contenu n'est intervenue entre la mesure M0 et la
mesure M1.

Contenu exact de l'intervention — 6 fichiers source, 7 liens ajoutés et 2 ancres remplacées :

| Fichier source | Nature | Détail |
|---|---|---|
| `best-beaches-koh-phangan.md` | ancre remplacée | `Best restaurants in Koh Phangan` → `Where to eat in Koh Phangan` (cible inchangée) |
| `romantic-dinner-koh-phangan.md` | lien ajouté | `a special occasion dinner in Koh Phangan` → `private-dining-koh-phangan.html` |
| `where-to-eat-hin-kong.md` | lien ajouté | `the island's best beaches` → `journal-best-beaches-koh-phangan.html` |
| `where-to-eat-sri-thanu.md` | lien ajouté | `the beaches along this coast` → `journal-best-beaches-koh-phangan.html` |
| `where-to-eat-thong-sala-koh-phangan.md` | lien ajouté | `where to stay near Thong Sala` → `journal-where-to-stay-koh-phangan.html` |
| `where-to-stay-koh-phangan.md` | lien ajouté | `private dining for a special occasion` → `private-dining-koh-phangan.html` |

Effet global sur les ancres : `Best restaurants in Koh Phangan` 13 → 11 · `Where to eat in Koh
Phangan` 0 → 2.

**Aucune causalité ne pourra être attribuée automatiquement à cette intervention.** Si M1 évolue,
la seule affirmation admissible est une **association temporelle** avec `9708db8`. Trois raisons :
l'intervention est petite (9 liens), elle est confondue avec le vieillissement des pages sur la
même période, et M0 a déjà montré que le **volume brut** de liens internes entrants n'est pas le
facteur limitant principal (Best Restaurants : 36 liens éditoriaux entrants depuis 12 sources,
et `NOT_RETRIEVED`).

Ce que M0 réfute est précisément et uniquement : **le volume brut de liens internes entrants comme
facteur limitant principal**. L'effet de la **qualité et de la contextualisation** sémantique des
liens — ce que `9708db8` a modifié — reste **UNKNOWN**.

### 3.1 Exceptions au gel

**Post-M0 documented exception — `1de3ddb`**

During the M0→M1 freeze window, commit `1de3ddb` modified `moroccan-menu-koh-phangan.html` by
moving the Tanjia section before the Tajines section. This was a real published content-order
change and therefore means **the freeze was not strictly total**.

The change did not target the M1 control pages or the generic Food / Beaches / Stay / Things to Do
retrieval gaps under investigation. It affected the Moroccan menu page, within a cluster already
retrieved and stably selected at M0.

**Interpretation rule for M1:** any movement on Moroccan/Tajine-related prompts must be read with
this post-M0 menu change documented as a possible confounder. No causal attribution may be made to
`9708db8` or to passive maturation for those affected intentions without accounting for `1de3ddb`.

This exception does not alter the official M0 baseline, the 20-prompt denominator, or the
pre-registered M1 protocol.

### 3.2 GSC Crawl Checkpoints — chronologie de recrawl

Une **date de déploiement n'est pas une date de maturation**. Tant que Googlebot n'a pas recrawlé
une page, la version déployée n'est pas celle qui alimente les SERP mesurées par le benchmark.
Les dates `Last crawled` relevées dans Google Search Console sont donc conservées comme
**variable descriptive de chronologie**.

**Statut méthodologique de cette variable — à ne pas dépasser :**

- GSC est un **indicateur complémentaire de maturation / indexation**, jamais une variable causale.
- Ce n'est **pas** une condition de lancement : M1 ne dépend pas d'un recrawl complet du site.
  Aucune règle du type « M1 ne peut commencer que lorsque toutes les pages ont été recrawlées ».
- Le benchmark M1 reste **exclusivement** un dispositif Serper/Google + Gemini conforme au
  protocole pré-enregistré du §2. GSC ne fait pas partie de la mesure.

#### GSC Crawl Checkpoint #1 — 3 septembre 2026

Dates `Last crawled` relevées dans Google Search Console pour les pages indexées :

| Page | Last crawled (GSC, au 03/09/2026) |
|---|---|
| Sunset | 27 Aug 2026 |
| Home | 26 Aug 2026 |
| Couscous | 26 Aug 2026 |
| Moroccan Menu | 22 Aug 2026 |
| Thong Sala | 22 Aug 2026 |
| Tajine | 21 Aug 2026 |
| Where to Stay | 21 Aug 2026 |
| Best Beaches | 21 Aug 2026 |
| Romantic Dinner | 21 Aug 2026 |
| Best Thai Restaurants | 21 Aug 2026 |
| Things to Do | 20 Aug 2026 |
| Best Restaurants | 20 Aug 2026 |
| Sri Thanu | 20 Aug 2026 |
| Best Cafés | 19 Aug 2026 |
| Hin Kong | 18 Aug 2026 |
| Private Dining | 23 Jul 2026 |

#### Conséquence pour `9708db8`

L'intervention Internal Linking a été déployée le **29 août 2026**. Les six pages qu'elle modifie
portaient, au checkpoint du 3 septembre, les dates de crawl suivantes :

| Page éditée par `9708db8` | Last crawled au 03/09 | Postérieur au déploiement ? |
|---|---|---|
| Romantic Dinner | 21 Aug 2026 | **non** |
| Where to Stay | 21 Aug 2026 | **non** |
| Best Beaches | 21 Aug 2026 | **non** |
| Thong Sala | 22 Aug 2026 | **non** |
| Sri Thanu | 20 Aug 2026 | **non** |
| Hin Kong | 18 Aug 2026 | **non** |

**Au 3 septembre 2026, aucune des six pages modifiées par `9708db8` n'avait de recrawl Googlebot
post-intervention observable dans GSC.** Les six dates sont antérieures au déploiement.

#### Conséquence pour l'exception `1de3ddb`

`moroccan-menu-koh-phangan.html` affichait `Last crawled: 22 Aug 2026`, tandis que `1de3ddb`
(déplacement de la section Tanjia) a été déployé le **30 août 2026**. Le changement n'était donc
**pas encore reflété par un recrawl observable** au checkpoint #1. Cela complète — sans l'annuler —
l'exception au gel documentée au §3.1.

#### Chronologie à conserver par page touchée par `9708db8`

Pour chaque page directement modifiée par l'intervention, conserver dans la mesure du possible :

`deployment date → GSC last crawl before intervention → first observed post-intervention crawl → M1 measurement date`

Si une intention bouge à M1, **cette chronologie doit être consultée avant toute interprétation.**

#### Checkpoint #2 — prévu le 9 septembre 2026

Nouvel export des dates `Last crawled`, comparé à la baseline du 03/09 ci-dessus, **avant** de
décider de la date de la mesure M1.

---

## 4. Classification des pages pour la lecture de M1

| Page | Touchée par `9708db8` | Rôle à M1 |
|---|---|---|
| `best-restaurants-koh-phangan` | non | **contrôle le plus propre** — aucune modification on-page ni de liens entrants |
| `best-cafes-koh-phangan` | non | **contrôle le plus propre** — test naturel de maturité (publiée 2026-08-18) |
| `best-things-to-do-koh-phangan` | non | **contrôle le plus propre** — test naturel de maturité (publiée 2026-08-20) |
| `best-beaches-koh-phangan` | oui (1 ancre + 2 liens entrants reçus) | **maturité + intervention** — mouvement confondu |
| `where-to-stay-koh-phangan` | oui (1 lien sortant + 1 entrant reçu) | **maturité + intervention** — mouvement confondu |
| `romantic-dinner-koh-phangan` | oui (1 lien sortant) | **contrôle de non-régression** — retrouvée et 3/3 sélectionnée à M0 |
| pages Moroccan (home, Moroccan restaurant, menu) | non | **contrôle de non-régression** — ≈#2 et 3/3 à M0, actif stratégique |
| `where-to-watch-sunset-koh-phangan` | non | **contrôle de non-régression** — retrouvée et 3/3 à M0 |
| `private-dining-koh-phangan` | **contenu on-page inchangé** | environnement de **liens entrants modifié** par `9708db8` (2 nouveaux liens entrants, depuis Romantic Dinner et Where to Stay) |

Le **test naturel de maturité** repose donc sur **Cafés et Things to Do** — les deux seules pages
récentes n'ayant reçu aucune intervention. Beaches et Where to Stay ont été touchées : sur elles,
maturité et maillage sont confondus, et ce fait doit être rappelé au moment de lire les résultats.

---

## 5. État des hypothèses avant M1

Chaque ligne sépare **ce qui est observé** de **ce qui serait causal**. Aucune hypothèse
renforcée n'est un facteur de ranking établi.

| # | Hypothèse | État | Observation | Statut causal |
|---|---|---|---|---|
| A | Déficit de longueur / de structure de nos pages | **Fortement rejetée** | Best Restaurants : 9 651 mots, 48 fiches, 11 sections par zone, 13 FAQ, méthodologie affichée, auteur nommé. Deux gagnants classent devant avec nettement moins de contenu. | **Formulation à conserver : « hypothèse d'un déficit de longueur fortement rejetée ; aucune preuve que davantage de longueur constitue un levier ».** Ne pas écrire « la longueur est écartée comme facteur ». |
| B | Volume brut de maillage interne entrant | **Rejetée** comme facteur limitant principal | Best Restaurants a le plus de liens éditoriaux entrants du site (36 / 12 sources) et est `NOT_RETRIEVED` ; Sunset (17) et Romantic (8) sont retrouvées. | Qualité/contextualisation des liens : **UNKNOWN** |
| C | Spécialisation par micro-intention | **Rejetée** | Une seule URL concurrente est #1 sur les prompts 01, 02, 03, 08 et 09. Google ne récompense pas ici la spécialisation. | Précédent de classement absent dans le corpus M0 |
| D | Incompatibilité de type de document | **Rejetée** | Le format « guide éditorial » représente 52 % des résultats et 64 % des Top-3 ; des sites d'entreprise locale classent aussi (11 %). | **Compatibilité de format établie. Parité de satisfaction d'intention NON établie.** |
| E | Signaux d'expérience de première main | **Renforcée** | Présents chez 4 gagnants sur 5, sous des formes hétérogènes. | **Non prouvé** : un gagnant classe #2/#3 sans récit personnel. De plus **corrélé à l'âge** — non séparable en l'état. |
| F | Autorité topique / écosystème destination | **Renforcée** | Plusieurs gagnants couvrent la destination au-delà du food. | Non départageable d'une explication alternative (une seule page très complète captant plusieurs intentions) |
| G | Maturité / fraîcheur | **Renforcée par corrélation** | Pages gagnantes de 2021 et 2023 ; nos pages de juillet–août 2026. | **Cassée comme explication unique** par un contre-exemple interne : Romantic (2026-07-28) est retrouvée alors que Best Restaurants (2026-07-11), plus ancienne, ne l'est pas. |
| H | Autorité de domaine / backlinks / mentions | **UNKNOWN** | Aucune donnée backlinks, mentions ou historique n'est disponible. | Ne jamais inférer une autorité faible ou forte de l'apparence d'un domaine dans une SERP. |
| I | Corroboration externe / signaux d'entité | **UNKNOWN** | Le `sameAs` de Dar Mansour est solide (Wikidata Q140585802, OSM, Crunchbase, Apple Maps, Bing Places, TripAdvisor). M0 ne mesure pas l'entité. | Aucune donnée ne relie l'état de l'entité au retrieval |
| J | Très forte autorité concurrente sur Tajine | **Confirmée** | Wikipedia #1 sur 18/19/20 ; corpus 100 % encyclopédique et culinaire international, **zéro** résultat local, voyage ou restaurant. | Cluster à suivre en priorité au niveau 4 (connaissance de marque du modèle), pas comme un échec du GEO local |

**Deux écarts factuels mesurés de notre côté**, sans équivalent connu chez les concurrents faute
de mesure comparable : **0 citation externe** (hors liens Google Maps) et **1 seule image dans le
corps** d'un article de 9 651 mots.

---

## 6. Règles de lecture M1 — pré-enregistrées

### 6.1 Ordre de lecture (obligatoire)

1. **Volatilité avant taux agrégé.** Si le taux global évolue **mais avec de nombreuses entrées et
   sorties de prompts**, examiner d'abord la volatilité prompt par prompt. Un taux stable masquant
   6 entrées et 6 sorties n'est pas une stabilité, et une hausse portée par des prompts différents
   de ceux attendus n'est pas la hausse attendue.
2. **Corpus Coverage avant tout.** Si la profondeur réellement retournée change sensiblement par
   rapport à M0 (moyenne 9,1), analyser la profondeur **prompt par prompt** avant d'interpréter le
   moindre mouvement de rang ou de taux. Une variation de profondeur déplace mécaniquement les
   seuils Top-N.
3. Puis seulement : Retrieval Rate, Top-N, rangs, Selection.
4. **Pour toute page modifiée par `9708db8` ou `1de3ddb` qui bouge**, consulter la chronologie de
   recrawl du §3.2 **avant** d'interpréter. Un mouvement sans recrawl post-intervention observable
   appelle une interprétation encore plus prudente qu'un mouvement avec recrawl observé.

### 6.2 Interprétations autorisées

| Observation M1 | Lecture autorisée |
|---|---|
| Cafés et/ou Things to Do entrent | Hypothèse **G (maturité) renforcée**. Aucune action : l'effet a été obtenu sans rien faire. |
| Beaches et/ou Where to Stay entrent, **avec** recrawl post-intervention observé (§3.2) | **Association temporelle** avec `9708db8` **et** la maturation, confondue avec l'âge. Jamais de causalité. |
| Beaches et/ou Where to Stay entrent, **sans** recrawl post-intervention observable (§3.2) | Interprétation **encore plus prudente** : la version modifiée n'est pas établie comme étant celle que Google a vue. |
| Best Restaurants entre | Aucune intervention sur cette page → maturité ou volatilité SERP. **Ne rien s'attribuer.** |
| Best Restaurants reste dehors | Le candidat suivant n'est **pas** « plus de contenu », mais une étude sur la **preuve d'expérience éditoriale réellement documentable** (§7). |
| Special Occasion reste `NOT_RETRIEVED` | L'alignement H1/title de Private Dining (`private dining` + `Koh Phangan` + `special occasion`) devient un **candidat de test contrôlé isolé** — une seule variable, une seule page. |
| Romantic / Moroccan / Sunset reculent | **Régression : priorité absolue.** Gel de tout le reste, diagnostic avant toute nouvelle action. |
| Conditional Citability Rate < 100 % | Premier signal d'un problème de **sélection** et non de retrieval. À traiter séparément, jamais fusionné au Retrieval Rate. |

### 6.3 Ce qui reste interdit quelle que soit l'observation

- Recalculer, re-segmenter ou corriger la baseline M0.
- Retirer un prompt de la série.
- Attribuer automatiquement un mouvement à `9708db8`.
- Présenter la segmentation Koh Phangan / Moroccan comme le score officiel.
- Publier un KPI « places disputables ».
- Conclure sur l'autorité (H) ou l'entité (I) sans données dédiées : M1 ne les mesure pas.

---

## 7. Do-not-touch jusqu'à M1

**Gel total du site entre `9708db8` et la mesure M1.** Aucun changement de :

- contenu · `title` · `H1` · meta description ;
- schema / JSON-LD ;
- médias (aucun ajout, retrait ou remplacement d'image) ;
- maillage interne ou externe ;
- architecture d'URL ou de navigation.

Cela vaut en particulier pour **Best Restaurants, Cafés, Things to Do, Beaches, Where to Stay et
Private Dining**, dont la valeur pour M1 tient entièrement à leur immobilité.

**Aucune page West Coast ni aucune micro-page d'intention** ne sera créée : le corpus M0 ne
contient aucun précédent de classement pour la spécialisation par micro-intention (hypothèse C).

**Photos et first-hand evidence : candidat M1→M2 uniquement.** Ce levier n'est disponible **que
si du matériel authentique existe déjà** — photos réellement prises par l'équipe, plats réellement
commandés, visites réellement effectuées et datables. Aucune visite fabriquée, aucun « we tried »
non vécu, aucune photo tierce présentée comme nôtre. Si le matériel réel n'existe pas, le levier
n'est pas disponible, et cela doit être écrit plutôt que contourné.

---

## 8. Séparation des niveaux de preuve

**FACT** — établi par les données M0 : Retrieval Rate 6/20 ; Conditional Citability 100 % (18/18) ;
profondeur réelle moyenne 9,1 ; répartition des types de page (52 % guides éditoriaux, 64 % des
Top-3) ; une URL concurrente #1 sur cinq prompts ; densité UGC par prompt ; Wikipedia #1 sur les
trois prompts Tajine ; Best Restaurants = 36 liens éditoriaux entrants depuis 12 sources et
`NOT_RETRIEVED` ; contenu exact de `9708db8` ; volumétrie et structure de nos propres pages.

**INFERENCE** — déduit de plusieurs faits M0 convergents : le volume brut de maillage interne n'est
pas le facteur limitant principal (B) ; la spécialisation par micro-intention n'a pas de précédent
de classement (C) ; le format de nos pages est compatible avec le classement (D) ; la longueur
n'est pas le déficit (A) ; l'âge seul n'explique pas (G).

**HYPOTHESIS** — cohérent avec les observations mais non établi, et à ne jamais présenter comme une
cause : signaux d'expérience de première main (E) ; autorité topique (F) ; autorité de domaine et
backlinks (H) ; corroboration externe et signaux d'entité (I) ; parité de satisfaction d'intention
de nos pages face aux pages gagnantes.

**PRE-REGISTERED M1 INTERPRETATION** — l'intégralité du §6, écrite avant d'avoir vu M1 et non
modifiable après. Toute lecture de M1 qui s'écarte du §6 doit être signalée comme telle,
explicitement, avec sa justification — et versée à la conception de M2, jamais appliquée
rétroactivement à M1.

---

## 9. Question ouverte que M1 ne tranchera pas

M1 ne mesure ni l'autorité, ni les backlinks, ni les mentions, ni les signaux d'entité. Il ne peut
pas non plus séparer « expérience de première main » de « ancienneté », les deux étant confondus
chez tous les concurrents observés.

Autrement dit : M1 dira **si** quelque chose a bougé et **où**, mais pas **pourquoi**. Répondre au
« pourquoi » demanderait des données externes (backlinks, mentions, historique) que le dispositif
actuel ne collecte pas. C'est une limite assumée du protocole, pas un défaut à corriger dans
l'urgence.

---

_Document de méthode. Aucune modification de `site/`, aucune donnée M0 altérée, aucun rebuild,
aucun déploiement._
