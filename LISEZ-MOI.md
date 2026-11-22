# Recherche « recherche-20261122-184148 »

Généré par Lexiax le 2026-11-22 18:05:50. 6 idée(s) cherchée(s), 10 candidats par idée, parmi 80 vidéo(s) et 5419 idées indexées.

## Organisation

```
(racine du dépôt)
  recherche.json          paramètres de la recherche (modèle, date, vidéos indexées, avertissements)
  LISEZ-MOI.md            ce fichier
  idea1/ ... idea6/    un dossier par idée du JSON d'origine, dans l'ordre
    scenario_candidats/
      idea.json           l'idée d'origine : {"id": ..., "texte": "..."}
      resultats.json      les candidats classés (rang, score, vidéo, titre, temps), sans le détail
      candidat01/ ... candidat10/    du plus proche (01) au moins proche
        segment.json      TOUT sur le candidat : score, vidéo, temps, titre, résumé, mots-clés, texte exact du speech
        frames.axz        les frames de ce passage (archive zip sans compression : l'ouvrir comme un .zip)
```

## Les frames

- `frames.axz` est un zip de fichiers WebP, résolution d'origine de la vidéo.
- Chaque fichier s'appelle `tNNNNNNNNN.webp` : NNNNNNNNN est l'instant en MILLISECONDES depuis le début de la vidéo (ex. `t000012500.webp` = 12,5 s).
- `segment.json > debut` et `fin` sont en secondes depuis le début de la vidéo : les frames de l'archive vont de `debut` à `fin`.
- `segment.json > frames` donne le nombre de frames et le pas (en secondes) entre deux frames.

## Score

`score` est la similarité cosinus (de 0 à 1) entre l'idée et le candidat : plus il est proche de 1, plus l'idée est proche.
