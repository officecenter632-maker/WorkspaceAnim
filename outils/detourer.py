#!/usr/bin/env python3
"""Detourage d'un asset (etape 3.1) : un SVG par piece, a partir de attribution.json.
Usage : python3 outils/detourer.py ideaN <asset> [--verifier]
attribution.json : {"ordre": [pieces de l'arriere vers l'avant], "pieces": {id: [numeros de formes]}, "pivots": {id: [x, y]}}
Les formes sont numerotees dans l'ordre du SVG d'etape 2 ; la forme 0 (fond uni) est retiree."""
import re, sys, json, os, subprocess, tempfile
idee, asset = sys.argv[1], sys.argv[2]
base = f"{idee}/animation"
src = f"{base}/etape2_assets/svg/{asset}.svg"
dst = f"{base}/etape3_animation/assets/{asset}"
s = open(src, encoding="utf-8").read()
head = re.match(r'<svg[^>]*>', s).group(0)
defs = re.search(r'<defs>.*?</defs>', s, re.S).group(0)
defs = re.sub(r'<clipPath.*?</clipPath>', '', defs, flags=re.S)
g = re.search(r'<g id="c"([^>]*)>', s).group(1)
g = re.sub(r'\s*clip-path="[^"]*"', '', g)
paths = re.findall(r'<path\b[^>]*?/>', s)
att = json.load(open(f"{dst}/attribution.json", encoding="utf-8"))
vus = [i for l in att["pieces"].values() for i in l]
assert len(vus) == len(set(vus)), "forme dans deux pieces : " + str(sorted({i for i in vus if vus.count(i) > 1}))
manque = sorted(set(range(1, len(paths))) - set(vus))
assert not manque, f"formes sans piece : {manque}"
assert 0 not in vus, "la forme 0 est le fond"
assert set(att["ordre"]) == set(att["pieces"]), "ordre incomplet"
def svg(ids, pid):
    return f'{head}\n{defs}\n<g id="{pid}"{g}>\n' + "\n".join(paths[i] for i in sorted(ids)) + "\n</g>\n</svg>\n"
for pid, ids in att["pieces"].items():
    open(f"{dst}/{pid}.svg", "w", encoding="utf-8").write(svg(ids, pid))
print(len(att["pieces"]), "pieces ecrites dans", dst)
# pivots.json et index_assets.json (au niveau de etape3_animation, mis a jour asset par asset)
racine = f"{base}/etape3_animation"
def maj(nom, fn):
    f = f"{racine}/{nom}"
    d = json.load(open(f, encoding="utf-8")) if os.path.exists(f) else {}
    fn(d); json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
maj("pivots.json", lambda d: d.__setitem__(asset, {p: {"x": x, "y": y} for p, (x, y) in att["pivots"].items()}))
maj("index_assets.json", lambda d: d.__setitem__(asset, {"etat": "fait", "ordre": att["ordre"], "pieces": {p: f"assets/{asset}/{p}.svg" for p in att["ordre"]}}))
if "--verifier" in sys.argv:
    from PIL import Image; import numpy as np
    def rendre(texte, nom):
        f = tempfile.mktemp(suffix=".svg"); open(f, "w", encoding="utf-8").write(texte)
        subprocess.run(["rsvg-convert", f, "-o", nom], check=True); return Image.open(nom).convert("RGBA")
    sans_fond = head + "\n" + defs + f'\n<g id="c"{g}>\n' + "\n".join(paths[1:]) + "\n</g></svg>"
    sc = os.environ.get("SCRATCH", "/tmp")
    ref = rendre(sans_fond, f"{sc}/{asset}_ref.png")
    empile = head + "\n" + defs + "\n" + "\n".join(re.search(r'<g.*</g>', svg(att["pieces"][p], p), re.S).group(0) for p in att["ordre"]) + "\n</svg>"
    emp = rendre(empile, f"{sc}/{asset}_empile.png")
    d = np.abs(np.asarray(ref, int) - np.asarray(emp, int)).max(axis=2)
    print("pixels differents (ecart > 8) :", int((d > 8).sum()), "sur", d.size)
    palette = ["#e6194b","#3cb44b","#4363d8","#f58231","#911eb4","#46f0f0","#f032e6","#bcf60c","#008080","#9a6324"]
    col = head + "\n" + defs
    for k, p in enumerate(att["ordre"]):
        col += f'\n<g fill="{palette[k%10]}" stroke="{palette[k%10]}" stroke-width="3">' + "\n".join(re.sub(r'fill="[^"]*"|stroke="[^"]*"', '', paths[i]).replace('<path', '<path fill="none"' if 'fill="none"' in paths[i] else '<path') for i in att["pieces"][p]) + "</g>"
    rendre(col + "\n</svg>", f"{sc}/{asset}_couleurs.png")
    print("rendus :", f"{sc}/{asset}_ref.png, _empile.png, _couleurs.png")
