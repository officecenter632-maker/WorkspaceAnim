# Idée 1 : liste des assets (étape 2, revérifiée)

Candidats utilisés pour les références d'assets : **10** (frames 0,5–32 s) et **05** (953–1022 s). Les candidats **04 et 09 ne montrent qu'un carton de texte** : aucun asset à reprendre. Images fixes uniquement : le mouvement se fait en code. Prompts complets dans `assets.json`, pièces dans `pieces.json`, frames de référence dans `references/` (assets) et `references_code/` (style des infographies).

## Assets à générer (11 générations)
| id | Beats | Remplace (frame de référence) | Nature | Mouvements / pièces | Référence | Détourage / fond |
|---|---|---|---|---|---|---|
| decor_maison_rose | 1, 2 | façade rose du candidat 10, sans personnages, **plan large** | STRUCTUREL | aucun | c10 · t009000 (plan large, même échelle que les personnages en pied) | non : plein cadre 16:9 |
| pere_locataire | 1, 2 | le père (barbe, chemise crème) | STRUCTUREL | se prend la tête, lève les bras. **7 pièces** | c10 · t006500 (visage, vêtements) + t009000 (jambes, chaussures) | oui : #00FF00 |
| mere_locataire | 1, 2 | la mère (haut violet, jean teal) | STRUCTUREL | hoche la tête, croise les bras. **7 pièces** (bras en 2 segments) | c10 · t006500 + t009000 | oui : #00FF00 |
| enfants_locataires | 1, 2 | le garçon et la fille | STRUCTUREL | aucun par membre : 2 images entières (à séparer à l'étape 3) | c10 · t006500 + t009000 | oui : #00FF00 |
| decor_champ | 3 | campagne et collines du candidat 05, sans maison | STRUCTUREL | aucun | c05 · t000960500 | non : plein cadre 16:9 |
| maison_a_louer | 3, 5 | maison, pins et panneau (vide) du candidat 05 | STRUCTUREL | image unique | c05 · t000960500 | oui : #FF00FF (sapins verts) |
| decor_bureau | 3 | la pièce de bureau (mur brique, rideaux, sol rayé ; **sans fauteuil**, la chaise est une pièce du travailleur) du candidat 05 | STRUCTUREL | aucun | c05 · t001016500 (panneau de droite) | non : plein cadre 16:9 |
| travailleur_bureau | 3 | le salarié casqué du candidat 05 | STRUCTUREL | tape au clavier, tourne la tête. **10 pièces** (dont ordinateur, chaise, bureau) | c05 · t001016500 | oui : #00FF00 |
| decor_quartier | 4, 5 | décor bleu et vert de la scène « bombe », sans bombe | STRUCTUREL | aucun | c10 · t000028500 | non : plein cadre 16:9 |
| porte_avis | 4 | la porte d'entrée de la scène « bombe » | THÉMATIQUE | le battant pivote sur la charnière. 2 pièces | c10 · t000028500 | oui : #00FF00 (porte brune) |
| papiers | 4, 5 | le document « LOAN » du candidat 10 | THÉMATIQUE | 2 images fixes sans texte, **à séparer à l'étape 3** : avis d'expulsion (bande rouge, sceau rouge), fiche de paie (bande bleue, pièce dorée) | c10 · t000019000 | oui : #00FF00 |

**Choix du fond de la famille (mesuré sur le plan large t009000)** : haut de la mère #8A2478 (violet-magenta, teinte ≈ 310°), jean #23868F (teal saturé, ≈ 186°), robe de la fille #546CDE (bleu, ≈ 228°), short du garçon #101830 (bleu marine très sombre), chaussures orange #E08818 et jaunes #C8A820. Le magenta aurait mangé le haut de la mère (10° d'écart), le bleu la robe (12°). Le vert (120°) reste à au moins 65° de toutes ces teintes : c'est le plus éloigné, mais **le jean teal n'est qu'à 66°** : risque d'un bord vert sur le jean (à regarder après le détourage ; le bleu et le magenta sont pires pour la mère, donc on règle la tolérance du détourage plutôt que de changer de fond). Même fond pour les trois générations.

## Récapitulatif par beat
| Beat | Temps (s) | Décor | Assets | Éléments en code (fiches plus bas) |
|---|---|---|---|---|
| 1 | 0,0–5,3 | decor_maison_rose | pere_locataire, mere_locataire, enfants_locataires | compteur_menages, icones_menages |
| 2 | 5,3–10,0 | decor_maison_rose (pas assombri : la carte blanche du donut suffit) | mêmes personnages | carte_donut, etiquette_record |
| 3 | 10,0–16,0 | deux panneaux comme le candidat 05 : decor_champ (gauche), decor_bureau (droite) | maison_a_louer (gauche), travailleur_bureau (droite) | carte_date_2001, cercle_loyers, etiquette_revenus, texte du panneau « FOR RENT » |
| 4 | 16,0–26,1 | decor_quartier | porte_avis, papiers (avis d'expulsion posé sur la porte), **famille (mêmes assets qu'au beat 1, aucune génération de plus)** | compteur_dossiers, etiquette_austin, etiquette_source, texte_avis |
| 5 | 26,1–28,7 | decor_quartier | papiers (fiche de paie), maison_a_louer | escalier_ascenseur, etiquette_paies, etiquette_logement, texte_avis (« PAYCHECK ») |

## Fiches des éléments faits en code (aucun prompt)
Niveau = niveau de recherche de la référence de style (2.2 bis). Frames dans `references_code/`. Toutes les données viennent de `speech_adapte.md`.

**Style commun** (relevé sur les frames) : cartes blanches `#F9FCF8` à coins arrondis, texte `#282828` gras en capitales, très légère ombre ; rouge d'alerte `#F80000` (cercle, flèches, pictos) ; jaune-orangé `#F8A000` (icône de calendrier) ; donut bleu `#005090` / rouge `#B8322E` ; mêmes aplats que les assets. Pas de logo, pas de badge de la chaîne des frames.

| élément | beat | type | données (texte exact) | référence de style | style repris | animation | emplacement |
|---|---|---|---|---|---|---|---|
| compteur_menages | 1 | compteur (carte blanche) | « 12.1 MILLION » + « RENTER HOUSEHOLDS » + « MORE THAN HALF OF INCOME ON RENT » (le speech dit « more than half », pas « 50% ») | N1 · c05 · t000988000 (pilules de prix) | carte `#F9FCF8`, chiffre grand `#282828`, coins arrondis | la carte glisse depuis la gauche, le nombre compte de 0 à 12.1 | haut gauche |
| icones_menages | 1 | rangée de pictogrammes maison | aucune donnée chiffrée | N1 · c05 · t000966000 (icône de calendrier plate) | pictos plats `#F8A000`, un sur deux en `#F80000` | apparition en cascade | **haut droite** (le bas est pris par la famille en pied) |
| carte_donut | 2 | donut dans une carte blanche | « NEARLY HALF » au centre (le speech dit « nearly half » ; la part rouge est dessinée à 49 % d'après `recherches.md`, le chiffre n'est pas écrit) ; titre « PAST THE 30% LINE » | N2 · c02 · t000136500 (donut) | anneau bleu `#005090`, part rouge `#B8322E` ; carte blanche `#F9FCF8`, texte `#282828` (le fond blanc remplace le fond sombre du c02 pour ne pas assombrir la famille) | la part rouge se dessine, « NEARLY HALF » s'affiche, le titre apparaît lettre par lettre | **droite** (la carte ne couvre aucun visage) |
| etiquette_record | 2 | étiquette à flèche | « RECORD » | N1 · c05 · t001019500 (« 26% WAGES ») | carte blanche, flèche montante `#F80000`, texte `#282828` | glisse après le donut | droite, sous la carte |
| carte_date_2001 | 3 | carte DATE | « DATE: / SINCE 2001 » | N1 · c05 · t000966000 | carte blanche, icône calendrier `#F8A000`, « DATE: » petit, texte grand | glisse depuis la gauche | haut gauche du panneau maison |
| cercle_loyers | 3 | cercle rouge + flèche en zigzag | « RENTS » dans le cercle, « 30% » sur la flèche | N1 · c05 · t000966000 (« HOUSING COST INCREASE », 31%) | cercle `#F80000`, texte blanc gras, flèche en zigzag `#F80000` | le cercle apparaît, la flèche se dessine de bas en haut | sur la maison |
| etiquette_revenus | 3 | étiquette à flèche courte | « RENTER INCOMES » puis « 9% » (le nombre arrive avec le mot « 9 ») | N1 · c05 · t001019500 (« 26% WAGES ») | carte blanche, flèche `#F80000` plus courte que celle des loyers | entre après la flèche des loyers | bas gauche du panneau bureau |
| texte_panneau | 3 | texte sur panneau (**texte d'accessoire, pas une donnée** : « rent » est dans le speech ; affiché au beat 3 seulement, pas au beat 5 où la maison est trop petite pour qu'il soit lisible) | « FOR RENT » | N1 · c05 · t000960500 (panneau) | capitales blanches sur le panneau vide de maison_a_louer | apparaît avec la maison | sur le panneau |
| compteur_dossiers | 4 | compteur (carte blanche) | « 1.23 MILLION » + « EVICTION CASES » | N1 · c05 · t000988000 | idem compteur_menages | compte de 0 à 1.23 | haut gauche |
| etiquette_austin | 4 | étiquette | « AUSTIN: 30% ABOVE NORMAL » | N1 · c05 · t001019500 | idem etiquette_revenus | apparaît à « Around Austin » | **haut droite** (le bas droit cacherait les jambes de la mère) |
| etiquette_source | 4 | petite étiquette | « PRINCETON EVICTION LAB » | N1 · c05 · t001019500 | carte blanche, texte plus petit | apparaît avec le compteur | sous le compteur |
| texte_avis | 4, 5 | texte sur objets | « EVICTION NOTICE » (bande rouge), « PAYCHECK » (bande bleue) | N1 · c10 · t000019000 (titre du document) | capitales `#282828` ou blanches sur la bande | apparaît avec l'objet ; « EVICTION NOTICE » suit l'avis (parent : battant de porte_avis) | sur la bande |
| escalier_ascenseur | 5 | formes géométriques (pas de texte) | marches à gauche, cage d'ascenseur à droite | **N4** : aucune référence trouvée (N1 : c10, c05, c04, c09 ; N2 : c01, c02, c03, c06, c07, c08 ; N3 : transcriptions des idées 1 à 6, aucune mention d'escalier ni d'ascenseur ; recherche par texte, pas par image) | aplats `#314074` et `#C84E2E` (camembert du c07), blanc, sans ombre, formes simples | la fiche de paie monte les marches lentement, la maison monte dans la cage vite | centre, sur decor_quartier |
| etiquette_paies | 5 | étiquette | « PAYCHECKS » | N1 · c05 · t001019500 | idem etiquette_revenus | apparaît à « Paychecks » | à côté de l'escalier |
| etiquette_logement | 5 | étiquette | « HOUSING » | N1 · c05 · t001019500 | idem | apparaît à « Housing » | à côté de l'ascenseur |

**Animation de chaque asset : voir le bloc `animation` de `pieces.json`** (entrée, vie continue, mouvements décrits, sortie). **Les durées ne sont écrites nulle part : l'animateur les calcule** ; les instants ci-dessous sont les mots-clés du speech auxquels les gestes se déclenchent.

## Mise en place par beat (2.5 bis)
Mesures faites sur les frames (grille de 10 %), précision ±5 %. x et y en % de l'écran ; la **taille** est la hauteur en % de l'écran ; **couche** : 0 fond, puis 1, 2, 3 vers l'avant, 5 éléments en code. Instants = début du beat + rang du mot × durée par mot (durée du beat ÷ nombre de mots). **Taille minimale d'un texte : 2,5 % de la hauteur de l'écran** (27 px en 1080). Zones libres : quand les personnages sont en pied, **les 20 % du haut** sont réservés aux éléments en code.

### Beat 1 · 0,0–5,3 s · 16 mots · 0,331 s par mot
| quoi | instant (s) | x, y | taille | couche | note |
|---|---|---|---|---|---|
| decor_maison_rose | 0,0 | plein cadre | 100 % | 0 | poussée de caméra lente du **groupe** décor + personnages (voir `pieces.json`) |
| pere_locataire | 0,0 | x 26 %, pieds à y 99 % | 78 % | 1 | ses mouvements au beat 2 |
| mere_locataire | 0,0 | x 54 %, pieds à y 97 % | 72 % | 1 | |
| enfants_locataires (garçon / fille) | 0,0 | garçon x 60 %, fille x 66 %, pieds à y 100 % | 53 % / 56 % | 2 | devant la mère |
| compteur_menages | 0,66 (« 12.1 ») ; 3e ligne à 2,65 (« more than half ») | haut gauche : x 3–33 %, y 4–19 % | carte 15 % | 5 | compte de 0 à 12.1 |
| icones_menages | 1,99 (« households ») | haut droite : x 55–97 %, y 4–16 % | 12 % | 5 | 7 pictos en cascade |

### Beat 2 · 5,3–10,0 s · 14 mots · 0,336 s par mot
Sortie du beat 1 : compteur et icônes s'effacent à 5,3 (0,2 s).
| quoi | instant (s) | x, y | taille | couche | note |
|---|---|---|---|---|---|
| carte_donut | 5,3 (« nearly half ») ; titre à 8,33 (« thirty percent ») | x 71–98 %, y 10–56 % | carte 46 % | 5 | la fille est à x ≤ 70 % : aucun visage couvert |
| etiquette_record | 9,67 (« record ») | x 72–97 %, y 62–72 % | 10 % | 5 | |
| père : se prend la tête | 7,3 (« stretched ») | | | | pièces : bras_g_haut, bras_g_bas |
| mère : hoche la tête, croise les bras | 6,0 puis 8,3 | | | | bras en deux segments |
| père : lève les bras | 9,67 (« record ») | | | | |

### Beat 3 · 10,0–16,0 s · 18 mots · 0,333 s par mot
**Cadrage** : deux panneaux de 50 % de large (gauche = maison, droite = bureau), séparés par un trait blanc de 0,4 %. Chaque panneau ne montre que la moitié centrale de son décor (**x de 25 % à 75 % de l'image**) : decor_champ et decor_bureau sont donc générés avec le centre calme et les éléments décoratifs sur les côtés (voir leurs prompts). Transition d'entrée : **T2_3**.
| quoi | instant (s) | x, y (écran) | taille | couche | note |
|---|---|---|---|---|---|
| decor_champ (panneau gauche) / decor_bureau (panneau droit) | 10,0 | x 0–50 % / 50–100 % | 100 % | 0 | |
| maison_a_louer | 10,0 | x 27 %, bas à y 72 % | 50 % | 1 | le panneau « FOR RENT » (code) suit la maison |
| travailleur_bureau | 10,0 | x 74 %, bas à y 92 % | 62 % | 1 à 4 (ordre dans `pieces.json`) | tape au clavier dès 10,0 |
| carte_date_2001 | 12,0 (« 2001 ») | x 0–21 %, y 6–19 % | 13 % | 5 | |
| cercle_loyers | 13,0 (« rents ») | centre x 12 %, y 58 % ; diamètre 16 % de la largeur | 28 % | 5 | |
| flèche « 30% » | 14,0 (« 30 ») | de (19 %, 50 %) à (36 %, 24 %) ; « 30% » x 26–34 %, y 28–34 % | | 5 | se dessine de bas en haut |
| etiquette_revenus | 14,67 (« renter incomes ») ; « 9% » à 15,67 | x 55–82 %, y 68–78 % | 10 % | 5 | cache les cuisses du travailleur comme dans le c05, jamais son visage (y 30–42 %) |

### Beat 4 · 16,0–26,1 s · 30 mots · 0,337 s par mot
Transition d'entrée : **T3_4**. Poussée de caméra lente du groupe décor + porte + famille (voir `pieces.json`). Sortie du beat 3 : tout s'efface derrière la transition.
| quoi | instant (s) | x, y | taille | couche | note |
|---|---|---|---|---|---|
| decor_quartier | 16,0 | plein cadre | 100 % | 0 | |
| porte_avis | 16,0 | x 50 %, pieds à y 96 % | 48 % | 1 | |
| famille : père / mère / garçon / fille (mêmes assets qu'au beat 1) | 16,0 | père x 36 %, mère x 66 %, garçon x 62 %, fille x 66 % ; pieds à y 96 % | 50 % / 46 % / 31 % / 33 % | 1 / 1 / 2 / 2 | **décision à confirmer** : sans la famille l'avis d'expulsion n'a pas de sujet |
| avis_expulsion (papiers, image 1) | 18,7 (« court ») | x 50 %, y 62 % (sur la porte) | 12 % | 2 | parent : battant ; la porte tremble de ±3° deux fois |
| compteur_dossiers | 20,4 (« 1.23 ») | x 3–31 %, y 4–19 % | 15 % | 5 | compte de 0 à 1.23 |
| etiquette_source | 22,7 (« Princeton's ») | x 3–31 %, y 20–25 % | 5 % | 5 | |
| etiquette_austin | 24,1 (« Around ») ; « 30% » à 24,75 (« thirty ») | x 62–97 %, y 8–18 % | 10 % | 5 | |

### Beat 5 · 26,1–28,7 s · 8 mots · 0,325 s par mot
À 26,1 : la porte, l'avis, la famille et les éléments du beat 4 s'effacent (0,2 s) ; decor_quartier reste. Pas de transition (même décor). **Beat très court (2,6 s) : l'animateur règle les durées pour que tout tienne dans la fenêtre.**
| quoi | instant (s) | x, y | taille | couche | note |
|---|---|---|---|---|---|
| escalier_ascenseur | 26,1 | marches x 12–46 %, y 40–90 % ; cage x 56–88 %, y 15–90 % | 75 % | 1 | aplats `#314074` et `#C84E2E` |
| fiche de paie (papiers, image 2) | 26,1 | part de (14 %, 88 %) pour arriver à (40 %, 52 %) à 28,7 | 9 % | 2 | monte lentement |
| etiquette_paies | 26,1 (« Paychecks ») | x 14–38 %, y 28–36 % | 8 % | 5 | |
| maison_a_louer (dans la cage) | 27,4 (« Housing ») | x 72 %, monte de y 88 % à y 20 % entre 27,4 et 28,4 | 18 % | 2 | monte plus vite que la fiche de paie ; sans le texte « FOR RENT » |
| etiquette_logement | 27,4 (« Housing ») | x 62–86 %, y 6–14 % | 8 % | 5 | le haut de la maison s'arrête à y 20 % : pas de recouvrement |

## Transitions entre beats (fiches)
| transition | entre | référence de style | niveau | durée | style repris | à ne pas reprendre |
|---|---|---|---|---|---|---|
| T2_3 | beats 2 et 3 | c10 · t010000 (éclaboussure olive) | N1 | 10,0–10,6 s | éclaboussure plate `#909808` qui recouvre l'écran puis laisse voir le beat 3 | l'homme au drapeau, le texte |
| T3_4 | beats 3 et 4 | c10 · t016500 (tourbillon bleu) | N1 | 16,0–16,6 s | tourbillon plat `#3050A8` | le texte « BUT CORPORATE… », les panneaux |
| ouverture / fermeture | 0,0 et 28,7 | aucune | décision | coupe franche | début : première image du beat 1 ; fin : dernière image du beat 5 tenue jusqu'à 28,7 | à confirmer (rien dans la procédure) |
Pas de transition entre les beats 1 et 2 ni entre 4 et 5 : même décor.

## Éléments à séparer après génération (étape 3)
- `enfants_locataires` : deux personnages entiers, à découper en `garçon` et `fille`.
- `papiers` : deux objets, à découper en `avis_expulsion` et `fiche_de_paie`.
- Toutes les pièces détachées (père, mère, travailleur, porte) : découpées selon `pieces.json`.

## Objets attachés à une pièce mobile
- `avis_expulsion` suit `battant` (porte_avis) : il tremble avec la porte.
- « EVICTION NOTICE » (texte) suit `avis_expulsion`.
- « PAYCHECK » (texte) suit `fiche_de_paie`.

Non utilisés : les cartons de texte des candidats 04 et 09 (la chute est dite par l'escalier et l'ascenseur) ; « un dossier pour 13 ménages » et « Atlanta un pour 4 », qui sont dans `recherches.md` mais plus dans le speech.

## Corrections faites à la revérification
1. **Beat 3 sans décor** : ajout de `decor_champ` et `decor_bureau`.
2. **Données hors speech** retirées : « un pour treize » et « Atlanta » (dans `recherches.md`, pas dans le speech).
3. **Hex faux dans les prompts** : haut du garçon `#D9968C` (rose du mur) remplacé par `#C63636` ; pantalon du père `#4E3A47` remplacé par `#3C2A18` ; haut de la mère `#7A567A` remplacé par `#8A2478` ; jean `#547F97` par `#4E9CA2` ; robe de la fille, sans hex, maintenant `#546CDE`.
4. **Fond magenta de la famille** : le haut de la mère (#8A2478) est quasi du magenta ; fond vert pour toute la famille.
5. **Famille en 14 pièces dans une image** : coupée en trois générations (père 7, mère 7, enfants entiers).
6. **Mère** : « croise les bras » impossible avec un bras d'un seul bloc ; bras en deux segments.
7. **Travailleur** : contradiction « assis » / « pose debout bras écartés » ; hanches et jambes gardées assises, chaise et bureau en pièces séparées (bureau ajouté pour cacher les jambes).
8. **Papiers dans les mains du père** (référence) : mains vides demandées.
9. **Texte dans les images** (« FOR RENT », « EVICTION NOTICE », « PAYCHECK ») : retiré des prompts, écrit en code (fiches).
10. **Papiers** : deux références identiques fusionnées en une seule ; les deux documents se distinguent par la bande rouge ou bleue et le sceau.
11. **Format** : « 16:9 » ajouté à tous les prompts.
12. **Logo de la chaîne** : la liste précédente mettait « le logo de la chaîne » dans le code ; c'est celui du projet, pas celui des frames (« THE INFOGRAPHICS SHOW »).

## Corrections de la passe 2
0. **Animation** : tous les assets ont maintenant une consigne d'animation complète dans `pieces.json` (aucun asset fixe, aucune durée écrite) ; les durées qui figuraient dans les fiches ont été retirées.
1. **Décor et personnages à des échelles différentes** : le décor venait de la frame zoomée t006500, les personnages en pied de t009000. Le décor vient maintenant de t009000.
2. **Jambes et chaussures inventées** : la frame t006500 coupe les personnages à la taille. Deuxième référence en pied (t009000) pour le père, la mère et les enfants ; chaussures mesurées (père orange `#E08818`, mère `#908070`, enfants jaunes `#C8A820`), short du garçon `#101830` et chaussettes `#C83030`.
3. **Hex du jean faux** (`#4E9CA2` mesuré sur la frame zoomée) : `#23868F` mesuré sur le plan large ; risque de bord vert noté.
4. **Famille absente du beat 4** : l'avis d'expulsion posé sur une porte vide n'avait pas de sujet ; famille réutilisée (à confirmer).
5. **Donut sur le centre** : il aurait couvert la mère et les enfants ; carte blanche à droite, plus d'assombrissement.
6. **Icônes en bas** : elles auraient coupé les pieds de la famille ; en haut à droite.
7. **Étiquette « Austin » en bas à droite** : aurait caché les jambes de la mère ; en haut à droite.
8. **Texte affiché plus précis que le speech** : « OVER 50% » devient « MORE THAN HALF » ; « 49% » devient « NEARLY HALF » (la part du donut reste à 49 %).
9. **Panneaux plus étroits que l'image** : cadrage x 25–75 % décrit ; decor_bureau demandé avec le centre calme.
10. **Fauteuil orange du décor de bureau** : retiré, la chaise du travailleur est une pièce séparée (sinon deux chaises).
11. **Travailleur** : la référence montre aussi la voiture et la pharmacie ; le prompt dit de les ignorer. Le bandeau « 26% WAGES » cache ses cuisses : le prompt les demande complètes.
12. **Transitions** : T2_3 et T3_4 ajoutées avec leur référence ; frames copiées dans `references_code/`.
13. **Beat 5 très court (2,6 s)** : noté ; l'animateur règle les durées pour tenir dans la fenêtre, la maison monte plus vite que la fiche de paie.
14. **Objet attaché** : l'avis suit le battant de la porte.
15. **Gauche et droite** : définis côtés de l'image dans les prompts et `pieces.json`.
16. **Ordre des couches du travailleur** ajouté à `pieces.json`.

## À vérifier à la première génération
- Décors : les frames montrent des personnages devant la maison, le modèle invente les parties cachées (porche, porte).
- Détourage : bord vert autour du jean teal de la mère ; pièces bien séparées, même échelle, 7 pièces chacun.
- Travailleur : 10 pièces présentes, jambes complètes, bureau séparé.
- Papiers : bandes et lignes vides, aucun texte.
- Les chemins du JSON sont relatifs au dépôt : à remplacer par des chemins absolus dans IngXAi.
- Chiffres du speech vérifiés dans `recherches.md` : 12,1 M (plus de 50 %) et 22,7 M soit 49 % (plus de 30 %, un record).
