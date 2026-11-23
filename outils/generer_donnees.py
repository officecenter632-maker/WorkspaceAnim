#!/usr/bin/env python3
"""python3 outils/generer_donnees.py ideaN
Regroupe index_assets.json, pivots.json et les montage.json de chaque asset dans
ideaN/animation/etape3_animation/donnees.js (la page HTML ne peut pas lire de JSON sans serveur)."""
import json, sys, glob, os
idee = sys.argv[1]
base = f"{idee}/animation/etape3_animation/"
d = {"index": json.load(open(base + "index_assets.json")),
     "pivots": json.load(open(base + "pivots.json")),
     "montage": {}}
for f in glob.glob(base + "assets/*/montage.json"):
    d["montage"][os.path.basename(os.path.dirname(f))] = {k: v for k, v in json.load(open(f)).items() if not k.startswith("_")}
open(base + "donnees.js", "w", encoding="utf8").write("window.DONNEES = " + json.dumps(d, ensure_ascii=False) + ";\n")
print("OK", base + "donnees.js", len(d["index"]), "assets,", len(d["montage"]), "montages")
