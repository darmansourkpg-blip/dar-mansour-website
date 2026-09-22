# M1 — File inventory / manifest

Generated 2026-09-22. Branch `claude/dar-mansour-geo-audit-qflqxf`. **Not merged to `main`.**

## Delivered

| Filename | Path | Format | Purpose | Round | Raw or derived |
|---|---|---|---|---|---|
| `m1-pre-measurement-state.md` | `docs/geo/m1/` | Markdown | **Report 3** — frozen pre-measurement state, commit history, PR #144–#147 confounder classification, deployment timing, experimental limitations, execution instructions | M1 | derived |
| `m1-pre-measurement-state.json` | `docs/geo/m1/` | JSON | Machine-readable equivalent of Report 3 | M1 | derived |
| `m0-m1-protocol-comparability-check.md` | `docs/geo/m1/` | Markdown | §5 comparability check — every protocol parameter classified IDENTICAL / DIFFERENT; STOP verdict | M0+M1 | derived |
| `m0-m1-prompt-comparison.csv` | `docs/geo/m1/` | CSV | 20-prompt comparison table — **M0 columns populated, M1 columns empty pending the run** | M0 (+M1 scaffold) | derived |
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
| **Report 2 — `M0_M1_RETRIEVAL_GAP_ANALYSIS`** | Requires the M1 run **and** the M0 raw corpora |
| M1 raw runs (per prompt, per run) | idem |
| M1 Retrieval Rate / Conditional Citability | idem |
| URL-level analysis | idem |
| Competitive retrieval evidence | idem |
| GSC Crawl Checkpoint #3 | Operator export — must cover the 12 guides touched by PR #147 |

## Raw data locations (outside this repository, by policy)

| Round | Path |
|---|---|
| M0 | `~/.dar-mansour-geo/citability/M0/` |
| M1 | `~/.dar-mansour-geo/citability/M1/` (new, not yet created) |

Raw SERP payloads, third-party snippets, third-party titles and competitor domains are **never**
committed to this public repository.

## QA status

| Check | Status |
|---|---|
| Exactly 20 official prompts | ✅ verified — `geo_prompts.json`, IDs 1–20 |
| Prompt wording unchanged | ✅ verified by file hash |
| M0 data untouched | ✅ not read, not written, not present in this environment |
| Correct number of runs | ⬜ pending run |
| Same methodology as M0 | ✅ all measurement parameters IDENTICAL |
| All raw M1 evidence preserved | ⬜ pending run |
| Retrieval Rate calculated | ⬜ pending run |
| Conditional Citability calculated | ⬜ pending run |
| 20/20 prompts classified M0→M1 | ⬜ pending run |
| Competing retrieval evidence preserved | ⬜ pending run |
| PR #147 documented as potential confounder | ✅ Report 3 §3.4 |
| Timestamps recorded | ✅ commit + deployment; IndexNow UNKNOWN |
| Machine-readable export generated | ✅ JSON + CSV (M0 populated, M1 pending) |
| No website modification performed | ✅ zero files under `site/` |
| No M2 optimisation performed | ✅ |
