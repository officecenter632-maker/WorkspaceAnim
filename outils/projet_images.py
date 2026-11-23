#!/usr/bin/env python3
"""Construit le(s) projet(s) IngXAi « imgen » des images qui restent a generer (procedure_animation.md, 2.12).

Usage, depuis la racine du depot :  python3 outils/projet_images.py

Refuse de produire quoi que ce soit tant qu'une idee n'a pas fini les etapes 1 et 2 (speech, assets, deux passes a true).
Produit :
  generation_images/projet_images_global.json              toutes les idees, une seule liste de taches
  ideaN/animation/etape2_assets/projet_images.json         une idee seule (chaque idee, meme sans image restante : taches = [])
Ne liste que les images ABSENTES de ideaN/animation/etape2_assets/generes/ (une image est presente si un fichier du dossier a
pour nom l'id de l'asset, quelle que soit son extension).
"""
import json, re, sys
from pathlib import Path

DEPOT = "officecenter632-maker/WorkspaceAnim"
BRANCHE = "main"
RACINE = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()


def lire(p):
    return json.loads(p.read_text(encoding="utf-8"))


def main():
    idees = sorted((d for d in RACINE.iterdir() if d.is_dir() and re.fullmatch(r"idea\d+", d.name)),
                   key=lambda d: int(d.name[4:]))
    if not idees:
        sys.exit("Aucun dossier ideaN dans %s" % RACINE)

    # 1) toutes les idees doivent avoir fini les etapes 1 et 2
    bloquees = []
    for d in idees:
        a = d / "animation"
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
        if manque:
            bloquees.append("%s : %s" % (d.name, ", ".join(manque)))
    if bloquees:
        print("Projet global NON produit : les idees suivantes n'ont pas fini les etapes 1 et 2 :")
        for b in bloquees:
            print("  -", b)
        sys.exit(1)

    # 2) images restantes, idee par idee
    globales, ids_vus, erreurs, rapport = [], set(), [], []
    for d in idees:
        n = int(d.name[4:])
        e2 = d / "animation" / "etape2_assets"
        dossier = lire(e2 / "assets.json").get("dossier") or "%s/animation/etape2_assets/generes" % d.name
        presentes = {f.stem for f in (e2 / "generes").glob("*") if f.is_file()} if (e2 / "generes").is_dir() else set()
        restantes = []
        for t in lire(e2 / "assets.json")["taches"]:
            if t.get("desactive") or t["id"] in presentes:
                continue
            for ref in t.get("references") or []:
                if not (RACINE / ref).is_file():
                    erreurs.append("%s/%s : reference introuvable : %s" % (d.name, t["id"], ref))
            restantes.append(t)
        # projet de cette idee seule (champs deja reconnus par IngXAi)
        projet_idee = {
            "type": "imgen", "projet": "Idée %d : images des assets" % n,
            "depot_references": DEPOT, "branche_references": BRANCHE,
            "depot": DEPOT, "dossier_depot": dossier,
            "message_commit": "Idée %d : image générée {nom}" % n, "nommage": "{tache}{ext}",
            "taches": [dict(t, validation="manuelle", mode_prompt="fichier", consigne_prompt="") for t in restantes],
        }
        (e2 / "projet_images.json").write_text(json.dumps(projet_idee, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        # taches du projet global : id prefixe, dossier / nommage / commit propres a chaque tache
        for t in restantes:
            gid = "idea%d__%s" % (n, t["id"])
            if gid in ids_vus:
                erreurs.append("id en double : " + gid)
            ids_vus.add(gid)
            globales.append(dict(
                t, id=gid, depend_de=["idea%d__%s" % (n, x) for x in (t.get("depend_de") or [])],
                dossier_depot=dossier, nommage=t["id"] + "{ext}",
                message_commit="Idée %d : image générée {nom}" % n,
                validation="manuelle", mode_prompt="fichier", consigne_prompt=""))
        rapport.append("%s : %d image(s) a generer sur %d" % (d.name, len(restantes), len(lire(e2 / "assets.json")["taches"])))

    if erreurs:
        print("ERREURS (rien de global ecrit) :")
        for e in erreurs:
            print("  -", e)
        sys.exit(1)

    glob = {"type": "imgen", "projet": "Toutes les idées : images des assets restantes",
            "depot_references": DEPOT, "branche_references": BRANCHE, "depot": DEPOT,
            "taches": globales}
    sortie = RACINE / "generation_images"
    sortie.mkdir(exist_ok=True)
    (sortie / "projet_images_global.json").write_text(json.dumps(glob, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("\n".join(rapport))
    print("TOTAL : %d image(s) -> generation_images/projet_images_global.json" % len(globales))


if __name__ == "__main__":
    main()
