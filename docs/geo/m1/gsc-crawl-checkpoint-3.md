# GSC CRAWL CHECKPOINT #3 — POST-#147

**Checkpoint date:** 2026-09-23 · **final — timezone rule resolved**
**Reference threshold:** PR #147 (`6f00cb2`) deployment completed **2026-09-15 05:38:13 UTC**
= **2026-09-15 12:38:13 ICT (UTC+7)**

**Question:** for each of the 12 guides modified by #147, does the available GSC evidence show
that Google recrawled the URL **after** that deployment?

---

## 1. Result — final

| | |
|---|---|
| **POST-#147 RECRAWL CONFIRMED** | **9 / 12** |
| **NO POST-#147 RECRAWL OBSERVED** | **3 / 12** |
| **UNKNOWN** | **0 / 12** |

All twelve URLs are classified. No UNKNOWN remains.

---

## 2. Timezone rule — resolved with an official source

Google documents that `Last crawl` in the URL Inspection tool is displayed **in the user's local
time**:

> **Last crawl** — "The last time this page was crawled by Google, **in your local time**."
> — Google Search Console Help, *URL Inspection tool*, section *Last crawl*.

The inspections were performed **in Thailand (ICT, UTC+7)**. Every `Last crawl` value in this
checkpoint is therefore read as ICT, and the #147 threshold converts to:

```
2026-09-15 05:38:13 UTC  →  2026-09-15 12:38:13 ICT
```

This replaces §7 of the previous version of this document, which recorded the display timezone as
unstated and unresolved. The seven values then classified `UNKNOWN — TIME-OF-DAY REQUIRED` are now
classified: the times were supplied, and the display timezone is established by Google's own
documentation rather than assumed.

*(Note on the rule: it is the **user's** local time, not the property's. Should a future checkpoint
be performed from a different country, its values must be converted from that location's offset,
not from ICT.)*

---

## 3. Per-URL table

| # | Guide | `Last crawl` (ICT, as displayed) | UTC equivalent | vs threshold | Classification |
|---|---|---|---|---|---|
| 1 | Romantic Dinner | Sep 15, 2026, 1:29:16 PM | 2026-09-15T06:29:16Z | +51 min | ✅ **CONFIRMED** |
| 2 | Best Thai Restaurants | Sep 15, 2026, 1:33:16 PM | 2026-09-15T06:33:16Z | +55 min | ✅ **CONFIRMED** |
| 3 | Best Breakfast & Brunch | Sep 15, 2026, 1:33:17 PM | 2026-09-15T06:33:17Z | +55 min | ✅ **CONFIRMED** |
| 4 | Where to Eat — Hin Kong | Sep 15, 2026, 1:35:16 PM | 2026-09-15T06:35:16Z | +57 min | ✅ **CONFIRMED** |
| 5 | Where to Eat — Sri Thanu | Sep 15, 2026, 1:37:16 PM | 2026-09-15T06:37:16Z | +59 min | ✅ **CONFIRMED** |
| 6 | Best Beaches | Sep 15, 2026, 1:39:17 PM | 2026-09-15T06:39:17Z | +61 min | ✅ **CONFIRMED** |
| 7 | Where to Eat — Thong Sala | Sep 15, 2026, 1:41:17 PM | 2026-09-15T06:41:17Z | +63 min | ✅ **CONFIRMED** |
| 8 | Best Sunset Spots | Sep 17, 2026 | — (date only) | +2 days | ✅ **CONFIRMED** |
| 9 | Where to Stay | Sep 18, 2026 | — (date only) | +3 days | ✅ **CONFIRMED** |
| 10 | Best Things to Do | Sep 13, 2026 | — (date only) | −2 days | ❌ **NO POST-#147 RECRAWL OBSERVED** |
| 11 | Best Restaurants | Sep 2, 2026, 1:01:26 PM | 2026-09-02T06:01:26Z | −13 days | ❌ **NO POST-#147 RECRAWL OBSERVED** |
| 12 | Best Cafés | Aug 20, 2026, 11:10:56 PM | 2026-08-20T16:10:56Z | −26 days | ❌ **NO POST-#147 RECRAWL OBSERVED** |

Machine-readable: `gsc-crawl-checkpoint-3.csv`, which carries both the displayed ICT value and the
computed UTC equivalent. All URLs resolved from the repository, none guessed.

Rows 8, 9 and 10 were supplied as dates without a time. They need none: each is at least two full
days from the threshold, so no offset within ±24 h could change the classification.

---

## 4. Observation on the seven 15 September crawls

Recorded as a fact, with no explanation attached:

```
first  13:29:16 ICT  (06:29:16Z)  —  51 min after the deployment
last   13:41:17 ICT  (06:41:17Z)  —  63 min after the deployment
span   12 minutes 1 second
```

Seven of the twelve modified guides were fetched inside a twelve-minute window, starting about
fifty minutes after the deployment completed.

**This is an OBSERVATION.** No mechanism is asserted. In particular, this document does not claim
that the deployment, the IndexNow submission, the sitemap or any other signal caused this
sequence, and does not claim that #147 had any effect on retrieval or performance. A temporal
sequence is not a cause.

---

## 5. Wording discipline for the three NO RECRAWL

For Best Restaurants, Best Cafés and Best Things to Do, the finding means exactly:

> *GSC `Last crawl` does not show a post-#147 recrawl for this URL at the checkpoint of
> 2026-09-23.*

It does **not** mean:

> *Google definitely never processed any #147 signal by another mechanism.*

---

## 6. Evidence deliberately NOT used

`Last crawl` was not inferred from any of the following, all available and all set aside:

| Available signal | Why it was not used |
|---|---|
| Sitemap `Last read` = 2026-09-21, status Success, 39 pages | A sitemap read is **not** evidence that an individual URL was recrawled. |
| Coverage export 2026-09-22: 40 indexed / 2 not indexed | Index status is **not** evidence of a post-#147 recrawl. |
| GSC Performance impressions 16–18 September | Performance data is **not** crawl data. |
| GA4 sessions | Traffic is **not** crawl data. |
| Deployment dates, Git commits | Publication is **not** fetching. |
| Assumptions about Google's crawl frequency | Not evidence. |

Every classification above rests on a `Last crawl` value read directly from GSC URL Inspection,
plus the documented timezone rule.

---

## 7. Baseline comparison — checkpoint #2 → #3

| Guide | Checkpoint #2 (07/09) | Checkpoint #3 (23/09) | Recrawled since #2 |
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

Ten of twelve were recrawled between the two checkpoints, but only nine after the #147 threshold —
Best Things to Do was recrawled on 13 September, two days **before** the deployment.

**Best Restaurants and Best Cafés have not been recrawled at all since before #147**, and Best
Cafés not since 20 August. Both are M1 control pages.

---

## 8. Interpretation boundary

Everything above is **OBSERVATION**. That Google fetched nine of the twelve modified guides after
15 September 05:38:13 UTC is evidence of a fetch, nothing more. It is not evidence that #147 had,
or did not have, any effect on retrieval, ranking or performance, and it supports no causal claim
in either direction. The three pages with no observed post-#147 recrawl support no claim either.

---

## 9. Change log of this document

| Version | Date | Result |
|---|---|---|
| 1 | 2026-09-23 | 0 CONFIRMED · 1 NO RECRAWL · 11 UNKNOWN — only Best Restaurants had an observation later than the deployment |
| 2 | 2026-09-23 | 2 CONFIRMED · 3 NO RECRAWL · 7 UNKNOWN — 11 inspections received; seven dated 15 September without a time |
| **3 (final)** | **2026-09-23** | **9 CONFIRMED · 3 NO RECRAWL · 0 UNKNOWN** — times supplied and the display timezone established from Google's documentation |

---

_Documentation only. No site file modified, no M0 data touched, no indexing requested, no API call
made, no causal analysis performed._
