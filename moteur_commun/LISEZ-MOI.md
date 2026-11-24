# Moteur d'animation commun (version dans `VERSION`)

Le moteur est écrit **une seule fois**, ici. Aucune idée ne le réécrit : elle le **copie** dans son propre dossier et ne code que ses scènes.

## Contenu

| Fichier | Rôle |
|---|---|
| `moteur.js` | horloge unique, mise à l'échelle de la scène (1672 x 941), lecture / pause / curseur, flèches ← → (0,1 s), caméra `Anim.camera(t, zoom)` qui oscille toujours |
| `personnage.js` | `Anim.creerPersonnage` (personnage articulé : jambes, torse, bras, tête, visage en pièces), `Anim.creerBloc` (personnage d'un seul bloc, avec son visage), `Anim.clignement` (régulier) |
| `elements.js` | éléments en code : compteur, icônes |

Sans bibliothèque externe. Les scènes (`scenes/beatN.js`) appellent ces fonctions, elles ne contiennent aucun moteur.

## Règle d'usage (voir `procedure_animation.md`, section « Moteur commun »)

1. **Installer** : `python3 outils/installer_moteur.py ideaN` copie ce dossier dans `ideaN/animation/etape3_animation/moteur/`. C'est le seul endroit où une idée a le moteur.
2. **Ne jamais modifier `moteur_commun/`** depuis une idée. Toute amélioration ou correction se fait **sur la copie** de l'idée.
3. **Noter chaque modification** dans `ideaN/animation/etape3_animation/moteur/AMELIORATIONS.md` (à côté de la copie), au moment où elle est faite.
4. **À la fin**, l'utilisateur et une autre IA relisent les `AMELIORATIONS.md` de toutes les idées (`python3 outils/diff_moteur.py ideaN` donne le patch exact) et reportent ce qui est retenu dans `moteur_commun/`, en changeant `VERSION`.
