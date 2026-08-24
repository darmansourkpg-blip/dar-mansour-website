#!/usr/bin/env python3
"""IndexNow differentiel pour darmansour.com.

Notifie IndexNow (Bing, Yandex...) UNIQUEMENT des URLs reellement ajoutees,
modifiees ou supprimees par un deploiement — au lieu de re-soumettre les 39
URLs du sitemap a chaque fois. Objectif : precision, moins de bruit, et une
mesure propre de ce qui a ete soumis et quand.

Principe : un manifeste { url: empreinte } est publie AVEC le site. Au
deploiement suivant, on compare le manifeste de PRODUCTION au manifeste du
nouveau build. D'ou l'ordre impose dans le workflow :

    build  ->  diff (AVANT deploiement)  ->  deploy  ->  submit (APRES succes)

Lire le manifeste distant apres le deploiement comparerait le nouveau
manifeste a lui-meme : le CDN de GitHub Pages rendrait le resultat non
deterministe selon l'etat de propagation. D'ou la separation stricte.

Empreinte : SHA-256 du HTML complet, a l'exclusion de la SEULE valeur du champ
`dateModified` des blocs JSON-LD. Ce champ est derive de la date du dernier
commit des fichiers du generateur : retoucher un commentaire dans build.py le
ferait changer sur les 39 pages sans qu'aucun contenu n'ait bouge. Tout le
reste du structured data (@type, name, address, sameAs, author, headline...)
reste dans l'empreinte, comme title, meta description, canonical, H1, contenu
et images.

Usage :
  python3 site/build/indexnow.py diff   --changes /tmp/indexnow-changes.json
  python3 site/build/indexnow.py submit --changes /tmp/indexnow-changes.json [--dry-run]
  python3 site/build/indexnow.py diff   --force        # rattrapage : tout re-soumettre
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
SITE_DIR = HERE.parent
SITE = "https://darmansour.com"
HOST = "darmansour.com"
KEY = "d560aac2461f36d3a26e14cd4bd4f84f"
KEY_LOCATION = f"{SITE}/{KEY}.txt"
MANIFEST_NAME = "indexnow-manifest.json"
MANIFEST_URL = f"{SITE}/{MANIFEST_NAME}"
ENDPOINT = "https://api.indexnow.org/indexnow"
SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"

# La SEULE valeur neutralisee avant hachage. Ancree sur le nom du champ, donc
# sans effet sur le reste du JSON-LD.
DATEMODIFIED_RE = re.compile(r'("dateModified"\s*:\s*")[^"]*(")')
LDJSON_RE = re.compile(
    r'(<script[^>]*type=["\']application/ld\+json["\'][^>]*>)(.*?)(</script>)',
    re.DOTALL | re.IGNORECASE,
)


# --------------------------------------------------------------------------
# Empreintes
# --------------------------------------------------------------------------
def normalise(html: str) -> str:
    """Neutralise `dateModified` a l'interieur des blocs JSON-LD, et rien d'autre."""
    def scrub(m: re.Match) -> str:
        open_tag, body, close_tag = m.group(1), m.group(2), m.group(3)
        return open_tag + DATEMODIFIED_RE.sub(r"\1<NORMALISED>\2", body) + close_tag

    return LDJSON_RE.sub(scrub, html)


def page_hash(path: Path) -> str:
    html = path.read_text(encoding="utf-8")
    return hashlib.sha256(normalise(html).encode("utf-8")).hexdigest()


def url_to_path(loc: str) -> Path | None:
    """Inverse de `_loc()` dans build.py : URL publique -> fichier sur disque."""
    if not loc.startswith(SITE):
        return None
    rel = loc[len(SITE):].lstrip("/")
    candidate = SITE_DIR / (rel if rel else "index.html")
    if candidate.is_dir() or rel.endswith("/"):
        candidate = SITE_DIR / rel / "index.html"
    return candidate if candidate.is_file() else None


def sitemap_urls() -> list[str]:
    """URLs indexables, telles que le sitemap les declare.

    Le sitemap exclut deja les pages `noindex` (build.py) : s'y adosser evite
    de soumettre /links ou toute page volontairement hors index."""
    sm = SITE_DIR / "sitemap.xml"
    if not sm.is_file():
        sys.exit("sitemap.xml introuvable — lance d'abord `python3 site/build/build.py`.")
    root = ET.fromstring(sm.read_text(encoding="utf-8"))
    return [el.text.strip() for el in root.iter(f"{SITEMAP_NS}loc") if el.text]


def build_manifest() -> dict:
    pages, missing = {}, []
    for loc in sitemap_urls():
        path = url_to_path(loc)
        if path is None:
            missing.append(loc)
            continue
        pages[loc] = page_hash(path)
    if missing:
        print(f"  ! {len(missing)} URL(s) du sitemap sans fichier local : {missing[:3]}")
    return {
        "version": 1,
        "host": HOST,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "pages": pages,
    }


# --------------------------------------------------------------------------
# Manifeste de production
# --------------------------------------------------------------------------
class RemoteState:
    ABSENT = "absent"           # 404 : premier deploiement -> sitemap complet une fois
    UNREACHABLE = "unreachable"  # reseau/5xx : on ne deduit AUCUNE suppression
    OK = "ok"


def fetch_remote_manifest(url: str, timeout: int = 20) -> tuple[str, dict]:
    # Anti-cache : le CDN de GitHub Pages peut servir une copie plus ancienne.
    # Recuperer une version trop ancienne ne fait que sur-soumettre quelques
    # URLs — jamais en manquer — donc ce cas reste sans danger.
    bust = f"{url}?t={int(datetime.now(timezone.utc).timestamp())}"
    req = urllib.request.Request(bust, headers={
        "User-Agent": "dar-mansour-indexnow/1.0",
        "Cache-Control": "no-cache",
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return RemoteState.OK, json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return RemoteState.ABSENT, {}
        return RemoteState.UNREACHABLE, {"error": f"HTTP {exc.code}"}
    except Exception as exc:  # reseau, TLS, JSON invalide
        return RemoteState.UNREACHABLE, {"error": str(exc)[:200]}


# --------------------------------------------------------------------------
# diff — AVANT deploiement
# --------------------------------------------------------------------------
def cmd_diff(args) -> None:
    new = build_manifest()
    new_pages = new["pages"]

    manifest_path = SITE_DIR / MANIFEST_NAME
    manifest_path.write_text(json.dumps(new, indent=2) + "\n", encoding="utf-8")
    print(f"Manifeste ecrit : site/{MANIFEST_NAME} ({len(new_pages)} URL(s))")

    if args.force:
        state, old_pages = "force", {}
        print("Mode --force : toutes les URLs du sitemap seront soumises.")
    else:
        state, remote = fetch_remote_manifest(args.old_url)
        old_pages = remote.get("pages", {}) if state == RemoteState.OK else {}
        if state == RemoteState.OK:
            print(f"Manifeste de production lu : {len(old_pages)} URL(s), "
                  f"genere le {remote.get('generated_at', '?')}")
        elif state == RemoteState.ABSENT:
            print("Aucun manifeste en production (404) — premier deploiement :")
            print("  le sitemap complet sera soumis une fois, sans deduire de suppression.")
        else:
            print(f"Manifeste de production INJOIGNABLE ({remote.get('error', '?')}) —")
            print("  repli sur le sitemap complet. AUCUNE suppression ne sera deduite :")
            print("  une erreur reseau ne doit jamais etre lue comme une page disparue.")

    if state == RemoteState.OK:
        added = sorted(u for u in new_pages if u not in old_pages)
        modified = sorted(u for u in new_pages if u in old_pages and old_pages[u] != new_pages[u])
        deleted = sorted(u for u in old_pages if u not in new_pages)
    else:
        # Pas de reference fiable : on soumet tout, on ne supprime rien.
        added, modified, deleted = sorted(new_pages), [], []

    changes = {
        "computed_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "remote_state": state,
        "added": added,
        "modified": modified,
        "deleted": deleted,
        "urls": sorted(set(added) | set(modified) | set(deleted)),
    }
    Path(args.changes).write_text(json.dumps(changes, indent=2) + "\n", encoding="utf-8")

    print()
    print(f"  ajoutees  : {len(added)}")
    print(f"  modifiees : {len(modified)}")
    print(f"  supprimees: {len(deleted)}")
    for label, urls in (("+", added), ("~", modified), ("-", deleted)):
        for u in urls[:12]:
            print(f"    {label} {u}")
        if len(urls) > 12:
            print(f"    … et {len(urls) - 12} autre(s)")
    print(f"\n  -> {len(changes['urls'])} URL(s) a soumettre — {args.changes}")
    if not changes["urls"]:
        print("     Rien n'a change : aucun appel IndexNow ne sera fait.")


# --------------------------------------------------------------------------
# submit — APRES un deploiement reussi
# --------------------------------------------------------------------------
def warn(message: str) -> None:
    """Warning visible : annotation GitHub + resume du job. Non bloquant, mais
    jamais silencieux — un echec avale sans trace est un echec qu'on repete."""
    print(f"::warning title=IndexNow::{message}")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write(f"\n### ⚠️ IndexNow\n\n{message}\n")


def cmd_submit(args) -> None:
    path = Path(args.changes)
    if not path.is_file():
        # L'etape `diff` n'a pas produit sa sortie (elle est non bloquante).
        # On ne devine rien : on signale, on ne soumet pas.
        warn(f"Aucun fichier de changements ({args.changes}) : l'etape `diff` "
             "n'a pas abouti. Aucune URL soumise. Rattrapage : "
             "`indexnow.py diff --force` puis `submit`.")
        return
    changes = json.loads(path.read_text(encoding="utf-8"))
    urls = changes["urls"]

    if not urls:
        print("0 URL changee — aucun appel IndexNow (comportement attendu).")
        return

    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }
    print(f"Soumission de {len(urls)} URL(s) a IndexNow "
          f"(+{len(changes['added'])} ~{len(changes['modified'])} -{len(changes['deleted'])})")
    for u in urls:
        print(f"    {u}")

    if args.dry_run:
        print("\n--dry-run : aucune requete envoyee. Charge utile :")
        print(json.dumps(payload, indent=2)[:1200])
        return

    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(ENDPOINT, data=body, method="POST", headers={
        "Content-Type": "application/json; charset=utf-8",
        "User-Agent": "dar-mansour-indexnow/1.0",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            code, detail = r.status, r.read().decode("utf-8", "replace")[:300]
    except urllib.error.HTTPError as exc:
        code, detail = exc.code, exc.read().decode("utf-8", "replace")[:300]
    except Exception as exc:
        warn(f"Appel IndexNow echoue ({str(exc)[:150]}). "
             f"{len(urls)} URL(s) NON soumise(s) — elles ne seront pas rattrapees "
             f"automatiquement (le manifeste de production est deja a jour). "
             f"Rattrapage : `python3 site/build/indexnow.py diff --force` puis submit.\n\n"
             + "\n".join(f"- {u}" for u in urls))
        return

    meaning = {
        200: "OK — URLs acceptees",
        202: "Accepte — cle en cours de validation",
        400: "Requete invalide",
        403: "CLE REFUSEE — le fichier de cle n'est pas servi ou ne correspond pas",
        422: "URL hors du domaine declare, ou cle incoherente",
        429: "Trop de soumissions",
    }.get(code, "code inattendu")
    print(f"\nHTTP {code} — {meaning}")
    if detail.strip():
        print(f"  reponse : {detail}")

    if code not in (200, 202):
        warn(f"IndexNow a repondu HTTP {code} ({meaning}). {len(urls)} URL(s) "
             f"probablement NON prises en compte. Rattrapage : "
             f"`indexnow.py diff --force` puis submit.\n\n"
             + "\n".join(f"- {u}" for u in urls))


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    d = sub.add_parser("diff", help="AVANT deploiement : construit le manifeste et "
                                    "le compare a celui de production")
    d.add_argument("--changes", default="/tmp/indexnow-changes.json")
    d.add_argument("--old-url", default=MANIFEST_URL)
    d.add_argument("--force", action="store_true",
                   help="ignore le manifeste distant et soumet tout le sitemap")
    d.set_defaults(func=cmd_diff)

    s = sub.add_parser("submit", help="APRES un deploiement reussi : soumet les URLs calculees")
    s.add_argument("--changes", default="/tmp/indexnow-changes.json")
    s.add_argument("--dry-run", action="store_true", help="affiche sans envoyer")
    s.set_defaults(func=cmd_submit)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
