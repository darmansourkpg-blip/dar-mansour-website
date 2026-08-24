# GEO Tracker — mode d'emploi

Mesure la visibilité de Dar Mansour dans les réponses IA, de façon **reproductible et gratuite**.

## Deux modes de mesure

### `ungrounded` (défaut — le seul actif)
**Gemini API ungrounded visibility benchmark.** Gemini 3.6 Flash répond **sans outil de recherche** :
on mesure ce que le modèle sait de Dar Mansour **par lui-même**, pas ce qu'il citerait après une
recherche web. Gratuit, aucun appel facturable possible.

Mesuré : `Mention Frequency` · `Average Position When Mentioned` · `GEO Stability` ·
`Competitor Frequency`.
**Non mesuré, et marqué `N/A — no grounding` partout** : citations, URLs de darmansour.com, sources
externes, requêtes Google. Ces champs ne sont **jamais** remplis comme s'ils avaient été mesurés.

**Comparaisons interdites** : AI Overviews de Google · Gemini avec grounding · application Gemini
grand public. Ce sont des grandeurs différentes. **Seule comparaison valide** : un autre round du
même benchmark ungrounded, même modèle, même protocole.

### `grounded` (conservé, verrouillé)
Gemini + Google Search grounding. **Indisponible en free tier sur ce compte** : la fonctionnalité
exige un compte de facturation, volontairement non activé. Le code est conservé intact pour plus
tard ; `resolve_mode()` refuse ce mode tant que `grounding_confirmed_free` est `false`.

Ce qui compte dans les deux cas : l'évolution M0 → M1 → M2 sur un protocole strictement identique.

## Protocole
- 20 prompts fixes (`tools/geo_prompts.json`) × **3 runs indépendants** = 60 tests par round.
- `temperature=0` : supprime la variance de *sampling*, **pas** celle du grounding — les résultats
  de recherche récupérés varient d'un appel à l'autre. Cette variance-là est justement le signal.
- **Jamais de médiane sur les 3 runs.** On calcule des fréquences :
  - `Mention Frequency` = runs où Dar Mansour apparaît / runs
  - `Citation Frequency` = runs citant darmansour.com / runs
  - `Avg Position When Mentioned` (moyenne calculée **uniquement** sur les runs avec mention)
  - `GEO Stability` : 3/3 `Strong` · 2/3 `Emerging` · 1/3 `Weak` · 0/3 `Invisible`
- **Convention de position** : rang d'apparition dans la liste des établissements *nommés* de la
  réponse (1 = premier cité). Une mention en prose, hors liste, compte comme **mention sans position**.

## Traçabilité (`check` et rapports)
`check` affiche explicitement, sans jamais logger la clé : modèle demandé, **modèle exact servi**
(`modelVersion`), Response ID, succès/échec du grounding, présence et clés de `groundingMetadata`,
nombre de sources et de requêtes Google, et — en cas de `429` — le **corps d'erreur complet** avec
les identifiants de quota cités (seul endroit où l'API laisse deviner le tier).

Chaque run archive `model_requested`, `model_version` et `response_id`. Le rapport M0 ouvre sur un
bloc « Provenance de la mesure » listant la ou les versions exactes utilisées : si Google change de
build en cours de route, on le voit, et on saura dans 6 mois ce qui a servi à M0.

## Authentification — clés `AIza` et clés `AQ.`
Google migre les clés AI Studio du format Standard `AIza…` vers les **auth keys `AQ.…`**. Le script
**n'inspecte ni ne valide aucun format de clé** : elle est transmise telle quelle, et c'est le
serveur qui tranche.

`auth_mode` dans `tools/geo_config.json` :
| valeur | transport |
| --- | --- |
| `auto` (défaut) | essaie `x-goog-api-key`, puis `Authorization: Bearer`, puis `?key=` |
| `header` / `bearer` / `query` | force un transport unique |

En mode `auto`, un `401 ACCESS_TOKEN_TYPE_UNSUPPORTED` sur un transport fait immédiatement passer au
suivant (pas de retry inutile) ; le transport accepté est mémorisé pour la suite de l'exécution et
`check` indique lequel figer dans la config.

**Secrets** : toute sortie passe par `redact()` — clé exacte de l'environnement, motif `AIza…`,
motif `AQ.…`, et tout `?key=` dans une URL. `.env` est gitignoré.

## Coût
Free tier Gemini uniquement. Le script **refuse** tout autre provider et n'utilise que
`GEMINI_API_KEY`. Aucune dépense ne peut être engagée sans modifier le code.

## Grounding : verrou avant M0
Le grounding Google Search est une fonctionnalité **potentiellement facturée**. L'outil
`google_search` n'est donc **jamais envoyé implicitement**, et `run` refuse de démarrer tant que
`grounding_confirmed_free` est à `false` dans `tools/geo_config.json`.

| étape | commande | ce qui est envoyé |
| --- | --- | --- |
| Phase 1 | `check` | aucun outil — confirme seulement l'accès au modèle en free tier |
| Phase 2 | `check --grounding` | outil `google_search`, en opt-in explicite |
| M0 | `run --round M0` | bloqué tant que le flag est `false` |

Tout `400/403/429` mentionnant une facturation lève `BillingRequired` : **arrêt immédiat**, sans
retry et sans repli sur un autre modèle. Aucune bascule silencieuse vers du grounding payant.

## Utilisation
```bash
export GEMINI_API_KEY='...'          # clé gratuite : https://aistudio.google.com/apikey

python3 tools/geo_tracker.py check              # phase 1 : accès modèle, sans grounding
python3 tools/geo_tracker.py check --grounding  # phase 2 : sonde le grounding (opt-in)
python3 tools/geo_tracker.py run --round M0     # 60 tests en mode ungrounded (reprenable)
python3 tools/geo_tracker.py report --round M0
```

`run` est **reprenable** : si le quota journalier free tier est atteint, le script s'arrête
proprement et relancer la même commande le lendemain repart exactement où il s'était arrêté.

## Sorties
- `data/geo/M0/prompt-NN_run-N.json` — réponse brute + `groundingMetadata` (**auditable**, tout est recalculable sans réappeler l'API)
- `data/geo/Dar_Mansour_GEO_Tracker_M0.xlsx` — Dashboard · GEO Tracker (agrégé) · Runs (raw) · Prompt Library
- `data/geo/geo-report-M0.md` — rapport lisible : KPI, stabilité par prompt, concurrents, angles morts

## À ne pas sur-interpréter
Un prompt qui passe de `1/3` à `2/3` reste dans le bruit. Les signaux solides : `0/3 → 3/3` sur un
prompt, ou la moyenne **au niveau du cluster**.

## Extension future
`call_gemini()` est isolé derrière une interface simple : ajouter OpenAI ou Perplexity plus tard
ne demande qu'un nouveau provider + son entrée dans `ALLOWED_PROVIDERS`. Volontairement **non fait**
en V1 (ces APIs sont payantes).
