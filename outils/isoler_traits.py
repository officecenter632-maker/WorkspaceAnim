#!/usr/bin/env python3
"""Isole des traits du visage (yeux, bouche...) de la piece 'tete' en pieces separees (procedure 2.4 point 8), sans rien redessiner :
les formes sont celles de l'image generee ; seuls les trous que ces traits laissaient dans la peau ou la barbe sont refermes
pour que la peau reste continue dessous (un clignement ne laisse alors rien voir). Relancable sans risque.
Usage : python3 outils/isoler_traits.py ideaN <asset> "oeil_g=26;oeil_d=27;bouche=24" [piece_parente]      (numeros de formes du SVG d'etape 2)
piece_parente : par defaut la piece « *_tete » ; pour un personnage entier en un bloc (enfants), donner le nom du bloc (ex. garcon) : les pieces s'appellent alors garcon_oeil_g, etc.
Puis : python3 outils/detourer.py ideaN <asset>  et  python3 outils/generer_donnees.py ideaN"""
import re, sys, json
idee, asset, spec = sys.argv[1], sys.argv[2], sys.argv[3]
base = f"{idee}/animation"; fa = f"{base}/etape3_animation/assets/{asset}/attribution.json"; fs = f"{base}/etape2_assets/svg/{asset}.svg"
att = json.load(open(fa, encoding="utf-8")); svg = open(fs, encoding="utf-8").read(); paths = re.findall(r'<path\b[^>]*?/>', svg)
tete = sys.argv[4] if len(sys.argv) > 4 else next(p for p in att["ordre"] if p.endswith("tete"))
pre = tete[:-len("tete")] if tete.endswith("tete") else tete + "_"
def bb(d):
    """boite d'une courbe (commandes absolues) ; pour un arc A, seul le point d'arrivee compte (les 5 premiers nombres sont des parametres)"""
    t = re.findall(r'[A-Za-z]|-?\d*\.?\d+(?:e-?\d+)?', d); xs = []; ys = []; i = 0; c = "M"
    while i < len(t):
        if t[i].isalpha(): c = t[i].upper(); i += 1; continue
        if c == "A": xs.append(float(t[i + 5])); ys.append(float(t[i + 6])); i += 7
        else: xs.append(float(t[i])); ys.append(float(t[i + 1])); i += 2
    return (min(xs), min(ys), max(xs), max(ys))
def dd(p): return re.search(r' d="([^"]+)"', p).group(1)
traits = {k: [int(x) for x in v.split(",")] for k, v in (e.split("=") for e in spec.split(";"))}
tous = {i for l in traits.values() for i in l}
for nom, ids in traits.items():
    pid = pre + nom
    for l in att["pieces"].values():
        for i in ids:
            if i in l and l is not att["pieces"].get(pid): l.remove(i)
    att["pieces"][pid] = sorted(ids)
    if pid not in att["ordre"]: att["ordre"].insert(att["ordre"].index(tete) + 1, pid)
    b = [bb(dd(paths[i])) for i in ids]
    att["pivots"][pid] = [round((min(x[0] for x in b) + max(x[2] for x in b)) / 2), round((min(x[1] for x in b) + max(x[3] for x in b)) / 2)]   # centre du trait : pivot du clignement
    x0, y0, x1, y1 = min(x[0] for x in b), min(x[1] for x in b), max(x[2] for x in b), max(x[3] for x in b)
    for i in att["pieces"][tete]:
        d = dd(paths[i]); subs = [s for s in re.split(r'(?=M)', d.strip()) if s.strip()]
        garde = [s for k, s in enumerate(subs) if k == 0 or not (lambda h: h[0] <= x0 + 2 and h[1] <= y0 + 2 and h[2] >= x1 - 2 and h[3] >= y1 - 2)(bb(s))]
        if len(garde) != len(subs):
            nouveau = paths[i].replace(d, " ".join(s.strip() for s in garde)); svg = svg.replace(paths[i], nouveau); paths[i] = nouveau
            print(f"  trou referme sous {nom} : forme {i}")
att["notes"] = [n for n in att.get("notes", []) if not n.startswith("traits du visage")] + ["traits du visage isoles : " + spec]
json.dump(att, open(fa, "w", encoding="utf-8"), ensure_ascii=False, indent=1); open(fs, "w", encoding="utf-8").write(svg)
print(asset, ":", {p: len(l) for p, l in att["pieces"].items()})
