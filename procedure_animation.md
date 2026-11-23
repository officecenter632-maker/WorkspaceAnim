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
7. **L'agent tranche lui-même tout ce qu'il peut trancher, à toutes les étapes.** Il ne pose pas de question à l'utilisateur quand il peut décider seul (réutilisation d'un asset, type de transition, couleur de fond, amplitude d'un mouvement, nom de fichier, ordre de travail, passer à l'étape suivante). Il choisit l'option la plus raisonnable, l'inscrit dans le registre (« décisions fermées ») avec sa raison, puis continue. Il ne demande JAMAIS « veux-tu que je continue ? » ni « confirmes-tu ? » : il continue. L'utilisateur corrige après coup s'il n'est pas d'accord. Une question n'est permise que pour une information qu'il est impossible de deviner ou de trouver (accès, mot de passe, choix purement personnel), et alors une seule question, jamais une liste.

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

**But :** à partir du speech et des frames des candidats, obtenir la liste des images à générer (les assets), chacune avec son image de référence, son fond (ou l'absence de fond) et son **prompt complet**. Tout ce qui doit bouger est généré **en pièces détachées**, pour que l'animation en code soit fluide. Aucune validation humaine : l'agent fait tout et livre les fichiers, après **deux passes de vérification complètes** notées dans un registre (2.10).

**Principes**
- **Les assets sont des images fixes.** Il n'y a ni GIF ni vidéo. Le mouvement est fait en code à l'étape suivante, en déplaçant et en faisant pivoter des pièces.
- **Ce qui bouge est généré en pièces détachées**, dans une seule image par élément (un personnage, une porte, un ventilateur, une balance…). On ne génère ni planches de poses ni élément entier à plusieurs poses : la pose se calcule en code.
- **Rien d'inventé.** Un asset existe seulement si un beat du speech en a besoin et s'il correspond à un élément visible dans les frames d'un candidat retenu. On n'emprunte rien à un candidat non retenu.
- **Deux passes de vérification.** Une fois les fichiers produits, l'agent les vérifie en entier deux fois de suite (contenu, puis simulation et technique) et note à chaque passe ce qu'il a mis à jour. Les agents oublient des détails : une seule relecture ne suffit pas. L'étape 3 ne commence que si les trois passes sont faites.
- **Commit et push au fur et à mesure.** Après chaque bloc terminé (fichiers de 2.8, puis chaque passe), l'agent fait un commit et pousse sur `main`, sans attendre la fin de l'étape, pour que rien ne soit perdu si le travail s'interrompt.
- **Mêmes références.** Les images de référence viennent uniquement des frames des candidats listés dans `plan_scenario.md`.

Entrées : `speech_adapte.md` (beats), `plan_scenario.md` (candidats retenus), et pour chaque candidat retenu `segment.json` et `frames.axz`.

### 2.1 Regarder les frames

Pour chaque candidat retenu : extraire `frames.axz` (zip de WebP, `tNNNNNNNNN.webp` = instant en millisecondes), faire une planche-contact pour situer les passages, puis ouvrir en pleine taille les frames correspondant à chaque beat (instant du beat dans le candidat). Une frame qu'on n'a pas regardée ne peut pas être citée.

**En regardant les frames, relever aussi les éléments graphiques** (compteurs, chiffres animés, barres, courbes, flèches, jauges, cadres, bandeaux, formes, icônes simples, transitions visibles). Ils ne sont pas des assets, mais ils servent de **références de style** pour les infographies faites en code (2.2 bis). On ne part jamais de zéro : un graphique du speech est dessiné en s'inspirant d'un élément réellement vu dans les frames d'un candidat retenu.

### 2.2 Décider ce qui est un asset

Pour chaque élément visible dans les frames d'un beat :
- **Est un asset** : un décor, un personnage, un objet ou une icône qui doit exister comme fichier image.
- **N'est jamais un asset** (fait en code ou au montage) : les textes et chiffres, les cartons et badges, le logo de la chaîne du projet (celui qui est fourni, jamais celui des frames de référence), les bandeaux de narrateur, et tout ce qui est géométrique ou graphique (barres, courbes, flèches, jauges, compteurs, traits, formes simples).

Ces éléments en code sont quand même notés dans une section « Éléments faits en code » de `Liste_assets.md`, sans prompt, pour que l'étape suivante sache les dessiner.

### 2.2 bis Fiche de chaque élément fait en code

Chaque élément fait en code (compteur, barre, jauge, courbe, flèche, icône, cadre…) reçoit une fiche. L'étape suivante dessine l'élément d'après cette fiche, sans deviner.

1. **Chercher une référence de style, dans cet ordre, et s'arrêter au premier niveau qui en donne une.** L'agent ne décide lui-même qu'en dernier.
   - **Niveau 1 : les candidats retenus** de l'idée (ceux de `plan_scenario.md`). Prendre l'élément graphique le plus proche de l'élément voulu (un compteur pour un compteur, des barres pour des barres).
   - **Niveau 2 : les autres candidats de la même idée** (`scenario_candidats/`, non retenus). Ouvrir leur planche-contact et leurs frames. Ils ne fournissent ici que du **style graphique**, jamais d'assets ni de contenu.
   - **Niveau 3 : les candidats des autres idées de la même recherche** (même chaîne, donc même univers visuel). Même usage : style graphique seulement.
   - **Niveau 4 : décision de l'agent**, seulement si les niveaux 1 à 3 ne montrent aucun élément graphique utilisable. L'agent définit alors un style sobre, **dérivé de ce qui existe déjà** : la palette hex et les aplats des frames des candidats retenus et des assets générés, sans ombre, formes simples. Il écrit dans la fiche « style décidé par l'agent, aucune référence trouvée » et indique **quels niveaux il a cherchés**.
   La frame choisie est copiée dans `references_code/`, avec son niveau noté dans la fiche.
2. **Décrire ce qui est repris** de cette référence : palette (hex mesurée sur la frame), forme (barre pleine ou contour, coins droits ou arrondis), épaisseur des traits, police ou allure des chiffres, position à l'écran, ombre ou non, façon d'apparaître et de bouger.
3. **Choisir le type** adapté à la donnée : compteur pour un total, jauge ou barre pour une part, barres côte à côte pour comparer deux valeurs, courbe pour une évolution, icônes répétées pour une proportion (« un sur treize »). Le type doit pouvoir se lire en quelques secondes.
4. **Donner les données exactes** de `speech_adapte.md` (chiffres, unités, étiquettes), **sans en ajouter** : un chiffre qui est dans `recherches.md` mais pas dans le speech n'est pas affiché. Les textes affichés (titres, étiquettes) sont écrits en toutes lettres dans la fiche. Quand le speech dit un mot (« nearly half »), l'écran affiche ce mot ; le dessin (la part d'un donut) peut suivre le chiffre exact de `recherches.md`, mais le chiffre exact n'est pas écrit.
7. **Les transitions entre beats** (volet, glissement, fondu) vues dans les frames sont aussi des éléments en code, avec leur fiche (frame de référence, durée).
5. **Dire l'animation** : ce qui entre, comment (compte, grandit, se dessine), à quel beat, pour quelle durée.
6. **Ne pas reprendre** le logo, les badges, les textes et les chiffres de la frame de référence : seul le style est repris.

Les fiches sont écrites dans `Liste_assets.md`, section « Éléments faits en code », au format :

```
| élément | beat | type | données | référence de style (niveau · candidat · frame) | style repris (hex, forme, trait, police) | animation | emplacement |
```

### 2.3 Prévoir les mouvements de chaque asset

À partir des beats, noter pour chaque asset les mouvements qu'il doit faire (marcher, lever le bras, hocher la tête, ouvrir une porte, tourner, se balancer…). Trois cas :
- **Il ne bouge pas par lui-même** (il peut être déplacé, zoomé ou apparaître en code) : une image unique.
- **Il bouge d'un seul bloc** (glisse, tourne, grossit) : une image unique.
- **Il a des parties qui bougent les unes par rapport aux autres** : il est décomposé en **pièces détachées** (2.4).

### 2.4 Décomposer en pièces détachées

Pour un asset à parties mobiles :
1. **Découper selon les mouvements voulus, pas plus.** Mais un mouvement qui **plie** un membre (croiser les bras, se prendre la tête, taper au clavier, se gratter) exige **deux segments** (le bras, de l'épaule au coude, et l'avant-bras, du coude au bout des doigts) : un bras en un seul bloc ne sait que pivoter droit. **Un bras = 2 pièces, jamais 3** : la main fait partie de l'avant-bras, elle n'est pas une pièce à part (sauf si un beat anime vraiment les doigts ou le poignet). Même règle pour la jambe : cuisse + jambe basse avec le pied, et seulement si elle est animée. **On ne découpe une pièce que si elle sera utilisée par un mouvement des beats** : un personnage qui ne fait que lever le bras n'a pas besoin de jambes en deux segments, et un personnage immobile reste entier. Exemple complet (le maximum, jamais le minimum) : tête, torse, bras en deux segments × 2, jambes en deux segments × 2 si elles marchent. Ajouter des variantes (bouche ouverte, yeux fermés…) seulement si les beats les demandent.
2. **Gauche et droite = côtés gauche et droit de l'image** (pas ceux du personnage). Cette convention est écrite dans le prompt et dans `pieces.json`.
   **Pour chaque pièce, noter** : son id, sa **pièce parent** (l'avant-bras a pour parent le haut du bras) et son **articulation** (le coude, l'épaule…). Les coordonnées exactes du pivot sont mesurées à l'étape 3, après découpage.
3. **Une seule génération par asset**, qui contient toutes ses pièces. **Un personnage = un asset** : un groupe (une famille, une équipe) est découpé par personnage, une génération chacun, et les personnages qui ne bougent pas par membre (des enfants immobiles) sont regroupés entiers dans une même image. **Maximum 10 pièces par génération** : au-delà, les modèles d'image mélangent ou oublient des pièces. Elles sont **séparées les unes des autres** dans l'image, **à la même échelle**, vues dans une **pose neutre** (debout, bras écartés, pièces posées à plat), avec un **même style et un même fond**.
4. **Chaque pièce dépasse un peu sur l'articulation suivante** (le haut du bras se prolonge sous l'épaule, l'avant-bras sous le coude), pour qu'aucun trou n'apparaisse quand la pièce pivote. Les pièces restent séparées dans l'image, mais chacune porte sa partie de recouvrement.
5. **Les petits éléments qui ne bougent pas** (petits objets, icônes) sont regroupés dans une même image de 4 à 6 éléments, séparés, avec une référence par élément et un fond commun.
6. **Le torse est généré sans manches (épaule nue, emmanchure).** La manche appartient à la pièce du haut du bras, jamais au torse. Un torse qui garde un bout de manche (T-shirt dessiné avec ses manches courtes) laisse ce bout visible et immobile quand le bras pivote : la manche apparaît en double et l'épaule se décroche. Le torse s'arrête donc à l'emmanchure, sans tissu qui dépasse. Le haut du bras, avec sa manche arrondie à l'épaule, **passe devant le torse** et recouvre l'emmanchure ; il se prolonge sous elle pour qu'aucun trou n'apparaisse quand il tourne. Même principe à la hanche : le bas du torse ne porte aucune partie de la cuisse. Un vêtement qui dépasse d'une articulation est coupé sur la pièce qui reste fixe, et dessiné sur la pièce qui tourne.

### 2.5 Une ligne par asset

Un asset qui revient d'un beat à l'autre n'est listé qu'une fois, avec la même forme partout. Chaque ligne contient :
- **id** : nom court, lettres, chiffres, `_`, `.` et `-` seulement (c'est aussi le nom du fichier généré) ;
- **beats** : les numéros de beats où il apparaît ;
- **remplace** : l'élément de la frame de référence qu'il remplace ;
- **nature** : *structurel conservé* (même rôle, même place, même taille) ou *thématique remplacé* (nouveau contenu du sujet, même forme visuelle) ;
- **mouvements** : ceux prévus en 2.3, et la liste des **pièces** si l'asset est décomposé (id, parent, articulation) ;
- **image de référence** : le candidat et la frame choisie (nom du fichier) ;
- **zone utile** et **à ne pas reprendre** (logo, badge, texte) ;
- **détourage** : oui ou non, et le **fond** (2.6).

### 2.5 bis Mise en place par beat

Pour chaque beat, `Liste_assets.md` note **où et quand** chaque asset et chaque élément en code apparaît, pour que l'étape 3 n'ait rien à deviner :
- **instant d'apparition**, en secondes : début du beat + rang du mot-clé × durée par mot (durée du beat divisée par son nombre de mots) ;
- **position** (x et y en % de l'écran, à ±5 %), **taille** (hauteur en % de l'écran) et **couche** (derrière ou devant), **mesurées sur la frame de référence** du même beat, pas devinées ;
- **cadrage** : si l'écran est partagé en panneaux plus étroits que l'image (deux panneaux côte à côte), dire quelle partie de l'image reste visible, et placer les assets dans cette partie ;
- **objet parent** : un avis posé sur une porte suit la rotation du battant ;
- **éléments à séparer après génération** (deux objets dans une même image, plusieurs personnages entiers) : listés pour l'étape 3 ;
- aucun élément n'en cache un autre sans que ce soit voulu (un compteur ne cache pas un visage).

### 2.5 ter Animation de chaque asset (obligatoire)

**Chaque asset a une consigne d'animation écrite, sans exception.** Sans elle, l'étape 3 oublie ou invente le mouvement. Il n'existe pas d'asset « fixe » : un décor, un objet, un personnage qui ne fait rien pendant le beat reçoivent quand même un mouvement de vie, écrit.

Elle est écrite dans `pieces.json`, dans un bloc `animation` par asset généré, et dans `elements_code.json` pour **chaque élément fait en code** (compteurs, étiquettes, flèches, cercles, donuts, textes sur objets, formes) **et chaque transition**, avec la même structure. Chaque entrée de `elements_code.json` porte aussi un champ `reference_style` (fichier de `references_code/`, niveau, à reprendre, à ne pas reprendre) : la frame que l'étape 3 doit regarder avant de dessiner l'élément. Un élément en code sans bloc d'animation ni référence de style est une erreur, comme un asset sans bloc :
- **`entree`** : comment il arrive (présent dès la première image, glisse, tombe, fondu, après quelle transition).
- **`vie`** : le mouvement **continu** tant qu'il est à l'écran (respiration, balancement, pulsation, poussée de caméra lente, défilement derrière un autre élément). Jamais « immobile ».
- **`mouvements`** : un par geste voulu par le speech, avec `id`, les `pieces` concernées (ids de `pieces.json`), le `declencheur` (beat et mot-clé du speech, avec l'instant de 2.5 bis) et la `description` exacte du geste : quelle pièce, autour de quelle articulation, vers où (gauche et droite = côtés de l'image), de combien (angle ou fraction de l'écran), ce qui bouge avec elle (la tête suit, l'objet attaché suit), ce qui se passe après (tenu, retour à la pose neutre, rebond).
- **`sortie`** : comment il disparaît ou ce qui le recouvre.

**Les durées ne sont pas écrites.** L'animateur (étape 3) les calcule à partir des instants du speech. L'agent décrit le geste, pas sa durée.

Règles :
1. Un mouvement qui plie un membre est décrit avec ses deux segments (2.4).
2. Un décor ou un groupe qui zoome zoome **en bloc** avec ce qui est posé dessus, jamais seul ; les éléments en code ne zooment pas.
3. Un objet attaché à une pièce mobile le dit (« l'avis suit le battant »).
4. Un asset qui apparaît dans plusieurs beats a une consigne par beat.
5. Le geste correspond au sens du mot du speech (un « record » ne se mime pas en souriant).
6. Un élément en code est animé aussi : arrivée (glisse, se dessine, compte, apparaît lettre par lettre), vie continue (flottaison, pulsation), changement de valeur au mot du speech, sortie. Il est décrit par ce qui bouge (le nombre défile de 0 à X, la part se dessine dans le sens des aiguilles d'une montre depuis le haut), jamais par « il apparaît » seul. Un texte posé sur un objet est attaché à lui (parent).
7. Quand le mouvement est visible dans les frames des candidats, l'amplitude est mesurée dessus ; sinon une valeur de départ est écrite et notée « à ajuster à l'étape 3 » dans `Liste_assets.md`.

### 2.6 Choisir l'image de référence et le fond

- **Référence** : parmi les frames du candidat concerné, celle où l'élément est le plus entier, le plus net et le moins caché. Si aucune frame ne montre l'élément, prendre la frame du même candidat la plus proche par sa nature (décor, objet, matière) comme **référence de style**. Il y a toujours une référence. **Si l'élément est coupé dans la frame** (personnage en plan serré dont on ne voit pas les jambes ni les chaussures), ajouter une **deuxième référence** : une frame du même candidat où il est en pied. Le prompt dit à quoi sert chaque référence (« la première pour le visage et les vêtements, la deuxième pour les jambes et les chaussures »), et les couleurs de ce qui n'est visible que dans la deuxième sont mesurées sur elle.
- **Le fond dépend de l'image, il est décidé pour chaque génération :**
  - **Image à détourer** (personnage ou pièces détachées, objet, icône, décor qui sera posé sur un autre fond) : un **fond uni détourable**, dont la couleur est **écrite explicitement en hexadécimal dans le prompt**. **La couleur se choisit sur des mesures, pas à l'œil** : mesurer les couleurs dominantes de la référence (médiane sur de petites zones, ou couleur la plus fréquente de chaque vêtement ou partie), les écrire en hexadécimal, puis choisir parmi vert `#00FF00`, magenta `#FF00FF` et bleu `#0000FF` celle dont la teinte est la plus éloignée de toutes les couleurs de l'asset (vert par défaut). Un violet-magenta ou un rose vif exclut le magenta ; un vert, un jaune-vert ou un turquoise très saturé exclut le vert ; un bleu vif exclut le bleu. Un bleu-teal désaturé (jean) n'exclut pas le vert. La couleur n'apparaît nulle part dans l'asset, même approchée. Une seule couleur pour toutes les pièces d'un même élément. On note en une demi-ligne pourquoi cette couleur.
  - **Image qui n'a pas besoin d'être détourée** (décor plein cadre, fond de scène, contenu d'écran rectangulaire) : **aucun fond uni**. Le prompt ne mentionne aucune couleur de fond et demande une image complète de bord à bord, et la liste note « détourage : non, fond : aucun (plein cadre) ».

### 2.7 Écrire le prompt de chaque génération

Le prompt demande à l'IA de transformer l'image de référence en l'asset voulu. Il contient, dans cet ordre :
1. **le fond** : pour une image à détourer, « fond uni #XXXXXX, aplat parfait, aucun dégradé, aucune ombre, aucun sol, chaque élément entier avec de la marge » ; pour une image qui n'est pas détourée, « image pleine de bord à bord, sans fond uni » ;
2. **ce qui est conservé** de la référence (cadrage, forme, proportions, style) et **ce qui est remplacé** (tenue, icône, contenu) ;
3. **la description de l'asset** (forme, taille, détails) ;
4. **les couleurs** en hexadécimal, **mesurées sur la frame** (jamais estimées ni recopiées d'un autre élément : un hex de mur rose n'est pas celui d'un haut rouge) ; chaque couleur nommée dans le texte a son hex ;
5. **le style** (aplats, sans ombre portée) ;
6. **la pose** : immobile, sans flou de mouvement ; pour des pièces détachées, la pose neutre de 2.4, **cohérente avec l'asset** (un personnage assis garde ses jambes en position assise, avec la chaise et le bureau en pièces séparées ; ne pas écrire « assis » et « debout » dans le même prompt) ; mains vides : ne pas reprendre les objets tenus dans la référence ;
6 bis. **le format** : « 16:9 paysage (1920x1080) » pour un décor plein cadre ; « grande image 16:9 » pour une planche de pièces ou de petits éléments ;
7. **les pièces**, quand l'asset est décomposé : la liste exacte des pièces, leur séparation (aucune pièce ne touche une autre), la même échelle, et le recouvrement aux articulations (2.4, point 4) ; **le torse est demandé sans manches ni bras, épaules nues et coupées net à l'emmanchure, la manche étant dessinée sur le haut du bras** (2.4, point 6) ; la main est dessinée au bout de l'avant-bras, pas comme pièce à part ;
8. **les interdits** : ne pas reprendre le logo de la chaîne, les badges, les bandeaux ni le texte de la référence ; aucun logo réel ; aucune ressemblance avec une personne réelle ; **aucun texte, lettre ni chiffre dans l'image** (les modèles d'image les orthographient mal) : les panneaux, documents et étiquettes sont dessinés **vides** (panneau blanc, bande unie, lignes grises) et leur texte est ajouté en code, noté dans les fiches de 2.2 bis. Les objets qui doivent être reconnus sans texte (un avis d'expulsion, une fiche de paie) se distinguent par la forme et la couleur (bande rouge ou bleue, sceau, pièce).

### 2.8 Produire les fichiers de sortie

Dans `ideaN/animation/etape2_assets/` :

```
etape2_assets/
  assets.json          les générations, au format du projet imgen d'IngXAi
  Liste_assets.md      la liste en tableau lisible, un récapitulatif par beat (décor, assets, éléments en code), la mise en place par beat (2.5 bis), les fiches des éléments en code, les décisions
  pieces.json          pour **chaque** asset : pièces, parents, articulations et bloc `animation` (2.5 ter)
  elements_code.json   pour **chaque** élément en code et chaque transition : bloc `animation` (2.5 ter)
  references/          les frames de référence choisies, copiées (png, jpg ou webp)
  references_code/    les frames qui servent de référence de style pour les éléments faits en code
  registre_verification.json   le registre des deux passes de vérification (2.10), créé avec les deux passes à false
```

`assets.json` est un seul objet JSON valide :

```json
{
  "type": "imgen",
  "projet": "Idée N : assets",
  "dossier": "ideaN/animation/etape2_assets/generes",
  "taches": [
    {
      "id": "<id de l'asset>",
      "titre": "<nom lisible>",
      "prompt": "<prompt complet de 2.7>",
      "references": ["ideaN/animation/etape2_assets/references/<fichier>"],
      "depend_de": [],
      "desactive": false
    }
  ]
}
```

`pieces.json` donne, pour **chaque asset** (un décor ou un objet entier compte comme une seule pièce), la liste des pièces et sa consigne d'animation :

```json
{
  "<id de l'asset>": {
    "fond": "#00FF00",
    "pieces": [
      {"id": "torse", "parent": null, "articulation": null},
      {"id": "bras_droit_haut", "parent": "torse", "articulation": "épaule droite"},
      {"id": "bras_droit_bas", "parent": "bras_droit_haut", "articulation": "coude droit"}
    ],
    "animation": {
      "entree": "présent dès la première image",
      "vie": "respiration en continu : torse +1 %, tête qui suit",
      "mouvements": [
        {"id": "leve_le_bras", "pieces": ["bras_droit_haut", "bras_droit_bas"], "declencheur": "beat 2, « record » (9,67 s)", "description": "le bras monte autour de l'épaule d'environ 80° vers l'extérieur de l'image, l'avant-bras se déplie, tenu puis retombée avec rebond"}
      ],
      "sortie": "s'efface avec le reste du beat"
    }
  }
}
```

`elements_code.json` donne, pour **chaque élément fait en code et chaque transition** (même liste que les fiches de `Liste_assets.md`), la référence de style et la consigne d'animation. C'est un objet JSON valide, une clé par élément (`_convention` en tête) :

```json
{
  "compteur_menages": {
    "reference_style": {
      "fichier": "references_code/rc_n1_c05_t000988000_pilules_prix.webp",
      "niveau": "N1",
      "a_reprendre": "carte blanche à coins arrondis, grand chiffre sombre en gras",
      "a_ne_pas_reprendre": "le logo de la chaîne et tout texte ou donnée de la frame"
    },
    "entree": "comment l'élément arrive, avec le mot du speech",
    "vie": "mouvement continu tant qu'il est à l'écran",
    "mouvements": [
      { "id": "...", "declencheur": "beat, « mot » (instant)", "description": "ce qui bouge, comment, dans quel sens" }
    ],
    "sortie": "comment il disparaît"
  }
}
```

Le fichier est produit pendant l'étape 2, au même moment que `pieces.json`, et vérifié dans les deux passes. Il n'y a aucune durée dans ses blocs.

Une tâche d'`assets.json` = une génération (un asset avec toutes ses pièces, ou une image de petits éléments). Chaque tâche a au moins une référence. Les images générées prennent le nom de l'`id`. Les chemins sont relatifs au dépôt et le restent : IngXAi les fait télécharger depuis GitHub par sAutoniax (`depot_references`), rien n'est copié sur le PC.

### 2.9 Checklist de vérification

Cette checklist est déroulée **en entier à chaque passe** de 2.10 (deux fois), pas une seule fois. Une case n'est cochée que si l'agent a rouvert les fichiers et les frames pour la vérifier.

- [ ] Toutes les frames citées ont été regardées.
- [ ] Chaque asset renvoie à au moins un beat et à un élément d'une frame d'un candidat retenu.
- [ ] Chaque objet, personnage ou décor visible dans les beats est dans la liste, dans une image de petits éléments ou dans « Éléments faits en code ».
- [ ] Aucun asset n'est un texte, un badge, un logo ou une forme géométrique.
- [ ] Aucun GIF ni animation n'est demandé dans les prompts : images fixes uniquement.
- [ ] Chaque asset à parties mobiles est décomposé en pièces, avec parent et articulation pour chaque pièce, et seulement les pièces utiles aux mouvements des beats.
- [ ] Les prompts de pièces demandent des pièces séparées, à la même échelle, avec recouvrement aux articulations.
- [ ] **Bras = 2 pièces** (bras + avant-bras avec la main), jamais 3 ; aucune pièce n'est découpée si aucun beat ne l'anime.
- [ ] **Le torse est demandé sans manches** (emmanchure nue) et la manche est sur le haut du bras (2.4, point 6).
- [ ] Chaque génération a un « détourage » oui ou non. S'il est oui, le prompt donne une couleur de fond en hexadécimal, identique pour toutes les pièces d'un élément, qui n'apparaît pas dans l'asset. S'il est non, le prompt ne mentionne aucune couleur de fond.
- [ ] Le JSON est valide, les `id` sont uniques et valides, chaque tâche a au moins une référence existante.
- [ ] Chaque prompt contient les interdits (logo, badges, bandeaux, texte).
- [ ] **Récapitulatif par beat** : chaque beat a un décor (ou un fond uni noté), ses assets, ses éléments en code et ses données. Aucun beat sans fond ; aucun asset ou élément absent du récapitulatif.
- [ ] **Chaque donnée affichée est dans `speech_adapte.md`** (pas seulement dans `recherches.md`).
- [ ] Aucun prompt ne contient de texte à écrire dans l'image ; les textes sont dans les fiches.
- [ ] Les hex des prompts sont mesurés sur la frame ; la couleur de fond est choisie sur ces mesures (2.6).
- [ ] Aucune contradiction dans un prompt (assis/debout, entier/partiel, avec/sans fond) ; au plus 10 pièces par génération ; les mouvements qui plient un membre ont deux segments.
- [ ] Les références identiques (même frame pour plusieurs assets) sont voulues ; une génération n'a pas deux fois la même référence.
- [ ] **Mise en place** : chaque beat a, pour chaque asset et chaque élément en code, un instant, une position, une taille, une couche (2.5 bis) ; les parents, les panneaux et les éléments à séparer sont notés.
- [ ] Un asset coupé dans sa frame de référence a une deuxième référence en pied.
- [ ] Gauche et droite sont définis (côtés de l'image) dans les prompts et dans `pieces.json`.
- [ ] Les transitions entre beats ont une fiche.
- [ ] **Les instants** de la mise en place sont recalculés par script et concordent avec le speech.
- [ ] **Aucun recouvrement involontaire** : chaque élément en code est placé hors des visages et des pieds ; décor et personnages viennent du même plan de caméra.
- [ ] **Taille minimale d'un texte** : 2,5 % de la hauteur de l'écran.
- [ ] Un asset réutilisé dans un autre beat est noté (réutilisation, aucune génération de plus).
- [ ] **Animation (2.5 ter)** : chaque asset a un bloc `animation` dans `pieces.json` avec `entree`, `vie`, `mouvements` et `sortie` ; aucun asset « fixe » ; chaque geste du speech a sa description exacte (pièce, articulation, sens, amplitude, déclencheur) ; aucune durée écrite.
- [ ] Chaque élément fait en code a une fiche complète (type, données, référence de style, style repris, animation, emplacement).
- [ ] **`elements_code.json` (2.5 ter)** : chaque élément en code et chaque transition de `Liste_assets.md` y a une entrée avec `reference_style` (le fichier existe dans `references_code/`), `entree`, `vie`, `mouvements` et `sortie` ; aucune durée, aucun « fixe », aucun « ou » (choix tranché).
- [ ] Chaque référence de style est une frame réellement regardée, copiée dans `references_code/`, avec son niveau (1 à 3). Un style décidé par l'agent (niveau 4) n'est accepté que si les niveaux 1 à 3 ont été cherchés et sont cités dans la fiche.
- [ ] Les couleurs et formes des fiches viennent des frames, pas d'une invention ; les chiffres viennent du speech.
- [ ] Le style des éléments en code est cohérent avec celui des assets générés (mêmes aplats, mêmes couleurs).

### 2.10 Deux passes de vérification et registre

Une fois les fichiers de 2.8 produits, l'agent **ne passe pas à l'étape 3**. Il fait **deux passes de vérification complètes, l'une après l'autre**, et note chacune dans `registre_verification.json`. La première passe trouve des oublis ; la deuxième trouve ce que la première a manqué et confirme que les fichiers sont cohérents et prêts.

**Règles communes aux deux passes**
- **Complète.** Chaque passe déroule toute la checklist 2.9 sur tous les fichiers, relit `speech_adapte.md` beat par beat et rouvre les frames de référence. Une passe faite de mémoire ne compte pas.
- **Chaque passe a son angle**, en plus de la checklist :
  - **Passe 1, contenu** : le listing face au speech et aux frames. Chaque beat, chaque élément visible, chaque asset et élément en code, chaque donnée, chaque référence, chaque couleur mesurée. **Et l'animation et les références de style, un par un** : pour chaque asset de `pieces.json` et chaque élément en code et chaque transition de `elements_code.json`, (a) le bloc `entree`, `vie`, `mouvements`, `sortie` existe et chaque champ est rempli ; (b) chaque geste correspond au sens du mot du speech et a son déclencheur exact (beat, mot-clé, instant de `Liste_assets.md`) ; (c) la description dit ce qui bouge, comment, dans quel sens et de combien, pas seulement « apparaît » ; (d) aucune durée, aucun « fixe » ni « immobile », aucun « ou » (choix non tranché) ; (e) les pièces citées existent dans `pieces.json` ; (f) la `reference_style` pointe une frame **rouverte et regardée pendant la passe**, dont le fichier existe, et ce qu'elle dit de reprendre et de ne pas reprendre est exact.
  - **Passe 2, simulation et technique** : pour chaque beat, dérouler l'animation seconde par seconde en pensée, avec l'instant de chaque mot-clé du speech. Vérifier que l'étape 3 pourra construire l'écran **sans rien deviner** : le décor ; la position, la taille et la couche de chaque asset (2.5 bis) ; les pièces de chaque mouvement ; chaque élément en code avec sa fiche et son instant d'apparition ; les textes et chiffres affichés (tous dans le speech) ; l'accord de style entre assets et éléments en code ; ce qui se recouvre à l'écran ; les objets attachés à une pièce mobile ; les éléments à séparer après génération ; les transitions entre beats. **Pour l'animation** : à l'instant de chaque mot-clé, dérouler l'arrivée, la vie continue et la sortie de chaque élément en code et de chaque asset, et vérifier que (a) un élément qui glisse ou grossit ne couvre aucun visage pendant son arrivée, pas seulement une fois posé ; (b) deux mouvements successifs d'un même personnage s'enchaînent (retour à la pose neutre ou geste suivant écrit) et ne demandent pas la même pièce au même instant ; (c) chaque élément qui apparaît a sa sortie au changement de beat ; (d) un élément attaché (texte d'avis, panneau, étiquette de source) suit bien son parent ; (e) les mouvements de vie de deux éléments voisins ne les font pas se chevaucher ; (f) le beat le plus court (beat 5) peut contenir tous ses gestes sans que l'ordre écrit soit impossible. Tout ce qui manque est ajouté. **Puis la partie technique** : JSON valides, `id` uniques, chemins existants, cohérence entre `Liste_assets.md`, `assets.json`, `pieces.json`, `elements_code.json`, `references/` et `references_code/` (chaque élément en code et chaque transition de `Liste_assets.md` a une entrée dans `elements_code.json` et inversement ; chaque asset de `assets.json` a un bloc `animation` dans `pieces.json` ; chaque `reference_style.fichier` existe ; **contrôle par script** : quatre champs présents partout ; aucune durée (« en 0,8 s », « pendant 2 s », « durée », « secondes ») ; aucun asset ou élément « fixe » ou « immobile » (« pieds fixes » décrit un point d'ancrage et reste permis) ; aucun « ou » entre deux choix ; **chaque instant cité « mot-clé (T s) » est recalculé** (début du beat + rang du mot × durée du beat ÷ nombre de mots) et doit tomber sur ce mot à 0,02 s près ; les instants de déclenchement sont permis, ce ne sont pas des durées), relecture mot à mot de chaque prompt (2.7) et des pièges de 2.11 un par un (contradictions, format, hex, couleur de fond, texte dans l'image), et tout ce que la passe 1 a noté dans `non_verifie`.

- **Chaque passe corrige tout de suite** ce qu'elle trouve, dans les fichiers, et **note chaque mise à jour dans le registre** (fichier, changement, raison). Une passe qui ne trouve rien l'écrit (« aucune mise à jour ») : ce n'est pas une raison de la bâcler.
- **Ordre strict.** La passe 2 commence seulement quand la passe 1 est à `true`. Une passe passe à `true` seulement quand toutes ses corrections sont faites et sauvegardées. Une correction faite pendant la passe 2 est revérifiée aussitôt (relire la partie modifiée et les fichiers liés) et notée.
- **Un fichier, un bloc ou une fiche ajouté après une passe n'est couvert par aucune passe.** Il est vérifié avec les mêmes contrôles (angle de la passe 1 et de la passe 2) et le registre le dit, ligne par ligne, dans `mises_a_jour` (« revérification animation : ... ») ; sinon la passe concernée repasse à `false`. Un fichier non vérifié est noté dans `non_verifie`.
- **Commit et push après chaque passe**, avec le message « Idée N : vérification passe X ».
- **L'étape 3 ne commence que si `passe_1` et `passe_2` sont à `true`.**

**Format de `registre_verification.json`.** Il est créé en 2.8, avec les deux passes à `false`. L'agent met `faite` à `true` à la fin de chaque passe, renseigne la date, liste les mises à jour et ce qui n'a pas pu être vérifié (par exemple le rendu des images, qui n'existent pas encore) :

```json
{
  "idee": N,
  "passe_1": {
    "faite": false,
    "angle": "contenu : listing face au speech et aux frames",
    "date": null,
    "mises_a_jour": [
      {"fichier": "assets.json", "changement": "...", "raison": "..."}
    ],
    "non_verifie": []
  },
  "passe_2": {"faite": false, "angle": "simulation beat par beat et technique", "date": null, "mises_a_jour": [], "non_verifie": []}
}
```

### 2.10 bis Décisions fermées

Quand un choix reste ouvert (réutiliser un asset dans un autre beat, type d'ouverture ou de fermeture, couleur de fond d'un détourage), Claude le tranche seul (voir principe 7), l'inscrit dans le registre sous « décisions fermées » avec sa raison, et ne pose jamais la question à l'utilisateur, ni ne la repose si elle est déjà tranchée. L'utilisateur corrige s'il n'est pas d'accord.

Idée 1 : (D1) la famille revient au beat 4 devant la porte avec les assets du beat 1, sans génération de plus ; (D2) ouverture et fermeture en coupe franche ; (D3) fond vert pour la mère malgré son jean teal #23868F, tolérance de détourage réglée à l'étape 3.

### 2.11 Pièges à anticiper (erreurs de dernière minute)

1. **Un beat sans décor** : les éléments détourés flottent dans le vide. Vérifier le décor de chaque beat.
2. **Un chiffre ou un nom qui n'est pas dans le speech** (venu de `recherches.md`) : ne pas l'afficher.
3. **Un mouvement impossible avec les pièces prévues** (croiser les bras avec des bras d'un seul bloc).
4. **Une couleur de fond trop proche d'un vêtement** (haut violet et fond magenta) : le détourage mange le vêtement.
5. **Un hex faux** (recopié d'un autre élément, estimé à l'œil) : l'image sort d'une autre couleur que celle voulue.
6. **Du texte dans l'image** (« FOR RENT », « PAYCHECK ») : orthographe fausse ; mettre le texte en code.
7. **Une pose contradictoire** (« assis » puis « pose debout bras écartés »).
8. **Un objet tenu dans la référence repris par erreur** (papiers dans les mains du père).
9. **Une référence qui montre un élément caché** (décor derrière des personnages) : le modèle doit inventer les parties masquées ; le dire dans « à vérifier ».
10. **Le logo ou les badges de la chaîne des frames** repris dans l'image ou dans le code.
11. **Une référence qui n'existe pas dans le dépôt** : les chemins du JSON restent relatifs et sAutoniax les télécharge ; un chemin faux donne une erreur 404 à l'envoi. Les vérifier avant de pousser.
12. **Aucun format** précisé : l'image sort carrée ; toujours écrire le format.
13. **Des jambes ou des chaussures inventées** parce que la frame de référence est en plan serré : deuxième référence en pied.
14. **Un chiffre exact affiché alors que le speech dit un mot** (« nearly half » écrit « 49 % »).
15. **Un panneau plus étroit que l'image** : l'asset est placé hors du champ visible.
16. **Un objet posé sur une pièce mobile qui ne la suit pas** (l'avis reste en l'air quand la porte tourne).
17. **Un élément en code qui cache un visage** ou un asset.
18. **Gauche et droite ambigus** : côté du personnage ou côté de l'image.
19. **Deux objets dans une même image** sans noter qu'il faudra les séparer à l'étape 3.
20. **Une transition oubliée** entre deux beats.
21. **Décor et personnages tirés de plans de caméra différents** (un plan zoomé et un plan large) : les échelles ne s'accordent pas. Même plan pour le décor et les personnages en pied.
22. **Une couleur mesurée sur une frame zoomée ou sur une zone mélangée au décor** (un jean « teal » mesuré clair alors qu'il est saturé) : mesurer sur le plan large, par médiane des pixels de la pièce.
23. **Un élément en code posé sur des personnages en pied** (icônes en bas, étiquette sur les jambes) : réserver le haut de l'écran (20 %) aux éléments en code quand les personnages sont en pied, et placer chaque élément en vérifiant les visages et les pieds.
24. **Un décor ou une référence qui contient un objet que l'asset refait** (fauteuil dans le décor et chaise dans l'asset) : deux objets pour un seul, retirer l'un des deux.
25. **Une référence qui montre d'autres éléments que celui à redessiner** (une frame à trois panneaux) : le prompt dit lesquels ignorer.
26. **Un beat très court** (moins de 3 s) : le noter dans la mise en place ; l'animateur règle les durées pour tenir dans la fenêtre.
27. **Un asset qui doit revenir dans un autre beat sans être listé** : le noter dans le récapitulatif par beat (réutilisation, aucune génération de plus).
28. **Un instant noté à l'œil** : calculer chaque instant par script (début du beat + rang du mot × durée par mot) et comparer.
29. **Un texte d'accessoire (« FOR RENT » sur un panneau) pris pour une donnée** : le noter comme texte d'accessoire, présent seulement là où il est lisible.
30. **Un asset sans consigne d'animation**, ou un asset marqué « fixe » : l'étape 3 l'oublie ou l'invente. Tous ont un bloc `animation` (2.5 ter).
31. **Une durée écrite à la place du geste** : l'agent décrit le mouvement, l'animateur calcule les durées.
32. **Un décor qui zoome seul** alors que des personnages sont posés dessus : ils glissent dans le décor ; zoomer le groupe.

33. **Un torse généré avec ses manches** : le bout de manche reste immobile quand le bras pivote et dépasse de l'épaule. Demander le torse sans manches, la manche sur le haut du bras (2.4, point 6).
34. **Une main découpée à part** : un bras en trois pièces (bras, avant-bras, main) multiplie les jointures à caler pour rien. La main fait partie de l'avant-bras.
35. **Une pièce découpée sans être animée** : chaque pièce en plus est une jointure en plus à caler. On ne découpe que ce qui bouge.

### 2.12 Quand toutes les idées ont fini l'étape 2 : le projet de génération des images

**Quand.** Dès que **toutes** les idées du dépôt (`idea1` ... `ideaN`) ont leurs étapes 1 et 2 faites, c'est-à-dire pour chacune : `etape1_speech/speech_adapte.md`, `etape2_assets/assets.json` et `registre_verification.json` avec `passe_1` et `passe_2` à `true`. Il ne reste alors que la génération des images. L'agent ne demande rien : il lance le script ci-dessous, vérifie son résultat et livre le JSON.

**Comment.** Depuis la racine du dépôt :

```
python3 outils/projet_images.py
```

Le script ne remplace pas le travail de l'agent, il l'assemble sans erreur de copie. Il :
1. **refuse de produire quoi que ce soit** si une idée n'a pas fini les étapes 1 et 2 (il liste ce qui manque, idée par idée) : l'agent finit alors ces idées d'abord ;
2. **ne garde que les images absentes** de `ideaN/animation/etape2_assets/generes/` (une image est présente si un fichier a pour nom l'`id` de l'asset, quelle que soit l'extension : `.png`, `.webp`...). Les images déjà générées ne sont jamais redemandées ;
3. **refuse si une référence n'existe pas** dans le dépôt, ou si deux tâches ont le même `id` ;
4. écrit les fichiers ci-dessous.

**Fichiers produits**

```
generation_images/projet_images_global.json              toutes les idées, toutes les images restantes, un seul projet
ideaN/animation/etape2_assets/projet_images.json         le même projet, pour une seule idée (toujours écrit, même sans image restante)
```

`projet_images_global.json` est un projet `imgen` d'IngXAi. Chaque tâche porte ses propres champs, parce que chaque image doit partir dans le dossier de **son** idée :

```json
{
  "type": "imgen",
  "projet": "Toutes les idées : images des assets restantes",
  "depot_references": "officecenter632-maker/WorkspaceAnim",
  "branche_references": "main",
  "depot": "officecenter632-maker/WorkspaceAnim",
  "taches": [
    {
      "id": "idea2__pere_locataire",
      "titre": "...",
      "prompt": "<prompt de assets.json, inchangé>",
      "references": ["idea2/animation/etape2_assets/references/<fichier>"],
      "depend_de": [],
      "desactive": false,
      "dossier_depot": "idea2/animation/etape2_assets/generes",
      "nommage": "pere_locataire{ext}",
      "message_commit": "Idée 2 : image générée {nom}",
      "validation": "manuelle",
      "mode_prompt": "fichier",
      "consigne_prompt": ""
    }
  ]
}
```

- **`id`** : `ideaN__<id de l'asset>`, pour qu'il soit unique dans le projet. Les `depend_de` sont préfixés de la même façon.
- **`dossier_depot`, `nommage`, `message_commit` par tâche** : le fichier généré s'appelle `<id de l'asset>` + son vrai format (`{ext}`) et arrive dans `ideaN/animation/etape2_assets/generes/`, comme pour l'idée 1. L'étape 3 retrouve donc un asset par son `id` sans préfixe, **quelle que soit l'extension**.
- Les prompts et les références sont ceux de `assets.json`, **jamais réécrits** par le script.

**Si IngXAi ne lit pas `dossier_depot`, `nommage` et `message_commit` au niveau de la tâche**, le projet global enverrait toutes les images au même endroit : ne pas l'utiliser. Utiliser à la place les `projet_images.json` de chaque idée, un projet par idée : ils n'emploient que des champs au niveau du projet, déjà reconnus par IngXAi (c'est le format du projet de l'idée 1).

**Projet d'une seule idée** (`ideaN/animation/etape2_assets/projet_svg.json`). Ici il n'y a pas de `chemin_sauvegarde` par ligne : `nom` est l'`id` seul et `dossier_sortie` donne le dossier des SVG (le SVG est poussé dans `dossier_sortie/<nom>.svg`) :

```json
{
  "projet": "Idée 2 : SVG des assets",
  "depot_references": "officecenter632-maker/WorkspaceAnim",
  "branche_references": "main",
  "branche_sortie": "main",
  "dossier_sortie": "idea2/animation/etape2_assets/svg",
  "images": [
    { "nom": "pere_locataire", "source": "idea2/animation/etape2_assets/generes/pere_locataire.webp" }
  ]
}
```

**Écrire le JSON à la main** (si le script est indisponible, ou pour ajouter une seule ligne avec le bouton « + ») : reprendre exactement les champs ci-dessus.
- Projet global : chaque ligne a `nom` (`ideaN__<id>`), `source` (chemin réel, extension comprise) et `chemin_sauvegarde` (`ideaN/animation/etape2_assets/svg/<id>.svg`).
- Projet d'une idée : chaque ligne a `nom` (l'`id`) et `source` ; le dossier vient de `dossier_sortie`.
- Toujours `depot_references` et `branche_references` / `branche_sortie` = `main`, jamais de chemin local.
- Vérifier d'abord que le SVG n'existe pas déjà dans `svg/` (un SVG déjà fait n'est jamais redemandé) et que `nom` est unique.

**Fond uni à retirer (avant l'étape 3).** vectorizer.ai garde le fond uni de l'image : la première forme du SVG est un rectangle plein (vert proche de `#00FF00`, ou magenta pour `maison_a_louer`). Constaté sur 7 SVG sur 11 : `pere_locataire`, `enfants_locataires`, `mere_locataire`, `papiers`, `porte_avis`, `travailleur_bureau`, `maison_a_louer`. Les décors n'en ont pas. Ce rectangle doit être supprimé avant d'animer les personnages et les objets.

**Projets déjà créés.** Un projet sans `dossier_sortie` (ni `branche_sortie`) créé avant ce changement reste en mode PC. Il faut repartir d'un projet neuf, produit par `projet_svg.py`.

**Vérifications avant de livrer** (l'agent les fait, sans demander) :
- [ ] Le script s'est terminé sans erreur, et le total d'images affiché est égal à la somme des images manquantes de chaque idée.
- [ ] Les JSON sont valides, aucune image déjà présente dans `generes/` n'y figure.
- [ ] Le résultat est commité et poussé sur `main` (« Projet de génération des images : N images »).
- [ ] Le registre de chaque idée n'est pas modifié : cette section ne rouvre pas les passes de 2.10.

### 2.13 Vectoriser les images générées : le projet ImageVectorizer

**Quand.** Dès qu'il y a des images dans `ideaN/animation/etape2_assets/generes/`. On n'attend ni que toutes les images d'une idée soient générées, ni que toutes les idées aient fini : la vectorisation **part toujours de l'étape 2**, parce que les assets sont encore en préparation. Le script est incrémental, on le relance à chaque nouvelle série d'images. L'agent ne demande rien : il lance le script, vérifie son résultat et livre le JSON.

**Comment.** Depuis la racine du dépôt :

```
python3 outils/projet_svg.py
```

Le script assemble le projet sans erreur de copie. Il :
1. **ignore une idée** dont les étapes 1 et 2 ne sont pas finies (speech, `assets.json`, deux passes à `true`) et affiche pourquoi ; les autres idées sont traitées ;
2. **ne garde que les assets** non désactivés dont l'image **est déjà** dans `generes/` (un fichier a pour nom l'`id` de l'asset, quelle que soit l'extension) et dont le **SVG n'est pas déjà** dans `svg/`. Une image pas encore générée est comptée « pas encore générée » et sera prise au passage suivant ; un SVG déjà fait n'est jamais redemandé ;
3. si un même asset a deux fichiers (`decor_champ.png` et `decor_champ.webp`, par exemple après une régénération), **retient le plus récemment commité** et le signale ;
4. **refuse d'écrire quoi que ce soit** si un `id` n'est pas utilisable comme nom de fichier, si un nom est en double, ou si le fichier de l'image n'est pas une image (png, jpg, jpeg, webp, gif, bmp) ;
5. écrit les fichiers ci-dessous (et ne les écrit pas du tout s'il n'y a rien à vectoriser).

**Fichiers produits**

```
generation_svg/projet_svg_global.json                    toutes les idées, tous les SVG restants, un seul projet
ideaN/animation/etape2_assets/projet_svg.json            le même projet pour une seule idée (écrit seulement s'il a des lignes)
ideaN/animation/etape2_assets/svg/<id>.svg               les SVG, poussés par le bot (jamais écrits à la main)
```

`projet_svg_global.json` est le JSON à coller dans ImageVectorizer (bouton « + », nouveau projet) :

```json
{
  "projet": "Toutes les idées : SVG des assets",
  "depot_references": "officecenter632-maker/WorkspaceAnim",
  "branche_references": "main",
  "branche_sortie": "main",
  "images": [
    {
      "nom": "idea2__pere_locataire",
      "source": "idea2/animation/etape2_assets/generes/pere_locataire.webp",
      "chemin_sauvegarde": "idea2/animation/etape2_assets/svg/pere_locataire.svg"
    }
  ]
}
```

- **`nom`** : `ideaN__<id de l'asset>`, unique dans le projet. Dans `projet_svg.json` (une seule idée), `nom` est l'`id` seul et `dossier_sortie` donne le dossier des SVG (voir l'exemple ci-dessous).
- **`source`** : le chemin **réel** de l'image dans le dépôt, extension comprise (lue dans `generes/`, jamais déduite de l'`id`). C'est une référence git : ImageVectorizer refuse tout chemin local.
- **`chemin_sauvegarde`** : où le SVG est poussé dans le dépôt, toujours dans `svg/` de l'idée, sur la branche `main`.
- **Rien n'est écrit sur le PC.** Dès qu'un SVG est généré, le notebook `ImageVectorizer.py` (sAutoniax) le pousse sur `main` en un commit « SVG vectorisé : {nom} ». ImageVectorizer ne garde que l'état de chaque ligne (générée, en cours, échec) et un clic sur une ligne générée ouvre le SVG sur GitHub.

**Projet d'une seule idée** (`ideaN/animation/etape2_assets/projet_svg.json`). Ici il n'y a pas de `chemin_sauvegarde` par ligne : `nom` est l'`id` seul et `dossier_sortie` donne le dossier des SVG (le SVG est poussé dans `dossier_sortie/<nom>.svg`) :

```json
{
  "projet": "Idée 2 : SVG des assets",
  "depot_references": "officecenter632-maker/WorkspaceAnim",
  "branche_references": "main",
  "branche_sortie": "main",
  "dossier_sortie": "idea2/animation/etape2_assets/svg",
  "images": [
    { "nom": "pere_locataire", "source": "idea2/animation/etape2_assets/generes/pere_locataire.webp" }
  ]
}
```

**Écrire le JSON à la main** (si le script est indisponible, ou pour ajouter une seule ligne avec le bouton « + ») : reprendre exactement les champs ci-dessus.
- Projet global : chaque ligne a `nom` (`ideaN__<id>`), `source` (chemin réel, extension comprise) et `chemin_sauvegarde` (`ideaN/animation/etape2_assets/svg/<id>.svg`).
- Projet d'une idée : chaque ligne a `nom` (l'`id`) et `source` ; le dossier vient de `dossier_sortie`.
- Toujours `depot_references` et `branche_references` / `branche_sortie` = `main`, jamais de chemin local.
- Vérifier d'abord que le SVG n'existe pas déjà dans `svg/` (un SVG déjà fait n'est jamais redemandé) et que `nom` est unique.

**Fond uni à retirer (avant l'étape 3).** vectorizer.ai garde le fond uni de l'image : la première forme du SVG est un rectangle plein (vert proche de `#00FF00`, ou magenta pour `maison_a_louer`). Constaté sur 7 SVG sur 11 : `pere_locataire`, `enfants_locataires`, `mere_locataire`, `papiers`, `porte_avis`, `travailleur_bureau`, `maison_a_louer`. Les décors n'en ont pas. Ce rectangle doit être supprimé avant d'animer les personnages et les objets.

**Projets déjà créés.** Un projet sans `dossier_sortie` (ni `branche_sortie`) créé avant ce changement reste en mode PC. Il faut repartir d'un projet neuf, produit par `projet_svg.py`.

**Vérifications avant de livrer** (l'agent les fait, sans demander) :
- [ ] Le script s'est terminé sans erreur, et le total affiché est égal à la somme des SVG à générer de chaque idée.
- [ ] Les JSON sont valides, et aucune ligne ne correspond à un SVG déjà présent dans `svg/`.
- [ ] Le résultat est commité et poussé sur `main` (« Projet de vectorisation : N SVG »).
- [ ] Le registre de chaque idée n'est pas modifié : cette section ne rouvre pas les passes de 2.10.

---

## Étape 3 : l'animation

L'animation est une page HTML qui **appelle des fichiers par leur chemin**. Elle ne contient jamais le code SVG brut : seulement des chemins (`<img src="...">`) et la logique d'animation. Pas de serveur, pas de `fetch()` : la page s'ouvre par double-clic. Tout ce qui sert à l'animation est rangé dans un dossier dédié, séparé de l'étape 2 :

```
ideaN/animation/etape3_animation/
  assets/<asset>/<piece>.svg     un fichier par pièce détourée (personnages, objets articulés)
  decors/<id>.svg                décors et objets non articulés, un fichier chacun
  pivots.json                    point d'articulation de chaque pièce
  index_assets.json              chemin de chaque pièce et de chaque décor, état (fait / à faire)
```

### 3.1 Détourer les assets (première étape de l'animation)

**Rien n'est animé avant que tous les assets de l'idée soient détourés.** Le détourage part des SVG de `etape2_assets/svg/` et de `pieces.json`.

1. **Retirer le fond uni** (rectangle plein vert ou magenta, voir 2.13).
2. **Détourer chaque élément** : un personnage ou un objet articulé est découpé en une pièce par entrée de `pieces.json`, **un fichier SVG par pièce**. Toutes les pièces d'un même asset gardent le **même cadre (`viewBox`)** que le SVG d'origine : empilées, elles se remettent exactement en place. Un décor, ou un objet sans pièces, reste un seul fichier.
3. **Écrire le pivot** de chaque pièce dans `pivots.json` (l'articulation notée dans `pieces.json`).
4. **Ranger** chaque fichier à son chemin ci-dessus et **le déclarer** dans `index_assets.json`.

**Progressif.** Comme la vectorisation (2.13), le détourage est incrémental : il traite les assets dont le SVG existe et qui ne sont pas encore détourés, puis **pousse chaque asset sur `main` dès qu'il est fini** (un commit par asset, « Détourage : {asset} »), sans attendre les autres. Un asset déjà détouré n'est jamais refait, sauf si son SVG d'étape 2 a changé. **Règle de crédit : on ne regroupe jamais les pushs.** Chaque asset est poussé **dès qu'il passe ses vérifications**, avant de commencer le suivant, pour que rien ne soit perdu si la session s'arrête (crédits épuisés, coupure) : ce qui est déjà détouré est déjà sur `main`.

**L'agent détoure lui-même, et c'est lui qui nomme.** L'utilisateur n'intervient pas : l'agent décide quelle forme appartient à quelle pièce, nomme chaque fichier, vérifie, pousse. Il ne demande rien.

**Comment l'agent détoure un asset.** Le SVG de vectorizer.ai est une liste de formes (`<path>`) à plat, sans groupes ni noms : il n'y a rien à « retrouver », tout est à décider.
1. **Regarder** l'image d'origine (`generes/<asset>.png`) et le SVG rendu, pour voir où est chaque pièce.
2. **Inventorier les formes** du SVG (script) : numéro, couleur, trait ou remplissage, boîte englobante. L'agent lit cet inventaire, **jamais le SVG brut** (trop long).
3. **Attribuer chaque forme à une seule pièce** de `pieces.json`, d'après sa position, sa couleur et ce qu'elle représente (zone de la tête, de la manche, de la main…). Aucune forme ne reste sans pièce, aucune n'est dans deux pièces. Une forme qui ne correspond à rien (ombre, liseré) va à la pièce la plus proche, et l'agent le note. Le résultat est écrit dans `attribution.json` (numéro de forme → id de pièce).
4. **Générer les fichiers par script** à partir de `attribution.json` : un SVG par pièce, même `viewBox`, avec un groupe racine `<g id="<id de la pièce>">`. Le fichier porte le nom de la pièce (`pere_bras_g_haut.svg`). L'agent n'écrit jamais un SVG à la main.
5. **Contrôler en images** : un rendu où chaque pièce a une couleur vive distincte, et un rendu des pièces empilées comparé à l'original. L'agent regarde les deux. Si une forme est mal attribuée, il corrige `attribution.json` et regénère. Il ne pousse que quand l'empilement redonne l'original.
6. **Articulations.** Là où deux pièces se rejoignent (épaule, coude, cou, taille), la pièce qui tourne ne doit pas laisser de vide visible. Si la coupe en laisse un, l'agent ajoute un recouvrement de la même couleur (une petite forme à l'extrémité de la pièce) et le note. Les parties cachées derrière une autre pièce n'existent pas dans l'image : on ne les invente pas. **Contrôler l'épaule en particulier** : si le torse détouré garde un bout de manche (ou si la manche est coupée entre le torse et le haut du bras), ce bout reste visible quand le bras pivote. On l'attribue alors au haut du bras, pas au torse ; si l'image ne le permet pas, la pièce est à regénérer avec un torse sans manches (2.4, point 6).
7. **Pivots.** L'agent place le pivot de chaque pièce (à l'articulation décrite dans `pieces.json`) dans `pivots.json`, en coordonnées du `viewBox`.

**Fichiers de détourage d'un asset**

```
ideaN/animation/etape3_animation/
  assets/<asset>/<piece>.svg          une pièce par fichier
  assets/<asset>/attribution.json     forme → pièce (sert à refaire le détourage sans tout relire)
  decors/<id>.svg                     décor, sans découpe
```

**Vérifications avant de pousser un asset** (l'agent les fait, sans demander)
- [ ] Le fond uni a disparu.
- [ ] Chaque forme du SVG est dans une seule pièce (rien d'oublié, rien en double), et toutes les pièces de `pieces.json` ont leur fichier, déclaré dans `index_assets.json`.
- [ ] Le rendu des pièces empilées reproduit l'image d'origine.
- [ ] Aucun vide visible aux articulations quand on pense à la rotation (recouvrements notés).
- [ ] Le commit est poussé sur `main` (« Détourage : {asset} »).

### 3.1 bis Assets à une seule pièce (décors, objets)

`python3 outils/detourer.py ideaN <asset> --entier` : un décor ou un objet sans pièces est copié dans `decors/<id>.svg` (ou `assets/<asset>/<asset>.svg`). Le script retire le fond uni quand il existe, y compris les petits morceaux de fond tracés comme formes séparées (même couleur exacte que le fond).

### 3.2 Monter les personnages

Beaucoup d'images sont des **planches** : les pièces d'un personnage sont déjà séparées et loin les unes des autres (mère, travailleur de bureau). Avant d'animer, l'agent écrit un `montage.json` par asset : pour chaque pièce, le décalage `{dx, dy}` (en coordonnées du `viewBox`) qui la remet à sa place dans le personnage assemblé. Il vérifie en ouvrant l'assemblage. Les pivots de `pivots.json` sont donnés dans les coordonnées de la planche : le moteur les décale avec la pièce.

**Fichiers du montage.** `assets/<asset>/montage.json` (décalages `{dx, dy}` par pièce). Contrôle visuel obligatoire : on regarde l'assemblage et on corrige les **vides** (cou, taille, coudes, épaules) en décalant la pièce, jamais en redessinant. Comme la page ne peut pas lire de JSON en double-clic, `python3 outils/generer_donnees.py ideaN` regroupe `index_assets.json`, `pivots.json` et les `montage.json` dans `etape3_animation/donnees.js` : **à relancer après chaque modification de ces fichiers.**

### 3.3 L'animation : une page HTML vectorielle

**Le livrable est la page HTML animée, en vectoriel. Aucun rendu vidéo (pas de MP4, pas d'enregistrement), aucun audio à cette étape.** L'agent ne produit pas de vidéo.

```
ideaN/animation/etape3_animation/
  index.html            la page : une scène de 1672 x 941 mise à l'échelle de la fenêtre, avec lecture / pause / curseur de temps
  moteur/               le code commun (horloge, chargement des pièces, gestes, éléments en code), sans bibliothèque externe
  scenes/beat1.js ...   un fichier par beat : ce qui est placé, quand, et les gestes
```

- **Que des chemins.** Chaque pièce est une balise `<img src="assets/...svg">`. Aucun SVG brut dans la page, aucun serveur, aucune bibliothèque téléchargée : la page s'ouvre par double-clic.
- **Une seule horloge**, en secondes, calée sur les instants du speech (`speech_adapte.md`). Chaque scène lit cette horloge.
- **Les données viennent de l'étape 2** : placements par beat (`Liste_assets.md`, « Mise en place par beat »), gestes (`pieces.json`), éléments en code (`elements_code.json`). L'agent n'invente ni position ni geste qui y figure déjà. Les durées des gestes, que l'étape 2 ne fixe pas, sont calculées à partir des instants des mots.
- **Un beat à la fois, poussé dès qu'il fonctionne** (« Animation : beat N »). On ouvre la page, on regarde, on passe au suivant.
- **Éléments en code** (cartes, compteurs, flèches, étiquettes) : dessinés en HTML/CSS ou SVG dans le moteur, jamais en images.

**État du moteur (idée 1, beat 1 fait).** `moteur/moteur.js` (horloge, échelle de la scène, lecture / pause / curseur, flèches ← → pour avancer de 0,1 s), `moteur/personnage.js` (personnage articulé : jambes, haut du corps autour de la taille, bras haut > bras bas imbriqués, tête ; respiration, poids, balancement des bras ; `creerBloc` pour une image entière), `moteur/elements.js` (compteur, pictogrammes). Tout est fonction du temps `t` : on peut glisser le curseur n'importe où. La sortie des éléments en code se fait à l'instant du changement de beat : la scène du beat 1 dure donc 5,7 s (5,3 + 0,4). Les pictogrammes de `icones_menages` : 7 maisons dont 4 rouges (choix de l'agent, l'étape 2 ne précise pas le nombre).

**Deux versions de la page : l'agent travaille sur l'une, l'utilisateur regarde l'autre.**
- **Version de travail** : `etape3_animation/index.html`, qui n'appelle que des chemins (aucun SVG brut). C'est la seule que l'agent lit, modifie et commite. Elle reste légère en jetons.
- **Version à regarder** : une page unique avec scripts et SVG embarqués en base64, faite pour que l'utilisateur voie l'animation et dise les modifications à faire. Elle se fabrique par script : `python3 outils/embarquer.py ideaN <fichier_sortie.html>`. L'agent écrit le fichier **hors du dépôt** (dossier temporaire de la session), le **publie en artifact** pour que l'utilisateur la regarde, **ne la lit jamais** (elle est longue : la relire coûterait des jetons pour rien) et **ne la commite pas**. Seuls les assets cités par les scènes y sont embarqués.
- **Quand la fabriquer** : à la fin de chaque beat qui fonctionne (en même temps que le push « Animation : beat N »), et chaque fois que l'utilisateur demande à voir. Après une modification demandée, on corrige la version de travail, on relance `generer_donnees.py` si besoin, puis on regénère et on republie la version à regarder (même artifact).

### 3.4 et suivantes : à définir

Voix, enchaînement des beats, transitions.

---

## Étapes suivantes

- Génération des images : quand toutes les idées ont fini l'étape 2, `python3 outils/projet_images.py` produit le projet de génération (2.12).
- Vectorisation : dès que des images sont dans `generes/`, `python3 outils/projet_svg.py` produit le projet ImageVectorizer des SVG (2.13), toujours à partir de l'étape 2.
- Étape 3 (détourage 3.1) : commence quand `registre_verification.json` a ses deux passes à `true` et que les SVG de l'idée sont dans `svg/`.
