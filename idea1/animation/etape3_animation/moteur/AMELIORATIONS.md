# Ameliorations du moteur faites dans idea1

Base : moteur commun version 1.0 (empreintes dans `BASE.json`).
Ce fichier est relu a la fin par l'utilisateur et une autre IA pour decider quoi reporter dans `moteur_commun/`.
**Une entree par modification, ecrite au moment ou elle est faite.** Le patch exact : `python3 outils/diff_moteur.py idea1`.

## Modele d'entree

### AAAA-MM-JJ - titre court
- **Fichier / fonction** : `personnage.js`, `Anim.creerPersonnage`
- **Pourquoi** : le probleme rencontre dans cette idee (une phrase)
- **Ce qui change** : le comportement, en une ou deux phrases
- **Utilisation** : comment une scene l'appelle (exemple d'une ligne)
- **Compatible avec les autres idees** : oui / non (si non, ce qui casse)
- **Commit** : hash

## Entrees

### 2026-11-24 - Bras devant le torse, hochement vertical de la tete
- **Fichier / fonction** : `personnage.js`, `Anim.creerPersonnage` (`maj(t, extra)`)
- **Pourquoi** : se prendre la tete et croiser les bras demandent que les bras passent devant le torse et la tete ; un hochement ne se voit pas avec une simple rotation.
- **Ce qui change** : deux extras facultatifs. `devant` (vrai : les bras passent devant, l'ordre des couches ne change que quand l'etat change) et `tdy` (decalage vertical de la tete, en px de l'image). Sans ces extras, comportement inchange.
- **Utilisation** : `perso.maj(t, { devant: true, tdy: 12, tete: 4 })`
- **Compatible avec les autres idees** : oui
- **Commit** : voir le commit « Plan 2 »

### 2026-11-24 - Carte donut et etiquette avec fleche
- **Fichier / fonction** : `elements.js`, `Anim.creerDonut` et `Anim.creerEtiquette` (nouvelles fonctions)
- **Pourquoi** : le beat 2 de l'idee 1 a besoin d'un donut dont la part se dessine et d'une etiquette a fleche montante ; d'autres idees auront des cartes de pourcentage.
- **Ce qui change** : `creerDonut` (carte blanche entrant par la droite, anneau bleu, part rouge dessinee dans le sens horaire depuis le haut jusqu'a `vers` (0..1), texte au centre, titre lettre par lettre, sortie facultative) ; `creerEtiquette` (etiquette blanche, fleche rouge dessinee de la base a la pointe puis pulsation de 8 %, texte en capitales).
- **Utilisation** : `A.creerDonut(code, { x, y, w, h, entree:{t0,d}, part:{t0,d,vers:0.49}, centre:{t0,texte:['NEARLY','HALF']}, titre:{t0,d,texte:'...'} })` ; `A.creerEtiquette(code, { x, y, w, h, texte:'A RECORD', entree:{t0,d}, fleche:{t0,d} })`
- **Compatible avec les autres idees** : oui (ajouts seulement). Couleurs et textes de depart a rendre parametrables au report.
- **Commit** : voir le commit « Plan 2 »

