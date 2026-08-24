# AI Referral Traffic (GA4) — niveau 2 du dispositif GEO

## Ce que cette mesure est, et n'est pas
**AI Referral Traffic** = sessions arrivant sur darmansour.com depuis une plateforme IA
**identifiable dans GA4**.

**Ce n'est PAS un nombre de citations IA.** Une citation peut ne générer aucun clic ; un clic IA
peut perdre son référent et apparaître en `direct` ou sous une autre source.
→ **`0 Gemini identifiable` n'est pas une preuve de `0 trafic Gemini réel`.** Idem Copilot.

Les quatre niveaux sont **strictement séparés et ne s'additionnent jamais** :

| Niveau | Mesure | Source |
| --- | --- | --- |
| 1 | AI Citations | Bing Webmaster Tools / AI Performance |
| **2** | **AI Referral Traffic** | **GA4** |
| 3 | AI Crawl / Retrieval | à venir |
| 4 | Model Brand Knowledge | benchmark Gemini ungrounded (`tools/geo_tracker.py`) |

## Protocole GA4 — figé, ne jamais substituer
Deux exports, **du même rapport**, pour la même période :

1. `Reports → Acquisition → Traffic acquisition`
   dimension principale **Session source / medium**, secondaire **Landing page + query string**
2. Le **même rapport**, dimension secondaire **Event name** (pour `contact_click`)

Ne **jamais** utiliser *User acquisition*, *First user source/medium*, ni un autre modèle
d'attribution : cela changerait la métrique.

## Règles de calcul
- **Dénominateur** = somme des lignes de l'export brut du round. Jamais un total lu ailleurs dans GA4.
- **Détection** = liste explicite et versionnée (`tools/ai_referral_sources.json`), **jamais** le seul
  channel group `ai-assistant` : Perplexity arrive en `perplexity / (not set)` et y échappe.
  Toute évolution de la liste change sa `version` **et impose de recalculer les rounds antérieurs**,
  sinon une hausse ne serait qu'un effet de détection.
- **Landing pages** agrégées sur le chemin avant `?` (`fbclid`, `hl`… fragmenteraient une même page).
- **Contact** : `contact_sessions` vient de l'export **événements**. La colonne `Key events` de
  l'export trafic compte des **événements** — en M0, 2 `contact_click` viennent d'**une seule
  session** ChatGPT. Ne jamais écrire « 2 clients », « 2 leads » ni « 2 conversions ».
- **Temps moyen** repondéré par les sessions à chaque réagrégation.

## Comparabilité des rounds
M0 est une période historique de **56 jours** (2026-07-01 → 2026-08-25). À partir de M1 :
**mois calendaires complets** (M1 = septembre 2026, M2 = octobre, M3 = novembre). Pas de fenêtre
glissante. Les durées différant, **toujours comparer via `Sessions / Day`**, jamais via les sessions
brutes seules. Petits volumes : 5 → 10 sessions ne prouve pas un doublement de visibilité — chercher
la tendance sur plusieurs mois et la **distribution par landing page**, plus stable que les totaux.

## Archivage — raw immutable → traitement → agrégat
```
data/ga4/M0/
  round.json                                        # période, exports, protocole
  Traffic_acquisition_Session_source_medium.csv     # brut, jamais modifié
  Events_Session_source_medium_x_Event_name.csv     # brut, jamais modifié
data/ga4/Dar_Mansour_AI_Referral_Traffic.xlsx       # généré, tous rounds cumulés
```
Un round doit rester recalculable des années plus tard **sans retourner dans GA4**.

## Utilisation
```bash
python3 tools/ai_referral.py test                    # tests d'acceptation M0 (22)
python3 tools/ai_referral.py report --round M0 --dry-run
python3 tools/ai_referral.py report                  # tous les rounds -> classeur
```
Aucun appel API GA4 : l'export manuel suffit à la cadence actuelle (4 rounds/an).

## Importer M1 (septembre 2026)
1. Dans GA4, période **2026-09-01 → 2026-09-30**, faire les **deux** exports du protocole ci-dessus.
2. `mkdir data/ga4/M1` et y déposer les deux CSV **sans les modifier**.
3. Copier `data/ga4/M0/round.json` vers `data/ga4/M1/round.json`, puis ajuster `round`,
   `period_start`, `period_end` et les deux noms de fichiers.
4. `python3 tools/ai_referral.py report` — les deux rounds apparaissent dans le classeur.
5. Vérifier que `Detection Rules Version` est identique entre M0 et M1. Si la liste a changé,
   recalculer M0 avec la nouvelle version avant toute comparaison.
