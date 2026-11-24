#!/usr/bin/env python3
"""Vectorise une image generee avec vtracer et ecrit un SVG au format attendu par detourer.py (viewBox, <g id="c">, une <path fill d> par forme,
decalages transform integres, forme 0 = fond uni). Alternative locale a GenSVG (procedure 2.13).
Usage : python3 outils/vectoriser.py ideaN <asset> [reglage]    (reglage : fin = defaut, moyen, grossier)"""
import re, sys, os, tempfile
import vtracer
from PIL import Image
idee, asset = sys.argv[1], sys.argv[2]
reg = sys.argv[3] if len(sys.argv) > 3 else "fin"
P = {"fin": dict(color_precision=6, layer_difference=20, filter_speckle=8),
     "moyen": dict(color_precision=5, layer_difference=24, filter_speckle=6),
     "grossier": dict(color_precision=4, layer_difference=40, filter_speckle=10)}[reg]
base = f"{idee}/animation/etape2_assets"
img = next(f"{base}/generes/{f}" for f in os.listdir(f"{base}/generes") if os.path.splitext(f)[0] == asset)
im = Image.open(img).convert("RGB"); W, H = im.size
tmp = tempfile.mktemp(suffix=".png"); im.save(tmp); out = tempfile.mktemp(suffix=".svg")
vtracer.convert_image_to_svg_py(tmp, out, colormode="color", hierarchical="stacked", mode="spline", corner_threshold=60,
                                length_threshold=4.0, splice_threshold=45, path_precision=2, **P)
s = open(out, encoding="utf-8").read(); os.remove(tmp); os.remove(out)
formes = []
for m in re.finditer(r'<path d="([^"]+)" fill="([^"]+)"(?: transform="translate\(([-\d.]+),([-\d.]+)\)")?/>', s):
    d, fill, tx, ty = m.group(1), m.group(2), float(m.group(3) or 0), float(m.group(4) or 0)
    nums = re.findall(r'[MCLZ]|-?\d+\.?\d*', d); res = []; i = 0
    while i < len(nums):
        if nums[i] in "MCLZ": res.append(nums[i]); i += 1; continue
        res.append(f"{float(nums[i]) + tx:.2f}".rstrip("0").rstrip(".") + " " + f"{float(nums[i+1]) + ty:.2f}".rstrip("0").rstrip(".")); i += 2
    formes.append(f'<path fill="{fill.lower()}" stroke="none" d="{" ".join(res)}"/>')
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">\n'
       '<defs><style>path{vector-effect:non-scaling-stroke}</style><clipPath id="img"><rect width="%d" height="%d"/></clipPath></defs>\n' % (W, H)
       + '<g id="c" clip-path="url(#img)" stroke-width="2" stroke-linejoin="bevel">\n' + "\n".join(formes) + "\n</g>\n</svg>\n")
open(f"{base}/svg/{asset}.svg", "w", encoding="utf-8").write(svg)
print(f"{asset} : {len(formes)} formes, {len(svg)//1024} Ko, reglage {reg}")
