#!/usr/bin/env python3
"""python3 outils/embarquer.py ideaN <fichier_sortie.html> [--depart=SECONDES]
La lecture demarre au debut du dernier beat (celui sur lequel on travaille : plus grand « debut » des scenes), ou a --depart ; le curseur permet toujours de revenir a 0.
Fabrique UNE page HTML autonome (scripts et SVG embarqués en base64) pour que l'utilisateur regarde l'animation.
Réservée à l'aperçu : l'agent travaille toujours sur la version à chemins (index.html), ne lit jamais ce fichier
(trop long, il coûterait des jetons) et ne le commite pas. Seuls les assets cités par les scènes sont embarqués."""
import sys, os, re, glob, base64
idee, sortie = sys.argv[1], sys.argv[2]
args_dep = [a for a in sys.argv[3:] if a.startswith('--depart=')]
b = f"{idee}/animation/etape3_animation/"
def lire(p): return open(b + p, encoding="utf8").read()
scenes = sorted(glob.glob(b + "scenes/*.js"))
texte_scenes = "".join(open(s, encoding="utf8").read() for s in scenes)
js = "\n".join(lire(p) for p in ["donnees.js", "moteur/moteur.js", "moteur/personnage.js", "moteur/elements.js"])
js += "\n" + texte_scenes
depart = float(args_dep[0].split('=')[1]) if args_dep else max([float(x) for x in re.findall(r'debut:\s*([\d.]+)', texte_scenes)] or [0])
n = 0
for f in sorted(glob.glob(b + "assets/*/*.svg") + glob.glob(b + "decors/*.svg")):
    rel = os.path.relpath(f, b)
    asset = os.path.basename(os.path.dirname(f)) if rel.startswith("assets/") else os.path.splitext(os.path.basename(f))[0]
    if asset not in texte_scenes and os.path.basename(f)[:-4] not in texte_scenes:
        js = js.replace('"' + rel + '"', '""').replace("'" + rel + "'", "''"); continue
    uri = "data:image/svg+xml;base64," + base64.b64encode(open(f, "rb").read()).decode()
    js = js.replace('"' + rel + '"', '"' + uri + '"').replace("'" + rel + "'", "'" + uri + "'"); n += 1
titre = f"Animation {idee}"
page = f"""<title>{titre}</title>
<style>
  :root{{color-scheme:dark;--fond:#12151c;--texte:#e8ecf3;--barre:#1b1f29;--accent:#3a6df0}}
  html,body{{height:100%}}
  body{{margin:0;background:var(--fond);color:var(--texte);font-family:system-ui,Arial,sans-serif;overflow:hidden}}
  #fenetre{{position:absolute;left:0;top:0;right:0;bottom:48px;overflow:hidden}}
  #scene{{position:absolute;left:0;top:0;width:1672px;height:941px;transform-origin:0 0;overflow:hidden;background:#000}}
  #barre{{position:absolute;left:0;right:0;bottom:0;height:48px;display:flex;align-items:center;gap:14px;padding:0 16px;background:var(--barre)}}
  #bouton{{min-width:84px;padding:7px 12px;border:0;border-radius:8px;background:var(--accent);color:#fff;font-size:15px;cursor:pointer}}
  #curseur{{flex:1;min-width:0}}
  #temps{{font-variant-numeric:tabular-nums;font-size:14px;min-width:120px;text-align:right}}
</style>
<div id="fenetre"><div id="scene"></div></div>
<div id="barre"><button id="bouton">Pause</button><input id="curseur" type="range" min="0" value="0"><span id="temps"></span></div>
<script>
{js}
Anim.depart = {depart};
Anim.demarrer();
</script>
"""
open(sortie, "w", encoding="utf8").write(page)
print("OK", sortie, round(len(page) / 1e6, 2), "Mo,", n, "SVG embarqués")
