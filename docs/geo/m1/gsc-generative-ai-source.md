# GSC Generative AI (beta) — source record

Inventory and validation record for the two documents received 2026-09-23. **Independent
observational source**, kept distinct from every other evidence layer.

| | |
|---|---|
| Layer | **E — GSC Generative AI (beta)** |
| Nature | Impressions reported by Google Search Console under "Generative AI features" (beta) |
| Status | **Inventoried and validated. Source files held outside this repository.** |
| Role in M1 | Observational only. **Not** a substitute for any controlled GEO metric. |

---

## 1. Files inventoried

| # | File | Format | Location | Repository status |
|---|---|---|---|---|
| E1 | `https___darmansour.com_-Performance-on-Search-Generative-AI-Features-2026-09-23.xlsx` | XLSX | Operator machine | **NOT committed** — original preserved unchanged, held outside the public repository pending confirmation of its diffusion policy |
| E2 | `Dar_Mansour_M1_GSC_Generative_AI_2026-09-23.md` | Markdown | Operator machine | **NOT committed** — same holding decision pending instruction |

Neither file was modified. This record references them; it does not reproduce their contents
beyond the figures needed for validation.

---

## 2. Independent validation of E1

Recomputed directly from the workbook, not copied from E2.

| Tab | Rows | Sum, last 28 days | Sum, previous 28 days |
|---|---|---|---|
| Countries | 119 | **3 373** | **1 771** |
| Devices | 3 | **3 373** | **1 771** |
| **Pages** | 50 | **3 450** | **1 810** |
| Filters | 2 | — | — |

| Check | Result |
|---|---|
| Countries and Devices totals agree | ✅ 3 373 / 1 771 on both |
| Headline change | **+1 602 = +90,5 %** ✅ (1 602 / 1 771 = 90,46 %) |
| Devices breakdown | Mobile 1 968 / 1 239 · Desktop 1 382 / 516 · Tablet 23 / 16 — sums to 3 373 / 1 771 ✅ |
| Duplicated trailing rows | **None** — unlike the classic Performance export of the same date, whose `Devices` and `Search appearance` tabs repeat their last rows |

**Every figure in E2 is confirmed against E1.** No discrepancy between the report and the export.

---

## 3. The Pages divergence — documented, not corrected

```
Pages tab sum        3 450 / 1 810
Countries & Devices  3 373 / 1 771
divergence            + 77 /  + 39
```

The `Pages` tab sums **higher** than the site total given by both other dimensions. The cause is
not established from the workbook.

**Consequences, applied here:**

- The `Pages` sum must **not** be used as the site total.
- **No traffic share may be derived** from the Pages tab without first clarifying the divergence.
- The 50 raw rows — including unusual URL variants at very low volume — are **kept as they are**.
  Nothing is merged, deduplicated, reallocated or "reconciled".
- **No arbitrary correction has been applied**, and none is proposed.

Per-dimension totals may be used within their own dimension. Cross-dimension arithmetic may not.

---

## 4. Observations recorded from E1

Descriptive only. No mechanism, no attribution.

| Page | Last 28 d | Previous 28 d | Change |
|---|---:|---:|---:|
| Best Beaches | 855 | 319 | +536 |
| Where to Stay | 717 | 257 | +460 |
| Best Sunset Spots | 471 | 365 | +106 |
| Best Things to Do | 232 | 31 | +201 |
| What Is a Tajine | 181 | 130 | +51 |
| Gnaoua Music | 172 | 41 | +131 |
| Thong Sala | 170 | 74 | +96 |
| Best Restaurants | 136 | 128 | +8 |
| **Sri Thanu** | 124 | 156 | **−32** |
| Best Cafés | 82 | 9 | +73 |
| Best Thai Restaurants | 61 | 45 | +16 |
| Breakfast & Brunch | 56 | 44 | +12 |
| Hin Kong | 48 | 45 | +3 |
| Romantic Dinner | 36 | 29 | +7 |
| **Homepage** | 25 | 44 | **−19** |

Countries: Thailand 1 084 / 722 · United Kingdom 252 / 97 · Israel 203 / 106 · United States
195 / 126 · Germany 174 / 65 · Australia 146 / 49.

**Two pages move against the overall trend** — Sri Thanu (−32) and the homepage (−19) — while the
site total rises 90,5 %. Recorded as a fact.

---

## 5. What this source is not

Per the brief, and repeated here so the boundary survives in the document rather than in a message:

- ❌ **Not explicit recommendation by an AI.** These are impressions reported by GSC under a beta
  feature, not evidence that Dar Mansour was cited, quoted or recommended in any generated answer.
- ❌ **Not comparable to the Serper/Gemini results.** The controlled GEO benchmark measures
  retrieval into a corpus and selection from it. This measures impressions. They are different
  objects on different populations.
- ❌ **Not a substitute for Retrieval Rate or Conditional Citability Rate.** Neither may be
  replaced by, compared against, or blended with these impressions.
- ❌ **Not clicks, not sessions, not visits.** The export contains no queries, no clicks and no
  daily breakdown; those measures cannot be reconstructed from it.
- ❌ **Not attributable to any SEO intervention.** The observed change is **not** attributed to
  `9708db8`, to PR #147, to `1de3ddb`, to passive maturation, or to any editorial action.

---

## 6. Limitations

**L1 — Calendar dates unknown.** The `Filters` tab records only `Search type: Web` and
`Date: Last 28 days`. The exact start and end dates of both windows are absent. They must **not**
be assumed equal to the GA4 windows (25/08 → 21/09 vs 28/07 → 24/08) or to any other window in the
M1 dossier. Per E2: compare periods only once their exact dates are established.

**L2 — Generative AI scope not self-evidencing.** The `Filters` tab contains no row naming the
Generative AI feature; the scope is carried by the export's origin and filename, not by the
workbook's own metadata. This does not contradict the source — it means the workbook alone does
not attest its own scope, and the provenance rests on how it was exported.

**L3 — Beta feature.** GSC labels "Generative AI features" as beta. Its definition and
measurement may change without notice, which limits its value as a longitudinal series.

**L4 — No queries, no clicks, no daily series.** Not reconstructible from this export.

---

## 7. Relation to the rest of the M1 dossier

The evidence layers stay separate. This source adds a fifth and does not merge into any existing
one:

| Layer | Source | This source? |
|---|---|---|
| A — GEO retrieval / citability | Serper + Gemini | no |
| B — GSC Search performance | classic Performance export | **no — distinct export, distinct metric** |
| C — GSC crawl / indexation | Coverage, URL Inspection, Sitemap | no |
| D — GA4 traffic | Landing pages, Traffic acquisition | no |
| **E — GSC Generative AI (beta)** | this export | **yes** |

Any future statement combining E with another layer must name both layers explicitly and must not
present one as evidence for the other.

**The controlled M1 measurement remains incomplete** while the Gemini selection phase stands at
17/60. Nothing in this source shortens that wait or substitutes for it.

---

_Inventory and validation only. Source files unmodified and held outside the public repository. No
site file modified, no M0 data touched, no protocol parameter changed, no causal claim made._
