#!/usr/bin/env python3
"""Repare l'epaule d'un personnage dont le torse a ete genere avec ses manches (procedure 2.4 point 6).
La forme du t-shirt est coupee en deux par clip-path : le corps reste au torse, le bout de manche passe au haut du bras
(copie decalee de -montage pour retomber a sa place apres le montage). Les pivots d'epaule sont replaces sur le bout de manche.
Usage : python3 outils/reparer_epaule.py ideaN <asset> <forme_tshirt> <x_bord_gauche> <x_bord_droit> [recouvrement]"""
import re, sys, json
idee, asset, num, L, R = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
rec = int(sys.argv[6]) if len(sys.argv) > 6 else 14
bas = int(sys.argv[7]) if len(sys.argv) > 7 else 332   # y du bas de la manche : le bras ne prend rien du corps en dessous
base = f"{idee}/animation"; d = f"{base}/etape3_animation/assets/{asset}"
src = open(f"{base}/etape2_assets/svg/{asset}.svg", encoding="utf-8").read()
paths = re.findall(r'<path\b[^>]*?/>', src); chemise = paths[num]
mon = json.load(open(f"{d}/montage.json")); pv = json.load(open(f"{base}/etape3_animation/pivots.json"))
H = int(re.search(r'viewBox="0 0 \d+ (\d+)"', src).group(1)); W = int(re.search(r'viewBox="0 0 (\d+)', src).group(1))
def clip(cid, x0, x1, y1=None): return f'<clipPath id="{cid}"><rect x="{x0}" y="0" width="{x1-x0}" height="{y1 or H}"/></clipPath>'
def ajoute(fichier, cid, x0, x1, y1=None):
    s = open(fichier, encoding="utf-8").read()
    s = re.sub(r'<clipPath id="(c_ep\w*)".*?</clipPath>', '', s, flags=re.S)
    s = s.replace('</defs>', clip(cid, x0, x1, y1) + '</defs>', 1)
    return s
# torse : corps seulement (entre les deux bords), la forme du t-shirt est remplacee par sa version coupee
f = f"{d}/pere_torse.svg"; s = ajoute(f, "c_ep_torse", L, R, None)
orig = chemise
s = s.replace(orig, orig.replace('<path', '<path clip-path="url(#c_ep_torse)"', 1)) if 'c_ep_torse)' not in s else s
open(f, "w", encoding="utf-8").write(s)
# bras : bout de manche, copie decalee de -montage, mise derriere (premier dans le groupe)
for cote, (x0, x1) in (("g", (0, L + rec)), ("d", (R - rec, W))):
    f = f"{d}/pere_bras_{cote}_haut.svg"; m = mon[f"pere_bras_{cote}_haut"]
    s = ajoute(f, f"c_ep_{cote}", x0, x1, bas)
    s = re.sub(r'<!--stub-->.*?<!--/stub-->\n', '', s, flags=re.S)
    stub = f'<!--stub--><g id="c_stub" transform="translate({-m["dx"]} {-m["dy"]})"><g clip-path="url(#c_ep_{cote})">{chemise}</g></g><!--/stub-->\n'
    s = re.sub(r'(<g id="pere_bras_%s_haut"[^>]*>\n)' % cote, lambda mo: mo.group(1) + stub, s, count=1)
    open(f, "w", encoding="utf-8").write(s)
print("epaule reparee : bord gauche", L, "bord droit", R, "recouvrement", rec)
