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
if "--entier" in sys.argv:
    # asset a une seule piece (decor ou objet) : on retire le fond uni s'il existe, sans decouper
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    m = re.search(r'viewBox="0 0 (\d+) (\d+)"', head); W, H = int(m.group(1)), int(m.group(2))
    nums = [float(x) for x in re.findall(r'-?\d+\.?\d*', re.search(r' d="([^"]+)"', paths[0]).group(1))]
    fond = (min(nums[0::2]) <= 0 and max(nums[0::2]) >= W and min(nums[1::2]) <= 0 and max(nums[1::2]) >= H and 'fill="none"' not in paths[0])
    if fond:  # retire aussi les morceaux de fond traces comme formes separees (meme couleur exacte que le fond)
        cf = re.search(r'fill="([^"]+)"', paths[0]).group(1)
        garde = [q for q in paths[1:] if re.search(r'fill="([^"]+)"', q).group(1) != cf]
    else:
        garde = paths
    decor = asset.startswith("decor_")
    out = f"{base}/etape3_animation/" + (f"decors/{asset}.svg" if decor else f"assets/{asset}/{asset}.svg")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(f'{head}\n{defs}\n<g id="{asset}"{g}>\n' + "\n".join(garde) + "\n</g>\n</svg>\n")
    racine = f"{base}/etape3_animation"; f = f"{racine}/index_assets.json"
    d = json.load(open(f, encoding="utf-8")) if os.path.exists(f) else {}
    d[asset] = {"etat": "fait", "fond_retire": fond, "pieces": {asset: out.replace(racine + "/", "")}}
    json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(asset, ":", "fond uni retire" if fond else "pas de fond uni", "->", out, f"({len(garde)} formes)")
    sys.exit(0)
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
