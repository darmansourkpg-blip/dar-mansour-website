# Qualification off-site — état figé avant M1

**Statut : document de qualification, figé avant la mesure M1.** Il consolide trois sources
distinctes qui ne doivent jamais être fusionnées ni utilisées pour en déduire une causalité :

| Couche | Source | Ce qu'elle établit |
|---|---|---|
| **Observation** | Benchmark L3 M0 (corpus Serper) | Quels domaines apparaissent dans les SERP mesurées, à quel rang |
| **Contexte** | Fichier Backlink Outreach + audit Gmail | Quelles relations et sollicitations externes existent réellement |
| **Vérification** | Recherche web manuelle | Quels domaines mentionnent déjà Dar Mansour, dans quel contexte |

**Chaîne de qualification : M0 observe → Outreach/Gmail contextualise → Web vérifie →
qualification C/D → décision d'action.**

Aucune coïncidence entre une action d'outreach et un mouvement de retrieval ne constitue une
causalité. Le fichier Backlink Outreach est la **master source de l'historique off-site** ; il ne
remplace pas M0, qui mesure le retrieval.

---

## 1. Classification employée

| Code | Définition |
|---|---|
| **A** | Déjà contacté + Dar Mansour désormais mentionné → maintenir la relation, **pas de cold outreach** |
| **B** | Déjà contacté + aucune mention → relance uniquement si l'importance M0 est forte **et** qu'aucune relance récente n'a eu lieu |
| **C** | Jamais contacté (ou aucun outreach retrouvé) + mentionne déjà Dar Mansour → **corroboration organique potentielle : documenter avant toute action** |
| **D-CANDIDATE** | M0 relevant / no prior outreach found / current DM mention not yet verified |
| **D CONFIRMED** | Après vérification web : aucune mention trouvée |
| **INCONCLUSIVE** | Vérification impossible à conclure proprement |

### Réserve permanente sur `NO MENTION FOUND (search-verified)`

Cette mention signifie **uniquement qu'aucune mention n'a été trouvée avec notre méthode de
recherche**. Ce n'est **jamais** la preuve qu'aucune page n'existe : une page peut être non
indexée, trop récente, bloquée aux crawlers, ou formulée de manière non détectable. Tout
`D CONFIRMED` de ce document est donc **confirmé opérationnellement**, pas absolument.

### Champ `Strategic purpose`

`GEO corroboration | SEO authority | Referral business | Concierge relationship | PR | Brand awareness`

Une cible absente de M0 **n'est pas** une mauvaise cible. M0 mesure le retrieval sur 20 requêtes ;
une villa, un resort ou un concierge peut avoir une forte valeur commerciale, de referral ou de
notoriété sans jouer le moindre rôle observable dans M0.

---

## 2. Constat structurant — l'ancienne liste et M0 se recoupent peu

Sur les **30 cibles** du fichier Backlink Outreach, **11 seulement apparaissent dans les corpus
M0** : Phanganist, Phangan Life, Global Gallivanting, Tristan Balme, Adventures of Jellie, Tiki
Beach, Traveler's Itch, Type1 Travelling, The Froggy Adventures, Anantara, phangan.events.

**19 sur 30 n'ont aucune présence M0.** Elles avaient été retenues sur l'autorité de domaine et le
statut dofollow — critères désormais abandonnés comme critère principal.

Ce chiffre démontre que la stratégie « DA / backlinks » et la stratégie GEO ne sont **pas** la même
chose. Il ne disqualifie pas les 19 autres : il impose de leur attribuer un `Strategic purpose`
autre que `GEO corroboration`, où leur absence de M0 est normale et non un signal négatif.

---

## 3. Relations établies — aucun cold outreach

| Cible | Classe | Statut réel | Valeur M0 | Conduite |
|---|---|---|---|---|
| **Phanganist** | A | Relation éditoriale établie + publication obtenue | 4 app · 3 Top-3 | Maintenir ; vérifier l'exactitude du listing. **Plus une cible cold.** |
| **Phangan Life** | A | Listing obtenu + relation directe (Sergei) | 2 app | Maintenir et optimiser l'existant. Pas de nouvelle demande de listing. |
| **Adventures of Jellie** | B chaud | **Réponse positive** — ont regardé le menu, souhaitent venir essayer Dar Mansour | **6 app · 6 Top-3 · #1 sur 01, 02, 03, 08, 09** | **Attendre une vraie visite. Aucune sollicitation SEO/backlink.** Préserver leur indépendance éditoriale. |
| **Global Gallivanting** | B chaud | **Réponse positive d'Anna** — souhaite découvrir DM lors de son prochain passage | 3 app · **3 Top-3** | Même règle : relation chaude, **pas de demande de backlink**. |
| **Tiki Beach** | B | Contact + follow-up effectués | 5 app | Attendre. Pas de nouvelle relance. |
| **La Favela / Pearl Properties** | B | Intérêt réel, mais modèle à commission — DM a décliné | — | **Ne pas répéter le même pitch.** Rouvrir seulement sur un angle non commissionné réellement nouveau. |
| **Thailand Vloggers** | — | Ne fonctionnent pas comme plateforme promotionnelle | — | **Sortir du cold outreach média.** Garder en référence écosystème. |
| **Anantara Rasananda** | B | Contacts juin 2025 puis juillet/août 2026 | 1 app (prompt 08) | **Ne pas solliciter à nouveau.** |
| **Bay Villas · Santhiya · Kupu Kupu** | B | Contacts répétés dans le temps + follow-up | 0 | Attendre. Ne pas dupliquer. `Strategic purpose` = Concierge / Referral. |
| **Nomadic Matt · Southeast Asia Backpacker** | B | Contact + follow-up ; pas de réponse positive | 0 | Pas de nouvelle relance actuellement. |
| **TravelTriangle** | B | Contact confirmé, aucune réponse retrouvée | 0 | Faible priorité. |
| **The Broke Backpacker** | — | Gmail confirme surtout une **inscription newsletter automatique** | 0 | **Ne pas considérer l'outreach éditorial comme vérifié** sans preuve supplémentaire. |

### `OUTREACH SHEET SAYS CONTACTED / GMAIL NOT CONFIRMED`

Plusieurs cibles portent `email sent` au tableur sans trace Gmail. Elles sont classées ainsi — et
**non** « jamais contactées » : un formulaire web ou un autre canal a pu être utilisé. Concernées :
We Love Koh Phangan, The Froggy Adventures, On a Hammock, Type1 Travelling, Traveler's Itch,
Aritra Bose (Medium), **Tristan Balme**.

**Tristan Balme — `OUTREACH HISTORY VERIFICATION — HIGH PRIORITY`.** 9 apparitions M0 (la 2e
présence éditoriale des corpus), mais outreach non confirmé. **Vérifier d'abord le canal
historique** (email, formulaire, autre) avant d'envisager tout nouveau contact. Envoyer un email
de plus sans savoir lequel a déjà été envoyé serait une erreur de méthode.

---

## 4. Secret Mountain Phangan — cas témoin

**Classification : `C — EXISTING MULTI-INTENT EDITORIAL CORROBORATION`**

| Champ | Valeur |
|---|---|
| Mention status | **MENTION FOUND** |
| Pages identifiées | **≥ 5** |
| Earliest observable publication date | **2026-08-04** |
| Recommendation vs simple mention | **RECOMMENDATION** |
| Intents corroborated | Best Restaurants · Where to Eat · Romantic · Fine Dining · Birthday · Special Occasion |
| Outreach history | **Aucun outreach retrouvé** (fichier historique + audit Gmail) |
| Organic status | **UNKNOWN** — l'absence d'outreach retrouvé n'est pas une preuve d'absence d'outreach |
| Strategic purpose | GEO corroboration |
| Confidence | **HIGH** pour la corroboration actuelle · **UNKNOWN** pour l'origine organique |
| Next action | **DO NOT CONTACT — préserver comme cas d'observation** |

**Pourquoi ce cas est précieux :** les intentions corroborées — Best Restaurants, Where to Eat,
Romantic, Special Occasion — recouvrent précisément les gaps M0 où Dar Mansour est
`NOT_RETRIEVED`. Et il s'agit de **recommandations**, pas de simples mentions en liste.

**Deux limites à ne pas franchir :**

1. **L'origine organique n'est pas établie.** Aucun outreach retrouvé ≠ aucun outreach. Le statut
   reste `UNKNOWN`, et le document ne doit pas laisser croire l'inverse dans six mois.
2. **La chronologie ne démontre rien à ce stade.** La première publication observable
   (2026-08-04) est **postérieure** au lancement du Journal Dar Mansour (juillet 2026) et à la
   vague d'outreach de juillet 2026 adressée à d'autres cibles. Elle n'établit donc **pas** une
   antériorité qui prouverait la spontanéité. Elle ne l'exclut pas non plus.

**Ne pas contacter.** La valeur de ce cas tient entièrement à ce qu'il n'a pas été touché : c'est
notre seul exemple documenté de corroboration éditoriale multi-intentions dont l'origine n'est pas
une sollicitation connue. Un contact détruirait irréversiblement cette propriété.

---

## 5. `D CONFIRMED` — vérification web effectuée

Les 20 D-CANDIDATES ont été vérifiés : **`NO MENTION FOUND (search-verified)` pour les 20**, donc
**`D CONFIRMED` opérationnellement**, sous la réserve permanente du §1.

Portée exacte de cette observation :

> Among the 20 D-CONFIRMED domains examined, no indexed Dar Mansour mention was found during the
> web verification. This observation applies only to this qualified subset of M0 domains and must
> not be generalized to all domains appearing ahead of Dar Mansour in M0.

> The absence of Dar Mansour from these pages and the absence of darmansour.com from the
> corresponding SERPs are two distinct observations. No causal relationship is inferred.

Le sous-ensemble vérifié exclut notamment les domaines classés `OUTREACH SHEET SAYS CONTACTED /
GMAIL NOT CONFIRMED` (dont Tristan Balme, 9 apparitions M0), les relations déjà établies, et
l'ensemble des domaines UGC et plateformes des corpus.

### D1 — cluster Food : deux gaps M0 distincts, aucun classement global

Meagan Lyn et East London Girl répondent à **deux problèmes différents**. Aucun arbitrage entre
elles n'est établi ni souhaitable.

| Domaine | M0 | Prompts | Best rank | Gap M0 visé |
|---|---|---|---|---|
| **eastlondongirl.com** | 3 app | 01, 02, 03 | 4 | **Generic Food authority** — les trois intentions Food génériques où Best Restaurants échoue |
| **meaganlyn.com** | 2 app · **2 Top-3** | 03, 10 | **3** | **West Coast / local relevance** — #3 sur *west coast restaurants*, soit Hin Kong / Sri Thanu, notre zone exacte |
| **julychoo.com** | 3 app | 01, 02, 03 | 7 | Generic Food — même couverture qu'East London Girl, rangs nettement plus faibles. **Candidat suivant.** |

### D2 — autorité destination multi-cluster

| Domaine | M0 | Prompts | Best rank |
|---|---|---|---|
| northabroad.com | 3 app · 1 Top-3 | 11, 16, 17 | 1 |
| travelfish.org | 2 app · 1 Top-3 | 15, 16 | ≤ 3 |
| timetravelturtle.com | 1 app · Top-3 | 17 | ≤ 3 |

### D3 — éditorial mono-cluster

| Domaine | M0 | Prompts | Best rank | Cluster |
|---|---|---|---|---|
| backpackerswanderlust.com | 2 app · **2 Top-3** | 11, 12 | ≤ 3 | Beaches |
| gotothailand.com | 2 app · 1 Top-3 | 11, 12 | ≤ 3 | Beaches |
| thousandtravelmiles.nl | 1 app · Top-3 | 11 | ≤ 3 | Beaches |
| 22places.com | 2 app | 15, 16 | > 3 | Stay |
| abeachcreature.com | 1 app | 11 | > 3 | Beaches |
| themanduls.com | 1 app | 12 | > 3 | Beaches |
| kateandmikestravels.com | 1 app | 12 | > 3 | Beaches |
| travelmermaid.com | 1 app | 15 | > 3 | Stay |
| roads-and-rivers.com | 1 app | 17 | > 3 | Things to Do |
| homeiswhereyourbagis.com | 1 app | 17 | > 3 | Things to Do |
| nomadwise.io | 1 app | 10 | > 3 | Cafés |

### D4 — entreprises locales classant éditorialement (logique distincte de l'outreach média)

| Domaine | M0 | Prompts | Best rank | Note |
|---|---|---|---|---|
| **explorarhotels.com** | 1 app | **08** | 6 | **Seule cible D du cluster Special Occasion.** Blog d'hôtel alignant *romantic + couple + celebration + private beachfront*. |
| eclipsehostel.com | 2 app | 11, 12 | > 3 | Business local classant sur du contenu éditorial |
| bubbascoffee.com | 1 app | 10 | > 3 | Idem |

Les rangs notés `≤ 3` / `> 3` sont des **bornes établies** (position Top-3 connue, rang exact non
conservé dans l'extraction minimale des corpus). Ils ne sont pas approximés.

---

## 6. Segment Tajine — hors campagne off-site locale actuelle

Les prompts **18–20 restent intégralement dans le benchmark L3 et dans le Retrieval Rate officiel
M0 6/20 = 30 %**. Leur exclusion de la vague d'outreach actuelle est uniquement une **segmentation
opérationnelle** : les domaines gagnants (Wikipedia, My Moroccan Food, Le Creuset, Serious Eats,
dictionnaires, médias food internationaux) répondent principalement à une intention
informationnelle et culturelle internationale, différente du problème de corroboration locale
Koh Phangan. **Aucune reclassification rétroactive de ces prompts vers un autre niveau GEO.**

Aucun de ces domaines n'a été contacté. `mymoroccanfood.com` et `ksarighnda.com` sont les seules
entités marocaines du segment et pourraient relever, à très long terme, de la corroboration
d'entité — jamais d'un pitch backlink.

---

## 7. Règle de priorisation en vigueur

Ne plus classer les opportunités principalement selon le DA ou le statut dofollow. Séparer :

**SEO link authority · entity corroboration · editorial recommendation · local topical authority ·
referral traffic.**

Pour le chantier GEO actuel, une **mention éditoriale pertinente sur un véritable guide
Koh Phangan** peut valoir davantage qu'un backlink dofollow sur un domaine générique.

La priorité croise : `M0 presence + local/topic relevance + existing Dar Mansour corroboration +
outreach history + relationship status + opportunity for genuine editorial coverage`.

---

## 8. Décision opérationnelle — aucun outreach avant M1

**Aucune sollicitation n'est lancée avant la mesure M1.** Trois raisons :

1. Le site est sous **gel total** jusqu'à M1 (voir `docs/geo/m1-plan.md`, §7). Une vague
   d'outreach pendant la fenêtre de mesure introduirait une seconde variable et rendrait M1
   illisible — exactement ce que le pré-enregistrement cherche à éviter.
2. Les deux relations les plus précieuses (Adventures of Jellie, Global Gallivanting) sont en
   attente d'une **visite réelle**. Une relance les dégraderait.
3. Secret Mountain doit rester intact comme cas d'observation.

Ce que ce document autorise après M1, et rien d'autre : ouvrir une vague ciblée sur les
`D CONFIRMED`, en priorité `eastlondongirl.com` (Generic Food) et `meaganlyn.com` (West Coast),
puis `julychoo.com` — et vérifier le canal historique de Tristan Balme.

**Interdits permanents :** acheter des liens, fabriquer des mentions, échanger un backlink contre
une contrepartie dissimulée, ou solliciter un avis. Aucune expérience de première main
fabriquée, aucune visite inventée.

---

_Document de qualification off-site. Aucune modification de `site/`, aucune donnée M0 altérée,
aucun outreach lancé, aucun rebuild, aucun déploiement._
