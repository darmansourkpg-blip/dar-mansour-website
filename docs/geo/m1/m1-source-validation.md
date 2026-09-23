# M1 — SOURCE VALIDATION

Validation of the four primary evidence files received on 2026-09-23. All are treated as
**immutable source evidence**: nothing was overwritten, corrected or inferred. Where a file
diverges from expectation, the divergence is recorded, not fixed.

---

## FILE 1 — GSC Performance (authoritative)

| | |
|---|---|
| Filename | `https___darmansour.com_-Performance-on-Search-2026-09-23.xlsx` |
| Source | Google Search Console → Performance → Search results |
| Reporting period | Last 28 days |
| Comparison period | Previous 28 days |
| Filters (`Filters` tab) | `Search type = Web` · `Date = Last 28 days` |
| **Page filter** | **NONE — verified in the `Filters` tab** ✅ |
| Tabs present | Queries · Pages · Countries · Devices · Search appearance · Filters ✅ |
| Queries | **1 093** (1 094 rows incl. header) — matches the ~1 093 expected ✅ |
| Pages | **125** (126 rows incl. header) — matches the ~125 expected ✅ |
| Countries | 168 · Devices | 3 · Search appearance | 2 |
| **Suitable for M1** | **YES — authoritative** |

Replaces the 2026-09-22 export, which carried an unintended page filter. The earlier file is not
used anywhere in this package.

**Anomaly recorded, not corrected:** the `Devices` and `Search appearance` tabs repeat their last
rows (Desktop and Tablet appear twice; Translated results and Review snippet appear twice). This
is an artefact of the GSC export itself. Any aggregation over those two tabs must de-duplicate
before summing. `Queries`, `Pages` and `Countries` are unaffected.

---

## FILE 2 — GSC Coverage / Indexing

| | |
|---|---|
| Filename | `https___darmansour.com_-Coverage-2026-09-22.xlsx` |
| Source | GSC → Indexing → Pages |
| Scope (`Metadata`) | `Sitemap: All known pages` |
| Tabs | Chart · Critical issues · Non-critical issues · Metadata |
| `Chart` range | 2026-07-03 → **2026-09-18** (78 daily rows) |
| Latest data date | **2026-09-18** |
| Latest state | **40 indexed · 2 not indexed** · 655 impressions on 18/09 |
| `Critical issues` | Excluded by 'noindex' tag — 1 page · Alternate page with proper canonical — 1 page · Discovered/not indexed — 0 · Crawled/not indexed — 0 |
| `Non-critical issues` | empty |
| **Suitable for M1** | **YES**, as an indexing/coverage source |

**Material limitation:** this workbook contains **no per-URL `Last crawled` table**. The 2026-09-07
export did (41 rows), which is why Crawl Checkpoint #2 could be built from an export and
Checkpoint #3 cannot. This is a difference between exports, not an operator error.

Per §6 and §12: **"indexed" is not evidence of a post-#147 recrawl.** A page indexed before
15 September remains "indexed" without being refetched.

---

## FILE 3 — GA4 Organic Landing Pages

| | |
|---|---|
| Filename | `Landing page_ Landing page.xlsx` |
| Source | GA4 → Landing page report |
| Current period | **2026-08-25 → 2026-09-21** ✅ |
| Comparison period | **2026-07-28 → 2026-08-24** ✅ |
| Audience line | `# All Users` |
| Rows | 28 landing pages per period |
| Metrics | Sessions · Active users · New users · Avg engagement time/session · Key events · Total revenue · Session key event rate |
| **Suitable for M1** | **YES, with the truncation limitation below** |

**Organic Search filter — verified indirectly.** The export header states `# All Users` and does
not name the channel filter, so the filter was checked by cross-reference against File 4:

| Period | Landing-page sessions | Organic Search (File 4) | All channels (File 4) | Coverage |
|---|---|---|---|---|
| 25/08 → 21/09 | 323 | **338** | 743 | **95.6 % of Organic** · 43 % of all |
| 28/07 → 24/08 | 280 | **300** | 690 | **93.3 % of Organic** · 41 % of all |

The totals track Organic Search closely and are nowhere near the all-channel totals. **The
Organic Search filter is applied.**

**Limitation:** the export is truncated to 28 rows per period, so **15 sessions (4.4 %) in the
current period and 20 (6.7 %) in the comparison period are not represented** — GA4's long tail
plus any `(not set)`. Per-page figures are sound; **do not treat the row sum as the organic
total.** Use File 4 for channel totals.

---

## FILE 4 — GA4 Traffic Acquisition

| | |
|---|---|
| Filename | `Traffic_acquisition_Session_primary_channel_group_(Default_Channel_Group).csv` |
| Source | GA4 → Traffic acquisition → Session primary channel group |
| Current period | **2026-08-25 → 2026-09-21** ✅ |
| Comparison period | **2026-07-28 → 2026-08-24** ✅ |
| Filter | **NONE — `# All Users`, all channel groups retained** ✅ |
| Channels present | Organic Search · Direct · **AI Assistant** · Organic Social · Unassigned · Referral ✅ |
| **Suitable for M1** | **YES** |

Descriptive facts recorded, **no interpretation**:

| Channel | 25/08–21/09 sessions | 28/07–24/08 sessions |
|---|---|---|
| Organic Search | 338 | 300 |
| Direct | 295 | 321 |
| **AI Assistant** | **100** | **44** |
| Organic Social | 4 | 8 |
| Unassigned | 4 | 7 |
| Referral | 2 | 10 |
| **Total** | **743** | **690** |

⚠️ Per §7: **`AI Assistant` sessions are NOT the controlled GEO Citability metric.** They are
GA4 referral traffic (layer D). The GEO measurement (layer A) is the Serper + Gemini benchmark and
is independent. These numbers are recorded here and must not be substituted for, or compared
against, the M1 Retrieval Rate or Conditional Citability Rate.

Note also that the GA4 periods (25/08 → 21/09) do **not** align with the L2 M0 baseline period
(01/07 → 25/08, 56 days) recorded in the AI Referral level-2 work. Any M0→M1 comparison at level 2
must use rates, not session volumes, or be rebuilt on matching windows.

---

## FILE 5 — GSC Sitemap (screenshot observation)

| | |
|---|---|
| Sitemap | `/sitemap.xml` |
| Submitted | 2026-07-16 |
| **Last read** | **2026-09-21** |
| Status | Success |
| Discovered pages | 39 · videos 0 |
| Observed | 2026-09-23 |

This establishes that Google read the sitemap **after** #147 was deployed (15/09).

⚠️ Per §6: **a sitemap read is not evidence that any of the 12 guides was individually
recrawled.** It is not used in Crawl Checkpoint #3.

---

## Cross-file consistency

| Check | Result |
|---|---|
| GSC Coverage "39 discovered pages" (sitemap) vs 40 indexed (Coverage chart) | Consistent — the sitemap lists 39; the index count includes pages reachable outside the sitemap. No action. |
| GSC Performance 125 pages vs 40 indexed | Consistent — Performance lists any URL with an impression in the window, including pages now excluded or redirected. |
| GA4 landing pages vs GA4 channels | Consistent — see File 3. |

---

## Evidence-layer discipline

The four layers are kept separate throughout and are never collapsed:

| Layer | Source | Status |
|---|---|---|
| **A — GEO retrieval / citability** | Serper + Gemini | Retrieval 20/20 complete · **Gemini selection incomplete** |
| **B — GSC search performance** | File 1 | Complete |
| **C — GSC crawl / indexation** | File 2, File 5, URL Inspection | Coverage complete · crawl 1/12 classifiable |
| **D — GA4 traffic** | Files 3 and 4 | Complete |

An increase in Organic Search sessions is not proof of a GEO effect. An increase in GSC
impressions is not proof that #147 caused it. An increase in AI Assistant sessions is not the GEO
Citability metric. A sitemap read is not an individual recrawl. An indexed URL is not proof that
Google processed the #147 version.

---

_Validation only. No source file modified. No missing value inferred. No causal claim made._
