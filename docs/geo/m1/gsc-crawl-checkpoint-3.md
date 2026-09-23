# GSC CRAWL CHECKPOINT #3 — POST-#147

**Checkpoint date:** 2026-09-23 · **updated 2026-09-23 with 11 manual URL Inspections**
**Reference threshold:** PR #147 (`6f00cb2`) deployment completed **2026-09-15 05:38:13 UTC**

**Question:** for each of the 12 guides modified by #147, does the available GSC evidence show
that Google recrawled the URL **after** that deployment?

---

## 1. Result

| | |
|---|---|
| **POST-#147 RECRAWL CONFIRMED** | **2 / 12** |
| **NO POST-#147 RECRAWL OBSERVED** | **3 / 12** |
| **UNKNOWN — TIME-OF-DAY REQUIRED** | **7 / 12** |

All 12 URLs now have a `Last crawl` value read after the deployment. Five classify unambiguously.
**Seven were crawled on 15 September — the deployment day itself** — and cannot be classified
without the time of day (see §3).

---

## 2. Per-URL table

| # | Guide | `Last crawl` (as displayed) | Classification |
|---|---|---|---|
| 1 | Where to Stay | Sep 18, 2026 | ✅ **POST-#147 RECRAWL CONFIRMED** |
| 2 | Best Sunset Spots | Sep 17, 2026 | ✅ **POST-#147 RECRAWL CONFIRMED** |
| 3 | Best Beaches | Sep 15, 2026 *(time not supplied)* | ⚠️ **UNKNOWN — TIME-OF-DAY REQUIRED** |
| 4 | Where to Eat — Thong Sala | Sep 15, 2026 *(time not supplied)* | ⚠️ **UNKNOWN** |
| 5 | Romantic Dinner | Sep 15, 2026 *(time not supplied)* | ⚠️ **UNKNOWN** |
| 6 | Best Thai Restaurants | Sep 15, 2026 *(time not supplied)* | ⚠️ **UNKNOWN** |
| 7 | Best Breakfast & Brunch | Sep 15, 2026 *(time not supplied)* | ⚠️ **UNKNOWN** |
| 8 | Where to Eat — Hin Kong | Sep 15, 2026 *(time not supplied)* | ⚠️ **UNKNOWN** |
| 9 | Where to Eat — Sri Thanu | Sep 15, 2026 *(time not supplied)* | ⚠️ **UNKNOWN** |
| 10 | Best Things to Do | Sep 13, 2026 | ❌ **NO POST-#147 RECRAWL OBSERVED** |
| 11 | Best Restaurants | Sep 2, 2026, 1:01:26 PM | ❌ **NO POST-#147 RECRAWL OBSERVED** |
| 12 | Best Cafés | Aug 20, 2026, 11:10:56 PM | ❌ **NO POST-#147 RECRAWL OBSERVED** |

Machine-readable: `gsc-crawl-checkpoint-3.csv`. All URLs resolved from the repository, none guessed.

---

## 3. Why seven are UNKNOWN

The threshold is a **timestamp**, not a date: **2026-09-15 05:38:13 UTC**. Seven guides were
crawled **on 15 September**, the same calendar day. Whether each crawl falls before or after
05:38:13 UTC depends on two things that are not currently available:

1. **the time of day** — GSC displays it (e.g. "Sep 2, 2026, 1:01:26 PM"), but the values supplied
   for these seven were truncated after the date;
2. **the timezone GSC is displaying in** — GSC does not state it, and the threshold is expressed
   in UTC.

Classifying them either way would be an assumption. Recording a crawl as CONFIRMED because it
happened "on the 15th" would silently assume it occurred after 05:38 UTC; recording it as NO
RECRAWL would assume the opposite. Neither is supported by the evidence.

**No UNKNOWN has been converted into an estimate.**

### To resolve them

Re-read the same seven URL Inspections and supply the **full displayed timestamp**, including
time. Once the time is known, the GSC display timezone must also be established (Settings →
property, or by comparing a known-UTC event) before comparing against 05:38:13 UTC.

```
https://darmansour.com/journal-best-beaches-koh-phangan.html
https://darmansour.com/journal-where-to-eat-thong-sala-koh-phangan.html
https://darmansour.com/journal-romantic-dinner-koh-phangan.html
https://darmansour.com/journal-best-thai-restaurants-koh-phangan.html
https://darmansour.com/journal-best-breakfast-brunch-koh-phangan.html
https://darmansour.com/journal-where-to-eat-hin-kong.html
https://darmansour.com/journal-where-to-eat-sri-thanu.html
```

⚠️ **URL Inspection only — do not press Request Indexing**, which would trigger a crawl and
destroy the observation.

---

## 4. The five unambiguous classifications

| Guide | Value | Gap from threshold | Robust to timezone? |
|---|---|---|---|
| Where to Stay | Sep 18 | +3 days | Yes — no plausible offset closes 3 days |
| Best Sunset Spots | Sep 17 | +2 days | Yes |
| Best Things to Do | Sep 13 | −2 days | Yes |
| Best Restaurants | Sep 2, 1:01:26 PM | −13 days | Yes |
| Best Cafés | Aug 20, 11:10:56 PM | −26 days | Yes |

---

## 5. Evidence deliberately NOT used

`Last crawl` was not inferred from any of the following, all available and all set aside:

| Available signal | Why it was not used |
|---|---|
| Sitemap `Last read` = 2026-09-21, status Success, 39 pages | A sitemap read is **not** evidence that an individual URL was recrawled. |
| Coverage export 2026-09-22: 40 indexed / 2 not indexed | Index status is **not** evidence of a post-#147 recrawl. |
| GSC Performance impressions 16–18 September | Performance data is **not** crawl data. |
| GA4 sessions | Traffic is **not** crawl data. |
| Deployment dates, Git commits | Publication is **not** fetching. |
| Assumptions about Google's crawl frequency | Not evidence. |

---

## 6. Baseline comparison — checkpoint #2 → #3

| Guide | Checkpoint #2 (07/09) | Checkpoint #3 (23/09) | Moved |
|---|---|---|---|
| Where to Stay | 2026-09-02 | 2026-09-18 | ✅ |
| Best Sunset Spots | 2026-08-27 | 2026-09-17 | ✅ |
| Best Beaches | 2026-09-02 | 2026-09-15 | ✅ |
| Thong Sala | 2026-09-02 | 2026-09-15 | ✅ |
| Romantic Dinner | 2026-09-02 | 2026-09-15 | ✅ |
| Best Thai Restaurants | 2026-08-21 | 2026-09-15 | ✅ |
| Breakfast & Brunch | 2026-09-02 | 2026-09-15 | ✅ |
| Hin Kong | 2026-09-02 | 2026-09-15 | ✅ |
| Sri Thanu | 2026-09-02 | 2026-09-15 | ✅ |
| Best Things to Do | 2026-09-04 | 2026-09-13 | ✅ |
| Best Restaurants | 2026-09-02 | 2026-09-02 | — |
| Best Cafés | 2026-08-20 | 2026-08-20 | — |

Ten of twelve were recrawled between the two checkpoints. **Best Restaurants and Best Cafés have
not been recrawled since before #147** — and Best Cafés not since 20 August.

---

## 7. Timezone note

GSC displays `Last crawl` in a timezone it does not state. For the five classified URLs the gap
from the threshold is at least two days, so no classification depends on resolving it. For the
seven UNKNOWN URLs, the timezone **must** be established alongside the time of day.

---

## 8. Interpretation boundary

Everything above is **OBSERVATION**. That Google fetched a page after 15 September is evidence of
a fetch, nothing more. It is not evidence that #147 had, or did not have, any effect on retrieval
or performance, and supports no causal claim in either direction.

---

_Documentation only. No site file modified, no M0 data touched, no indexing requested, no API call
made._
