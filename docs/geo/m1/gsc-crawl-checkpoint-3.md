# GSC CRAWL CHECKPOINT #3 — POST-#147

**Checkpoint date:** 2026-09-23
**Reference threshold:** PR #147 (`6f00cb2`) deployment completed **2026-09-15 05:38:13 UTC**

**Question:** for each of the 12 guides modified by #147, does the available GSC evidence show
that Google recrawled the URL **after** that deployment?

---

## 1. Result

| | |
|---|---|
| **POST-#147 RECRAWL CONFIRMED** | **0 / 12** |
| **NO POST-#147 RECRAWL OBSERVED** | **1 / 12** |
| **UNKNOWN — NEW GSC INSPECTION REQUIRED** | **11 / 12** |

---

## 2. Per-URL table

| # | Guide | Latest reliable `Last crawl` | Observed on | Classification |
|---|---|---|---|---|
| 1 | Best Restaurants | 2026-09-02 | **2026-09-23** (URL Inspection) | **NO POST-#147 RECRAWL OBSERVED** |
| 2 | Best Cafés | 2026-08-20 | 2026-09-07 (checkpoint #2) | UNKNOWN |
| 3 | Best Beaches | 2026-09-02 | 2026-09-07 | UNKNOWN |
| 4 | Where to Stay | 2026-09-02 | 2026-09-07 | UNKNOWN |
| 5 | Where to Eat in Thong Sala | 2026-09-02 | 2026-09-07 | UNKNOWN |
| 6 | Romantic Dinner | 2026-09-02 | 2026-09-07 | UNKNOWN |
| 7 | Best Thai Restaurants | 2026-08-21 | 2026-09-07 | UNKNOWN |
| 8 | Best Breakfast & Brunch | 2026-09-02 | 2026-09-07 | UNKNOWN |
| 9 | Where to Eat in Hin Kong | 2026-09-02 | 2026-09-07 | UNKNOWN |
| 10 | Where to Eat in Sri Thanu | 2026-09-02 | 2026-09-07 | UNKNOWN |
| 11 | Best Sunset Spots | 2026-08-27 | 2026-09-07 | UNKNOWN |
| 12 | Best Things to Do | 2026-09-04 | 2026-09-07 | UNKNOWN |

Machine-readable: `gsc-crawl-checkpoint-3.csv`. All URLs resolved from the repository
(`site/journal-<slug>.html` on `origin/main`), none guessed.

---

## 3. Why 11 are UNKNOWN and not "NO RECRAWL"

This is the central methodological point of this checkpoint.

For eleven guides, the most recent reliable `Last crawl` value comes from **Crawl Checkpoint #2,
exported 2026-09-07** — **eight days before #147 was deployed**. An observation made before an
event cannot establish anything about what happened after it. Those values prove only that the
pages had been crawled by 7 September; they are silent on 15–23 September.

Classifying them as `NO POST-#147 RECRAWL OBSERVED` would convert a gap in evidence into a
finding. They are therefore `UNKNOWN — NEW GSC INSPECTION REQUIRED`.

**Best Restaurants is different**, and is the only URL that can be classified. Its `Last crawl`
was read on **2026-09-23 — eight days after the deployment** — and still shows 2 September.
Because the observation window covers the post-deployment period, the absence of a later crawl is
itself informative.

### Wording discipline

For Best Restaurants, the finding means exactly:

> *GSC `Last crawl` does not show a post-#147 recrawl for this URL at the checkpoint.*

It does **not** mean:

> *Google definitely never processed any #147 signal by another mechanism.*

---

## 4. Evidence deliberately NOT used

Per §12, `Last crawl` was not inferred from any of the following, all of which were available and
all of which were set aside:

| Available signal | Why it was not used |
|---|---|
| Sitemap `Last read` = 2026-09-21, status Success, 39 pages discovered | A sitemap read is **not** evidence that any individual URL was recrawled. |
| Coverage export 2026-09-22: 40 indexed / 2 not indexed | Index status is **not** evidence of a post-#147 recrawl. A URL indexed before 15 September remains "indexed" without being refetched. |
| GSC Performance impressions rising through 16–18 September | Performance data is **not** crawl data. |
| GA4 sessions | Traffic is **not** crawl data. |
| Deployment dates, Git commits | Publication is **not** fetching. |
| Assumptions about Google's crawl frequency | Not evidence. |

**No UNKNOWN was converted into an estimate.**

---

## 5. What the Coverage export could and could not provide

The 2026-09-22 Coverage workbook (`Coverage-2026-09-22.xlsx`) was examined first, before asking
for any manual inspection. It contains:

- a `Chart` sheet — daily Not indexed / Indexed / Impressions, 2026-07-03 → 2026-09-18;
- a `Critical issues` sheet — 4 reasons, 2 affected pages;
- a `Non-critical issues` sheet — empty;
- a `Metadata` sheet — `Sitemap: All known pages`.

It does **not** contain a per-URL `Last crawled` table. The 2026-09-07 export did contain one
(41 rows), which is why checkpoint #2 could be built from it and checkpoint #3 cannot.

This is a difference in the export, not an error by the operator.

---

## 6. URLs requiring a new manual GSC URL Inspection

Eleven. Best Restaurants is **not** in this list — sufficient evidence already exists.

```
https://darmansour.com/journal-best-cafes-koh-phangan.html
https://darmansour.com/journal-best-beaches-koh-phangan.html
https://darmansour.com/journal-where-to-stay-koh-phangan.html
https://darmansour.com/journal-where-to-eat-thong-sala-koh-phangan.html
https://darmansour.com/journal-romantic-dinner-koh-phangan.html
https://darmansour.com/journal-best-thai-restaurants-koh-phangan.html
https://darmansour.com/journal-best-breakfast-brunch-koh-phangan.html
https://darmansour.com/journal-where-to-eat-hin-kong.html
https://darmansour.com/journal-where-to-eat-sri-thanu.html
https://darmansour.com/journal-where-to-watch-sunset-koh-phangan.html
https://darmansour.com/journal-best-things-to-do-koh-phangan.html
```

For each, record: `Last crawl` (as displayed), `Crawled as`, `Page fetch`, `Indexing allowed`,
`Google-selected canonical`, and the date of observation. **Use URL Inspection only — do not press
Request Indexing**, which would itself trigger a crawl and destroy the observation.

---

## 7. Timezone note

GSC displays `Last crawl` in the property's timezone without stating it (e.g. "Sep 2, 2026,
1:01:26 PM"). The Coverage export gives dates only. The #147 threshold is 2026-09-15 05:38:13 UTC.
Every value recorded here is separated from that threshold by **at least eight days**, so no
classification in this checkpoint depends on timezone resolution. Should a future value fall
within ±1 day of the threshold, the timezone must be established before classifying it.

---

## 8. Interpretation boundary

The single classifiable URL shows no post-#147 recrawl as of 23 September — **eight days** after
deployment. This is an **OBSERVATION**. It is not evidence that #147 had or did not have an
effect, and it supports no causal claim in either direction. The eleven UNKNOWN URLs support no
claim at all until inspected.

---

_Documentation only. No site file modified, no M0 data touched, no indexing requested, no API call
made._
