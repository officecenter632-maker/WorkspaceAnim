#!/usr/bin/env python3
"""python3 outils/construire_bras_pere.py
Reconstruit les 4 pièces de bras du père (idée 1) en vectoriel propre, à la place des pièces détourées de l'image
générée (manches en double, vide au coude). Choix : le bras est dessiné pendant, presque droit, collé au torse ; la manche
est celle du torse (le bras passe derrière) ; le coude est un cercle commun au haut du bras et à l'avant-bras, donc
aucun vide ni marche quelle que soit la rotation. Écrit les 4 SVG, met à jour pivots.json et montage.json."""
import json, math, os
D = 'idea1/animation/etape3_animation'
P = D + '/assets/pere_locataire/'
PEAU, OMBRE = '#ef9b7a', '#e48c6c'
R = 22                      # rayon du coude (demi-largeur du bras)
LH, LB = 128, 130           # longueur haut du bras, avant-bras (jusqu'au poignet)
ANG = 3                     # inclinaison de repos (degrés), vers l'extérieur
SX, SY = 752, 312           # épaule gauche (cachée sous la manche du torse) ; la droite est le miroir autour de x=840
CX = 840

haut = (f'<path fill="{PEAU}" d="M{-R-1} 0A{R+1} {R+1} 0 0 1 {R+1} 0L{R} {LH}A{R} {R} 0 0 1 {-R} {LH}Z"/>')
# avant-bras : calotte du coude (même cercle que le haut), puis poignet plus fin, puis main (pouce côté corps = +x)
bas = (f'<path fill="{PEAU}" d="M{-R} 0A{R} {R} 0 0 1 {R} 0L17 {LB}L-17 {LB}Z"/>'
       f'<path fill="{PEAU}" d="M-17 {LB-2}C-21 {LB+12} -23 {LB+30} -20 {LB+42}C-18 {LB+54} -9 {LB+60} 0 {LB+59}'
       f'C9 {LB+59} 17 {LB+56} 19 {LB+46}L19 {LB+28}L17 {LB-2}Z"/>'
       f'<ellipse cx="24" cy="{LB+24}" rx="7" ry="19" transform="rotate(-10 24 {LB+24})" fill="{PEAU}"/>'
       f'<path fill="none" stroke="{OMBRE}" stroke-width="1.6" stroke-linecap="round" d="M-7 {LB+46}L-7 {LB+57}M5 {LB+46}L5 {LB+58}"/>')

def svg(pid, tr, corps):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1672 941" width="1672" height="941">\n'
            f'<g id="{pid}"><g transform="{tr}">{corps}</g></g>\n</svg>\n')

def pos(cote, nom):
    """transformation d'un segment : épaule (nom=haut) ou coude (nom=bas), pour le côté g ou d."""
    s = 1 if cote == 'g' else -1
    a = s * ANG
    ex = SX - LH * math.sin(math.radians(ANG)); ey = SY + LH * math.cos(math.radians(ANG))
    x, y = (SX, SY) if nom == 'haut' else (ex, ey)
    if s == -1: x = 2 * CX - x
    return x, y, a

piv = json.load(open(D + '/pivots.json')); mon = json.load(open(P + 'montage.json'))
for cote in 'gd':
    for nom, corps in (('haut', haut), ('bas', bas)):
        x, y, a = pos(cote, nom); pid = f'pere_bras_{cote}_{nom}'
        tr = f'translate({x:.1f} {y:.1f}) rotate({a})'
        if cote == 'd':   # côté droit : l'image est celle du bras gauche, retournée (le pouce reste côté corps)
            tr = f'translate({x:.1f} {y:.1f}) rotate({a}) scale(-1 1)'
        open(P + pid + '.svg', 'w').write(svg(pid, tr, corps))
        piv[pid] = {'x': round(x, 1), 'y': round(y, 1)}; mon[pid] = {'dx': 0, 'dy': 0}
mon['_note'] = ("Père : tête, torse et jambes viennent de l'image générée (montage ci-dessous). Les 4 pièces de bras sont reconstruites "
                "par outils/construire_bras_pere.py (bras pendants, manche = celle du torse, coude en cercle commun), sans décalage.")
json.dump(piv, open(D + '/pivots.json', 'w'), indent=1); json.dump(mon, open(P + 'montage.json', 'w'), indent=2, ensure_ascii=False)
print('OK', {k: piv[k] for k in piv if k.startswith('pere_bras')})
