# Idée 1 : liste des assets (étape 2, revérifiée)

Candidats utilisés pour les références d'assets : **10** (frames 0,5–32 s) et **05** (953–1022 s). Les candidats **04 et 09 ne montrent qu'un carton de texte** : aucun asset à reprendre. Images fixes uniquement : le mouvement se fait en code. Prompts complets dans `assets.json`, pièces dans `pieces.json`, frames de référence dans `references/` (assets) et `references_code/` (style des infographies).

## Assets à générer (11 générations)
| id | Beats | Remplace (frame de référence) | Nature | Mouvements / pièces | Référence | Détourage / fond |
|---|---|---|---|---|---|---|
| decor_maison_rose | 1, 2 | façade rose du candidat 10, sans personnages | STRUCTUREL | aucun | c10 · t000006500 | non : plein cadre 16:9 |
| pere_locataire | 1, 2 | le père (barbe, chemise crème) | STRUCTUREL | se prend la tête, lève les bras. **7 pièces** | c10 · t000006500 | oui : #00FF00 |
| mere_locataire | 1, 2 | la mère (haut violet, jean teal) | STRUCTUREL | hoche la tête, croise les bras. **7 pièces** (bras en 2 segments) | c10 · t000006500 | oui : #00FF00 |
| enfants_locataires | 1, 2 | le garçon et la fille | STRUCTUREL | aucun par membre : 2 images entières | c10 · t000006500 | oui : #00FF00 |
| decor_champ | 3 | campagne et collines du candidat 05, sans maison | STRUCTUREL | aucun | c05 · t000960500 | non : plein cadre 16:9 |
| maison_a_louer | 3, 5 | maison, pins et panneau (vide) du candidat 05 | STRUCTUREL | image unique | c05 · t000960500 | oui : #FF00FF (sapins verts) |
| decor_bureau | 3 | la pièce de bureau (mur brique, rideaux, fauteuil) du candidat 05 | STRUCTUREL | aucun | c05 · t001016500 (panneau de droite) | non : plein cadre 16:9 |
| travailleur_bureau | 3 | le salarié casqué du candidat 05 | STRUCTUREL | tape au clavier, tourne la tête. **10 pièces** (dont ordinateur, chaise, bureau) | c05 · t001016500 | oui : #00FF00 |
| decor_quartier | 4, 5 | décor bleu et vert de la scène « bombe », sans bombe | STRUCTUREL | aucun | c10 · t000028500 | non : plein cadre 16:9 |
| porte_avis | 4 | la porte d'entrée de la scène « bombe » | THÉMATIQUE | le battant pivote sur la charnière. 2 pièces | c10 · t000028500 | oui : #00FF00 (porte brune) |
| papiers | 4, 5 | le document « LOAN » du candidat 10 | THÉMATIQUE | 2 images fixes sans texte : avis d'expulsion (bande rouge, sceau rouge), fiche de paie (bande bleue, pièce dorée) | c10 · t000019000 | oui : #00FF00 |

**Choix du fond de la famille (mesuré)** : haut de la mère #8A2478 (violet-magenta), jean #4E9CA2 (teal désaturé), robe de la fille #546CDE (bleu). Le magenta aurait mangé le haut de la mère et le bleu la robe ; le vert est le plus éloigné en teinte de toutes ces couleurs. Même fond pour les trois générations de la famille.

## Récapitulatif par beat
| Beat | Temps (s) | Décor | Assets | Éléments en code (fiches plus bas) |
|---|---|---|---|---|
| 1 | 0,0–5,3 | decor_maison_rose | pere_locataire, mere_locataire, enfants_locataires | compteur_menages, icones_menages |
| 2 | 5,3–10,0 | decor_maison_rose (assombri sous le donut) | mêmes personnages, inquiets | donut_49, etiquette_record |
| 3 | 10,0–16,0 | deux panneaux comme le candidat 05 : decor_champ (gauche), decor_bureau (droite) | maison_a_louer (gauche), travailleur_bureau (droite) | carte_date_2001, cercle_loyers, etiquette_revenus, texte du panneau « FOR RENT » |
| 4 | 16,0–26,1 | decor_quartier | porte_avis, papiers (avis d'expulsion posé sur la porte) | compteur_dossiers, etiquette_austin, etiquette_source |
| 5 | 26,1–28,7 | decor_quartier | papiers (fiche de paie), maison_a_louer | escalier_ascenseur, etiquette_paies, etiquette_logement |

## Fiches des éléments faits en code (aucun prompt)
Niveau = niveau de recherche de la référence de style (2.2 bis). Frames dans `references_code/`. Toutes les données viennent de `speech_adapte.md`.

**Style commun** (relevé sur les frames) : cartes blanches `#F9FCF8` à coins arrondis, texte `#282828` gras en capitales, très légère ombre ; rouge d'alerte `#F80000` (cercle, flèches, pictos) ; jaune-orangé `#F8A000` (icône de calendrier) ; donut bleu `#005090` / rouge `#B8322E` ; mêmes aplats que les assets. Pas de logo, pas de badge de la chaîne des frames.

| élément | beat | type | données (texte exact) | référence de style | style repris | animation | emplacement |
|---|---|---|---|---|---|---|---|
| compteur_menages | 1 | compteur (carte blanche) | « 12.1 MILLION » + « RENTER HOUSEHOLDS » + « OVER 50% OF INCOME ON RENT » | N1 · c05 · t000988000 (pilules de prix) | carte `#F9FCF8`, chiffre grand `#282828`, coins arrondis | la carte glisse depuis la gauche, le nombre compte de 0 à 12.1 en ~1,2 s | haut gauche |
| icones_menages | 1 | rangée de pictogrammes maison | aucune donnée chiffrée | N1 · c05 · t000966000 (icône de calendrier plate) | pictos plats `#F8A000`, un sur deux en `#F80000` | apparition en cascade | bas de l'écran |
| donut_49 | 2 | donut | « 49% » ; titre « RENTERS PAST THE 30% LINE » | N2 · c02 · t000136500 (donut) | anneau bleu `#005090`, part rouge `#B8322E`, chiffre blanc, titre blanc en capitales ; fond assombri | la part rouge se dessine en ~1 s, le chiffre s'affiche, le titre apparaît lettre par lettre | centre |
| etiquette_record | 2 | étiquette à flèche | « RECORD » | N1 · c05 · t001019500 (« 26% WAGES ») | carte blanche, flèche montante `#F80000`, texte `#282828` | glisse après le donut | bas droite |
| carte_date_2001 | 3 | carte DATE | « DATE: / SINCE 2001 » | N1 · c05 · t000966000 | carte blanche, icône calendrier `#F8A000`, « DATE: » petit, texte grand | glisse depuis la gauche | haut gauche du panneau maison |
| cercle_loyers | 3 | cercle rouge + flèche en zigzag | « RENTS » dans le cercle, « 30% » sur la flèche | N1 · c05 · t000966000 (« HOUSING COST INCREASE », 31%) | cercle `#F80000`, texte blanc gras, flèche en zigzag `#F80000` | le cercle apparaît, la flèche se dessine de bas en haut en ~0,8 s | sur la maison |
| etiquette_revenus | 3 | étiquette à flèche courte | « 9% RENTER INCOMES » | N1 · c05 · t001019500 (« 26% WAGES ») | carte blanche, flèche `#F80000` plus courte que celle des loyers | entre après la flèche des loyers | bas gauche du panneau bureau |
| texte_panneau | 3 | texte sur panneau | « FOR RENT » | N1 · c05 · t000960500 (panneau) | capitales blanches sur le panneau vide de maison_a_louer | apparaît avec la maison | sur le panneau |
| compteur_dossiers | 4 | compteur (carte blanche) | « 1.23 MILLION » + « EVICTION CASES » | N1 · c05 · t000988000 | idem compteur_menages | compte de 0 à 1.23 | haut gauche |
| etiquette_austin | 4 | étiquette | « AUSTIN: 30% ABOVE NORMAL » | N1 · c05 · t001019500 | idem etiquette_revenus | apparaît à « Around Austin » | bas droite |
| etiquette_source | 4 | petite étiquette | « PRINCETON EVICTION LAB » | N1 · c05 · t001019500 | carte blanche, texte plus petit | apparaît avec le compteur | sous le compteur |
| texte_avis | 4, 5 | texte sur objets | « EVICTION NOTICE » (bande rouge), « PAYCHECK » (bande bleue) | N1 · c10 · t000019000 (titre du document) | capitales `#282828` ou blanches sur la bande | apparaît avec l'objet | sur la bande |
| escalier_ascenseur | 5 | formes géométriques | marches à gauche, cage d'ascenseur à droite | **N4** : aucune référence trouvée (N1 : c10, c05, c04, c09 ; N2 : c01, c02, c03, c06, c07, c08 ; N3 : transcriptions des idées 1 à 6, aucune mention d'escalier ni d'ascenseur ; recherche par texte, pas par image) | aplats `#314074` et `#C84E2E` (camembert du c07), blanc, sans ombre, formes simples | la fiche de paie monte les marches lentement, la maison monte dans la cage vite | centre, sur decor_quartier |
| etiquette_paies | 5 | étiquette | « PAYCHECKS » | N1 · c05 · t001019500 | idem etiquette_revenus | apparaît à « Paychecks » | à côté de l'escalier |
| etiquette_logement | 5 | étiquette | « HOUSING » | N1 · c05 · t001019500 | idem | apparaît à « Housing » | à côté de l'ascenseur |

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

## À vérifier à la première génération
- Décors : les frames montrent des personnages devant la maison, le modèle invente les parties cachées (porche, porte).
- Détourage : bord vert autour du jean teal de la mère ; pièces bien séparées, même échelle, 7 pièces chacun.
- Travailleur : 10 pièces présentes, jambes complètes, bureau séparé.
- Papiers : bandes et lignes vides, aucun texte.
- Les chemins du JSON sont relatifs au dépôt : à remplacer par des chemins absolus dans IngXAi.
- Chiffres du speech vérifiés dans `recherches.md` : 12,1 M (plus de 50 %) et 22,7 M soit 49 % (plus de 30 %, un record).
