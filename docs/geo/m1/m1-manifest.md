# M1 — File inventory / manifest

Generated 2026-09-22. Branch `claude/dar-mansour-geo-audit-qflqxf`. **Not merged to `main`.**

## Delivered

| Filename | Path | Format | Purpose | Round | Raw or derived |
|---|---|---|---|---|---|
| `m1-pre-measurement-state.md` | `docs/geo/m1/` | Markdown | **Report 3** — frozen pre-measurement state, commit history, PR #144–#147 confounder classification, deployment timing, experimental limitations, execution instructions | M1 | derived |
| `m1-pre-measurement-state.json` | `docs/geo/m1/` | JSON | Machine-readable equivalent of Report 3 | M1 | derived |
| `m0-m1-protocol-comparability-check.md` | `docs/geo/m1/` | Markdown | §5 comparability check — every protocol parameter classified IDENTICAL / DIFFERENT; STOP verdict | M0+M1 | derived |
| `m0-m1-prompt-comparison.csv` | `docs/geo/m1/` | CSV | 20-prompt comparison table — **M0 columns populated from primary corpus evidence (2026-09-23), M1 columns empty pending the run** | M0 (+M1 scaffold) | derived |
| `m1-manifest.md` | `docs/geo/m1/` | Markdown | This manifest | M1 | derived |

## Pre-existing context (same repository)

| Filename | Path | Purpose |
|---|---|---|
| `m1-plan.md` | `docs/geo/` | Pre-registered M1 protocol, freeze rules, GSC crawl checkpoints #1 and #2, reading rules. On `main` at `f309c40`. |
| `offsite-qualification.md` | `docs/geo/` | Off-site qualification frozen before M1. On `main`. |

## Tooling (branch only, never merged to `main`)

| Filename | Path | Purpose |
|---|---|---|
| `geo_citability.py` | `tools/` | L3 benchmark — retrieval (Serper) + selection (Gemini) |
| `geo_citability_config.json` | `tools/` | Frozen protocol parameters |
| `geo_citability_selection_prompt.txt` | `tools/` | Versioned selection instrument v1.0 |
| `geo_citability_tests.py` | `tools/` | 101 offline tests |
| `geo_prompts.json` | `tools/` | The 20 official prompts · SHA-256 `28d2c6de4cbc6f4dbc8b9d0cdc6026a5ec64925f39acf2d1c65986ae0e08a88f` |
| `geo_tracker.py` | `tools/` | L4 ungrounded brand-knowledge benchmark |
| `ai_referral.py` | `tools/` | L2 GA4 AI referral |

## NOT delivered — requires execution on the operator's machine

| Deliverable | Blocked by |
|---|---|
| **Report 1 — `M1_GEO_CITABILITY`** | M1 run not possible here (credentials, Serper egress) |
| **Report 2 — `M0_M1_RETRIEVAL_GAP_ANALYSIS`** | M0 side now available; **blocked only by the incomplete M1 Gemini phase** |
| M1 raw runs (per prompt, per run) | idem |
| M1 Retrieval Rate / Conditional Citability | idem |
| URL-level analysis | idem |
| Competitive retrieval evidence | idem |
| ~~GSC Crawl Checkpoint #3~~ | **Delivered 2026-09-23 — see the update below** |

## Raw data locations (outside this repository, by policy)

| Round | Path |
|---|---|
| M0 | `~/.dar-mansour-geo/citability/M0/` |
| M1 | `~/.dar-mansour-geo/citability/M1/` (new, not yet created) |

Raw SERP payloads, third-party snippets, third-party titles and competitor domains are **never**
committed to this public repository.

---

# Update — 2026-09-23 · Evidence consolidation + Crawl Checkpoint #3

## Files added

| Filename | Path | Format | Purpose | Round | Raw or derived |
|---|---|---|---|---|---|
| `gsc-crawl-checkpoint-3.md` | `docs/geo/m1/` | Markdown | Crawl Checkpoint #3 — post-#147 recrawl status of the 12 modified guides | M1 | derived |
| `gsc-crawl-checkpoint-3.csv` | `docs/geo/m1/` | CSV | Machine-readable checkpoint #3 — displayed ICT value **and** computed UTC equivalent per URL | M1 | derived |
| `m1-source-validation.md` | `docs/geo/m1/` | Markdown | Validation of the four primary GSC/GA4 source files + sitemap observation | M1 | derived |
| `m0-corpus-evidence.md` | `docs/geo/m1/` | Markdown | M0 minimal corpus — integrity checks, actual depths, Dar Mansour presence, reconciliation with the official baseline | M0 | derived |
| `m0-minimal-corpus.csv` | `docs/geo/m1/` | CSV | The extraction itself — 187 rows, one per result | M0 | **primary evidence (derived from raw)** |
| `m0-corpus-depth.csv` | `docs/geo/m1/` | CSV | Requested vs actual depth per prompt, retrieval status, best rank | M0 | derived |
| `m0-corpus-depth.json` | `docs/geo/m1/` | JSON | Same, machine-readable | M0 | derived |

## Source files received (immutable, held outside the repository)

| # | Filename | Source | Period | Comparison | Filter | Status |
|---|---|---|---|---|---|---|
| 1 | `…Performance-on-Search-2026-09-23.xlsx` | GSC Performance | Last 28 days | Previous 28 days | Web, **no page filter** | ✅ authoritative |
| 2 | `…Coverage-2026-09-22.xlsx` | GSC Indexing | → 2026-09-18 | — | All known pages | ✅ usable; **no per-URL Last crawled** |
| 3 | `Landing page_ Landing page.xlsx` | GA4 Landing pages | 25/08 → 21/09 | 28/07 → 24/08 | Organic Search (verified indirectly) | ✅ usable; truncated to 28 rows |
| 4 | `Traffic_acquisition_…csv` | GA4 Traffic acquisition | 25/08 → 21/09 | 28/07 → 24/08 | **none** — all channels | ✅ |
| 5 | GSC Sitemap screenshot | GSC Sitemaps | Last read 2026-09-21 | — | — | ✅ observation recorded |

The earlier 2026-09-22 Performance export (unintended page filter) is **superseded and unused**.

## Evidence inventory by layer

| Layer | Item | Status |
|---|---|---|
| **A — GEO** | M0 raw corpus (operator machine) | **COMPLETE** |
| **A — GEO** | M0 minimal corpus extraction, 20/20 prompts, 187 rows | **COMPLETE** — integrated 2026-09-23; reproduces every official M0 figure exactly |
| **A — GEO** | M1 Serper retrieval, 20/20 | **COMPLETE** |
| **A — GEO** | M1 Gemini selection, target 60/60 | **PARTIAL** — HTTP 503 then 429; runner resumable |
| **A — GEO** | Report 1 `M1_GEO_CITABILITY` | **WAITING** |
| **A — GEO** | Report 2 `M0_M1_RETRIEVAL_GAP_ANALYSIS` | **WAITING** |
| **B — GSC Performance** | File 1 | **COMPLETE** |
| **C — GSC Coverage** | File 2 | **COMPLETE** |
| **C — GSC Sitemap** | File 5 | **COMPLETE** |
| **C — GSC Crawl** | Checkpoint #3 | **COMPLETE** — 2026-09-23, all 12 classified: **9/12 POST-#147 RECRAWL CONFIRMED · 3/12 NO POST-#147 RECRAWL OBSERVED · 0/12 UNKNOWN**. Timezone rule resolved: GSC `Last crawl` is shown in the user's local time (Google Search Console Help, URL Inspection tool), inspections made in Thailand (ICT, UTC+7); threshold = 2026-09-15 12:38:13 ICT. |
| **D — GA4** | Files 3 and 4 | **COMPLETE** |
| **Pre-measurement** | Report 3 | **COMPLETE** |

## Missing evidence

1. **Gemini selection runs** — the controlled GEO measurement is not complete until 60/60.
   Reports 1 and 2 stay pending. No run may be simulated, and the model, provider and protocol
   must not be changed.
2. ~~11 manual GSC URL Inspections~~ · ~~time of day for the 7 URLs of 2026-09-15~~ —
   **all received and resolved 2026-09-23. Crawl Checkpoint #3 is closed: 9/12 CONFIRMED,
   3/12 NO RECRAWL, 0/12 UNKNOWN.** Nothing further is needed on the crawl layer.
3. ~~Minimal M0 corpus extraction for the 20 prompts~~ — **received and integrated 2026-09-23.**
   20/20 prompts, 187 rows, integrity verified; the M0 side of Report 2 now rests on primary
   evidence. See `m0-corpus-evidence.md`.

**Only item 1 remains outstanding.**

## QA status

| Check | Status |
|---|---|
| Exactly 20 official prompts | ✅ verified — `geo_prompts.json`, IDs 1–20 |
| Prompt wording unchanged | ✅ verified by file hash |
| M0 data untouched | ✅ source files never read or written by this environment; the extraction was supplied by the operator and parsed read-only |
| Correct number of runs | ⬜ pending run |
| Same methodology as M0 | ✅ all measurement parameters IDENTICAL |
| All raw M1 evidence preserved | ⬜ pending run |
| Retrieval Rate calculated | ⬜ pending run |
| Conditional Citability calculated | ⬜ pending run |
| 20/20 prompts classified M0→M1 | ⬜ pending run — **M0 side complete for all 20** |
| Competing retrieval evidence preserved | ⬜ pending run |
| PR #147 documented as potential confounder | ✅ Report 3 §3.4 |
| Timestamps recorded | ✅ commit + deployment; IndexNow UNKNOWN |
| Machine-readable export generated | ✅ JSON + CSV — M0 fully populated from primary evidence (187 rows), M1 pending |
| No website modification performed | ✅ zero files under `site/` |
| No M2 optimisation performed | ✅ |
