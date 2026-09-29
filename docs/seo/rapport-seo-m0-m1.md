# RAPPORT SEO M0 → M1 — provisoire

**Document de travail, non commité.** Autonome : lisible sans connaître l'historique technique.

---

## 1. Executive Summary

**La visibilité organique a fortement progressé, les clics beaucoup moins, et l'engagement a
baissé.** Sur les fenêtres disponibles :

| Indicateur | Avant | Après | Variation |
|---|---|---|---|
| Impressions Google | 17 885 | **27 078** | **+51,4 %** |
| Clics Google | 186 | **228** | **+22,6 %** |
| CTR global | 1,04 % | **0,84 %** | **−19 %** |
| Sessions Organic Search (GA4) | 300 | **338** | +12,7 % |
| Durée d'engagement moyenne | 47 s | **32 s** | **−32 %** |
| Key events | 13 | **11** | −2 |

Quatre constats structurent le reste du rapport :

1. **La croissance est entièrement éditoriale.** Les guides du Journal portent la totalité du
   gain. Beaches, Cafés, Things to Do, Where to Stay et Best Restaurants apportent à eux seuls
   +7 700 impressions.
2. **Le socle de marque recule.** Les requêtes *branded* perdent des impressions **et** des clics,
   alors que les *non-branded* explosent. La page d'accueil perd des clics, des impressions et
   24 sessions organiques.
3. **La qualité du trafic se dégrade.** CTR en baisse malgré des positions moyennes en
   amélioration, durée d'engagement divisée par 1,5, key events en recul.
4. **La baisse récente est CONFIRMÉE et expliquée.** Rupture le **18 septembre**, −36,4 %
   d'impressions. Elle recouvre **deux phénomènes distincts** :
   - **A — une contraction d'exposition sans valeur** : les États-Unis produisaient 2 756
     impressions pour **2 clics** (CTR 0,07 %) et en perdent 1 915 ; le desktop perd 2 480. **Au
     moins 1 537 impressions perdues sont à la fois US et desktop.** Perte de clics associée :
     **zéro**.
   - **B — une seule vraie perte de classement** : **Where to Stay**, −89,5 % d'impressions et
     **7 des 10 clics nets perdus**, sa requête principale passant de la position **20,1 à 32,0**.

   Partout ailleurs, CTR et positions **s'améliorent** : 11 pages sur 17 gagnent du CTR, 6 gagnent
   des clics. La Thaïlande perd 467 impressions et seulement 2 clics, en améliorant CTR et
   position. Voir §9.

5. **⚠️ L'impact sur le trafic réel n'est pas vérifiable.** Aucun export GA4 disponible ne
   ventile les sessions par jour. **Il est donc impossible de confirmer ou d'infirmer que le
   trafic a suivi, ou non, la chute des impressions du 18 septembre.** Le diagnostic du §9 porte
   sur l'exposition mesurée par GSC, pas sur le trafic. Voir §9, encadré « Limite GA4 ».

**Aucun score SEO global n'est produit** et aucune évolution n'est attribuée à une intervention.

> **Correction.** La version précédente de ce rapport lisait la valeur du 18/09 comme un artefact
> de dernier jour d'export. Le nouvel export montre qu'il s'agissait du **premier jour de la
> baisse**. La conclusion « aucun retournement » est annulée.

---

## 2. Périmètre et méthodologie

### Sources et fenêtres

| Source | Fenêtre récente | Fenêtre de comparaison | Comparabilité |
|---|---|---|---|
| **GSC Performance** (export 23/09) | **24/08 → 20/09** | **27/07 → 23/08** | ✅ **dates identifiées** — voir encadré |
| **GSC Performance** (export 29/09) — série quotidienne | **01/08 → 25/09** | — | ✅ clics, impressions, CTR **et position** par jour |
| **GSC Coverage** (export 22/09) — série quotidienne | 03/07 → 18/09 | — | ✅ recoupe l'export du 29/09 |
| **GA4 Traffic acquisition** | 25/08 → 21/09 | 28/07 → 24/08 | ✅ dates explicites, fenêtres de 28 jours |
| **GA4 Landing pages** (Organic) | 25/08 → 21/09 | 28/07 → 24/08 | ✅ mêmes dates · ⚠️ **tronqué à 28 lignes** |
| **GSC Coverage / indexation** | au 22/09 | — | ponctuel |
| **GSC Sitemap** | au 23/09 | — | ponctuel |
| **GSC Generative AI (bêta)** | « Last 28 days » | « Previous 28 days » | couche séparée, §11 |

### Les dates de l'export du 23/09 sont désormais connues

L'export du 23/09 n'indiquait que « Last 28 days » / « Previous 28 days ». La série quotidienne du
29/09 permet de les retrouver **par correspondance exacte** :

| | Somme attendue | Fenêtre trouvée | Vérification |
|---|---|---|---|
| Last 28 days | 27 078 impr · 228 clics | **24/08 → 20/09** | 27 078 · 228 — **exact** |
| Previous 28 days | 17 885 impr · 186 clics | **27/07 → 23/08** | par construction |

C'est un gain méthodologique : les comparaisons GSC ↔ GA4 (25/08 → 21/09) portent désormais sur
des fenêtres **quasi superposées**, décalées d'un seul jour.

### Incompatibilités signalées

- Les fenêtres GSC (24/08 → 20/09) et GA4 (25/08 → 21/09) se recouvrent à 27 jours sur 28. Elles
  restent comparées **en tendance**, jamais additionnées.
- **Ces fenêtres ne correspondent pas à la fenêtre M0 du niveau 2** (01/07 → 25/08, 56 jours).
  Aucune comparaison directe avec cette baseline n'est faite ici.
- « M0 → M1 » désigne dans ce rapport **période précédente → période récente** des exports
  ci-dessus, pas les dates du benchmark GEO.

### Référence de totalisation retenue

L'onglet `Pages` de l'export GSC **ne peut pas servir de total du site** (voir §12). Tous les
totaux de ce rapport utilisent l'onglet **`Devices`**, cohérent avec `Countries`.

---

## 3. Performance SEO globale

**Source : GSC Performance, onglet Devices — 28 jours vs 28 jours précédents.**

| Métrique | Précédent | Récent | Δ absolu | Δ relatif |
|---|---|---|---|---|
| Impressions | 17 885 | 27 078 | +9 193 | **+51,4 %** |
| Clics | 186 | 228 | +42 | **+22,6 %** |
| CTR | 1,040 % | 0,842 % | −0,198 pt | **−19,0 %** |

Par appareil :

| Appareil | Impressions | Clics | Position moyenne |
|---|---|---|---|
| Mobile | 9 225 → **13 185** (+42,9 %) | 143 → **183** (+28,0 %) | 7,81 → **7,69** |
| Desktop | 8 606 → **13 792** (+60,3 %) | 43 → **44** (+2,3 %) | 9,78 → **8,41** |
| Tablette | 54 → 101 | 0 → 1 | 7,17 → 7,69 |

**Observation.** Desktop gagne 60 % d'impressions pour +1 clic. Le CTR desktop passe de 0,50 % à
0,32 %. Mobile reste le moteur des clics.

**Source : GA4 Traffic acquisition — 25/08 → 21/09 vs 28/07 → 24/08.**

| Canal | Précédent | Récent | Δ |
|---|---|---|---|
| **Organic Search** | 300 | **338** | +38 (+12,7 %) |
| Direct | 321 | 295 | −26 |
| AI Assistant | 44 | 100 | +56 |
| Organic Social | 8 | 4 | −4 |
| Referral | 10 | 2 | −8 |
| Unassigned | 7 | 4 | −3 |
| **Total** | **690** | **743** | +53 (+7,7 %) |

Organic Search, détail (fourni par l'opérateur) : utilisateurs actifs 192 → **234**, nouveaux
utilisateurs 188 → **226**, durée d'engagement moyenne 47 s → **32 s**, key events 13 → **11**.

**Écart de croissance à noter.** Impressions +51,4 %, clics +22,6 %, sessions organiques +12,7 %.
L'entonnoir se rétrécit à chaque étape.

---

## 4. Analyse GSC

### Ce que l'export permet et ne permet pas

| Disponible | Non disponible |
|---|---|
| Requêtes (1 093), pages (125), pays (168), appareils, apparence | **Ventilation quotidienne** — aucun onglet `Dates` |
| Clics, impressions, CTR, position par dimension | Dates calendaires des deux fenêtres |
| Comparaison 28 j vs 28 j | Croisement requête × page |

### Couverture de l'onglet Queries

| | Impressions | Clics |
|---|---|---|
| Somme onglet Queries | 3 442 → 5 588 | 45 → 43 |
| Total site (Devices) | 17 885 → 27 078 | 186 → 228 |
| **Couverture** | **19,2 % → 20,6 %** | **24,2 % → 18,9 %** |

⚠️ **L'onglet Queries ne couvre qu'un cinquième du volume.** GSC tronque et masque les requêtes
rares. Les analyses de §7 portent sur cette fraction visible, jamais sur l'ensemble.

---

## 5. Analyse GA4 Organic

**Landing pages, filtre Organic Search, 28 lignes visibles** (323/338 sessions récentes,
280/300 précédentes — export non exhaustif, ~4–7 % non représentés).

| Page | Précédent | Récent | Δ |
|---|---|---|---|
| Best Cafés | 4 | **25** | **+21** |
| Best Beaches | 13 | **31** | **+18** |
| Where to Stay | 9 | **27** | **+18** |
| Best Restaurants | 21 | **34** | **+13** |
| Things to Do | 2 | 6 | +4 |
| What Is a Tajine | 2 | 5 | +3 |
| Moroccan Menu | 7 | 10 | +3 |
| Best Thai Restaurants | 14 | 17 | +3 |
| **Page d'accueil `/`** | **68** | **44** | **−24** |
| Réservation | 7 | **2** | **−5** |
| Sri Thanu | 20 | 16 | −4 |
| Les Dadas | 5 | 2 | −3 |
| Gnaoua | 5 | 3 | −2 |
| Private Dining | 2 | **0** | −2 |

### Export GA4 Traffic acquisition, 01 → 28 septembre

Reçu le 29/09. **Agrégats par canal uniquement, aucune ventilation quotidienne.**

| Canal | Sessions | Engaged | Taux d'engagement | Durée moy./session | Key events |
|---|---|---|---|---|---|
| **Organic Search** | **329** | 141 | 42,9 % | **29,7 s** | **7** |
| Direct | 286 | 98 | 34,3 % | 19,0 s | 25 |
| AI Assistant | 79 | 26 | 32,9 % | 14,6 s | 5 |
| Organic Social | 4 | 4 | 100 % | 147 s | 0 |
| Referral · Unassigned · Cross-network | 2 · 2 · 0 | — | — | — | 1 · 0 · 0 |

*Le fichier contient aussi un bloc 01 → 29/09 : Organic Search y reste à **329 sessions**, le
29/09 n'ayant apporté aucune session organique enregistrée à l'heure de l'export.*

#### Trois fenêtres de 28 jours — à lire avec prudence

| Fenêtre | Sessions Organic | /jour | Durée moy. | Key events |
|---|---|---|---|---|
| 28/07 → 24/08 | 300 | 10,71 | 47 s | 13 |
| 25/08 → 21/09 | 338 | 12,07 | 32 s | 11 |
| **01/09 → 28/09** | **329** | **11,75** | **29,7 s** | **7** |

⚠️ **Ces trois fenêtres se recouvrent largement** — 21 jours communs entre les deux dernières.
Elles **ne constituent pas trois mesures indépendantes** et aucune conclusion sur la rupture du
18 septembre n'en est tirée (voir §9).

**Observation, indépendante de la rupture.** Les key events reculent sur les trois fenêtres
successives — **13 → 11 → 7** — et la durée d'engagement moyenne suit la même pente —
**47 s → 32 s → 29,7 s**. Cette tendance est antérieure au 18 septembre et n'est pas expliquée
par la contraction d'exposition.

### Engagement par page — la dégradation est générale

| Page | Précédent | Récent |
|---|---|---|
| Page d'accueil | 55,1 s | **30,7 s** |
| Best Restaurants | 81,6 s | **33,8 s** |
| Sri Thanu | 97,2 s | 85,7 s |
| Best Beaches | 29,9 s | 26,0 s |
| Breakfast & Brunch | 24,8 s | 16,8 s |
| Romantic Dinner | 48,1 s | **57,5 s** ▲ |

**Observation.** Romantic Dinner est la seule page principale dont l'engagement progresse, et la
seule à gagner un key event (0 → 1). La page d'accueil perd 44 % de durée d'engagement et un key
event (8 → 7).

---

## 6. Winners / Losers par page

**Source : GSC Performance, onglet Pages, lignes sans ancre.**

### Gains d'impressions

| Page | Impressions | Clics | Position | CTR |
|---|---|---|---|---|
| Things to Do | 159 → **1 841** (+1 682) | 2 → 7 | 11,11 → **9,56** | 1,26 → **0,38 %** |
| Best Beaches | 1 895 → **3 529** (+1 634) | 10 → **25** | 8,26 → **6,73** | 0,53 → **0,71 %** |
| Best Cafés | 213 → **1 668** (+1 455) | 4 → **21** | 6,46 → 6,70 | 1,88 → 1,26 % |
| Best Restaurants | 3 353 → **4 618** (+1 265) | 15 → 19 | 9,22 → **8,25** | 0,45 → 0,41 % |
| Thong Sala | 1 528 → **2 689** (+1 161) | 15 → 16 | 7,39 → 8,05 | 0,98 → **0,60 %** |
| Where to Stay | 1 090 → **1 967** (+877) | 9 → **21** | 12,08 → **10,93** | 0,83 → **1,07 %** |
| Sunset | 1 817 → **2 453** (+636) | 14 → 14 | 7,33 → 7,19 | 0,77 → 0,57 % |
| What Is a Tajine | 550 → **1 079** (+529) | 1 → 2 | 15,58 → **14,02** | 0,18 → 0,19 % |
| Gnaoua | 180 → **511** (+331) | **4 → 2** | 14,27 → **8,78** | 2,22 → **0,39 %** |
| Moroccan Menu | 186 → **450** (+264) | 2 → **7** | **11,18 → 4,85** | 1,08 → **1,56 %** |

### Pertes

| Page | Impressions | Clics | Position |
|---|---|---|---|
| Best Thai Restaurants | 1 739 → 1 571 (−168) | 11 → 12 | 8,75 → 8,64 |
| Moroccan Cuisine Guide | 232 → 79 (−153) | 0 → 1 | — |
| **Romantic Dinner** | 566 → **426** (−140) | **12 → 9** | 7,79 → 7,50 |
| What Is Couscous | 116 → 13 (−103) | 0 → 0 | — |
| `/blog.html` | 175 → 90 (−85) | 0 → 0 | — |
| `/koh-phangan-guide.html` | 86 → **3** (−83) | 0 → 0 | — |
| **Page d'accueil `/`** | 584 → **540** (−44) | **18 → 16** | 3,05 → 3,03 |

### Les deux plus grosses pertes de clics

| Page | Clics | Impressions | Lecture |
|---|---|---|---|
| **Sri Thanu** | **22 → 12 (−10)** | 1 465 → 1 473 (stable) | CTR **1,50 % → 0,81 %** à volume constant |
| Romantic Dinner | 12 → 9 (−3) | 566 → 426 | perte d'impressions ET de clics |

**Sri Thanu est la principale faiblesse du site sur la période** : même exposition, presque moitié
moins de clics.

### Par famille de pages

| Famille | Impressions | Clics |
|---|---|---|
| **Journal — guides locaux** | ≈ 13 000 → ≈ 22 000 | 116 → 159 |
| **Journal — culture marocaine** (Tajine, Couscous, Gnaoua, Dadas, Cuisine Guide) | 1 161 → 1 800 | 8 → 7 |
| **Commercial** (menu, réservation, private dining, reviews, press) | ≈ 560 → ≈ 1 050 | 7 → 9 |
| **Page d'accueil** | 584 → 540 | 18 → 16 |
| **Pages de listing** (blog, guide, authors) | 311 → 93 | 1 → 0 |

**Observation.** Le cluster commercial progresse en position de façon spectaculaire — Moroccan Menu
11,18 → **4,85**, Private Dining 19,97 → **9,57**, Reviews 19,89 → **11,17** — mais en volumes très
faibles. Private Dining et Reviews font **0 clic** sur la période.

---

## 7. Winners / Losers par requête

⚠️ Portée limitée : l'onglet Queries couvre ~20 % du volume (§4).

### Branded vs non-branded

| | Requêtes | Clics | Impressions |
|---|---|---|---|
| **Branded** (contient « dar mansour » / « mansour ») | 8 | **19 → 15 (−4)** | **300 → 225 (−25 %)** |
| **Non-branded** | 1 085 | 26 → 28 (+2) | 3 142 → **5 363 (+71 %)** |

**C'est le constat le plus important du rapport.** Le trafic de marque recule pendant que la
visibilité générique augmente.

### La plus grosse perte de clics du site

| Requête | Clics | Impressions | Position |
|---|---|---|---|
| **dar mansour - morocco's kitchen** | **14 → 7** | 105 → 77 | **2,00 → 1,20** ▲ |

La position **s'améliore** et les clics sont **divisés par deux**. CTR 13,3 % → 9,1 %. Cause
inconnue.

Autres requêtes de marque : `dar mansour koh phangan` 1 → 2 clics (96 → 60 impr), `dar mansour`
4 → 6 clics (88 → 75 impr). Le recul est concentré sur la requête longue.

### Gains d'impressions — intentions locales

| Requête | Impressions | Position |
|---|---|---|
| sri thanu | 17 → **148** | 10,5 → 9,8 |
| sunset koh phangan | 98 → **217** | 8,1 → 8,9 |
| mama kop | 0 → **119** | — → 10,9 |
| thong sala | 14 → **124** | 16,0 → 12,3 |
| best beaches in koh phangan | 11 → **99** | **37,4 → 14,6** |
| thong sala koh phangan | 79 → **166** | 10,4 → 11,2 |
| where to stay in koh phangan | 42 → **99** | 28,8 → 23,7 |
| things to do in koh phangan | 4 → **50** | 46,5 → 34,3 |

### Gains d'impressions — informationnel / hors zone

`breakfast near me` 39 → 92 · `best brunch spots near me` 2 → 50 · `tajine` 66 → 112 (0 → 1 clic).

⚠️ `near me` sans ancrage géographique : impressions peu qualifiées, contributrices probables à la
dilution du CTR.

### Pertes de clics par requête

| Requête | Clics | Impressions |
|---|---|---|
| dar mansour - morocco's kitchen | 14 → 7 | 105 → 77 |
| best breakfast koh phangan | 4 → 0 | 51 → 30 |
| mama kop koh phangan | 2 → 0 | 133 → 151 |
| cintamani koh phangan | 2 → 0 | 74 → 33 |
| frühstück koh phangan | 2 → 0 | 21 → 40 |
| dear phangan menu | 2 → 0 | 36 → 24 |

**Observation.** Les requêtes « nom d'établissement tiers + koh phangan » — sur lesquelles nos
guides se positionnaient — perdent leurs clics. Six requêtes passent de 2–4 clics à **zéro**.

### Renouvellement

**501 requêtes nouvelles** (0 impression auparavant) · **286 disparues**. Le corpus de requêtes
visibles se renouvelle fortement.

---

## 8. Analyse par cluster

| Cluster | Impressions | Clics | Position | Lecture |
|---|---|---|---|---|
| **Beaches** | 1 895 → 3 529 | 10 → **25** | 8,26 → 6,73 | Meilleure performance du site |
| **Cafés** | 213 → 1 668 | 4 → **21** | 6,46 → 6,70 | Plus forte progression relative |
| **Where to Stay** | 1 090 → 1 967 | 9 → **21** | 12,08 → 10,93 | Seul cluster à améliorer son CTR |
| **Things to Do** | 159 → 1 841 | 2 → 7 | 11,11 → 9,56 | Volume sans conversion en clics |
| **Restaurants KP** | 3 353 → 4 618 | 15 → 19 | 9,22 → 8,25 | Volume le plus élevé, CTR 0,41 % |
| **Thong Sala** | 1 528 → 2 689 | 15 → 16 | 7,39 → **8,05** ▼ | Impressions +76 %, clics +1 |
| **Sunset** | 1 817 → 2 453 | 14 → 14 | 7,33 → 7,19 | Clics strictement stables |
| **Hin Kong** | 379 → 413 | 8 → 10 | 7,06 → 6,48 | Meilleur CTR du site : **2,42 %** |
| **Sri Thanu** | 1 465 → 1 473 | **22 → 12** | 6,48 → **6,88** ▼ | **Perte la plus lourde** |
| **Romantic Dinner** | 566 → 426 | **12 → 9** | 7,79 → 7,50 | Seul cluster en repli sur les deux axes |
| **Thai Restaurants** | 1 739 → 1 571 | 11 → 12 | 8,75 → 8,64 | Stable |
| **Tajine / cuisine marocaine** | 1 161 → 1 800 | **8 → 7** | — | Impressions +55 %, clics en repli |
| **Moroccan restaurant (commercial)** | ≈ 560 → ≈ 1 050 | 7 → 9 | gains massifs | Volumes faibles |

### Visibilité éditoriale vs visibilité commerciale

**Fait établi.** L'éditorial porte ≈ 95 % des impressions et ≈ 70 % des clics. Le commercial gagne
énormément en position mais reste marginal en volume : Moroccan Menu 7 clics, Private Dining 0,
Reviews 0.

**Observation.** La page d'accueil — porte d'entrée commerciale principale — recule sur les trois
mesures : impressions 584 → 540, clics 18 → 16, sessions organiques 68 → 44.

---

## 9. Analyse du signal de baisse récente — **BAISSE CONFIRMÉE**

### Correction d'une lecture antérieure

La version précédente de ce rapport indiquait que la chute du 18/09 à 655 impressions était un
**artefact du dernier jour d'export**. **C'était faux.** L'export du 29/09 confirme 655 le 18/09,
et les jours suivants restent au même niveau. **Le 18 septembre est le premier jour d'un nouveau
régime, pas un artefact de mesure.**

### La rupture est nette et datée

Source : GSC Performance export 29/09, onglet Chart — 01/08 → 25/09, sans filtre.

| Semaine | Clics | Impressions | Impr./jour | CTR | Position |
|---|---|---|---|---|---|
| 01–07/08 | 40 | 3 087 | 441,0 | 1,30 % | 9,22 |
| 08–14/08 | 50 | 5 513 | 787,6 | 0,91 % | 8,59 |
| 15–21/08 | 51 | 5 927 | 846,7 | 0,86 % | 8,63 |
| 22–28/08 | 61 | 6 423 | 917,6 | 0,95 % | 8,42 |
| 29/08–04/09 | **74** | 6 701 | 957,3 | 1,10 % | 8,35 |
| 05–11/09 | 58 | 7 202 | 1 028,9 | 0,81 % | 7,88 |
| **12–18/09** | 56 | **7 215** | **1 030,7** | 0,78 % | 7,85 |
| **19–25/09** | **46** | **4 591** | **655,9** | **1,00 %** | **7,51** |

**Impressions −36,4 % · clics −17,9 %** par rapport à la semaine précédente.

### Le jour de bascule : 17 → 18 septembre

| Date | Impressions |
|---|---|
| 16/09 | 1 029 |
| 17/09 | 1 011 |
| **18/09** | **655** ← rupture |
| 19/09 | 717 |
| 20/09 | 632 |
| 21/09 | 613 |
| 22/09 | 553 |
| 23/09 | 692 |
| 24/09 | 750 |
| 25/09 | 634 |

**Chute de ~35 % en un jour, puis plateau stable à 550–750.** Ce n'est pas une décrue progressive :
c'est une **marche d'escalier**, suivie de huit jours sans reprise ni aggravation.

### Ce que la baisse n'est PAS

**Fait établi — il n'y a pas de perte de classement.**

| | 12–18/09 | 19–25/09 |
|---|---|---|
| Position moyenne pondérée | 7,85 | **7,51** ▲ |
| CTR | 0,78 % | **1,00 %** ▲ |
| Clics/jour | 8,0 | 6,6 |

La position **s'améliore**, le CTR **s'améliore**, et les clics reculent **deux fois moins vite**
que les impressions. Une perte de ranking produirait l'inverse : position dégradée, CTR stable ou
en baisse, clics chutant au moins aussi vite que les impressions.

### Mécanisme — ce que les données permettent de dire

**Observation.** Le profil observé — impressions en forte baisse, position et CTR en hausse, clics
peu touchés — est celui d'une **disparition d'impressions à faible valeur**, situées en profondeur
de SERP et ne générant presque aucun clic. Leur retrait améliore mécaniquement la position moyenne
et le CTR.

Deux réservoirs d'impressions à très bas rendement existent sur la période complète :

| Segment | Impressions | Clics | CTR |
|---|---|---|---|
| **États-Unis** | 11 049 | 17 | **0,15 %** |
| **Desktop** | 23 028 | 88 | **0,38 %** |
| Mobile | 23 460 | 347 | 1,48 % |
| Thaïlande | 20 164 | 267 | 1,32 % |

Desktop pèse autant que mobile en impressions et quatre fois moins en clics.

**Donnée insuffisante.** Les onglets Countries, Devices et Search Appearance du nouvel export sont
**agrégés sur 01/08 → 25/09** : ils ne sont pas ventilés par sous-période. **Il est donc impossible
d'établir si la baisse est concentrée sur les États-Unis, sur desktop, ou ailleurs.**

Quatre mécanismes restent ouverts et **ne peuvent pas être départagés** avec les exports actuels :

1. retrait d'impressions profondes à faible rendement (cohérent avec position et CTR en hausse) ;
2. baisse de la demande de recherche sur les requêtes concernées ;
3. changement de composition des SERP — élément ajouté ou retiré au-dessus de nos résultats ;
4. ajustement d'affichage ou de comptage côté Google.

**La cause reste ouverte.**

### Source : export comparatif contrôlé 19–25/09 vs 12–18/09

Les bornes de la version précédente sont **remplacées par les données exactes**. Filtres :
`Search type: Web`, aucun autre. Totaux vérifiés : impressions 7 215 → 4 591, clics 56 → 46.

> **Note sur la méthode des bornes.** Elles étaient valides — aucune n'est contredite — mais
> partiellement trompeuses dans leur hiérarchie. Elles avaient correctement désigné **Where to
> Stay** comme suspect principal (−89 % au plus ; réel **−89,5 %**). En revanche elles n'avaient
> **pas pu voir Best Restaurants**, qui est la plus grosse perte du site, et elles suspectaient
> **Sunset**, qui a en réalité **progressé**.

### Deux phénomènes distincts, à ne pas confondre

L'export révèle **deux mouvements de nature différente** qui se superposent.

---

### Phénomène A — contraction d'une exposition sans valeur

| Segment | Impressions | Clics | CTR | Position |
|---|---|---|---|---|
| **Desktop** | 4 284 → **1 804** (**−57,9 %**) | 14 → 10 | 0,33 → **0,55 %** | 7,78 → **7,35** |
| Mobile | 2 908 → 2 754 (**−5,3 %**) | 41 → 36 | 1,41 → 1,31 % | 7,94 → **7,62** |
| Tablette | 23 → 33 (+43,5 %) | 1 → 0 | — | — |

| Pays | Impressions | Clics | CTR | Position |
|---|---|---|---|---|
| **États-Unis** | 2 756 → **841** (**−69,5 %**) | **2 → 0** | **0,07 % → 0,00 %** | 7,33 → **7,12** |
| **Thaïlande** | 2 512 → 2 045 (−18,6 %) | 33 → 31 | 1,31 → **1,52 %** | 7,99 → **7,50** |
| Israël | 232 → 117 | 1 → 0 | — | — |
| Royaume-Uni | 203 → 162 | 2 → 1 | — | 12,24 → 9,18 |

**Le fait décisif : les États-Unis produisaient 2 756 impressions pour 2 clics.** Un CTR de
**0,07 %** — soit une exposition sans valeur commerciale. Leur disparition retire 1 915
impressions et **zéro clic net**.

**La Thaïlande — le seul marché commercialement pertinent — perd 467 impressions et 2 clics, en
améliorant son CTR (1,31 → 1,52 %) et sa position (7,99 → 7,50).**

#### Intersection US × desktop

Les deux segments **ne sont pas indépendants** et leurs pourcentages **ne se partitionnent pas** :
desktop représente 94,5 % de la perte nette et les États-Unis 73 %, ce qui fait 167,5 % — donc un
recouvrement massif.

Une **borne inférieure** est néanmoins déductible par inclusion-exclusion :

```
perte_US + perte_desktop − perte_nette_site  =  1 915 + 2 480 − 2 624  =  1 771
```

**Au moins 1 771 impressions perdues sont simultanément américaines et desktop**, et **au moins
1 537** si l'on retranche prudemment les gains observés ailleurs (tablette +10, pays +224). Soit
**entre 59 % et 67 % de toute la perte du site**, concentrés sur un seul croisement.

⚠️ **Ceci est une borne, pas une mesure.** La valeur exacte de l'intersection exige un export
croisé pays × appareil, qui n'existe pas dans les données actuelles. Aucun chiffrage n'est proposé
au-delà de cette borne.

#### Une anomalie dans cette anomalie

Les impressions américaines avaient une **position moyenne de 7,33** pour un CTR de **0,07 %**.
Une position 7 en résultat classique produit typiquement un CTR de l'ordre du pourcent, soit
**plus de dix fois** ce qui est observé. **Observation** : ce profil ne ressemble pas à des
impressions de lien bleu standard ; il évoque des affichages où la position est comptabilisée
sans visibilité réelle. **Donnée insuffisante** pour trancher — l'onglet Search Appearance du
comparatif est vide.

---

### Phénomène B — une perte de classement réelle, sur une seule page

| Page | Impressions | Δ | Clics | CTR | Position |
|---|---|---|---|---|---|
| Best Restaurants | 1 142 → 561 | **−581 (−50,9 %)** | 3 → **4** | 0,26 → **0,71 %** | 8,11 → 8,56 |
| Best Beaches | 1 265 → 729 | **−536 (−42,4 %)** | 7 → 7 | 0,55 → **0,96 %** | 6,18 → **5,34** |
| **Where to Stay** | 533 → 56 | **−477 (−89,5 %)** | **8 → 1** | 1,50 → 1,79 % | 9,33 → 7,95 |
| Things to Do | 731 → 327 | −404 (−55,3 %) | 3 → **0** | 0,41 → 0,00 % | 9,59 → 9,52 |
| Thong Sala | 811 → 475 | −336 (−41,4 %) | 3 → **5** | 0,37 → **1,05 %** | 8,10 → 8,01 |
| Sri Thanu | 425 → 230 | −195 (−45,9 %) | 1 → **2** | 0,24 → **0,87 %** | 7,05 → 7,40 |
| Breakfast & Brunch | 416 → 265 | −151 (−36,3 %) | 6 → 5 | 1,44 → **1,89 %** | 7,22 → 7,34 |
| Best Thai | 265 → 207 | −58 (−21,9 %) | 0 → **3** | 0,00 → **1,45 %** | 10,30 → **8,88** |
| Best Cafés | 494 → 448 | −46 (−9,3 %) | 9 → 6 | 1,82 → 1,34 % | 6,91 → 7,58 |
| **Sunset** | 415 → 497 | **+82 (+19,8 %)** | 3 → **4** | 0,72 → 0,80 % | 6,84 → 6,82 |
| **Hin Kong** | 98 → 156 | **+58 (+59,2 %)** | 1 → **2** | 1,02 → 1,28 % | 6,65 → 6,88 |
| What Is a Tajine | 263 → 300 | **+37** | 2 → 1 | — | 12,96 → **10,16** |

**Où sont réellement passés les 10 clics perdus ?**

| Page | Clics |
|---|---|
| **Where to Stay** | **8 → 1 (−7)** |
| Best Cafés · Romantic Dinner · Things to Do | −3 chacune |
| Breakfast, Tajine, Reservation, Les Dadas | −1 chacune |
| **Gains** : Best Thai +3 · Thong Sala +2 · Best Restaurants, Sunset, Sri Thanu, Hin Kong, Menu, accueil +1 chacune | **+10** |

**Where to Stay représente à elle seule 7 des 10 clics nets perdus.**

C'est la seule page dont la dégradation est corroborée au niveau requête :

| Requête | Impressions | **Position** |
|---|---|---|
| **where to stay in koh phangan** | 20 → 1 | **20,1 → 32,0** |
| ou dormir a koh phangan | 8 → 0 | 63,0 → hors corpus |

**Fait établi : c'est le seul déclassement documenté par une position en chute.** La position
moyenne de la *page* s'améliore pourtant (9,33 → 7,95) — précisément parce que ses impressions
profondes ont disparu. **La position moyenne d'une page est trompeuse quand le volume s'effondre ;
seule la position par requête est fiable ici.**

### Ce qui va bien, et qu'il ne faut pas masquer

Sur les 17 pages dépassant 50 impressions avant la rupture : **11 améliorent leur CTR** et
**8 améliorent leur position**. Deux pages progressent en impressions — Sunset (+82) et Hin Kong
(+58). Six pages gagnent des clics.

**Best Restaurants perd 581 impressions et gagne un clic** (CTR 0,26 → 0,71 %). **Thong Sala perd
336 impressions et gagne deux clics** (CTR 0,37 → 1,05 %). Ce sont des pertes d'exposition
improductive, pas des pertes commerciales.

### Les URLs à ancre ne sont pas en cause

| | 12–18/09 | 19–25/09 | Δ |
|---|---|---|---|
| Lignes à ancre (73) | 2 017 | 1 864 | **−153** |
| Total site | 7 215 | 4 591 | −2 624 |

Les fragments représentent **5,8 % de la perte**. **Hypothèse écartée** : le phénomène des ancres
— et donc toute piste liée à PR #147 par ce canal — n'explique pas la baisse.

### Requêtes — portée limitée, à ne pas surinterpréter

L'onglet Queries ne couvre que **1 296/7 215 (18,0 %)** puis **1 124/4 591 (24,5 %)** des
impressions. **Aucune attribution de l'ensemble de la baisse ne lui est faite.**

Pertes visibles : `sri thanu` 70 → 25 · `dear phangan` 43 → 12 · `where to stay in koh phangan`
20 → 1 · `authentic contemporary thai food` 19 → 3 (position 30,1 → 49,3) · `best brunch spots
near me` 16 → 1 · `breakfast koh phangan` 17 → 5.

Gains : `sunset koh phangan` 32 → 56 · `tajine` 41 → 61 · `hin kong` 7 → 20 · `srithanu` 4 → 15 ·
`breakfast near me` 23 → 35.

**Deux requêtes seulement montrent une position en chute** : `where to stay in koh phangan`
(20,1 → 32,0) et `authentic contemporary thai food` (30,1 → 49,3, volume négligeable).

### ⚠️ Limite GA4 — l'impact sur le trafic réel n'est pas vérifiable

Le test décisif aurait été de comparer les sessions organiques **avant et après le 18 septembre**.
**Il n'a pas pu être conduit.**

| | |
|---|---|
| Export GA4 disponible | Traffic acquisition, **agrégats par canal**, 01 → 28/09 |
| Ce qu'il contient | 329 sessions organiques sur 28 jours, engagement, key events |
| Ce qu'il ne contient pas | **toute ventilation quotidienne** |
| Décision | Une exploration GA4 dédiée n'a **pas** été construite pour obtenir cette ventilation |

**Conséquences, à respecter strictement :**

1. **Le total GA4 de septembre ne permet ni de confirmer ni d'infirmer le diagnostic pré/post
   18 septembre.** Il agrège 17 jours avant la rupture et 11 jours après, sans les distinguer.
2. **« Le trafic réel n'a pas bougé » n'est PAS un fait établi** et ne doit pas être présenté
   comme tel. Ce rapport ne l'affirme nulle part.
3. La comparaison des trois fenêtres de 28 jours (§5) est **inopérante** pour cette question : les
   fenêtres se recouvrent sur 21 jours et ne sont pas indépendantes.
4. Le seul indice dont nous disposons sur l'impact réel est **interne à GSC** : les clics n'ont
   reculé que de **10 sur la semaine** (56 → 46), contre 2 624 impressions. C'est un indice
   **cohérent** avec une contraction d'exposition sans valeur, **pas une vérification** — les
   clics GSC ne sont pas les sessions GA4.

**Statut : donnée insuffisante.** La question reste ouverte et le restera tant que la ventilation
quotidienne GA4 n'est pas produite.

### Synthèse du mécanisme

| Mécanisme | Statut |
|---|---|
| **Contraction d'exposition sans valeur (US × desktop)** | **Établi comme dominant** — au moins 1 537 des 2 624 impressions perdues, 0 clic net associé |
| **Perte de classement ponctuelle (Where to Stay)** | **Établie** — position par requête 20,1 → 32,0, −7 clics |
| Perte de classement généralisée | **Aucun signal observé dans les données disponibles** — 11/17 pages améliorent leur CTR, 8/17 leur position, 6 pages gagnent des clics |
| Effet des URLs à ancre / PR #147 par ce canal | **Écarté** — 5,8 % de la perte |
| Baisse de la demande de recherche | **Non testable** — aucune donnée de volume de recherche |
| Changement de comptage ou d'affichage côté Google | **Non testable** — Search Appearance vide, pas de croisement pays × appareil |
| **Impact sur le trafic réel (sessions)** | **Non vérifiable** — aucune ventilation quotidienne GA4 disponible |

**Les deux derniers mécanismes restent ouverts** et ne sont pas départageables avec les données
disponibles.

### Coïncidences temporelles — sans attribution

| Date | Événement |
|---|---|
| 15/09 | Déploiement PR #147, puis recrawl de 7 guides |
| 17/09 | Recrawl de Sunset |
| **18/09** | **Rupture des impressions** |
| 18/09 | Recrawl de Where to Stay |

La rupture survient le jour du recrawl de Where to Stay, la seule page en perte de classement
avérée. **Aucune causalité n'est déduite**, et trois éléments s'y opposent : Sunset, recrawlée le
17/09, **progresse de 19,8 %** ; Best Cafés, non recrawlée depuis le 20 août, perd à peine
9,3 % ; et le canal par lequel #147 aurait pu agir — les ancres — ne représente que 5,8 % de la
perte.

## 10. Crawl / indexation / sitemap

### Indexation — au 22/09

| | |
|---|---|
| Pages indexées | **40** |
| Non indexées | **2** |
| Motifs | 1 × « Excluded by 'noindex' tag » · 1 × « Alternate page with proper canonical tag » |
| Découvertes non indexées | 0 |
| Explorées non indexées | 0 |

Le nombre d'indexées est passé de 38 (mi-août) à 40 depuis le 18/08 et n'a plus bougé. Les deux
exclusions sont **intentionnelles** — aucun problème d'indexation.

### Sitemap — au 23/09

Soumis 16/07 · dernière lecture **21/09** · statut Success · **39 URLs découvertes** · 0 vidéo.

⚠️ **Une lecture du sitemap n'est pas un crawl des 39 URLs.** Elle n'est pas utilisée ici comme
preuve de recrawl.

### Crawl — Checkpoint #3, seuil PR #147 du 15/09 05:38:13 UTC

| Statut | Nombre | Pages |
|---|---|---|
| **Recrawl post-#147 confirmé** | **9 / 12** | Romantic Dinner, Best Thai, Breakfast & Brunch, Hin Kong, Sri Thanu, Best Beaches, Thong Sala (tous le 15/09 entre 13:29 et 13:41 ICT), Sunset (17/09), Where to Stay (18/09) |
| **Pas de recrawl post-#147 observé** | **3 / 12** | Things to Do (13/09), Best Restaurants (02/09), **Best Cafés (20/08)** |

### Le point à retenir pour toute interprétation de page

**Best Cafés gagne +1 455 impressions et +17 clics alors que Google ne l'a pas recrawlée depuis le
20 août** — avant l'intervention de maillage du 29/08 et avant #147.

**Fait établi : la progression de cette page ne peut pas s'expliquer par une modification
post-M0 de la page elle-même.** L'explication est ailleurs — évolution de la SERP, maturation de
l'indexation antérieure, ou facteur externe.

Même logique pour **Best Restaurants** (+1 265 impressions, dernier crawl 02/09) et **Things to
Do** (+1 682 impressions, dernier crawl 13/09, avant #147).

**Les trois plus fortes progressions d'impressions du site sont sur des pages sans recrawl
post-#147.**

---

## 11. GSC Generative AI — observation séparée

| | Récent | Précédent | Δ |
|---|---|---|---|
| Impressions | **3 373** | 1 771 | **+1 602 (+90,5 %)** |

**Ce que ce n'est pas** — reprise intégrale des limites consignées dans `gsc-generative-ai-source.md` :

- ❌ **pas du trafic** — ni clics, ni sessions, ni visites ;
- ❌ **pas une mesure de citation par Gemini** ou par un assistant ;
- ❌ **pas le Retrieval Rate** ;
- ❌ **pas la Conditional Citability Rate** ;
- ❌ **les dates calendaires exactes des deux fenêtres ne figurent pas dans l'export** ;
- ❌ **l'onglet Pages diverge** : somme 3 450 / 1 810 contre un total site de 3 373 / 1 771, soit
  +77 / +39 — divergence documentée, non corrigée, et la somme de cet onglet ne peut servir de
  total ;
- ❌ **aucune causalité déductible.**

**Cette hausse ne compense ni ne masque aucune évolution du SEO classique.** Les deux couches sont
mesurées séparément et le restent. Deux pages y reculent d'ailleurs à contre-courant : Sri Thanu
(−32) et la page d'accueil (−19) — les deux mêmes pages qui reculent en SEO classique.

---

## 12. Risques et anomalies

**A1 — L'onglet Pages de l'export GSC ne totalise pas le site.**

| | Récent | Précédent |
|---|---|---|
| Somme onglet Pages | 38 183 | 21 994 |
| Total site (Devices / Countries) | 27 078 | 17 885 |
| Écart | **+11 105** | **+4 109** |

Cause identifiée : **73 des 125 lignes sont des URLs à ancre** (`…html#sunset-quick-picks`). Elles
portent **9 140 impressions récentes contre 2 395 avant** et **0 clic** dans les deux périodes.
Hors ancres, la somme retombe à 29 043 / 19 599 — un écart résiduel de +1 965 / +1 714 qui reste
inexpliqué.

→ **Ne jamais utiliser la somme de l'onglet Pages comme total.** Ce rapport utilise `Devices`.

**A1 bis — Le phénomène persiste dans l'export du 29/09.** 73 des 128 lignes sont des URLs à
ancre, portant **12 887 impressions et 0 clic**. Somme hors ancres 50 280 contre 46 659 au total
site : écart résiduel +3 621. Même conclusion — utiliser `Devices`.

**A2 — Croissance des impressions sur fragments : ×3,8.** 2 395 → 9 140. Dix pages ont entre 6 et
11 variantes d'URL. **Observation**, pas conclusion : les ancres de titres existaient déjà
partiellement avant PR #147, qui n'a étendu la profondeur d'IDs aux H4 que le 15/09, soit 4 jours
sur 28. **Hypothèse à tester**, non attribuable en l'état.

**A3 — CTR en baisse malgré des positions en hausse.** CTR global 1,04 % → 0,84 % pendant que la
position moyenne s'améliore sur presque tous les clusters. Compatible avec un élargissement vers
des requêtes moins qualifiées (`near me`, noms d'établissements tiers) — **hypothèse**.

**A4 — Érosion du socle de marque.** Branded : −4 clics, −25 % d'impressions. `dar mansour -
morocco's kitchen` : clics ÷2 en gagnant 0,8 position. **Anomalie non expliquée par les données
disponibles.**

**A5 — Engagement en chute.** 47 s → 32 s au global ; page d'accueil 55 → 31 s ; Best Restaurants
82 → 34 s. Key events 13 → 11. Cohérent avec A3 : plus de visiteurs moins qualifiés.

**A6 — Pages de listing effondrées.** `/blog.html` 175 → 90, `/koh-phangan-guide.html` 86 → **3**,
`/journal-authors.html` 50 → **0**. À surveiller : perte de rôle de hub.

**A7 — Onglet Queries tronqué à ~20 % du volume.** Toute analyse de requête est partielle.

---

## 13. Hypothèses à tester

| # | Hypothèse | Ce qui la testerait |
|---|---|---|
| H1 | Une baisse réelle s'est produite après le 18/09 | Export GSC journalier couvrant 19–29/09 (§14 n° 1) |
| H2 | La dilution du CTR vient de l'élargissement vers des requêtes non qualifiées | Export Queries avec position + CTR sur les nouvelles requêtes uniquement |
| H3 | La perte de clics de marque vient d'un changement de SERP sur la requête (pack local, avis, sitelinks) | Inspection de la SERP `dar mansour - morocco's kitchen` + onglet Search Appearance détaillé |
| H4 | La chute du CTR de Sri Thanu est liée à un changement de titre ou de snippet | Historique du title/meta de la page + vérification de la SERP |
| H5 | Les impressions sur fragments sont liées à l'extension des IDs de titres | Export Pages sur une fenêtre postérieure au 15/09 uniquement |
| H6 | La baisse d'engagement est un effet de composition (nouvelles pages, nouveau public) | GA4 engagement par page × source, fenêtre identique |

**Aucune de ces hypothèses n'est retenue comme établie.** Aucune évolution n'est attribuée à
`9708db8`, `1de3ddb`, PR #144 ou PR #147.

---

## 14. Données supplémentaires — état final

Quatre exports ont été fournis et exploités. **Le rapport est finalisé en l'état**, avec une
limite assumée et documentée.

### Ce qui a été obtenu

| Export | Apport |
|---|---|
| GSC Performance 23/09 (28 j vs 28 j) | Performance globale M0 → M1, pages, requêtes |
| GSC Performance 29/09 (quotidien 01/08 → 25/09) | **Date exacte de la rupture** + dates des fenêtres du 23/09 |
| GSC Performance 29/09 (19–25/09 vs 12–18/09) | **Localisation exacte** : pages, requêtes, pays, appareils |
| GA4 Traffic acquisition (01 → 28/09) | Agrégats canaux de septembre |

### Ce qui manque, et qui ne sera pas demandé

**GA4 sessions organiques quotidiennes.** C'était le test décisif de l'impact réel. Sa production
exigeait une exploration GA4 dédiée, **que nous avons choisi de ne pas construire**. La question
de l'impact sur le trafic reste donc **ouverte et documentée comme telle** (§9, encadré
« Limite GA4 »), et non résolue par défaut dans un sens ou dans l'autre.

Si cette question devient déterminante pour une décision, l'élément requis est : GA4 → Explorer ·
dimension **Date** · métriques Sessions, Utilisateurs actifs, Durée d'engagement, Key events ·
période **01/09 → 29/09** · filtre `Session default channel group` = `Organic Search`.

### Ce qui ne sera pas obtenable

- **Croisement pays × appareil** — GSC ne l'exporte pas. La borne de 1 537–1 771 impressions sur
  l'intersection US × desktop est ce que la donnée autorise, et ne sera pas affinée.
- **Volume de recherche** — aucun export GSC ne l'expose. Départager « moins d'impressions parce
  que moins de recherches » de « moins d'impressions par décision de Google » exigerait une source
  tierce, hors périmètre.
- **Changement de comptage ou d'affichage côté Google** — non observable de l'extérieur. L'onglet
  Search Appearance du comparatif est **vide**.

### Action non-export recommandée

**Inspection manuelle de la SERP `where to stay in koh phangan`** — seul déclassement avéré
(position 20,1 → 32,0). Aucun export ne dira pourquoi. Relever : qui occupe les positions 15–25,
présence d'un AI Overview, d'un pack local ou d'un carrousel hôtels. Compléter par GSC → URL
Inspection sur `journal-where-to-stay-koh-phangan.html` pour vérifier qu'aucun changement
d'indexation ou de canonique n'est intervenu depuis le crawl du 18/09.

## 15. Conclusions SEO provisoires

**Fait établi.**
1. Sur 24/08 → 20/09 vs 27/07 → 23/08 : impressions +51,4 %, clics +22,6 %, sessions organiques
   +12,7 %, CTR −19 %, engagement 47 s → 32 s, key events 13 → 11.
2. **Une rupture d'impressions est survenue le 18 septembre** : −36,4 % d'une semaine à l'autre,
   puis plateau stable sur huit jours. **Confirmée par la série quotidienne GSC.**
3. **La perte est massivement concentrée sur le croisement États-Unis × desktop.** Desktop
   −57,9 %, États-Unis −69,5 %. **Au moins 1 537 des 2 624 impressions perdues** appartiennent aux
   deux segments à la fois.
4. **Cette exposition ne produisait pas de clics** : les États-Unis généraient 2 756 impressions
   pour **2 clics** (CTR 0,07 %) et en génèrent désormais **0**.
5. La Thaïlande — seul marché commercialement pertinent — perd 467 impressions et **2 clics**, en
   **améliorant** CTR (1,31 → 1,52 %) et position (7,99 → 7,50).
6. **Aucun signal de déclassement généralisé n'est observé dans les données disponibles** :
   11 pages sur 17 améliorent leur CTR, 8 leur
   position, 6 gagnent des clics. Sunset **+19,8 %** d'impressions, Hin Kong **+59,2 %**.
7. **Une seule page subit une perte de classement réelle** : Where to Stay, −89,5 % d'impressions,
   **7 des 10 clics nets perdus**, requête principale **20,1 → 32,0**.
8. **Les URLs à ancre ne sont pas en cause** : 5,8 % de la perte.
9. Indexation saine : 40 indexées, 2 exclusions volontaires.

**Observation.**
- Le site a perdu de l'exposition GSC ; le CTR global remonte de 0,78 % à 1,00 %.
- Les impressions américaines affichaient une position moyenne de 7,33 pour un CTR de 0,07 % —
  plus de dix fois sous ce qu'une position 7 produit normalement.
- Best Restaurants perd 581 impressions **et gagne un clic** ; Thong Sala perd 336 impressions
  **et gagne deux clics**.
- Key events et engagement reculent sur trois fenêtres successives (13 → 11 → 7 et
  47 s → 32 s → 29,7 s), **indépendamment** de la rupture du 18 septembre.

**Donnée insuffisante — et le restera.**
- **L'impact de la rupture du 18 septembre sur le trafic réel.** Aucun export GA4 disponible ne
  ventile les sessions par jour ; le total de septembre agrège 17 jours avant et 11 jours après
  sans les distinguer. **« Le trafic réel n'a pas bougé » n'est pas un fait établi** et n'est
  affirmé nulle part dans ce rapport. Les −10 clics GSC sont un indice cohérent, pas une preuve.
- La valeur exacte de l'intersection US × desktop — GSC n'exporte pas ce croisement.
- La cause du déclassement de Where to Stay.
- Une éventuelle baisse de la demande de recherche.
- Un éventuel changement de comptage ou d'affichage côté Google.

**Aucune causalité n'est établie**, et aucune évolution n'est attribuée à `9708db8`, `1de3ddb`,
PR #144 ou PR #147. Trois éléments s'opposent d'ailleurs à une attribution à #147 : Sunset,
recrawlée le 17/09, progresse ; Best Cafés, non recrawlée depuis le 20 août, perd à peine 9 % ; et
le canal des ancres ne pèse que 5,8 % de la perte.

### Ce que ce rapport autorise à conclure — et ce qu'il n'autorise pas

| Question | Réponse |
|---|---|
| Y a-t-il eu une baisse ? | **Oui — des impressions GSC, à partir du 18/09** |
| Est-elle localisée ? | **Oui — US × desktop, plus Where to Stay** |
| **Déclassement généralisé observé ?** | **Non dans les données disponibles.** |
| Est-ce un problème de classement ponctuel ? | **Oui — Where to Stay, une page** |
| Le trafic réel a-t-il baissé ? | **Non vérifiable avec les données disponibles** |
| La cause de la contraction d'exposition ? | **Ouverte** |

## 16. État du benchmark GEO — encore incomplet

| Volet | État |
|---|---|
| Serper M1 | **20/20 — complet** |
| Retrieval M0 → M1 | **analysé et documenté** (`m0-m1-retrieval-gap-analysis.md`) |
| **Gemini M1** | **31/60 — 29 générations manquantes**, limitées par quota |
| Conditional Citability Rate M1 | ⛔ **non calculée** |
| Conclusion GEO globale | ⛔ **non produite** |

**Les 31 générations disponibles ne sont pas extrapolées aux 60 prévues.** Aucun taux de sélection
M1, aucune Conditional Citability, aucune conclusion GEO ne figure dans ce rapport.

Pour mémoire, le seul résultat GEO établi à ce jour est le volet Retrieval : Retrieval Rate
6/20 = 30 % à M0 comme à M1, avec deux entrées (prompts 10 et 12) et deux sorties (07 et 14) —
**un taux identique à composition changée, ce qui n'est pas une stabilité générale**.

**Le GSC Generative AI (§11) n'est en aucun cas un substitut au benchmark GEO contrôlé.**

---

_Rapport provisoire. Aucun appel Serper ni Gemini, aucune modification du site, aucun changement de
protocole, aucune donnée brute privée ajoutée au dépôt, aucun score SEO artificiel._
