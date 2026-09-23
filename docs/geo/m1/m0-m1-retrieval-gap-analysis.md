# M0 → M1 RETRIEVAL GAP ANALYSIS — Report 2, retrieval section

**Status: the retrieval section is COMPLETE and finalisable.** The selection section is not: the
M1 Gemini phase stands at 17/60. This document covers retrieval only.

| | |
|---|---|
| Date | 2026-09-23 |
| M0 evidence | `m0-retrieval-extract.csv` — 20 prompts, **187 results** |
| M1 evidence | `m1-retrieval-extract.csv` — 20 prompts, **195 results** |
| Actions taken | None. No Serper or Gemini call, no corpus modified, no protocol parameter changed. |

---

## 1. Integrity of both extractions

| Check | M0 | M1 |
|---|---|---|
| Prompts | 20 / 20 | 20 / 20 |
| Result rows | 187 | 195 |
| Ranks contiguous `1..n` | ✅ | ✅ |
| Duplicate ranks within a prompt | 0 | 0 |
| Format | `prompt_id, rank, domain, path, title` | identical |

M0 reproduces the official baseline exactly — Retrieval Rate 6/20 = 30,0 %, Top-3 10 %, Top-5
15 %, mean rank 5,83, median 6. **No correction to M0 was needed or made.**

### Two data-quality observations, recorded and not corrected

**Q1 — Duplicate URL inside one M1 corpus.** Prompt 14 returns **the same third-party URL at rank
1 and rank 10**, under two different titles. Preserved as observed. It means prompt 14's 10 slots
cover 9 distinct URLs.

**Q2 — Path normalisation.** One competitor URL on prompt 12 appears **with a trailing slash at M1
and without at M0** — the same page, two strings. URL-identity comparisons in §7 treat them as
different, which slightly overstates churn on that prompt. Recorded rather than silently
normalised.

---

## 2. Step 1 of §6.1 — volatility before the aggregate

| | M0 | M1 |
|---|---|---|
| **Retrieval Rate** | **6/20 = 30,0 %** | **6/20 = 30,0 %** |
| Prompts | 04, 05, 06, 07, 13, 14 | 04, 05, 06, 10, 12, 13 |

**The rate is identical; the composition is not.** Two in, two out — a one-third turnover under an
unchanged headline. **This is not general stability and must not be presented as such.**

| Classification | Count | Prompts |
|---|---|---|
| **STILL RETRIEVED** | 4 | 04, 05, 06, 13 |
| **NEW RETRIEVED** | 2 | 10, 12 |
| **LOST RETRIEVED** | 2 | 07, 14 |
| **STILL NOT RETRIEVED** | 12 | 01, 02, 03, 08, 09, 11, 15, 16, 17, 18, 19, 20 |

---

## 3. Step 2 of §6.1 — Corpus Coverage — now resolved

| | M0 | M1 |
|---|---|---|
| Mean depth | 9,35 | **9,75** |
| Median | 10 | 10 |
| Min / Max | 7 / 10 | **9 / 10** |
| Total results | 187 | 195 |
| Distribution | 7→1 · 8→2 · 9→6 · 10→11 | **9→5 · 10→15** |

**Five prompts returned deeper corpora**, accounting for all +8 results:

| Prompt | M0 | M1 | Δ |
|---|---|---|---|
| 01 best restaurants | 9 | 10 | +1 |
| **10 best cafés** | 9 | 10 | **+1** |
| **12 beach swim/snorkel/sunset** | 8 | 10 | **+2** |
| 18 what is a tajine | 7 | 9 | +2 |
| 20 tajine vs tagine | 8 | 10 | +2 |

The other 15 prompts are unchanged in depth.

**Max depth is still 10 at M1, as at M0.** No corpus reached 11 results in either round, so
`Top-10` and `Top-20` remain mechanically identical. The constraint pre-registered on M0 holds.

### Depth does not explain the two entries

Both NEW RETRIEVED prompts are among the five that deepened, so this had to be checked:

- **Prompt 12** — Dar Mansour enters at **#5**, a position that existed at M0 (depth 8) and was
  then held by `facebook.com`. Five M0 domains now rank **below** us. This is a re-ranking, not a
  slot appended at the bottom.
- **Prompt 10** — Dar Mansour enters at **#9**, also a position that existed at M0 (depth 9),
  then held by a Facebook group post. Same conclusion.

**Neither entry is a depth artefact.** Step 3 can therefore be read.

---

## 4. Step 3 — Dar Mansour, per prompt

| # | M0 | M1 | Change |
|---|---|---|---|
| **04** Moroccan restaurant | `/` **#2** · `/moroccan-restaurant-reviews…` #10 | `/` **#1** · `/moroccan-restaurant-reviews…` **#8** | STILL ▲ both URLs |
| **05** authentic Moroccan food | `/` **#2** | `/` **#1** | STILL ▲1 |
| **06** best romantic restaurants | `/journal-romantic-dinner…` #10 | `/journal-romantic-dinner…` #10 | STILL = |
| **07** romantic dinner | `/journal-romantic-dinner…` #9 | — | **LOST** |
| **10** best cafés | — | **`/journal-best-cafes-koh-phangan.html` #9** | **NEW** |
| **12** beach swim/snorkel/sunset | — | **`/journal-best-beaches-koh-phangan.html` #5** | **NEW** |
| **13** best sunset places | `/journal-where-to-watch-sunset…` #8 | `/journal-where-to-watch-sunset…` #8 | STILL = |
| **14** sunset time | `/journal-where-to-watch-sunset…` #4 | — | **LOST** |

| | M0 | M1 |
|---|---|---|
| Mean rank when retrieved | 5,83 | 5,67 |
| Median rank | 6 | 6,5 |
| Top-3 / Top-5 / Top-10 | 10 % / 15 % / 30 % | 10 % / 15 % / 30 % |
| Total `darmansour.com` occurrences | 7 | 7 |
| **Distinct Dar Mansour URLs retrieved** | **4** | **6** |

**Prompt 04 — both URLs verified.** `/` and `/moroccan-restaurant-reviews-koh-phangan.html` are
both still present, and both improved: #2 → #1 and #10 → #8.

**Page diversity rose from 4 to 6 distinct URLs** at a constant 7 occurrences: Best Cafés and Best
Beaches enter, Romantic Dinner and Sunset each lose one of their two prompts.

---

## 5. The 06/07 divergence — measured

| | p06 ∩ p07 | Overlap |
|---|---|---|
| **M0** | 9 URLs in common of 10 each | **82 %** |
| **M1** | 7 URLs in common | **54 %** |

At M0 these two near-identical intents returned almost the same corpus. **At M1 they diverged
sharply.** Dar Mansour held rank 10 on p06 and left p07 entirely.

What occupies the space on M1 p07: `adventuresofjellie` enters at #9, and a new Facebook post at
#5. Two of p07's ten slots are now Facebook, against one at M0.

On p06, **`secretmountainphangan.com` enters at #9** — on a private-events page, immediately above
Dar Mansour at #10. This is the domain classified `C — EXISTING MULTI-INTENT
EDITORIAL CORROBORATION` in `offsite-qualification.md`, which mentions Dar Mansour and has never
been contacted. Recorded as a fact; the classification and the `DO NOT CONTACT` decision are
unaffected.

## 6. The 13/14 divergence — measured

| | p13 ∩ p14 | Overlap |
|---|---|---|
| **M0** | 4 URLs | **25 %** |
| **M1** | 4 URLs | **27 %** |

Unlike 06/07, these two were **already** different SERPs at M0 and stayed that way. Their split at
M1 is not a new divergence.

M1 p14 is dominated by time utilities: `timeanddate.com` at **#1, #3 and #10** (the duplicate of
Q1), plus `sunrise-sunset.org` #7 and `sunrise.maplogs.com` #5 — **five of nine distinct slots**
are sunrise/sunset time services, against three at M0. Dar Mansour's #4 slot at M0 is now held by
`theboldpassport.com`.

---

## 7. Corpus composition

### Churn per prompt — share of URLs not shared between the two rounds

| Churn | Prompts |
|---|---|
| **0 %** | **04, 05, 09, 17** |
| 20–33 % | 02, 03, 10, 11, 13, 15, 16 |
| 36–46 % | 01, 06, 07, 08, 14, 18, 19 |
| **62–71 %** | **12, 20** |

**The two Moroccan prompts have completely stable corpora** — 0 % churn, the same URLs in a
slightly different order — and they are the two prompts where Dar Mansour improved. Prompts 09 and
17 are equally stable, and unchanged for us.

The two most volatile prompts, 12 (62 %) and 20 (71 %), are both among the deepened corpora. Note
Q2: p12's churn is slightly overstated by a trailing-slash difference.

### Domains

| | M0 | M1 |
|---|---|---|
| Distinct domains | 60 | **69** |
| Left the global corpus | — | 3: `eater.com`, `epicureandculture.com`, `steemit.com` |
| Entered | — | 12, incl. `britannica.com`, `masterclass.com`, `marocmama.com`, `riadalkemia.com`, `thebrokebackpacker.com` (×2), `youtube.com` (×2), `thailandmagazine.com` |

Recurring domains, M0 → M1: `facebook.com` 26→24 · `tripadvisor.com` 16→16 · `reddit.com` 14→16 ·
`phanganist.com` 11→8 · `tristanbalme.com` 10→11 · `adventuresofjellie.com` 8→9 ·
`darmansour.com` 7→7 · `tikibeachkohphangan.com` 6→6.

Nine of the twelve incoming domains land in the Tajine cluster (18, 19, 20), which also shows the
largest depth increase. The local Koh Phangan competitive set is largely unchanged.

### UGC share — descriptive

| | M0 | M1 |
|---|---|---|
| UGC results | 45 / 187 | 45 / 195 |
| Share | **24,1 %** | **23,1 %** |

Counted as UGC: facebook, reddit, instagram, quora, youtube, steemit. **Essentially flat overall**,
with movement inside prompts: p13 4→2, p16 4→2, p14 1→0, against p18 0→2, p01 2→3, p03 2→3,
p12 1→2, p20 1→2.

⚠️ Descriptive only. No "contestable slots" KPI is derived, per the standing rule.

---

## 8. OBSERVATIONS

**O1 — The Moroccan cluster improved on the two most stable corpora in the series.** 0 % churn on
both prompts, and Dar Mansour moves #2 → #1 on each, with the second URL moving #10 → #8 on prompt
04.

**O2 — Retrieval diversified across pages while staying at 7 occurrences.** Four distinct URLs at
M0, six at M1.

**O3 — Two clusters each lost one of their two prompts** while holding the other at an identical
rank: Romantic (#10 held, #9 lost) and Sunset (#8 held, #4 lost). In both cases the same page is
concerned.

**O4 — The 06/07 corpora diverged from 82 % to 54 % overlap.** The two intents were nearly
interchangeable at M0 and are no longer.

**O5 — Prompt 14 became more utility-dominated.** Five of nine distinct slots are sunrise/sunset
time services.

**O6 — Best Cafés is retrieved while not having been recrawled.** Prompt 10's retrieved URL is
`/journal-best-cafes-koh-phangan.html`, and Crawl Checkpoint #3 records its last crawl as
**2026-08-20** — before the M0→M1 intervention and before PR #147. **This entry cannot be
explained by any post-M0 change to that page**, because Google has not refetched it. The
explanation lies outside the page itself.

**O7 — Twelve prompts remain closed**, including the whole Restaurants cluster (01, 02, 03, 09),
Special Occasion (08), Stay (15, 16), Things to Do (17) and Tajine (18, 19, 20).

---

## 9. HYPOTHESES — not established

**H1 — The entries and exits are SERP volatility.** One measurement per prompt cannot separate a
durable change from noise. Corpus churn of 20–71 % on most prompts shows the environment moves on
its own. *Test: M2, or repeated retrieval on the same prompt.*

**H2 — Retrieval on a prompt is governed by corpus composition more than by the page.** O6 is
consistent with this, and so is O1: the stable corpora are where we moved. *Test: M2 depth and
composition tracking.*

**H3 — Google is differentiating 06 and 07 more than before.** Supported by the overlap drop, on a
single observation. *Test: M2.*

**H4 — The 12 closed prompts are not blocked by a single common factor.** ÉTAPE 2 concluded they
sit in materially different SERP environments; nothing here revises that.

---

## 10. No causal claim

No movement is attributed to `9708db8`, PR #147, `1de3ddb`, passive maturation or any SEO action.

1. All three former control pages were technically modified post-freeze (Report 3 §3.4).
2. `9708db8` and #147 are confounded on six pages.
3. **O6 is a direct counter-example to page-level attribution**: a page not recrawled since
   20 August gained retrieval.
4. Corpus churn of 20–71 % across most prompts is large relative to the movements observed.
5. One measurement per prompt.

**OBSERVATION ≠ INTERPRETATION ≠ CAUSAL CLAIM.** Only the first is present.

---

## 11. Status of Report 2

| Section | Status |
|---|---|
| **Retrieval** | ✅ **COMPLETE — finalisable now.** Both corpora available, integrity verified, depths resolved, all 20 prompts classified, URLs identified, composition and UGC compared. |
| **Selection / Conditional Citability** | ⛔ **BLOCKED — Gemini 17/60.** 43 generations remain, blocked by HTTP 429 quota. |

**The overall M1 GEO benchmark is not complete** and must not be presented as such. The retrieval
section stands on its own and needs nothing further.

---

_Analysis only. No Serper or Gemini call, no corpus modified, no protocol parameter changed, no
site file touched, no M2 work, no recommendation._
