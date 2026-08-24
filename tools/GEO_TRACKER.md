# GEO Tracker — mode d'emploi

Mesure la visibilité de Dar Mansour dans les réponses IA, de façon **reproductible et gratuite**.

## Ce qu'on mesure exactement
**Gemini API + Google Search grounding.** Ce n'est **ni** l'application Gemini grand public,
**ni** les AI Overviews de Google. C'est un indicateur de **tendance** : ce qui compte, c'est
l'évolution M0 → M1 → M2 sur un protocole strictement identique.

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

**Secrets** : la clé transite par l'en-tête `x-goog-api-key`, jamais dans l'URL ; toute sortie passe
par `redact()` (clé exacte + motif `AIza…`) avant affichage. `.env` est gitignoré.

## Coût
Free tier Gemini uniquement. Le script **refuse** tout autre provider et n'utilise que
`GEMINI_API_KEY`. Aucune dépense ne peut être engagée sans modifier le code.

## Utilisation
```bash
export GEMINI_API_KEY='...'          # clé gratuite : https://aistudio.google.com/apikey

python3 tools/geo_tracker.py check           # 1 appel : vérifie clé + grounding actif
python3 tools/geo_tracker.py run --round M0  # 60 tests (reprenable)
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
