#!/usr/bin/env python3
"""Construit le(s) projet(s) GenSVG de vectorisation des images generees (procedure_animation.md, 2.13).

Usage, depuis la racine du depot :  python3 outils/projet_svg.py

Part TOUJOURS de l'etape 2 : les sources sont les images de ideaN/animation/etape2_assets/generes/, les SVG sont ranges dans
ideaN/animation/etape2_assets/svg/<id>.svg (pousses par le bot, depuis sAutoniax, des qu'ils sont generes).

Ne vectorise que :
  - les assets de assets.json non desactives dont l'image EST DEJA dans generes/ (un fichier a pour nom l'id de l'asset, quelle que
    soit l'extension) ;
  - dont le SVG n'est PAS deja dans svg/ (on peut relancer le script autant de fois qu'on veut : rien n'est refait).
Une idee dont les etapes 1 et 2 ne sont pas finies (speech, assets.json, deux passes a true) est ignoree, avec la raison affichee.

Produit :
  generation_svg/projet_svg_global.json                 toutes les idees, une seule liste de lignes (a coller dans GenSVG)
  ideaN/animation/etape2_assets/projet_svg.json         la meme chose pour une seule idee (ecrit seulement s'il y a des lignes)
"""
import json
import re
import subprocess
import sys
from pathlib import Path

DEPOT = "officecenter632-maker/WorkspaceAnim"
BRANCHE = "main"
EXTS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp"}      # formats d'image source acceptes par GenSVG
RACINE = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()


def lire(p):
    return json.loads(p.read_text(encoding="utf-8"))


def date_fichier(f):
    """Date du dernier commit du fichier (sinon date de modification) : sert a choisir le plus recent s'il y a deux extensions."""
    try:
        r = subprocess.run(["git", "log", "-1", "--format=%ct", "--", str(f.relative_to(RACINE))], cwd=str(RACINE),
                           capture_output=True, text=True, timeout=30)
        if r.returncode == 0 and r.stdout.strip().isdigit():
            return int(r.stdout.strip())
    except (OSError, subprocess.SubprocessError):
        pass
    return int(f.stat().st_mtime)


def raison_non_prete(a):
    """Pourquoi une idee n'a pas fini les etapes 1 et 2 (liste vide si elle les a finies)."""
    manque = []
    if not (a / "etape1_speech" / "speech_adapte.md").is_file():
        manque.append("etape 1 (speech_adapte.md)")
    if not (a / "etape2_assets" / "assets.json").is_file():
        manque.append("etape 2 (assets.json)")
    reg = a / "etape2_assets" / "registre_verification.json"
    if not reg.is_file():
        manque.append("registre_verification.json")
    else:
        r = lire(reg)
        for p in ("passe_1", "passe_2"):
            if not (r.get(p) or {}).get("faite"):
                manque.append(p + " a false")
    return manque


def main():
    idees = sorted((d for d in RACINE.iterdir() if d.is_dir() and re.fullmatch(r"idea\d+", d.name)),
                   key=lambda d: int(d.name[4:]))
    if not idees:
        sys.exit("Aucun dossier ideaN dans %s" % RACINE)

    globales, projets_idee, noms_vus, erreurs, rapport, ignorees = [], {}, set(), [], [], []
    for d in idees:
        n = int(d.name[4:])
        manque = raison_non_prete(d / "animation")
        if manque:
            ignorees.append("%s : %s" % (d.name, ", ".join(manque)))
            continue
        e2 = d / "animation" / "etape2_assets"
        dossier_svg = "%s/animation/etape2_assets/svg" % d.name
        generes = e2 / "generes"
        images = {}
        if generes.is_dir():
            for f in sorted(generes.iterdir()):
                if f.is_file():
                    images.setdefault(f.stem, []).append(f)
        deja = {f.stem for f in (e2 / "svg").glob("*.svg")} if (e2 / "svg").is_dir() else set()
        taches = lire(e2 / "assets.json")["taches"]
        lignes, nb_deja, nb_attente, doubles = [], 0, 0, []
        for t in taches:
            if t.get("desactive"):
                continue
            aid = t["id"]
            if not re.fullmatch(r"[A-Za-z0-9_][A-Za-z0-9_.-]*", aid):
                erreurs.append("%s/%s : id inutilisable comme nom de fichier SVG" % (d.name, aid))
                continue
            if aid in deja:
                nb_deja += 1
                continue
            fichiers = images.get(aid)
            if not fichiers:
                nb_attente += 1                       # l'image n'est pas encore generee : elle sera prise au prochain passage
                continue
            bons = [f for f in fichiers if f.suffix.lower() in EXTS]
            if not bons:
                erreurs.append("%s/%s : format de fichier non pris en charge : %s" % (d.name, aid, ", ".join(f.name for f in fichiers)))
                continue
            if len(bons) > 1:                          # ex. decor_champ.png ET decor_champ.webp : on prend le plus recemment commite
                bons.sort(key=date_fichier, reverse=True)
                doubles.append("%s/%s : %s (retenu : %s)" % (d.name, aid, ", ".join(f.name for f in bons), bons[0].name))
            nom = "idea%d__%s" % (n, aid)
            if nom in noms_vus:
                erreurs.append("nom en double : " + nom)
            noms_vus.add(nom)
            lignes.append({"id": aid, "nom": nom, "source": bons[0].relative_to(RACINE).as_posix(),
                           "sortie": "%s/%s.svg" % (dossier_svg, aid)})
        rapport.append("%s : %d SVG a generer (%d deja faits, %d image(s) pas encore generee(s), sur %d assets)"
                       % (d.name, len(lignes), nb_deja, nb_attente, sum(1 for t in taches if not t.get("desactive"))))
        rapport.extend("  ! deux fichiers pour un meme asset : " + x for x in doubles)
        for l in lignes:
            globales.append({"nom": l["nom"], "source": l["source"], "chemin_sauvegarde": l["sortie"]})
        if lignes:
            projets_idee[e2 / "projet_svg.json"] = {
                "projet": "Idée %d : SVG des assets" % n,
                "depot_references": DEPOT, "branche_references": BRANCHE,
                "branche_sortie": BRANCHE, "dossier_sortie": dossier_svg,
                "images": [{"nom": l["id"], "source": l["source"]} for l in lignes]}

    for i in ignorees:
        rapport.append("IGNOREE %s" % i)
    if erreurs:
        print("ERREURS (rien d'ecrit) :")
        for e in erreurs:
            print("  -", e)
        sys.exit(1)
    print("\n".join(rapport))
    if not globales:
        print("Rien a vectoriser pour l'instant : aucune image generee sans SVG.")
        return
    for chemin, projet in projets_idee.items():
        chemin.write_text(json.dumps(projet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    glob = {"projet": "Toutes les idées : SVG des assets", "depot_references": DEPOT, "branche_references": BRANCHE,
            "branche_sortie": BRANCHE, "images": globales}
    sortie = RACINE / "generation_svg"
    sortie.mkdir(exist_ok=True)
    (sortie / "projet_svg_global.json").write_text(json.dumps(glob, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("TOTAL : %d SVG a generer -> generation_svg/projet_svg_global.json" % len(globales))


if __name__ == "__main__":
    main()
