#!/usr/bin/env python3
"""Installe le moteur commun dans une idee : python3 outils/installer_moteur.py ideaN [--force]
Copie moteur_commun/*.js dans ideaN/animation/etape3_animation/moteur/ (le SEUL endroit ou une idee a le moteur), ecrit moteur/BASE.json
(version et empreinte de chaque fichier tel que copie) et cree moteur/AMELIORATIONS.md s'il n'existe pas.
Refuse d'ecraser une copie deja modifiee (sauf --force : les ameliorations non reportees seraient perdues)."""
import sys, os, json, hashlib, shutil
idee = sys.argv[1]; force = "--force" in sys.argv
src = "moteur_commun"; dst = f"{idee}/animation/etape3_animation/moteur"
h = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()[:16]
fichiers = sorted(f for f in os.listdir(src) if f.endswith(".js"))
version = open(f"{src}/VERSION", encoding="utf-8").read().strip()
os.makedirs(dst, exist_ok=True)
base_p = f"{dst}/BASE.json"
base = json.load(open(base_p)) if os.path.exists(base_p) else None
modifies = [f for f in fichiers if os.path.exists(f"{dst}/{f}") and h(f"{dst}/{f}") != h(f"{src}/{f}")]
if modifies and not force:
    sys.exit("Refus : la copie differe du moteur commun pour " + ", ".join(modifies) + ".\n"
             "Si ce sont des ameliorations, elles sont a garder (les noter dans AMELIORATIONS.md). Pour ecraser quand meme : --force.")
for f in fichiers: shutil.copyfile(f"{src}/{f}", f"{dst}/{f}")
json.dump({"version": version, "fichiers": {f: h(f"{src}/{f}") for f in fichiers}}, open(base_p, "w", encoding="utf-8"), indent=1)
am = f"{dst}/AMELIORATIONS.md"
if not os.path.exists(am):
    open(am, "w", encoding="utf-8").write(f"""# Ameliorations du moteur faites dans {idee}

Base : moteur commun version {version} (empreintes dans `BASE.json`).
Ce fichier est relu a la fin par l'utilisateur et une autre IA pour decider quoi reporter dans `moteur_commun/`.
**Une entree par modification, ecrite au moment ou elle est faite.** Le patch exact : `python3 outils/diff_moteur.py {idee}`.

## Modele d'entree

### AAAA-MM-JJ - titre court
- **Fichier / fonction** : `personnage.js`, `Anim.creerPersonnage`
- **Pourquoi** : le probleme rencontre dans cette idee (une phrase)
- **Ce qui change** : le comportement, en une ou deux phrases
- **Utilisation** : comment une scene l'appelle (exemple d'une ligne)
- **Compatible avec les autres idees** : oui / non (si non, ce qui casse)
- **Commit** : hash

## Entrees

(aucune pour l'instant)
""")
print(f"moteur {version} installe dans {dst} ({len(fichiers)} fichiers)" + (" ; copie modifiee conservee" if modifies else ""))
