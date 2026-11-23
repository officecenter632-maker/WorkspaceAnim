#!/usr/bin/env python3
"""python3 outils/controler_raccords.py ideaN
Pour chaque personnage articulé de la scène, rend la page sur fond magenta à plusieurs instants (les balancements
ouvrent les trous) et vérifie que toutes les pièces forment UN SEUL bloc (aucune pièce décollée, aucun vide aux
articulations). Écrit aussi des captures dans le dossier donné en 2e argument."""
import sys, os
import numpy as np
from scipy import ndimage
from PIL import Image
from playwright.sync_api import sync_playwright
idee = sys.argv[1]; sortie = sys.argv[2] if len(sys.argv) > 2 else '/tmp'
url = 'file://' + os.path.abspath(f'{idee}/animation/etape3_animation/index.html')
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1672, 'height': 989})
    pg.goto(url); pg.wait_for_timeout(600)
    pg.evaluate("Anim.pause(); document.querySelector('#scene').style.background='#f0f'; Anim.monde.firstChild.style.display='none'; Anim.code.style.display='none'")
    for t in [0.0, 1.3, 2.7, 4.1, 5.2]:
        pg.evaluate(f'Anim.aller({t})'); pg.wait_for_timeout(150)
        pg.screenshot(path=f'{sortie}/raccord_{t}.png', clip={'x': 0, 'y': 0, 'width': 1672, 'height': 941})
        a = np.array(Image.open(f'{sortie}/raccord_{t}.png').convert('RGB')).astype(int)
        masque = ~((abs(a[:, :, 0] - 255) < 12) & (a[:, :, 1] < 14) & (abs(a[:, :, 2] - 255) < 12))
        lab, n = ndimage.label(masque)
        tailles = sorted(ndimage.sum(masque, lab, range(1, n + 1)), reverse=True)
        print(f't={t}', 'blocs (px):', [int(x) for x in tailles[:6]])
