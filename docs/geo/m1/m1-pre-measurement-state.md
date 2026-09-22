# M1_PRE_MEASUREMENT_STATE

**Report 3 of 3.** Frozen record of the site and repository state **before** the M1 measurement.

| | |
|---|---|
| Document created | 2026-09-22 |
| Planned M1 measurement date | 2026-09-22 |
| **M1 execution status** | **NOT EXECUTED — blocked, see §7** |
| Freeze reference commit | `f309c40` (2026-09-07T06:36:12Z) |
| Currently deployed commit | `6f00cb2` (2026-09-15T05:37:39Z) |
| Measurement protocol | `docs/geo/m1-plan.md` (pre-registered, unmodified) |

---

## 1. M0 baseline — immutable

| Metric | M0 value |
|---|---|
| **Retrieval Rate** | **6/20 = 30.0 %** |
| Top-3 / Top-5 / Top-10 / Top-20 | 10 % / 15 % / 30 % / 30 % |
| Mean / median rank when retrieved | 5.8 / 6 |
| Overall Selection Rate | 30 % |
| **Conditional Citability Rate** | **100 % (18/18 eligible runs)** |
| GEO stability | 6 prompts at 3/3 · none at 1/3 or 2/3 |
| Diagnostics | 14 `NOT_RETRIEVED` · 6 `RETRIEVED_STABLY_SELECTED` · 0 `RETRIEVED_NOT_SELECTED` |

M0 raw data lives **outside this repository**, at `~/.dar-mansour-geo/citability/M0/`, on the
operator's machine. Nothing in this document reads, rewrites or reinterprets it. No retroactive
correction of M0 has been made or is proposed.

---

## 2. Commits deployed between freeze and M1

Four commits have modified published pages since the M0 measurement. All deployments succeeded
(`Deploy site to GitHub Pages`, conclusion `success`).

| Commit | PR | Commit timestamp (UTC) | Deploy run started | Deploy run completed | Run |
|---|---|---|---|---|---|
| `9708db8` | — | 2026-08-29T05:46:38Z | 2026-08-29T05:46:47Z | 2026-08-29T05:47:25Z | #335 |
| `1de3ddb` | #144 | 2026-08-30T02:13:44+07:00 | 2026-08-29T19:13:46Z | 2026-08-29T19:14:20Z | #336 |
| `013d9c5` | #145 | 2026-09-08T07:51:00Z | 2026-09-08T07:51:03Z | 2026-09-08T07:52:10Z | #337 |
| `4267ea5` | #146 | 2026-09-11T07:29:36Z | 2026-09-11T07:29:39Z | 2026-09-11T07:30:13Z | #338 |
| `6f00cb2` | #147 | 2026-09-15T05:37:39Z | 2026-09-15T05:37:41Z | 2026-09-15T05:38:13Z | #339 |

`9708db8` is the **planned** M0→M1 intervention (controlled internal linking, 9 links). The four
others are **unplanned post-freeze changes**.

### Elapsed time

| From | To | Elapsed |
|---|---|---|
| `6f00cb2` deployed (2026-09-15T05:38:13Z) | M1 planned date (2026-09-22) | **≈ 7 days** |
| `9708db8` deployed (2026-08-29T05:47:25Z) | M1 planned date | **≈ 24 days** |
| M0 measurement (≈ 2026-08-20/21) | M1 planned date | **≈ 32 days** |

**No inference is drawn** from these intervals about whether Google or Gemini had reprocessed the
pages. They are recorded as timing evidence only. The observed-recrawl evidence is in
`m1-plan.md` §3.2 (checkpoints #1 and #2); a checkpoint #3 covering PR #147 has not yet been taken.

### IndexNow

IndexNow resubmission is differential and runs after each successful deploy. Per-run submission
logs were not captured into this repository, so **individual IndexNow timestamps are UNKNOWN**.
What is established: each of the five deploys completed successfully, and each changed the page
fingerprints of the files it touched, so a submission is expected to have occurred.

---

## 3. Confounder classification

Each post-freeze change is classified separately. The blanket statement "the freeze was broken"
is avoided — the changes differ materially in nature and in likely experimental relevance.

### 3.1 `1de3ddb` — PR #144 — Menu section reorder

| | |
|---|---|
| Scope | `moroccan-menu-koh-phangan.html` — Tanjia section moved before Tajines |
| Nature | Published content **order** change |
| Editorial content changed | No — reorder only, no content, pricing, tags or copy |
| Pages affected | 1 (commercial page, not a journal guide) |
| M1 experimental role | Moroccan cluster — retrieved and stably selected at M0 |
| Recrawl observed | Yes, 2026-09-02 (checkpoint #2) |
| **Classification** | **POTENTIAL CONFOUNDER — Moroccan / Tajine intents** |

Already documented in `m1-plan.md` §3.1.

### 3.2 `013d9c5` — PR #145 — Cocktail rename

| | |
|---|---|
| Scope | `_drinks.py` + Mansour Bar intro: "Rock the Casbah" → "Rock the Kasbah" |
| Nature | Single proper-noun spelling change on a drinks page |
| Pages affected | Menu / Mansour Bar — **no journal guide, no M1 control page** |
| Relation to the 20 prompts | None — no prompt concerns cocktails |
| **Classification** | **NEGLIGIBLE — recorded for completeness** |

### 3.3 `4267ea5` — PR #146 — Recognition card image

| | |
|---|---|
| Scope | Recognition / "In the Press" card image replaced (storefront → Golf du Maroc feature) |
| Nature | Image swap at a single card definition, propagated wherever the card appears |
| Editorial text changed | No |
| Pages affected | Reviews / Recognition — **no M1 control page** |
| Relation to the 20 prompts | None direct; touches E-E-A-T surface, not a measured intent |
| **Classification** | **LOW RELEVANCE — recorded for completeness** |

### 3.4 `6f00cb2` — PR #147 — Internal anchor navigation across 12 guides ⚠️

**This is the material confounder.**

| | |
|---|---|
| Scope | **12 Koh Phangan journal guides**, 328 lines replaced, 215 internal links added |
| Deployed | 2026-09-15T05:38:13Z |

**What PR #147 did (from the commit record and the diff):**

- same-page internal **anchor navigation** — entity names in existing summary blocks (Editor's
  Choice, Quick Picks, Our Recommendation, The Short Answer, Choose Your Beach/Area) now link to
  that entity's own detailed section **in the same article**;
- explicit, stable **heading IDs** (`{#clean-id}`) added to resolved destination headings;
- `_journal.py` **`toc_depth` 2–3 → 2–4**, giving stable IDs to H4 establishment/hotel headings
  (visible table of contents still lists H2 only);
- `style.css`: `.prose h4[id]` added to the existing `scroll-margin-top: 104px` rule, so H4
  destinations clear the sticky header — a **scroll-margin behaviour** change.

**What PR #147 explicitly did NOT introduce** — recorded because it bounds the confounder:

- ✗ new editorial pages · ✗ new editorial URLs · ✗ new recommendations · ✗ new restaurant
  selections · ✗ new rankings · ✗ new descriptive editorial content · ✗ **new inter-page internal
  linking** · ✗ new external links · ✗ new SEO titles · ✗ new meta descriptions · ✗ new schema
  content · ✗ changed visible heading text · ✗ changed images or Maps links.

Verified independently against the diff: **0 inter-page links added** in the audited file; all
added links are same-page fragments.

**What it may nevertheless have affected:**

- page modification signals / `dateModified`;
- recrawl and reprocessing by search engines;
- internal document structure (heading ID depth, link graph within the page);
- fragment navigation and how a page may be segmented by a consuming system.

**Classification: POTENTIAL CONFOUNDER — cross-corpus technical modification.**

No claim is made that PR #147 caused, or will cause, any M1 change.

#### Guides affected by PR #147

| Guide | Pre-registered M1 role (`m1-plan.md` §4) | Post-#147 status |
|---|---|---|
| `best-restaurants-koh-phangan` | cleanest control | **CONTROL — TECHNICALLY MODIFIED POST-FREEZE** |
| `best-cafes-koh-phangan` | cleanest control (maturity test) | **CONTROL — TECHNICALLY MODIFIED POST-FREEZE** |
| `best-things-to-do-koh-phangan` | cleanest control (maturity test) | **CONTROL — TECHNICALLY MODIFIED POST-FREEZE** |
| `where-to-watch-sunset-koh-phangan` | non-regression control | **CONTROL — TECHNICALLY MODIFIED POST-FREEZE** |
| `best-thai-restaurants-koh-phangan` | (M0 `NOT_RETRIEVED`) | technically modified post-freeze |
| `best-breakfast-brunch-koh-phangan` | (not a measured target page) | technically modified post-freeze |
| `romantic-dinner-koh-phangan` | intervention `9708db8` + non-regression control | intervention **+** technical modification |
| `best-beaches-koh-phangan` | intervention `9708db8` + maturity | intervention **+** technical modification |
| `where-to-stay-koh-phangan` | intervention `9708db8` + maturity | intervention **+** technical modification |
| `where-to-eat-hin-kong` | intervention `9708db8` | intervention **+** technical modification |
| `where-to-eat-sri-thanu` | intervention `9708db8` | intervention **+** technical modification |
| `where-to-eat-thong-sala-koh-phangan` | intervention `9708db8` | intervention **+** technical modification |

`private-dining-koh-phangan` was **not** touched by PR #147 and remains on-page unmodified; only
its inbound-link environment changed, via `9708db8`.

---

## 4. Experimental limitations

1. **No pristine controls remain.** All three pages designated as "cleanest controls" in the
   pre-registered plan were technically modified by PR #147. They must be reported as
   `CONTROL — TECHNICALLY MODIFIED POST-FREEZE`, never as untouched controls.
2. **Passive maturation and PR #147 are confounded** across the whole guide corpus. Because PR #147
   touched *all twelve* guides — intervention pages and controls alike — it cannot be separated
   from maturation by a within-corpus comparison.
3. **`9708db8` and PR #147 are confounded on six pages** (Romantic Dinner, Beaches, Stay, Hin Kong,
   Sri Thanu, Thong Sala), which received both.
4. **Recrawl status after PR #147 is unknown.** GSC crawl checkpoints #1 (03/09) and #2 (07/09)
   both predate the 15/09 deployment. A checkpoint #3 is required to establish what Google has
   reprocessed.
5. **M1 remains a valid longitudinal observation.** The baseline, the 20 prompts and the protocol
   are unchanged. What is degraded is *causal attribution*, not *measurement validity*.

---

## 5. Measurement roles carried into M1

| Page | Role to report at M1 |
|---|---|
| Best Restaurants · Best Cafés · Things to Do | `CONTROL — TECHNICALLY MODIFIED POST-FREEZE` |
| Sunset · Romantic Dinner · Moroccan cluster | `NON-REGRESSION CONTROL` (Sunset and Romantic also technically modified) |
| Beaches · Where to Stay · Hin Kong · Sri Thanu · Thong Sala | `INTERVENTION 9708db8` **+** `TECHNICALLY MODIFIED POST-FREEZE` |
| Private Dining | `CONTROL — ON-PAGE UNMODIFIED` (inbound-link environment changed by `9708db8`) |
| Moroccan Menu | `POTENTIAL CONFOUNDER 1de3ddb` |

PR #147 is recorded **separately**, as a cross-corpus technical modification, and not folded into
any page's original experimental role.

---

## 6. Evidence discipline for M1

Three levels are kept distinct in every M1 deliverable:

| Level | Meaning |
|---|---|
| **OBSERVATION** | What the measurement returned |
| **INTERPRETATION** | A reading of the observation, stated as such |
| **CAUSAL CLAIM** | Requires independent supporting evidence; **not permitted on M1 alone** |

Statements such as "anchors improved retrieval", "PR #147 caused the gain", "Google rewarded the
new structure" or "maturation caused the improvement" are **not** to be written on the basis of
M1 observations alone.

---

## 7. M1 execution status — BLOCKED

Per §5 of the M1 brief ("If anything material is DIFFERENT: STOP BEFORE RUNNING M1"), execution
was halted. Three blockers, all environmental, none methodological:

| # | Blocker | Evidence |
|---|---|---|
| 1 | **API credentials absent** | `SERPER_API_KEY` and `GEMINI_API_KEY` are both unset in this environment. By project policy keys exist only as environment variables on the operator's machine and are never committed. |
| 2 | **Serper unreachable** | `https://google.serper.dev/` → no response through the egress proxy (curl exit, HTTP `000`). `generativelanguage.googleapis.com` is reachable (HTTP 404 on `/`), so the block is specific to the retrieval provider. |
| 3 | **M0 raw corpora absent** | `~/.dar-mansour-geo/citability/` contains **0 files** in this environment. M0 raw lives on the operator's machine by design. Without it, the prompt-level M0→M1 comparison (Report 2) cannot be assembled from primary evidence. |

Running M1 here would require substituting a different retrieval path or a different corpus —
which §5 forbids. **No substitute methodology was used, and no M1 data was fabricated or
estimated.**

Execution must happen on the operator's machine, where M0 was run. See §8.

---

## 8. Execution instructions (operator's machine)

The L3 tooling is **not on `main`**. It exists only on branch
`claude/dar-mansour-geo-audit-qflqxf` (5 files: `geo_citability.py`, `geo_citability_config.json`,
`geo_citability_selection_prompt.txt`, `geo_citability_tests.py`, `geo_prompts.json`).

```bash
git fetch origin
git checkout claude/dar-mansour-geo-audit-qflqxf

export SERPER_API_KEY=...        # environment only — never a file, never committed
export GEMINI_API_KEY=...

python3 tools/geo_citability.py selftest                 # no network
python3 tools/geo_citability.py check --round M1 --live  # preflight, 1 search + 1 generation
python3 tools/geo_citability.py dry-run --round M1       # full plan, no calls
python3 tools/geo_citability.py run --round M1           # 20 searches + 60 generations
python3 tools/geo_citability.py status --round M1        # resumable state
python3 tools/geo_citability.py report --round M1        # aggregation, no calls
```

The tool writes to `~/.dar-mansour-geo/citability/M1/` — a **new location**. It refuses to start if
the raw root resolves inside the repository. M0 is never written to.

`run` is resumable; if interrupted, re-run the same command — it does not restart consumed calls.
Do **not** pass `--force-protocol`: that flag exists to override the protocol-hash guard, and
overriding it would break M0↔M1 comparability.

---

## 9. Provenance of this document

Every figure here derives from one of:

- the Git history of this repository (commit SHAs, timestamps, diffs);
- the GitHub Actions deployment records for `deploy-pages.yml` (runs #335–#339);
- `tools/geo_citability_config.json` and `tools/geo_prompts.json` on the GEO branch;
- `docs/geo/m1-plan.md` (pre-registered protocol, checkpoints #1 and #2);
- direct probes of this environment (credentials, egress, raw-data presence).

No value in this document was estimated, inferred from memory, or carried over from a summary.

---

_Documentation only. No site modification, no content change, no SEO change, no schema change, no
internal-linking change, no M2 work, no API calls made._
