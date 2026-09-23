# M0 → M1 RETRIEVAL GAP ANALYSIS — PREPARATION

**Status: PREPARATION, not Report 2.** The M1 Gemini selection phase stands at **17/60**
(43 generations blocked by HTTP 429 quota). No selection or citability figure is computed here.

| | |
|---|---|
| Date | 2026-09-23 |
| M0 evidence | Minimal corpus extraction, 20/20 prompts, 187 rows — **complete, verified** |
| M1 evidence | Serper retrieval 20/20 **executed and preserved**; prompt-level observation supplied by the operator |
| M1 corpus extraction | **NOT YET RECEIVED** — see §6 |
| Actions taken | None. No Serper search re-run, no raw data modified, no protocol parameter changed. |

---

## 1. Reading order — as pre-registered

`docs/geo/m1-plan.md` §6.1 fixes the order before any aggregate is read. It is applied here.

### Step 1 — Volatility before the aggregate rate

> *"If the overall rate moves **but with many prompts entering and leaving**, examine
> prompt-by-prompt volatility first. A stable rate masking 6 entries and 6 exits is not
> stability."* — §6.1, written before M1 was run.

This is exactly the case that rule anticipated:

| | M0 | M1 |
|---|---|---|
| **Retrieval Rate** | **6/20 = 30.0 %** | **6/20 = 30.0 %** |
| Prompts retrieved | 04, 05, 06, 07, 13, 14 | 04, 05, 06, 10, 12, 13 |

**The rate is identical and the composition is not.** Two prompts entered, two left — a one-third
turnover inside an unchanged headline number. Reporting "30 % → 30 %, no change" would be false.

### Step 2 — Corpus Coverage — ⚠️ BLOCKING

> *"If the actual returned depth changes appreciably from M0 (mean 9.35), analyse depth
> **prompt by prompt** before interpreting any movement in rank or rate."* — §6.1

**M1 corpus depths are unknown.** Only prompt-level presence and Dar Mansour's rank were supplied.
Until the M1 minimal extraction arrives:

- **no Top-N comparison may be treated as final** — a change in returned depth mechanically shifts
  the Top-N thresholds;
- **no rank movement may be interpreted** — rank 5 in a corpus of 8 is not rank 5 in a corpus of 10;
- **no corpus composition comparison is possible** — competing domains at M1 are unknown.

Step 3 (Retrieval Rate, Top-N, ranks, selection) is therefore **not** reached in this document.

---

## 2. The four classifications — 20/20

| Classification | Count | Prompts |
|---|---|---|
| **STILL RETRIEVED** | **4** | 04, 05, 06, 13 |
| **NEW RETRIEVED** | **2** | 10, 12 |
| **LOST RETRIEVED** | **2** | 07, 14 |
| **STILL NOT RETRIEVED** | **12** | 01, 02, 03, 08, 09, 11, 15, 16, 17, 18, 19, 20 |

4 + 2 + 2 + 12 = 20. Machine-readable in `m0-m1-prompt-comparison.csv`.

---

## 3. Per-prompt table

| # | Prompt | Cluster | M0 | M1 | Change |
|---|---|---|---|---|---|
| 01 | best restaurants | Restaurants | — | — | STILL NOT RETRIEVED |
| 02 | where should I eat | Restaurants | — | — | STILL NOT RETRIEVED |
| 03 | best restaurants west coast | Restaurants | — | — | STILL NOT RETRIEVED |
| 04 | best Moroccan restaurant | Moroccan | **#2** | **#1** | **STILL RETRIEVED** ▲1 |
| 05 | authentic Moroccan food | Moroccan | **#2** | **#1** | **STILL RETRIEVED** ▲1 |
| 06 | best romantic restaurants | Romantic | #10 | #10 | **STILL RETRIEVED** = |
| 07 | romantic dinner | Romantic | #9 | — | **LOST RETRIEVED** |
| 08 | special occasion dinner | Romantic | — | — | STILL NOT RETRIEVED |
| 09 | best Thai restaurants | Restaurants | — | — | STILL NOT RETRIEVED |
| 10 | best cafés | Cafés | — | **#9** | **NEW RETRIEVED** |
| 11 | best beaches | Beaches | — | — | STILL NOT RETRIEVED |
| 12 | beach swimming/snorkelling/sunset | Beaches | — | **#5** | **NEW RETRIEVED** |
| 13 | best sunset places | Sunset | #8 | #8 | **STILL RETRIEVED** = |
| 14 | sunset time | Sunset | #4 | — | **LOST RETRIEVED** |
| 15 | where should I stay | Stay | — | — | STILL NOT RETRIEVED |
| 16 | best area first-time visitor | Stay | — | — | STILL NOT RETRIEVED |
| 17 | best things to do | Things to Do | — | — | STILL NOT RETRIEVED |
| 18 | what is a tajine | Tajine | — | — | STILL NOT RETRIEVED |
| 19 | tajine in English | Tajine | — | — | STILL NOT RETRIEVED |
| 20 | tajine vs tagine | Tajine | — | — | STILL NOT RETRIEVED |

Provisional aggregates, **not to be treated as final** until M1 depths are known:
mean rank when retrieved 5.83 → 5.67 · median 6 → 6.5 · Top-3 10 % → 10 % · Top-5 15 % → 15 %.

---

## 4. OBSERVATIONS

Facts from the two corpora. No mechanism is asserted for any of them.

**O1 — The Moroccan cluster moved from #2 to #1 on both its prompts.** Prompts 04 and 05, the
cluster the handover designates as the strategic asset and marks `DO NOT DESTABILIZE`. At M0,
prompt 04 carried **two** `darmansour.com` URLs (`/` at #2 and
`/moroccan-restaurant-reviews-koh-phangan.html` at #10); whether both are still present at M1 is
unknown.

**O2 — The Romantic cluster split.** Prompt 06 ("best romantic restaurants") held at #10; prompt
07 ("where can I have a romantic dinner") dropped out entirely from #9. Both prompts target the
**same page**, `journal-romantic-dinner-koh-phangan.html`, on near-identical intents. A single
page was retrieved on one and not the other.

**O3 — The Sunset cluster split the same way.** Prompt 13 ("best places to watch sunset") held at
#8; prompt 14 ("what time is sunset") dropped from #4. Both target the same page. At M0, prompt
14's corpus was headed by `timeanddate.com` at #1 and #3 — a corpus shape the handover already
described as one not to compete with.

**O4 — Two entries, in clusters that were absent at M0.** Prompt 10 (cafés) at #9 and prompt 12
(beach for swimming/snorkelling/sunset) at #5. **Which Dar Mansour URL was retrieved is unknown**
— only the rank was supplied. This must be resolved before any page-level statement: the
retrieved URL may or may not be the page the prompt nominally targets.

**O5 — Twelve prompts unchanged as NOT_RETRIEVED**, including the entire Restaurants cluster
(01, 02, 03, 09), Special Occasion (08), Stay (15, 16), Things to Do (17) and Tajine (18, 19, 20).
The clusters identified at M0 as the hardest remain closed.

**O6 — Cross-layer, to be resolved, not concluded.** Crawl Checkpoint #3 records that
`journal-best-cafes-koh-phangan.html` has **not been recrawled since 2026-08-20** — before the
intervention and before #147 — while prompt 10 (cafés) is a NEW RETRIEVED. If the URL retrieved
at prompt 10 turns out to be that page, the entry cannot be attributed to any post-M0 change to
it, since Google has not refetched it. **This is a question for §6, not a finding.** The retrieved
URL is unknown.

---

## 5. HYPOTHESES — not established

Explicitly separated from §4. None is supported by the current evidence; each names what would
test it.

**H1 — The two entries and two exits are SERP volatility rather than any effect of ours.** A
single measurement per prompt cannot distinguish a durable change from noise. *Would require: M2,
or repeated retrieval on the same prompt.*

**H2 — The Moroccan #2 → #1 movement reflects entity consolidation.** Plausible and untested.
Nothing in the protocol measures the entity, and the ±1 amplitude is within what any ranking
system moves on its own. *Would require: entity-level measurement, which does not exist.*

**H3 — Prompts 06/07 and 13/14 behave differently because Google treats these near-identical
intents as distinct SERPs.** Consistent with the split, but M0 already showed their corpora differ
in composition. *Would require: comparing the M1 corpora of 06 vs 07 and 13 vs 14.*

**H4 — The 12 STILL NOT RETRIEVED prompts are blocked by the same factor.** ÉTAPE 2 concluded the
opposite — these prompts sit in materially different SERP environments — and nothing here revises
that. *Would require: the M1 corpora.*

---

## 6. NOT ESTABLISHED, and what is required

| Question | Status | Required |
|---|---|---|
| Did M1 corpus depth change? | **UNKNOWN** | M1 minimal extraction |
| Which Dar Mansour URL was retrieved on prompts 10 and 12? | **UNKNOWN** | M1 minimal extraction |
| Are both Dar Mansour URLs still present on prompt 04? | **UNKNOWN** | idem |
| What changed in competitor composition? | **UNKNOWN** | idem |
| Did UGC share move? | **UNKNOWN** | idem |
| Selection / Conditional Citability at M1 | **PENDING** | 43 remaining Gemini generations |

### The one missing piece

The **M1 minimal extraction**, in the exact format used for M0:

```
prompt_id | rank | domain | path | title      (no snippets)
```

for the 20 prompts, from `~/.dar-mansour-geo/citability/M1/`, preserving actual depth as observed.
Without it, §3's rank comparison rests on prompt-level observation alone, and no corpus
composition comparison is possible.

⚠️ No new Serper search. The 20/20 M1 retrieval is already executed and preserved; the extraction
reads those stored corpora.

---

## 7. No causal claim

Nothing in this document attributes any M0→M1 movement to `9708db8` (internal linking), to PR #147
(anchor navigation), to `1de3ddb` (menu reorder), to passive maturation, or to any SEO action.

Four reasons, recorded so the constraint is not later mistaken for caution:

1. All three former control pages were technically modified post-freeze (Report 3 §3.4), so no
   uncontaminated comparison group remains.
2. `9708db8` and #147 are confounded on six pages.
3. Corpus depth at M1 is unknown, so even the ranks are not yet comparable on a stable basis.
4. A single measurement per prompt cannot separate a durable change from SERP volatility.

**OBSERVATION** ≠ **INTERPRETATION** ≠ **CAUSAL CLAIM**. Only the first is present here.

---

## 8. Data handling

- No Serper search re-run. No API call of any kind.
- No raw data modified — M0 and M1 corpora stay on the operator's machine, untouched.
- No third-party result file committed to this public repository. Only the agreed minimal format
  (rank, domain, URL path, title) is carried here, and only for M0.
- Protocol unchanged: 20 prompts, same wording, same parameters, same denominators.
- M0 baseline unchanged: **6/20 = 30.0 %**.

---

_Preparation only. Report 2 is not produced and will not be until the 60/60 Gemini generations are
complete. No site file modified, no M2 work, no optimisation, no recommendation._
