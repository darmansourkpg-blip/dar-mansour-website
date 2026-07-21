# SEO & GEO Playbook (portable)

All the SEO + GEO (Generative Engine Optimisation) rules validated for Dar Mansour,
written generically so they can be reused on another site — e.g. **Eden & Beyond**
(Maïja's interior & creative studio). Replace the placeholders:

- `[Brand]` — the brand name (e.g. "Eden & Beyond")
- `[Brand - Legal]` — full/legal name if any
- `[domain]` — the live domain (e.g. `edenandbeyond.com`)
- `[City/Area]` — main location(s)

> Goal: be **read and cited by AI engines** (ChatGPT, Perplexity, Google AI Overviews,
> Claude) **and** keep a healthy Google SEO. The structure serves the machine; the
> writing serves the human.

---

## 1. Technical readability (foundation — never break)

- **Static, pre-rendered HTML. Zero JS dependency for content.** LLMs and many crawlers
  don't execute JS — the text must be in the HTML.
- **Semantic, stable URLs.** Never rename an existing URL (it breaks indexing). Kebab-case,
  descriptive, keyword-bearing.
- **`llms.txt`** at the root: brand intro + key pages + all articles. Generate it from the
  build; don't hand-edit.
- **`robots.txt`** explicitly welcomes AI crawlers: `GPTBot, OAI-SearchBot, ChatGPT-User,
  ClaudeBot, Claude-Web, anthropic-ai, PerplexityBot, Perplexity-User, Google-Extended,
  CCBot, Applebot-Extended, cohere-ai`. `Allow: /` + a named opt-in for each.
- **Sitemap `<lastmod>` must be accurate**, not a blanket "today" on every deploy:
  per-page real change date (git commit date of the source). A lastmod that is always
  "today" while content is unchanged erodes Google's trust in the signal.

## 2. Answer-first (mandatory on every guide)

- Right under the title/subtitle, a **direct answer sentence** naming the best options by
  style/area/occasion → citable by AI + eligible for a Google featured snippet.
- **Vary the lead-in** across articles ("Short answer", "In a hurry?", "Quick answer",
  "Straight to it", "The quick version", "In short"…). Never the same boilerplate (Google
  penalises identical patterns). For a **culture/definition** article, prefer a definition
  sentence.
- The meta `description` must also contain the synthetic answer.

## 3. Fragment structure (each guide should tick all four)

1. **Explicit H2/H3** phrased as questions or direct statements ("Where to…", "Why you can
   trust this", "How to…").
2. **Bulleted AND numbered lists** at key moments.
3. **≥ 1 comparison table** (a "Quick Picks" style). *Exception: narrative/culture articles
   don't need one.*
4. **FAQ** at the end (5–8 questions, anticipating query fan-out) with FAQPage schema and a
   `#faq` anchor.

## 4. Schema.org / JSON-LD

- Types as relevant: `Organization`, `LocalBusiness`/`Restaurant`/appropriate subtype,
  `BlogPosting` (articles), `FAQPage`, `Person`, `Service`/`Product` if applicable.
- **Freshness**: `datePublished` + `dateModified`. `dateModified` = **last git commit date**
  of the file (fallbacks: front-matter `updated:`, then publish date). Never hard-set
  `dateModified = datePublished`. Keep `fetch-depth: 0` in the deploy workflow so git dates
  are available.
- **`sameAs`**: one canonical URL per official profile, kept **in sync** everywhere it
  appears (article schema + org/business schema). One profile per platform — never split
  across duplicate pages (a duplicated profile dilutes the entity).

## 5. Authority & trust (E-E-A-T + entity)

- **Attribute distinctions, don't self-proclaim.** "Featured by X among…" not "one of the
  best". AI cites the attributed claim and distrusts bare superlatives.
- **Build the entity graph**: create and cross-link official profiles — **Wikidata**,
  **Crunchbase**, **OpenStreetMap** (with `brand:wikidata` back-link), **Apple Maps**,
  **Bing Places** (stable ypid URL, never a session-token search URL), **Pinterest**
  (domain-verified), Google Business, Facebook, Instagram, TripAdvisor/relevant directories.
  Add each to `sameAs`. Wikipedia only once independent press coverage is sufficient.
- **Cross-media image naming convention**: name/describe the same photo consistently across
  the web (site alt text + Wikimedia Commons + Google) — e.g.
  `[Brand] <subject/scene>, [City/Area], [Country]`. Repeated co-occurrence teaches AI the
  entity. (One Wikimedia image can be linked as `image`/P18 on Wikidata.)
- **Never invent** `review`/`aggregateRating`, quotes, awards or facts. Real customer
  reviews are never rewritten (not even for banned words).

## 6. Internal linking

- **≥ 3 descriptive outgoing internal links** per article (never "click here").
- **≥ 2 incoming internal links** to every new article from topically related pages
  (aim 3+). **Never forward-only**: after publishing, update older articles to link to the
  new one. Enforce with a build linter that warns on under-linked pages.
- **"By area" pattern** (local SEO): geographic sections use H2 "Where to [X] Around
  [Area]" and H3 "[X] in [Zone]", each linking to the dedicated zone guide when it exists.

## 7. Images (mandatory checklist before referencing)

1. **Filename** kebab-case, descriptive, no spaces/capitals/apostrophes/`%`/random hashes.
   Rename ALL siblings (`.jpg` **and** `.webp`) and repoint every reference; then `grep` = 0
   old references.
2. **Weight**: cover < ~200 KB, other visuals < ~250 KB. Compress (lower quality, resize if
   > ~1700 px) before commit.
3. **WebP sibling** next to every visible `.jpg/.png` (the template serves WebP only if the
   sibling exists on disk).
4. **`alt` always filled** (except purely decorative images in `aria-hidden`); for
   subject/place photos follow the cross-media convention (§5).

## 8. Editorial voice & banned words

- Warm, informed, elegant, never salesy. Show, don't tell.
- **Ban empty marketing words** (linted at build across ALL pages, not just the blog):
  best ever, world-class, incredible, amazing, breathtaking, unforgettable, hidden gem,
  must-visit, bucket list, culinary journey, nestled in, vibrant/rich tapestry, foodies,
  paradise, game-changer, delve into, boasts, "whether you're…", "it's not just X, it's Y",
  "a testament to", "seamlessly blends". Whitelist only genuine quotes (press/customer).

## 9. Meta rules per page

- `title`/`seo_title` ~50–60 chars (Google truncates ~60) — don't overflow.
- `description` ~145–160 chars, containing the synthetic answer.
- One clear search intent per page; one main keyword + natural variations (no stuffing).
- Include common alternate spellings naturally in the body when relevant (e.g. tajine/tagine).

## 10. Getting crawled / indexed

- On deploy: regenerate sitemap + **ping IndexNow** (Bing/Yandex re-crawl in minutes).
  Note: **Google does not use IndexNow** — it re-crawls via sitemap on its own schedule.
- After a key change (title/meta/new page): **GSC → URL Inspection → Request Indexing** for
  the priority pages (limited daily quota — reserve for what matters).

## 11. Off-site (backlinks + AI visibility)

- For AI, being **mentioned by name** on high-authority guides matters almost as much as a
  dofollow link (entity co-occurrence). Target: local media, high-DA travel/industry guides
  frequently cited by AI, independent bloggers (add to existing listicles), and **reciprocal
  partnerships** with non-competing local businesses (e.g. luxury villas ↔ restaurant).
- Always personalise outreach; offer a real experience (tasting / studio visit) — it's the
  strongest conversion lever. Always disclose who publishes the content.

---

_Source of truth for Dar Mansour lives in its `CLAUDE.md`. This playbook is the portable,
brand-agnostic distillation to reuse on Eden & Beyond or any future site._
