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

**But :** à partir du speech et des frames des candidats, obtenir la liste des images à générer (les assets), chacune avec son image de référence, son fond (ou l'absence de fond) et son **prompt complet**. Tout ce qui doit bouger est généré **en pièces détachées**, pour que l'animation en code soit fluide. Aucune validation humaine : l'agent fait tout et livre les fichiers.

**Principes**
- **Les assets sont des images fixes.** Il n'y a ni GIF ni vidéo. Le mouvement est fait en code à l'étape suivante, en déplaçant et en faisant pivoter des pièces.
- **Ce qui bouge est généré en pièces détachées**, dans une seule image par élément (un personnage, une porte, un ventilateur, une balance…). On ne génère ni planches de poses ni élément entier à plusieurs poses : la pose se calcule en code.
- **Rien d'inventé.** Un asset existe seulement si un beat du speech en a besoin et s'il correspond à un élément visible dans les frames d'un candidat retenu. On n'emprunte rien à un candidat non retenu.
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
4. **Donner les données exactes** de `speech_adapte.md` (chiffres, unités, étiquettes), **sans en ajouter** : un chiffre qui est dans `recherches.md` mais pas dans le speech n'est pas affiché. Les textes affichés (titres, étiquettes) sont écrits en toutes lettres dans la fiche.
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
1. **Découper selon les mouvements voulus, pas plus.** Mais un mouvement qui **plie** un membre (croiser les bras, se prendre la tête, taper au clavier, se gratter) exige **deux segments** (bras et avant-bras, avec la main) : un bras en un seul bloc ne sait que pivoter droit. Un personnage qui ne fait que lever le bras n'a pas besoin de jambes en deux segments. Exemple complet : tête, torse, bassin, bras en deux segments, mains, jambes en deux segments, pieds. Ajouter des variantes (bouche ouverte, yeux fermés…) seulement si les beats les demandent.
2. **Pour chaque pièce, noter** : son id, sa **pièce parent** (l'avant-bras a pour parent le haut du bras) et son **articulation** (le coude, l'épaule…). Les coordonnées exactes du pivot sont mesurées à l'étape 3, après découpage.
3. **Une seule génération par asset**, qui contient toutes ses pièces. **Un personnage = un asset** : un groupe (une famille, une équipe) est découpé par personnage, une génération chacun, et les personnages qui ne bougent pas par membre (des enfants immobiles) sont regroupés entiers dans une même image. **Maximum 10 pièces par génération** : au-delà, les modèles d'image mélangent ou oublient des pièces. Elles sont **séparées les unes des autres** dans l'image, **à la même échelle**, vues dans une **pose neutre** (debout, bras écartés, pièces posées à plat), avec un **même style et un même fond**.
4. **Chaque pièce dépasse un peu sur l'articulation suivante** (le haut du bras se prolonge sous l'épaule, l'avant-bras sous le coude), pour qu'aucun trou n'apparaisse quand la pièce pivote. Les pièces restent séparées dans l'image, mais chacune porte sa partie de recouvrement.
5. **Les petits éléments qui ne bougent pas** (petits objets, icônes) sont regroupés dans une même image de 4 à 6 éléments, séparés, avec une référence par élément et un fond commun.

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

### 2.6 Choisir l'image de référence et le fond

- **Référence** : parmi les frames du candidat concerné, celle où l'élément est le plus entier, le plus net et le moins caché. Si aucune frame ne montre l'élément, prendre la frame du même candidat la plus proche par sa nature (décor, objet, matière) comme **référence de style**. Il y a toujours une référence.
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
7. **les pièces**, quand l'asset est décomposé : la liste exacte des pièces, leur séparation (aucune pièce ne touche une autre), la même échelle, et le recouvrement aux articulations (2.4, point 4) ;
8. **les interdits** : ne pas reprendre le logo de la chaîne, les badges, les bandeaux ni le texte de la référence ; aucun logo réel ; aucune ressemblance avec une personne réelle ; **aucun texte, lettre ni chiffre dans l'image** (les modèles d'image les orthographient mal) : les panneaux, documents et étiquettes sont dessinés **vides** (panneau blanc, bande unie, lignes grises) et leur texte est ajouté en code, noté dans les fiches de 2.2 bis. Les objets qui doivent être reconnus sans texte (un avis d'expulsion, une fiche de paie) se distinguent par la forme et la couleur (bande rouge ou bleue, sceau, pièce).

### 2.8 Produire les fichiers de sortie

Dans `ideaN/animation/etape2_assets/` :

```
etape2_assets/
  assets.json          les générations, au format du projet imgen d'IngXAi
  Liste_assets.md      la liste en tableau lisible, un récapitulatif par beat (décor, assets, éléments en code), les fiches des éléments en code, les décisions
  pieces.json          pour chaque asset décomposé : pièces, parents, articulations, mouvements
  references/          les frames de référence choisies, copiées (png, jpg ou webp)
  references_code/    les frames qui servent de référence de style pour les éléments faits en code
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

`pieces.json` donne, pour chaque asset décomposé, la liste des pièces :

```json
{
  "<id de l'asset>": {
    "fond": "#00FF00",
    "mouvements": ["lève le bras droit", "hoche la tête"],
    "pieces": [
      {"id": "torse", "parent": null, "articulation": null},
      {"id": "bras_droit_haut", "parent": "torse", "articulation": "épaule droite"},
      {"id": "bras_droit_bas", "parent": "bras_droit_haut", "articulation": "coude droit"}
    ]
  }
}
```

Une tâche d'`assets.json` = une génération (un asset avec toutes ses pièces, ou une image de petits éléments). Chaque tâche a au moins une référence. Les images générées prennent le nom de l'`id`. Les chemins sont relatifs au dépôt ; ils sont remplacés par les chemins absolus au moment d'utiliser le projet dans IngXAi.

### 2.9 Vérifications avant de passer à l'étape 3

- [ ] Toutes les frames citées ont été regardées.
- [ ] Chaque asset renvoie à au moins un beat et à un élément d'une frame d'un candidat retenu.
- [ ] Chaque objet, personnage ou décor visible dans les beats est dans la liste, dans une image de petits éléments ou dans « Éléments faits en code ».
- [ ] Aucun asset n'est un texte, un badge, un logo ou une forme géométrique.
- [ ] Aucun GIF ni animation n'est demandé dans les prompts : images fixes uniquement.
- [ ] Chaque asset à parties mobiles est décomposé en pièces, avec parent et articulation pour chaque pièce, et seulement les pièces utiles aux mouvements des beats.
- [ ] Les prompts de pièces demandent des pièces séparées, à la même échelle, avec recouvrement aux articulations.
- [ ] Chaque génération a un « détourage » oui ou non. S'il est oui, le prompt donne une couleur de fond en hexadécimal, identique pour toutes les pièces d'un élément, qui n'apparaît pas dans l'asset. S'il est non, le prompt ne mentionne aucune couleur de fond.
- [ ] Le JSON est valide, les `id` sont uniques et valides, chaque tâche a au moins une référence existante.
- [ ] Chaque prompt contient les interdits (logo, badges, bandeaux, texte).
- [ ] **Récapitulatif par beat** : chaque beat a un décor (ou un fond uni noté), ses assets, ses éléments en code et ses données. Aucun beat sans fond ; aucun asset ou élément absent du récapitulatif.
- [ ] **Chaque donnée affichée est dans `speech_adapte.md`** (pas seulement dans `recherches.md`).
- [ ] Aucun prompt ne contient de texte à écrire dans l'image ; les textes sont dans les fiches.
- [ ] Les hex des prompts sont mesurés sur la frame ; la couleur de fond est choisie sur ces mesures (2.6).
- [ ] Aucune contradiction dans un prompt (assis/debout, entier/partiel, avec/sans fond) ; au plus 10 pièces par génération ; les mouvements qui plient un membre ont deux segments.
- [ ] Les références identiques (même frame pour plusieurs assets) sont voulues ; une génération n'a pas deux fois la même référence.
- [ ] Chaque élément fait en code a une fiche complète (type, données, référence de style, style repris, animation, emplacement).
- [ ] Chaque référence de style est une frame réellement regardée, copiée dans `references_code/`, avec son niveau (1 à 3). Un style décidé par l'agent (niveau 4) n'est accepté que si les niveaux 1 à 3 ont été cherchés et sont cités dans la fiche.
- [ ] Les couleurs et formes des fiches viennent des frames, pas d'une invention ; les chiffres viennent du speech.
- [ ] Le style des éléments en code est cohérent avec celui des assets générés (mêmes aplats, mêmes couleurs).

### 2.10 Pièges à anticiper (erreurs de dernière minute)

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
11. **Les chemins relatifs** du JSON à remplacer par des chemins absolus dans IngXAi ; les références doivent exister.
12. **Aucun format** précisé : l'image sort carrée ; toujours écrire le format.

---

## Étapes suivantes (à définir)

- Étape 3 :
- Étape 4 :
