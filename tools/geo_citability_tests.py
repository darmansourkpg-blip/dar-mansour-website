#!/usr/bin/env python3
"""Tests du GEO Citability Benchmark — fixtures locales, AUCUN reseau.

Couvre les six familles exigees par le protocole : retrieval, normalisation,
selection, reprise, securite, rupture de protocole.
"""
from __future__ import annotations

import json
import os
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import geo_citability as g

RESULTS: list[tuple[bool, str, str]] = []


def check(label: str, got, expected) -> None:
    RESULTS.append((got == expected, label, f"attendu {expected!r}, obtenu {got!r}"))


def organic(*urls) -> list[dict]:
    return [{"link": u, "title": f"Title {i}", "snippet": f"Snippet {i}"}
            for i, u in enumerate(urls, start=1)]


CFG = json.loads((Path(__file__).resolve().parent / "geo_citability_config.json").read_text())
OTHER = "https://tripadvisor.com/x"
DM = "https://darmansour.com/journal-best-restaurants-koh-phangan.html"


# --- 1. Retrieval -----------------------------------------------------------
def test_retrieval() -> None:
    for pos in (1, 3, 10, 20):
        urls = [OTHER] * 20
        urls[pos - 1] = DM
        r = g.retrieval_metrics(g.build_corpus(organic(*urls), CFG))
        check(f"retrieval — Dar Mansour #{pos} detecte", r["retrieved"], True)
        check(f"retrieval — best_rank #{pos}", r["best_rank"], pos)
        check(f"retrieval — top_3 a #{pos}", r["top_3"], pos <= 3)
        check(f"retrieval — top_10 a #{pos}", r["top_10"], pos <= 10)

    r = g.retrieval_metrics(g.build_corpus(organic(*[OTHER] * 20), CFG))
    check("retrieval — absent", r["retrieved"], False)
    check("retrieval — best_rank absent = None", r["best_rank"], None)

    r = g.retrieval_metrics(g.build_corpus(
        organic(OTHER, DM, OTHER, "https://darmansour.com/faq.html"), CFG))
    check("retrieval — plusieurs URLs owned", r["owned_url_count"], 2)
    check("retrieval — best_rank = le meilleur", r["best_rank"], 2)

    # Domaine piege : contient le texte 'darmansour' sans etre le notre.
    for trap in ("https://notdarmansour.com/x", "https://darmansour.com.evil.net/x",
                 "https://fake-darmansour.com/", "https://blog.com/dar-mansour-review"):
        r = g.retrieval_metrics(g.build_corpus(organic(trap), CFG))
        check(f"retrieval — piege ignore : {g.domain_of(trap)}", r["retrieved"], False)

    check("retrieval — sous-domaine reconnu",
          g.is_owned("https://www2.darmansour.com/x", "darmansour.com"), True)

    # Profondeur reelle inferieure a la profondeur demandee : accepte tel quel.
    c = g.build_corpus(organic(*[OTHER] * 17), CFG)
    check("depth — actual_depth conserve", c["actual_depth"], 17)
    check("depth — requested_depth conserve", c["requested_depth"], 20)


# --- 2. Normalisation d'URL -------------------------------------------------
def test_normalisation() -> None:
    cases = {
        "https://darmansour.com/x?utm=1": True,
        "https://www.darmansour.com/x": True,
        "https://darmansour.com/": True,
        "https://DARMANSOUR.COM/X": True,
        "http://darmansour.com": True,
        "https://darmansour.com:443/x": True,
        "https://tripadvisor.com/darmansour.com": False,
        "": False,
    }
    for url, expected in cases.items():
        check(f"normalisation — {url or '(vide)'}", g.is_owned(url, "darmansour.com"), expected)


# --- 3. Selection -----------------------------------------------------------
def selection_payload(sources_used, rec_name=None, rec_ids=None, answer="") -> str:
    return json.dumps({
        "answer": answer,
        "recommendations": ([{"name": rec_name, "source_ids": rec_ids or []}]
                            if rec_name else []),
        "sources_used": sources_used,
    })


def test_selection() -> None:
    corpus = g.build_corpus(organic(OTHER, DM, OTHER), CFG)   # DM = S02

    a = g.analyse_selection(g.parse_selection(
        selection_payload(["S02"], "Dar Mansour", ["S02"], "Try Dar Mansour.")), corpus, CFG, "Commercial")
    check("selection — source owned utilisee", a["selected_source"], True)
    check("selection — rang de la source retenue", a["selected_source_rank"], 2)
    check("selection — marque nommee", a["mentioned_in_answer"], True)
    check("selection — recommandee", a["recommended"], True)
    check("selection — position de recommandation", a["selection_position"], 1)

    # Notre guide sert de source pour recommander un concurrent : selected sans
    # recommended. C'est le cas que la separation des metriques doit rendre visible.
    a = g.analyse_selection(g.parse_selection(
        selection_payload(["S02"], "Fisherman's Restaurant", ["S02"], "Try Fisherman's.")),
        corpus, CFG, "Commercial")
    check("selection — source owned mais concurrent recommande", a["selected_source"], True)
    check("selection — marque non recommandee", a["recommended"], False)
    check("selection — marque non nommee", a["mentioned_in_answer"], False)

    # Marque nommee sans que notre source soit utilisee.
    a = g.analyse_selection(g.parse_selection(
        selection_payload(["S01"], "Dar Mansour", ["S01"], "Dar Mansour is Moroccan.")),
        corpus, CFG, "Commercial")
    check("selection — mention sans source owned", a["selected_source"], False)
    check("selection — mention detectee", a["mentioned_in_answer"], True)

    a = g.analyse_selection(g.parse_selection(
        selection_payload(["S01", "S03"], "Other", ["S01"])), corpus, CFG, "Commercial")
    check("selection — aucune source owned", a["selected_source"], False)

    # Identifiant invente par le modele : ignore, jamais compte.
    a = g.analyse_selection(g.parse_selection(
        selection_payload(["S99"], None, None)), corpus, CFG, "Commercial")
    check("selection — source_id inexistant ignore", a["sources_used_count"], 0)

    for label, payload in (("malformed", "not json at all"),
                           ("tronque", '{"answer": "x", "sources_used": ['),
                           ("vide", "")):
        a = g.analyse_selection(g.parse_selection(payload), corpus, CFG, "Commercial")
        check(f"selection — sortie {label} signalee", a["malformed"], True)
        check(f"selection — sortie {label} non comptee", a["selected_source"], False)

    fenced = "```json\n" + selection_payload(["S02"]) + "\n```"
    check("selection — fences JSON tolerees",
          g.parse_selection(fenced)["sources_used"], ["S02"])

    # Stabilite 0/3 .. 3/3
    for k in range(4):
        check(f"diagnostic — retrieved, {k}/3",
              g.diagnose(True, k, 3),
              {0: "RETRIEVED_NOT_SELECTED", 1: "RETRIEVED_PARTIALLY_SELECTED",
               2: "RETRIEVED_PARTIALLY_SELECTED", 3: "RETRIEVED_STABLY_SELECTED"}[k])
    check("diagnostic — absent, 0 selection", g.diagnose(False, 0, 3), "NOT_RETRIEVED")
    check("diagnostic — absent mais selectionne = ANOMALY", g.diagnose(False, 1, 3), "ANOMALY")


# --- 4. Reprise -------------------------------------------------------------
def test_resumability() -> None:
    tmp = Path(tempfile.mkdtemp())
    cfg = dict(CFG, raw_root=str(tmp))
    root = g.raw_root(cfg, "TEST")
    root.mkdir(parents=True, exist_ok=True)
    prompts = g.load_prompts()

    st = g.round_state(cfg, "TEST")
    check("reprise — etat initial vide", len(st["corpus_done"]), 0)
    check("reprise — runs a faire", st["runs_total"], len(prompts) * 3)

    corpus = g.build_corpus(organic(OTHER, DM), cfg)
    pid = prompts[0]["id"]
    g.corpus_path(cfg, "TEST", pid).write_text(json.dumps(
        {"prompt_id": pid, "prompt": prompts[0]["prompt"], "corpus": corpus, "raw": {}}))
    st = g.round_state(cfg, "TEST")
    check("reprise — corpus existant detecte", st["corpus_done"], [pid])
    check("reprise — corpus restant", len(st["corpus_missing"]), len(prompts) - 1)

    g.run_path(cfg, "TEST", pid, 1).write_text(json.dumps({"prompt_id": pid, "run": 1}))
    st = g.round_state(cfg, "TEST")
    check("reprise — run 1 termine, reprise a run 2", st["runs_done"], [(pid, 1)])

    before = corpus["corpus_hash"]
    after = g.build_corpus(organic(OTHER, DM), cfg)["corpus_hash"]
    check("reprise — hash du corpus stable", after, before)
    check("immutabilite — un corpus different change le hash",
          g.build_corpus(organic(DM, OTHER), cfg)["corpus_hash"] != before, True)
    shutil.rmtree(tmp, ignore_errors=True)


# --- 5. Securite ------------------------------------------------------------
def test_security() -> None:
    os.environ["SERPER_API_KEY"] = "SERPERFAKEKEY_abcdef1234567890"
    os.environ["GEMINI_API_KEY"] = "AQ.FAKEGEMINI_abcdef1234567890"
    leaky = ("error: X-API-KEY SERPERFAKEKEY_abcdef1234567890 rejected; "
             "url=https://x/y?key=AQ.FAKEGEMINI_abcdef1234567890 "
             "other=AIzaSyABCDEFGHIJKLMNOP")
    out = g.redact(leaky)
    check("securite — cle Serper masquee", "SERPERFAKEKEY" in out, False)
    check("securite — cle Gemini masquee", "FAKEGEMINI" in out, False)
    check("securite — motif AIza masque", "AIzaSyABCDEFGHIJKLMNOP" in out, False)
    check("securite — ?key= masque", "key=***REDACTED***" in out, True)

    # Le chemin raw ne doit jamais pouvoir etre a l'interieur du depot.
    try:
        g.raw_root(dict(CFG, raw_root=str(g.ROOT / "data" / "raw")), "M0")
        check("securite — raw dans le depot refuse", "accepte", "refuse")
    except SystemExit:
        check("securite — raw dans le depot refuse", "refuse", "refuse")
    outside = g.raw_root(CFG, "M0")
    check("securite — raw par defaut hors depot", str(outside).startswith(str(g.ROOT)), False)

    gitignore = (g.ROOT / ".gitignore").read_text()
    check("securite — .dar-mansour-geo gitignore", ".dar-mansour-geo/" in gitignore, True)
    for env in g.KEY_ENV:
        os.environ.pop(env, None)


# --- 6. Rupture de protocole ------------------------------------------------
def test_protocol() -> None:
    base = g.protocol(CFG)
    for field, value in (("search_provider", "brave"), ("gl", "us"), ("hl", "fr"),
                         ("requested_depth", 10), ("selection_model", "other"),
                         ("temperature", 0.7), ("runs_per_prompt", 5)):
        changed = g.protocol(dict(CFG, **{field: value}))
        check(f"protocole — changement de {field} detecte",
              len(g.compare_protocol(base, changed)) >= 1, True)
        check(f"protocole — hash change avec {field}",
              changed["protocol_hash"] != base["protocol_hash"], True)
    check("protocole — prompt set hashe", len(base["prompt_set_hash"]), 64)
    check("protocole — selection prompt hashe", len(base["selection_prompt_hash"]), 64)
    check("protocole — identique = aucune rupture", g.compare_protocol(base, base), [])

    # Le prompt de selection ne doit jamais nommer la cible ni le domaine.
    text, version, _ = g.load_selection_prompt()
    low = text.lower()
    for forbidden in ("dar mansour", "darmansour", "morocco's kitchen"):
        check(f"protocole — prompt neutre ({forbidden!r} absent)", forbidden in low, False)
    check("protocole — version du prompt de selection", version, "1.0")


# --- 7. Budget d'appels -----------------------------------------------------
def test_budget() -> None:
    b = g.CallBudget(20, 60)
    for _ in range(20):
        b.spend("search")
    try:
        b.spend("search")
        check("budget — 21e recherche refusee", "acceptee", "refusee")
    except g.CallBudgetExceeded:
        check("budget — 21e recherche refusee", "refusee", "refusee")
    for _ in range(60):
        b.spend("generation")
    try:
        b.spend("generation")
        check("budget — 61e generation refusee", "acceptee", "refusee")
    except g.CallBudgetExceeded:
        check("budget — 61e generation refusee", "refusee", "refusee")

    for status, exc in ((429, g.QuotaExhausted), (402, g.BillingRequired),
                        (401, g.AuthFailure)):
        try:
            g.classify_http(status, "quota exceeded" if status == 429 else "nope")
            check(f"erreurs — HTTP {status} classe", "ignore", exc.__name__)
        except exc:
            check(f"erreurs — HTTP {status} classe", exc.__name__, exc.__name__)
    try:
        g.classify_http(403, "billing account required for this plan")
        check("erreurs — 403 billing classe BillingRequired", "ignore", "BillingRequired")
    except g.BillingRequired:
        check("erreurs — 403 billing classe BillingRequired", "BillingRequired", "BillingRequired")


def run_all() -> None:
    print("GEO Citability — tests sur fixtures locales (aucun reseau)\n")
    for fn in (test_retrieval, test_normalisation, test_selection,
               test_resumability, test_security, test_protocol, test_budget):
        fn()
    failures = [r for r in RESULTS if not r[0]]
    for ok, label, detail in RESULTS:
        if not ok:
            print(f"  FAIL  {label} — {detail}")
    print(f"\n{len(RESULTS) - len(failures)}/{len(RESULTS)} tests passes")
    if failures:
        sys.exit(f"{len(failures)} echec(s)")
    print("Aucun appel reseau effectue.")


if __name__ == "__main__":
    run_all()
