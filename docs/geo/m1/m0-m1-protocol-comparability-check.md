# M0_M1_PROTOCOL_COMPARABILITY_CHECK

**Date:** 2026-09-22 · **Verdict:** ⛔ **STOP — M1 not executed in this environment.**

Required by §5 of the M1 brief. Every parameter of the pre-registered protocol is classified
`IDENTICAL` or `DIFFERENT`. Sources: `tools/geo_citability_config.json` and
`tools/geo_prompts.json` on branch `claude/dar-mansour-geo-audit-qflqxf`, and `docs/geo/m1-plan.md`
§2 (pre-registered).

---

## 1. Measurement parameters

| Parameter | M0 (recorded) | M1 (intended) | Verdict |
|---|---|---|---|
| Protocol version | `1.0` | `1.0` | **IDENTICAL** |
| Prompt set | 20 prompts, `geo_prompts.json` | same file, unmodified | **IDENTICAL** |
| Prompt file SHA-256 | `28d2c6de4cbc6f4dbc8b9d0cdc6026a5ec64925f39acf2d1c65986ae0e08a88f` | same | **IDENTICAL** |
| Prompt wording | verbatim | verbatim (`query_mode: verbatim`) | **IDENTICAL** |
| Prompt order / IDs | 1–20, fixed | 1–20, fixed | **IDENTICAL** |
| Search provider | Serper → Google Search | Serper → Google Search | **IDENTICAL** |
| Search endpoint | `https://google.serper.dev/search` | same | **IDENTICAL** |
| `gl` | `th` | `th` | **IDENTICAL** |
| `hl` | `en` | `en` | **IDENTICAL** |
| `location` | `null` | `null` | **IDENTICAL** |
| Requested depth | 20 | 20 | **IDENTICAL** |
| Pagination | none | none | **IDENTICAL** |
| Searches per prompt | 1 | 1 | **IDENTICAL** |
| Selection model | `gemini-3.6-flash` | `gemini-3.6-flash` | **IDENTICAL** |
| Grounding / Google Search tool | disabled | disabled | **IDENTICAL** |
| Temperature | 0 | 0 | **IDENTICAL** |
| Runs per prompt | 3 | 3 | **IDENTICAL** |
| Corpus per run | same corpus for all 3 runs | same | **IDENTICAL** |
| Selection prompt | `geo_citability_selection_prompt.txt` v1.0 | same, unmodified | **IDENTICAL** |
| Source IDs | neutral `S01…SNN` | same | **IDENTICAL** |
| Target domain | `darmansour.com` | same | **IDENTICAL** |
| Brand aliases | Dar Mansour · Dar Mansur · Morocco's Kitchen · Moroccos Kitchen | same | **IDENTICAL** |
| Retrieval detection | domain match on `darmansour.com` in organic results | same | **IDENTICAL** |
| Selection detection | `selected_source` / `mentioned_in_answer` / `recommended`, three distinct metrics | same | **IDENTICAL** |
| Aggregation | Retrieval Rate = retrieved prompts / 20 · Conditional Citability = selected runs / eligible runs | same | **IDENTICAL** |
| Denominators | 20 prompts; eligible runs = runs on retrieved prompts | same | **IDENTICAL** |
| Call caps | 20 searches / 60 generations | same | **IDENTICAL** |
| Spacing | 7 s between calls | same | **IDENTICAL** |
| Retries | max 3, counted separately from caps | same | **IDENTICAL** |
| Raw root | `~/.dar-mansour-geo/citability/M0/` | `~/.dar-mansour-geo/citability/M1/` | **IDENTICAL** (by design: separate round directory, M0 never overwritten) |

**No measurement parameter is DIFFERENT.** The protocol itself is fully comparable, and the
protocol-hash guard in `geo_citability.py` will enforce it at run time.

---

## 2. Execution environment — where the difference lies

| Requirement | M0 | This environment | Verdict |
|---|---|---|---|
| `SERPER_API_KEY` | present (operator's machine) | **absent** | **DIFFERENT** |
| `GEMINI_API_KEY` | present (operator's machine) | **absent** | **DIFFERENT** |
| Serper reachable | yes | **no** — `https://google.serper.dev/` returns nothing through the egress proxy (HTTP `000`) | **DIFFERENT** |
| Gemini reachable | yes | yes — `generativelanguage.googleapis.com` responds (HTTP 404 on `/`) | IDENTICAL |
| M0 raw corpora available | yes | **no** — `~/.dar-mansour-geo/` contains 0 files | **DIFFERENT** |
| L3 tooling available | yes | yes, on branch `claude/dar-mansour-geo-audit-qflqxf` (not on `main`) | IDENTICAL |

---

## 3. Verdict

**Four environmental parameters are DIFFERENT. Execution is halted, as §5 requires.**

The differences are **environmental, not methodological**. Nothing in the protocol has drifted; the
container simply lacks the credentials, the network path to the retrieval provider, and the M0 raw
data. Running here would require substituting a different retrieval path or corpus — which §5
forbids, and which would silently destroy M0↔M1 comparability.

**No substitute methodology was used. No M1 data was generated, estimated or fabricated.**

### Consequences

1. **Report 1 (`M1_GEO_CITABILITY`)** cannot be produced here. It requires the run.
2. **Report 2 (`M0_M1_RETRIEVAL_GAP_ANALYSIS`)** cannot be produced here. It requires both the M1
   run *and* the M0 raw corpora.
3. **Report 3 (`M1_PRE_MEASUREMENT_STATE`)** is complete and delivered — it depends only on Git,
   deployment records and configuration, all of which are available.

### Required action

Execute M1 on the operator's machine, following `m1-pre-measurement-state.md` §8. Then supply:

- the aggregate report from `report --round M1`;
- real corpus depth per prompt, and UGC share per prompt;
- per-prompt, per-run records (prompt, run number, timestamp, Dar Mansour presence, retrieved URL,
  rank, selection status, competing domains);
- a minimal extraction — `rank | domain | path | title` — for the prompts still `NOT_RETRIEVED`;
- the same minimal extraction **from the M0 corpora** for all 20 prompts, so the prompt-level
  comparison can be built from primary evidence rather than from aggregates.

⚠️ Do **not** transmit raw SERP payloads or third-party snippets into this repository. The minimal
extraction format is the one used for the M0 gap analysis: rank, domain, URL path and title only.

---

_Documentation only. No API calls made. No M0 data read, written or altered._
