# M0 — Minimal corpus evidence

Integration record for the minimal extraction of the 20 original M0 Serper corpora, received
2026-09-23.

| | |
|---|---|
| Source file | `M0_minimal_corpus_20_prompts.txt` |
| Generated from | `~/.dar-mansour-geo/citability/M0/corpus-01.json … corpus-20.json` (immutable, outside the repository) |
| Fields extracted | `rank \| domain \| path \| title` — **no snippets** |
| Operator attestation | No M0 source file modified · no network or API call · no missing result reconstructed or supplemented |
| Integration | Parsed read-only. **No M0 value altered, corrected or supplemented.** |

This document records the corpus as observed. It performs **no** M0→M1 analysis: Report 2 waits
for the 60/60 Gemini generations.

---

## 1. Integrity checks

| Check | Result |
|---|---|
| Prompts present | **20 / 20** |
| Declared depth vs parsed rows | **match on all 20** — no discrepancy |
| Ranks contiguous `1..n` per prompt | ✅ all 20 |
| Requested depth | `20` on all 20 prompts |
| Total result rows | **187** |
| Snippets present | none |

---

## 2. Actual corpus depth per prompt

Serper returned **7 to 10 results** despite a requested depth of 20. Preserved exactly as
observed — not paginated, supplemented or reinterpreted.

| Prompt | Depth | Prompt | Depth |
|---|---|---|---|
| 01 | 9 | 11 | 9 |
| 02 | 10 | 12 | **8** |
| 03 | 10 | 13 | 10 |
| 04 | 10 | 14 | 10 |
| 05 | 9 | 15 | 10 |
| 06 | 10 | 16 | 10 |
| 07 | 10 | 17 | 9 |
| 08 | 10 | 18 | **7** |
| 09 | 10 | 19 | 9 |
| 10 | 9 | 20 | **8** |

| Statistic | Value |
|---|---|
| Mean | **9.35** |
| Median | **10** |
| Min / Max | **7 / 10** |
| Distribution | 7 → 1 prompt · 8 → 2 · 9 → 6 · 10 → 11 |
| Below requested depth 20 | **20 / 20** |
| Below 10 | **9 / 20** |

### Consequence — confirmed on all 20 prompts

`Top-10 Rate` and `Top-20 Rate` are **mechanically identical** in this instrument. No corpus ever
reached 11 results, so no rank above 10 can exist. Reporting them as two distinct metrics is
misleading. This was already established on the 14 `NOT_RETRIEVED` prompts (mean 9.1); it now
holds across the full series (mean 9.35).

"Being retrieved" means entering a top ~9, not a top 20.

---

## 3. Dar Mansour presence — recomputed from primary evidence

| Prompt | Intent | `darmansour.com` URL(s) | Best rank |
|---|---|---|---|
| 04 — best Moroccan restaurant | Commercial | `/` **(#2)** · `/moroccan-restaurant-reviews-koh-phangan.html` (#10) | **2** |
| 05 — authentic Moroccan food | Commercial | `/` (#2) | **2** |
| 06 — best romantic restaurants | Commercial | `/journal-romantic-dinner-koh-phangan.html` (#10) | 10 |
| 07 — romantic dinner | Commercial | `/journal-romantic-dinner-koh-phangan.html` (#9) | 9 |
| 13 — best sunset places | Editorial | `/journal-where-to-watch-sunset-koh-phangan.html` (#8) | 8 |
| 14 — sunset time | Editorial | `/journal-where-to-watch-sunset-koh-phangan.html` (#4) | 4 |

The other 14 prompts contain no `darmansour.com` result.

### Reconciliation with the official M0 baseline

Every published M0 figure is reproduced exactly from the primary corpora:

| Metric | Official M0 | Recomputed from the extraction | |
|---|---|---|---|
| Retrieval Rate | 6/20 = 30.0 % | 6/20 = 30.0 % | ✅ |
| Top-3 | 10 % | 2/20 = 10 % | ✅ |
| Top-5 | 15 % | 3/20 = 15 % | ✅ |
| Top-10 | 30 % | 6/20 = 30 % | ✅ |
| Top-20 | 30 % | 6/20 = 30 % | ✅ |
| Mean rank when retrieved | 5.8 | 5.8 | ✅ |
| Median rank when retrieved | 6 | 6 | ✅ |

**The baseline is unchanged and now rests on primary evidence rather than on aggregates.** No
correction to M0 was needed, and none was made.

### Detail gained over the previous record

Two ranks previously carried as approximations from the handover are now exact, and one fact is
new:

| Item | Before | Now |
|---|---|---|
| Prompt 06 rank | "≈9" | **10** |
| Prompt 07 rank | "≈10" | **9** |
| Prompt 05 rank | not recorded | **2** |
| Prompt 04 | one URL assumed | **two distinct `darmansour.com` URLs** in the same corpus (#2 and #10) |

Prompt 04 carrying two of our own URLs matters for the URL-level analysis in Report 2: retrieval
counted per prompt is not the same as retrieval counted per URL.

---

## 4. Files produced

| File | Content |
|---|---|
| `m0-minimal-corpus.csv` | **187 rows** — the full extraction, one row per result: `prompt_id, prompt, corpus_depth, requested_depth, rank, domain, path, title, is_dar_mansour` |
| `m0-corpus-depth.csv` | One row per prompt: requested vs actual depth, retrieval status, Dar Mansour best rank and URLs |
| `m0-corpus-depth.json` | Same, machine-readable |
| `m0-m1-prompt-comparison.csv` | **Report 2 scaffold** — 22 columns, M0 side fully populated from primary evidence, M1 columns empty |

The `m0-m1-prompt-comparison.csv` M0 columns are now: corpus depth, retrieval status, diagnostic,
Dar Mansour URL(s), best rank, URL count, 3-run selection, top-3 competing domains, and the
evidence source. The M1 columns (`m1_corpus_depth`, `m1_retrieval_status`, `m1_dar_mansour_url`,
`m1_rank`, `m1_selection_3runs`, `change_classification`, `notes`) stay **empty** until the run
completes.

---

## 5. What is deliberately not done here

- **No M0→M1 comparison.** The M1 Gemini selection phase is incomplete (HTTP 503 then 429, quota
  exhausted); Report 2 waits for 60/60.
- **No retrieval gap analysis**, no competitor reading, no page-level conclusion.
- **No causal claim** of any kind.
- **No M0 data modified.** The source files stay on the operator's machine, untouched.
- **No raw SERP payload or third-party snippet committed.** The extraction carries rank, domain,
  URL path and title only, which is the format agreed for this repository.

---

_Evidence integration only. No site file modified, no M0 data altered, no protocol parameter
changed, no API call made._
