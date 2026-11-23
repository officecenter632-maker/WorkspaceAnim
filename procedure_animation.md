# Procédure de réalisation de l'animation

Une idée du JSON devient une animation en plusieurs étapes. Chaque étape produit un fichier qui sert d'entrée à la suivante. On avance idée par idée, en commençant par l'idée 1.

## Données de départ

Dépôt `officecenter632-maker/workspaceanim`, branche **`main`**. Pour chaque idée :

```
ideaN/scenario_candidats/
  idea.json            l'idée d'origine : {"numero", "id", "texte"} + éventuellement "duree_speech_secondes" (durée maximale du speech de l'étape 1, en secondes)
  resultats.json       les 10 candidats classés (rang, score, vidéo, titre, debut, fin)
  candidat01 ... 10/
    segment.json       score, vidéo, debut/fin (secondes), titre, résumé, mots-clés, texte exact du speech, nombre et pas des frames
    frames.axz         frames du passage (zip de WebP, tNNNNNNNNN.webp = instant en millisecondes)
```

## Principe directeur (valable pour toutes les étapes)

1. **L'idée d'origine fait foi.** Le speech parle de CETTE idée : mêmes affirmations, même angle, même conclusion. On ne dévie pas, même légèrement, vers le sujet d'un candidat.
2. **Les scénarios candidats sont un guide, pas une source.** Ils servent à ne pas écrire le scénario de zéro : ils donnent un squelette (structure, rythme, style) et indiquent quelles images existent déjà.
3. **En cas de conflit, l'idée gagne.** Si un candidat aborde un point que l'idée ne contient pas, on n'en tient pas compte. Si l'idée contient un point que le candidat ne couvre pas, on l'écrit quand même.
4. **On ne recopie pas** les phrases des candidats.
5. **On peut enrichir l'idée par des recherches.** Un speech complet dit forcément des choses que l'idée ne contient pas directement (explications, exemples, chiffres). On les cherche, on les vérifie et on les cite, mais elles servent toujours l'idée : elles la précisent ou l'illustrent, elles ne la remplacent pas.
6. **L'agent décide seul.** Il choisit les candidats et écrit le speech dans le même mouvement, sans s'arrêter pour demander. Ses choix importants sont notés dans « Décisions prises ».

---

## Étape 1 : planifier le scénario, puis écrire le speech de l'idée

**But :** à partir d'un ou de plusieurs candidats, construire le plan du scénario de l'idée, puis écrire un speech fidèle à l'idée, dont la **durée est fixée (30 s maximum par défaut)** et dont la structure et le style s'inspirent des candidats, pour que leurs frames puissent illustrer le texte. Le speech n'est jamais écrit au hasard.

Deux temps : **A. planifier** (1.1 à 1.4), **B. écrire** (1.5 à 1.10).

### A. Planifier le scénario

#### 1.1 Décomposer l'idée

Lire `idea.json` et la découper en **points** numérotés (chaque affirmation ou étape du raisonnement). Cette liste sert de référence pour tout le reste : le speech final doit tous les contenir, dans un ordre logique, et rien qui ne serve pas l'idée.

#### 1.2 Choisir les candidats

1. Ouvrir `resultats.json` de l'idée.
2. Pour chaque candidat envisagé, lire le résumé, les mots-clés et le `texte` de `segment.json` : le candidat doit parler de la même chose que l'idée, pas seulement avoir un bon score.
3. Comparer ensuite le score, la durée (`fin - debut`) et la présence de frames (`frames: true`).
4. Écarter tout candidat qui ferait dériver le speech hors de l'idée, même s'il est bien classé.
5. Retenir **1 à N candidats guides** (ils inspirent le plan : structure, ordre, style) et désigner parmi eux **un candidat de référence** (il fournit le débit pour calculer le nombre de mots, voir 1.3).
6. Noter pour chaque candidat retenu : son dossier (`candidatNN`), son score, les points de l'idée qu'il illustre, son rôle (guide ou référence) et la raison du choix.

Le candidat de référence doit avoir une durée proche de la durée cible (voir 1.3) et ne pas faire dériver le sujet.

#### 1.3 Fixer la durée et le nombre de mots

1. **Durée cible** : lire le champ **`duree_speech_secondes` de `idea.json`**, exprimé **en secondes** (exemple : `"duree_speech_secondes": 45`). C'est la durée maximale du speech de l'étape 1. **Si le champ est absent, la durée par défaut est de 30 secondes maximum.**
2. **Candidat de référence** : on choisit, parmi les candidats retenus, celui dont la durée (`fin - debut`) est la plus proche de la durée cible, tout en parlant du même sujet que l'idée. Il fournit le débit.
3. **Débit** : nombre de mots du `texte` du candidat de référence ÷ sa durée, en mots par seconde.
4. **Mots maximum** : durée cible × débit. Le speech ne dépasse jamais ce plafond, et reste de préférence entre 90 % et 100 % de celui-ci.
5. **Durée du speech** : mots obtenus ÷ débit. Elle doit être inférieure ou égale à la durée cible.
6. **Frames** : relever leur nombre et leur pas en secondes pour savoir quand l'image change.

La durée remplace l'ancienne règle « 100 % à 130 % des mots du candidat ». Les autres candidats guides n'influencent pas le nombre de mots.

#### 1.4 Construire le plan du scénario

1. Pour chaque candidat guide, repérer la structure de son texte (accroche, développement, chute) et ses instants approximatifs.
2. Répartir les points de l'idée (1.1) dans cette structure : quel point à quel moment, dans quel ordre. L'ordre logique de l'idée prime sur l'ordre des candidats.
3. Répartir le budget de mots (plafond de 1.3) entre les parties du plan, au prorata de leur importance dans l'idée.
4. Repérer les points trop minces : ce sont eux qui demandent des recherches (1.5).

Résultat : un plan court (parties, points couverts, mots alloués, candidat qui inspire chaque partie).

### B. Écrire le speech

#### 1.5 Recherche complémentaire (quand l'idée ne suffit pas)

À faire seulement si un point de l'idée est trop mince pour être traité dans la durée visée, ou manque d'explications, d'exemples ou de chiffres. Ce n'est pas systématique.

1. **Cibler par point** : pour chaque point faible (1.4), noter ce qui manque, puis faire quelques recherches ciblées sur le web (2 à 3 par point), pas une recherche encyclopédique.
2. **Sources fiables** : publications scientifiques ou institutionnelles, sites officiels, presse sérieuse. Noter pour chaque information le titre, le site et la date.
3. **Recouper** : toute donnée clé (chiffre, date, nom, fait précis) doit être confirmée par au moins deux sources.
4. **Respecter le degré de certitude** : une hypothèse ou un sujet débattu est présenté comme tel (« des physiciens suggèrent… »), pas comme un fait établi.
5. **Servir les images** : à valeur égale, préférer les informations que les frames des candidats peuvent illustrer.
6. **Reformuler** : aucune phrase recopiée d'une source. Pas de citation, sauf une courte phrase si le mot exact est indispensable.
7. **Garder le plus fort** : la durée est limitée (1.3). On retient les chiffres et les faits les plus marquants, on écarte le reste.
8. **Trancher soi-même** : si les recherches contredisent l'idée ou la nuancent, l'agent ne s'arrête pas pour demander. Il garde l'angle de l'idée, écrit ce qui est exact, et n'affirme jamais quelque chose de faux. Il note sa décision en une ligne dans « Décisions prises ».

Résultat : une courte liste de faits retenus, chacun rattaché à un point de l'idée et accompagné de sa source.

#### 1.6 Relever le style des candidats

Lire le `texte` exact des candidats guides et relever leurs procédés : type d'ouverture, longueur des phrases, contractions, usage de chiffres, métaphores, chute. On reprend les procédés, jamais les phrases.

#### 1.7 Écrire le speech

1. Suivre le plan (1.4), partie par partie.
2. Respecter le plafond de mots (1.3), la structure prévue et le style relevé (1.6).
3. S'appuyer sur les faits retenus en 1.5 pour développer les points minces.
4. Soigner les transitions pour que le texte se lise d'un seul tenant.
5. La langue est celle de `idea.json`.

#### 1.8 Découper en beats

Découper le speech en beats (une idée courte par beat). Chaque beat reçoit une fenêtre de temps calculée avec le débit du candidat de référence, indique le point de l'idée qu'il couvre et le candidat dont les frames l'illustrent le mieux.

#### 1.9 Produire les fichiers de sortie

Le travail de l'étape 1 est rangé dans un dossier à part, à côté de `scenario_candidats/` qu'on ne modifie jamais :

```
ideaN/
  scenario_candidats/        (inchangé)
  animation/
    etape1_speech/
      speech_adapte.md       speech, beats, décisions
      plan_scenario.md       plans choisis (référence + guides), candidats rejetés, plan du speech
      recherches.md          faits retenus et sources
```

`plan_scenario.md` mentionne obligatoirement les plans (candidats) choisis avec leur rôle (référence ou guide), les candidats non retenus avec la raison, la structure du candidat de référence et la répartition des mots par partie. Les étapes suivantes iront dans `animation/etape2_…`, etc.

`speech_adapte.md` a ce contenu :

```
# Idée N : speech adapté

Idée d'origine : « … »
Durée cible : XX s (champ `duree_speech_secondes` de idea.json ; 30 s max si absent) | Candidat de référence : candidatNN (score 0.xxx, vidéo « … », debut–fin, débit X.XX mots/s)
Mots maximum : NNN | Mots obtenus : NNN | Durée du speech : XX s

## Points de l'idée
1. …
2. …

## Plan du scénario
| Partie | Points couverts | Mots alloués | Mots écrits | Candidat qui inspire |
|--------|-----------------|--------------|-------------|----------------------|
| P1     | 1               | …            | …           | 01                   |

## Beats
| # | Début (s) | Fin (s) | Candidat (frames) | Point de l'idée | Texte |
|---|-----------|---------|-------------------|-----------------|-------|
| 1 | 0.0       | 6.5     | 01                | 1               | …     |

## Décisions prises
(une ligne par choix important : candidat écarté, point nuancé ou adapté après recherche…)

## Informations ajoutées et sources
| Point de l'idée | Information ajoutée | Source (titre, site, date) |
|-----------------|---------------------|----------------------------|
| 2               | …                   | …                          |

## Speech complet
(le texte d'un seul bloc, prêt à être lu)
```

#### 1.10 Vérifications avant de passer à l'étape 2

- [ ] Tous les points de l'idée sont présents et le sens n'a pas changé.
- [ ] Le plan du scénario existe et le speech le suit.
- [ ] Le nombre de mots est sous le plafond (durée cible × débit) et la durée du speech ne dépasse pas la durée cible (30 s par défaut).
- [ ] Chaque information ajoutée vient de la recherche (1.5), sert un point de l'idée et figure dans « Informations ajoutées et sources ».
- [ ] Aucune information ajoutée ne change l'angle de l'idée, le degré de certitude des sources est respecté, et rien de faux n'est affirmé.
- [ ] Les candidats retenus parlent bien du même sujet que l'idée.
- [ ] Les beats se suivent sans trou ni chevauchement, et le dernier se termine à la durée du speech.
- [ ] Aucune phrase n'est recopiée à l'identique du speech d'un candidat.

---

## Étape 2 : lister les assets et écrire leurs prompts

**But :** à partir du speech et des frames des candidats, obtenir la liste des images à générer (les assets), chacune avec son image de référence, son fond et son **prompt complet**. Aucune validation humaine : l'agent fait tout et livre les fichiers.

**Principes**
- **Les assets sont des images fixes.** Il n'y a ni GIF ni vidéo. Le mouvement (déplacements, apparitions, zooms, animations) est fait en code à l'étape suivante.
- **Rien d'inventé.** Un asset existe seulement si un beat du speech (étape 1) en a besoin et s'il correspond à un élément visible dans les frames d'un candidat retenu. On n'emprunte rien à un candidat non retenu.
- **Même idée, mêmes références.** Les images de référence viennent uniquement des frames des candidats listés dans `plan_scenario.md`.

Entrées : `speech_adapte.md` (beats), `plan_scenario.md` (candidats retenus), et pour chaque candidat retenu `segment.json` et `frames.axz`.

### 2.1 Regarder les frames

Pour chaque candidat retenu : extraire `frames.axz` (zip de WebP, `tNNNNNNNNN.webp` = instant en millisecondes), faire une planche-contact pour situer les passages, puis ouvrir en pleine taille les frames correspondant à chaque beat (instant du beat dans le candidat). Une frame qu'on n'a pas regardée ne peut pas être citée.

### 2.2 Décider ce qui est un asset

Pour chaque élément visible dans les frames d'un beat :
- **Est un asset** : un décor, un personnage, un objet ou une icône qui doit exister comme fichier image.
- **N'est jamais un asset** (fait en code ou au montage) : les textes et chiffres, les cartons et badges, le logo de la chaîne, les bandeaux de narrateur, et tout ce qui est géométrique ou graphique (barres, courbes, flèches, jauges, compteurs, traits, formes simples).

Ces éléments en code sont quand même notés dans une section « Éléments faits en code » de `Liste_assets.md`, sans prompt, pour que l'étape suivante sache les dessiner.

### 2.3 Une ligne par asset

Un asset qui revient d'un beat à l'autre n'est listé qu'une fois, avec la même forme partout. Chaque ligne contient :
- **id** : nom court, lettres, chiffres, `_`, `.` et `-` seulement (c'est aussi le nom du fichier généré) ;
- **beats** : les numéros de beats où il apparaît ;
- **remplace** : l'élément de la frame de référence qu'il remplace ;
- **nature** : *structurel conservé* (même rôle, même place, même taille) ou *thématique remplacé* (nouveau contenu du sujet, même forme visuelle) ;
- **états** : les poses ou états nécessaires aux beats (de face, écran allumé…) ;
- **image de référence** : le candidat et la frame choisie (nom du fichier) ;
- **zone utile** et **à ne pas reprendre** (logo, badge, texte) ;
- **fond** (voir 2.5).

### 2.4 Élément clé, petit élément, planche

- **Élément clé** (grand, important ou récurrent) : une génération à lui.
- **Petits éléments** : regroupés en planche de 4 à 6 éléments de même famille, avec une image de référence par élément et un seul fond pour toute la planche.
- **Poses d'un même personnage** : une planche de poses (même personnage, même tenue, même fond).

### 2.5 Choisir l'image de référence et le fond

- **Référence** : parmi les frames du candidat concerné, celle où l'élément est le plus entier, le plus net et le moins caché. Si aucune frame ne montre l'élément, prendre la frame du même candidat la plus proche par sa nature (décor, objet, matière) comme **référence de style**. Il y a toujours une référence.
- **Fond détourable** : vert pur `#00FF00` par défaut ; magenta `#FF00FF` si l'asset contient du vert ou du turquoise ; bleu `#0000FF` s'il contient les deux. La couleur n'apparaît nulle part dans l'asset. Une seule couleur par élément, la même pour toutes ses poses.
- **Plein cadre** (décor qui remplit tout le cadre, contenu d'écran) : aucun fond uni, le fond est « aucun (plein cadre) ».

### 2.6 Écrire le prompt de chaque génération

Le prompt demande à l'IA de transformer l'image de référence en l'asset voulu. Il contient, dans cet ordre :
1. **le fond** : « fond uni #00FF00, aplat parfait, aucun dégradé, aucune ombre, aucun sol, asset entier avec de la marge » (pour un plein cadre : « image pleine de bord à bord, sans fond uni ») ;
2. **ce qui est conservé** de la référence (cadrage, forme, proportions, style) et **ce qui est remplacé** (tenue, icône, contenu) ;
3. **la description de l'asset** (forme, taille, détails) ;
4. **les couleurs** en hexadécimal ;
5. **le style** (aplats, sans ombre portée) ;
6. **la pose**, immobile, sans flou de mouvement ;
7. **les interdits** : ne pas reprendre le logo de la chaîne, les badges, les bandeaux ni le texte de la référence ; aucun logo réel ; aucune ressemblance avec une personne réelle ; aucun texte lisible sauf un texte imposé par le speech, donné mot pour mot.

Pour une planche : une seule image qui réunit tous les éléments, avec pour chacun sa référence et sa description, la consigne de transformer chaque élément à partir de **sa propre** référence, de bien les séparer et de les garder entiers.

### 2.7 Produire les fichiers de sortie

Dans `ideaN/animation/etape2_assets/` :

```
etape2_assets/
  assets.json          les générations, au format du projet imgen d'IngXAi
  Liste_assets.md      la même liste en tableau lisible + éléments faits en code
  references/          les frames de référence choisies, copiées (png, jpg ou webp)
```

`assets.json` est un seul objet JSON valide :

```json
{
  "type": "imgen",
  "projet": "Idée N : assets",
  "dossier": "ideaN/animation/etape2_assets/generes",
  "taches": [
    {
      "id": "<id de l'asset ou de la planche>",
      "titre": "<nom lisible>",
      "prompt": "<prompt complet de 2.6>",
      "references": ["ideaN/animation/etape2_assets/references/<fichier>"],
      "depend_de": [],
      "desactive": false
    }
  ]
}
```

Une tâche = une génération (un élément clé, une planche ou une planche de poses). Chaque tâche a au moins une référence. Les images générées prennent le nom de l'`id`. Les chemins sont relatifs au dépôt ; ils sont remplacés par les chemins absolus au moment d'utiliser le projet dans IngXAi.

### 2.8 Vérifications avant de passer à l'étape 3

- [ ] Toutes les frames citées ont été regardées.
- [ ] Chaque asset renvoie à au moins un beat et à un élément d'une frame d'un candidat retenu.
- [ ] Chaque objet, personnage ou décor visible dans les beats est dans la liste, dans une planche ou dans « Éléments faits en code ».
- [ ] Aucun asset n'est un texte, un badge, un logo ou une forme géométrique.
- [ ] Aucun GIF ni animation n'est demandé dans les prompts : images fixes uniquement.
- [ ] Le JSON est valide, les `id` sont uniques et valides, chaque tâche a au moins une référence existante.
- [ ] Le fond du prompt est celui de la liste et n'apparaît pas dans les couleurs de l'asset ; toutes les poses d'un même élément ont le même fond.
- [ ] Chaque prompt contient les interdits (logo, badges, bandeaux, texte).

---

## Étapes suivantes (à définir)

- Étape 3 :
- Étape 4 :
