# GEO Citability Benchmark — niveau 3 du dispositif GEO

> **This benchmark measures the retrievability and citability of darmansour.com against a real
> search corpus retrieved through Serper/Google and evaluated by Gemini. It does not reproduce the
> proprietary grounding systems of ChatGPT, Gemini, Copilot, Claude or Perplexity.**

Ce n'est **jamais** « Gemini Grounding », « citations ChatGPT », « AI Overview performance » ni
« citations Copilot ». C'est **notre pipeline expérimental versionné**.

## Deux étapes strictement séparées

**A — Retrieval** : le prompt part **verbatim** vers Serper (corpus Google réel).
darmansour.com apparaît-il, à quel rang, avec quelles URLs ?

**B — Selection** : ce corpus **exact** est fourni à Gemini 3.6 Flash, **sans aucun outil de
recherche**. Gemini choisit-il nos sources pour répondre ?

| Retrieval | Selection | Diagnostic |
| --- | --- | --- |
| NO | NO | `NOT_RETRIEVED` |
| YES | 0/3 | `RETRIEVED_NOT_SELECTED` |
| YES | 1/3 ou 2/3 | `RETRIEVED_PARTIALLY_SELECTED` |
| YES | 3/3 | `RETRIEVED_STABLY_SELECTED` |
| NO | oui | `ANOMALY` — à investiguer |

`RETRIEVED_NOT_SELECTED` ne signifie **jamais** « mauvais contenu » : le rang dans le corpus est un
confondant (une source en #2 n'a pas la même exposition qu'en #17). Le rang de retrieval est donc
conservé à côté de chaque décision.

## Trois métriques de sélection, jamais confondues

| Métrique | Sens |
| --- | --- |
| `selected_source` | Gemini a **utilisé une de nos URLs** comme source |
| `mentioned_in_answer` | la marque est **nommée** dans le texte de la réponse |
| `recommended` | la marque figure parmi les **établissements recommandés** |

Un de nos guides peut servir de source pour recommander un **concurrent** : `selected_source` sans
`recommended`. C'est un cas réel, et il doit rester visible.
**Le `Conditional Citability Rate` utilise `selected_source`, jamais la mention du nom.**

## Protocole figé (tout changement = rupture de protocole)

| | |
| --- | --- |
| Provider | `serper` (corpus Google) |
| Localisation | `gl=th`, `hl=en`, pas de `location` |
| Query mode | **verbatim** — aucune réécriture en requêtes de recherche |
| Profondeur | 20 demandés, **aucune pagination** ; `actual_depth` enregistré |
| Modèle | `gemini-3.6-flash`, **sans Google Search tool**, `temperature=0` |
| Runs | 3 par prompt, sur le **même corpus figé et hashé** |
| Prompts | les 20 de `tools/geo_prompts.json`, hashés |
| Prompt de sélection | `tools/geo_citability_selection_prompt.txt`, versionné et hashé |

Le prompt de sélection est un **instrument de mesure** : il ne nomme jamais Dar Mansour, ne
mentionne jamais notre domaine, et chaque résultat y porte un identifiant **neutre** `S01…S20`.
Le script seul sait que `S04 → darmansour.com`.

Le round enregistre son protocole au premier appel. Toute divergence ultérieure **bloque
l'exécution** avec la liste des écarts (`--force-protocol` pour outrepasser en connaissance de cause).

## Stockage — le dépôt est public

Les conditions contractuelles Serper sur la rediffusion **ne sont pas établies**. En V1, posture la
plus restrictive :

| Hors dépôt (privé) | Dans le dépôt (public) |
| --- | --- |
| réponses Serper brutes | prompt ID, requête |
| snippets tiers | retrieved YES/NO, best rank |
| titres tiers | nos URLs, nombre d'URLs owned |
| domaines concurrents | Top 3/5/10/20, profondeurs |
| réponses Gemini brutes | corpus hash, métriques de sélection, protocole |

Raw par défaut : `~/.dar-mansour-geo/citability/<ROUND>/`.
**Le script refuse de démarrer si le chemin raw est situé dans le dépôt** — `.gitignore` ne suffit
pas, `git add -f` passe outre. Le SHA-256 du corpus, lui, est versionné : il prouve que les 3 runs
ont vu le même input sans rien republier.

## Garde-fous

- Plafonds durs : **20 recherches, 60 générations** par round. Un dépassement est refusé.
  Les retries techniques sont comptés séparément.
- `429` → quota épuisé → **STOP reprenable**, jamais de repli payant.
  `401/403 billing`, `402` → **STOP immédiat**. `401/403` → auth → **STOP**. `5xx`/réseau → retry limité.
- Aucun appel réseau à l'import. `report` et `status` ne cherchent jamais ; un corpus manquant est
  **signalé**, jamais récupéré automatiquement.
- Clés uniquement en variables d'environnement (`SERPER_API_KEY`, `GEMINI_API_KEY`), jamais
  commitées ni loggées — `redact()` couvre la clé exacte, les motifs `AIza…`/`AQ.…` et tout `?key=`.
- Reprise : un corpus existant n'est **jamais** re-cherché (cela changerait le corpus et casserait
  la comparabilité des 3 runs). Un run terminé n'est jamais rejoué.

## Utilisation

```bash
python3 tools/geo_citability_tests.py            # 101 tests, aucun réseau
python3 tools/geo_citability.py dry-run --round M0   # plan complet, aucun appel
python3 tools/geo_citability.py check                # hors ligne par défaut
python3 tools/geo_citability.py check --live         # 1 recherche + 1 génération
python3 tools/geo_citability.py run --round M0       # M0 réel (reprenable)
python3 tools/geo_citability.py status --round M0
python3 tools/geo_citability.py report --round M0
```

## Ne pas sur-interpréter M0

Absent du Top 20 → problème de **retrievability dans ce corpus**. Présent mais non sélectionné →
faible sélection **dans notre protocole**, potentiellement liée au contenu, au snippet, à la source,
**au rang** ou à d'autres facteurs. Présent et sélectionné → bonne performance **dans notre
benchmark**. Aucune de ces observations ne prouve ce que ChatGPT, Gemini Search, Copilot ou
Perplexity montreront à un utilisateur réel.

## Prévu, non implémenté

Comparaison M0→M3 · contrôle multi-moteurs · expérience à ordre randomisé (position-controlled) ·
grounding queries réelles issues de Bing AI Performance (benchmark B, série séparée) · competitor
scoring · automatisation mensuelle. Aucun score GEO composite : les quatre niveaux ne s'additionnent pas.
