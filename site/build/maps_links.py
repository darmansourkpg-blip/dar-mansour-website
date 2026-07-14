#!/usr/bin/env python3
"""Pipeline semi-automatisé pour optimiser les liens Google Maps du Journal.

Chaque fiche restaurant se termine par une ligne :
    **Getting there —** ... [View on map ↗](URL)

Ce script gère deux modes :

  extract  Lit un article Markdown et produit un CSV (une ligne par établissement)
           avec : name, section, area_hint, status, current_link, new_link.
           « status » vaut « ok » si le lien est déjà un lien court/place
           (maps.app.goo.gl, share.google, /maps/place/) ou « generic » s'il
           s'agit d'une simple recherche (/maps/search/?api=1&query=...).
           On ne remplit « new_link » que pour les liens « generic ».

  apply    Relit le CSV rempli et remplace, dans le Markdown, chaque
           current_link par son new_link (quand new_link est non vide).
           Affiche un récapitulatif et n'écrit le fichier que si tout est cohérent.

Le seul geste manuel : ouvrir chaque établissement sur Google Maps, cliquer
« Partager » et coller le lien court dans la colonne new_link du CSV.

Usage :
    python3 build/maps_links.py extract content/journal/best-restaurants-koh-phangan.md maps-worksheet.csv
    # (remplir la colonne new_link dans maps-worksheet.csv)
    python3 build/maps_links.py apply   content/journal/best-restaurants-koh-phangan.md maps-worksheet.csv
    python3 build/build.py
"""

import csv
import re
import sys
from pathlib import Path

# Un lien est déjà « propre » (point exact) s'il correspond à l'un de ces motifs.
GOOD_LINK = re.compile(
    r"(maps\.app\.goo\.gl|share\.google|/maps/place/|[?&]query=-?\d+\.\d+,-?\d+\.\d+)"
)
MAP_LINK = re.compile(r"\[View on map[^\]]*\]\((?P<url>[^)]+)\)")
HEADING = re.compile(r"^####\s+(?P<name>.+?)\s*$")


def _sections(lines):
    """Génère (name, heading_index) pour chaque fiche #### de l'article."""
    for i, line in enumerate(lines):
        m = HEADING.match(line)
        if m:
            yield m.group("name"), i


def _find_h2(lines, upto):
    """Renvoie le dernier titre de section H2/H3 avant l'index donné."""
    for j in range(upto, -1, -1):
        if lines[j].startswith("## ") or lines[j].startswith("### "):
            return lines[j].lstrip("#").strip()
    return ""


def extract(md_path, csv_path):
    lines = Path(md_path).read_text(encoding="utf-8").splitlines()
    rows = []
    heads = list(_sections(lines))
    for idx, (name, hi) in enumerate(heads):
        end = heads[idx + 1][1] if idx + 1 < len(heads) else len(lines)
        block = "\n".join(lines[hi:end])
        m = MAP_LINK.search(block)
        if not m:
            continue
        url = m.group("url").strip()
        # Indice de localisation = texte "Getting there —" nettoyé du lien.
        hint = ""
        for bl in lines[hi:end]:
            if "Getting there" in bl:
                hint = re.sub(r"\s*\[View on map.*$", "", bl)
                hint = hint.replace("**Getting there —**", "").strip()
                break
        status = "ok" if GOOD_LINK.search(url) else "generic"
        rows.append(
            {
                "name": name,
                "section": _find_h2(lines, hi),
                "area_hint": hint,
                "status": status,
                "current_link": url,
                "new_link": "",
            }
        )

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["name", "section", "area_hint", "status", "current_link", "new_link"],
        )
        w.writeheader()
        w.writerows(rows)

    generic = sum(1 for r in rows if r["status"] == "generic")
    ok = len(rows) - generic
    print(f"{len(rows)} établissements — {ok} liens déjà propres, {generic} à optimiser.")
    print(f"CSV écrit : {csv_path}")
    print("→ Remplis la colonne new_link pour les lignes status=generic, puis lance 'apply'.")


def apply(md_path, csv_path):
    text = Path(md_path).read_text(encoding="utf-8")
    with open(csv_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    changed, skipped, missing = 0, 0, []
    for r in rows:
        new = (r.get("new_link") or "").strip()
        old = (r.get("current_link") or "").strip()
        if not new:
            skipped += 1
            continue
        if new == old:
            skipped += 1
            continue
        if old not in text:
            missing.append(r["name"])
            continue
        text = text.replace(old, new)
        changed += 1
        print(f"  ✓ {r['name']}")

    if missing:
        print("\n⚠ Liens introuvables dans le Markdown (à vérifier) :")
        for n in missing:
            print(f"    - {n}")
        print("Aucune écriture effectuée. Corrige le CSV puis relance.")
        sys.exit(1)

    Path(md_path).write_text(text, encoding="utf-8")
    print(f"\n{changed} liens remplacés, {skipped} inchangés.")
    print("→ Lance maintenant : python3 build/build.py")


def main():
    if len(sys.argv) != 4 or sys.argv[1] not in ("extract", "apply"):
        print(__doc__)
        sys.exit(2)
    mode, md_path, csv_path = sys.argv[1], sys.argv[2], sys.argv[3]
    (extract if mode == "extract" else apply)(md_path, csv_path)


if __name__ == "__main__":
    main()
