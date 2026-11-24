#!/usr/bin/env python3
"""python3 outils/diff_moteur.py ideaN   -> patch (diff unifie) entre le moteur commun et la copie de l'idee.
C'est ce que relisent l'utilisateur et l'autre IA pour decider quoi reporter dans moteur_commun/.
Avertit si la copie a change sans qu'AMELIORATIONS.md ait ete complete."""
import sys, os, difflib, json
idee = sys.argv[1]; src = "moteur_commun"; dst = f"{idee}/animation/etape3_animation/moteur"
base = json.load(open(f"{dst}/BASE.json"))
n = 0
for f in sorted(os.listdir(src)):
    if not f.endswith(".js"): continue
    a = open(f"{src}/{f}", encoding="utf-8").read().splitlines(True); b = open(f"{dst}/{f}", encoding="utf-8").read().splitlines(True)
    d = list(difflib.unified_diff(a, b, f"moteur_commun/{f}", f"{dst}/{f}"))
    if d: n += 1; sys.stdout.writelines(d)
txt = open(f"{dst}/AMELIORATIONS.md", encoding="utf-8").read()
vide = "(aucune pour l'instant)" in txt
print(f"\n# {idee} : {n} fichier(s) different(s) de moteur_commun (base {base['version']})", file=sys.stderr)
if n and vide: print("# ATTENTION : le moteur a ete modifie mais AMELIORATIONS.md n'a aucune entree.", file=sys.stderr)
