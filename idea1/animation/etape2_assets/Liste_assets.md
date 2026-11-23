# Idée 1 : liste des assets (étape 2)

Candidats utilisés pour les références : **10** (frames 0,5–32 s) et **05** (frames 953–1021 s). Images fixes uniquement : le mouvement se fait en code.
Les prompts complets sont dans `assets.json`, les pièces dans `pieces.json`, les frames de référence dans `references/`.

## Assets à générer
| id | Beats | Remplace (frame de référence) | Nature | Mouvements / pièces | Référence | Détourage / fond |
|---|---|---|---|---|---|---|
| decor_maison_rose | 1, 2 | la façade rose du candidat 10, sans personnages | STRUCTUREL | aucun | c10 · t000006500 (maison entière) | non : plein cadre |
| famille_locataire | 1, 2 | le père, la mère, le garçon, la fille du candidat 10 | STRUCTUREL | père : se prend la tête, lève les bras ; mère : hoche la tête, croise les bras. 14 pièces (voir pieces.json) | c10 · t000006500 (famille, à droite de la façade) | oui : #FF00FF (jean bleu-teal et haut violet : le vert est écarté) |
| decor_quartier | 4, 5 | le décor bleu et vert de la scène « bombe », sans bombe ni personnages | STRUCTUREL | aucun | c10 · t000028500 | non : plein cadre |
| maison_a_louer | 3, 5 | la maison et le panneau « FOR RENT » du candidat 05 | STRUCTUREL | image unique (déplacée, zoomée, montée en code) | c05 · t000960500 (maison + panneau) | oui : #FF00FF (sapins et haies verts) |
| travailleur_bureau | 3 | le salarié casqué du candidat 05 | STRUCTUREL | tape au clavier, tourne la tête. 9 pièces | c05 · t001016500 (panneau de droite) | oui : #00FF00 (aucun vert dans l'asset) |
| porte_avis | 4 | la porte d'entrée de la scène « bombe » du candidat 10 | THÉMATIQUE | le battant pivote sur la charnière. 2 pièces | c10 · t000028500 (porte) | oui : #00FF00 (porte brune) |
| papiers | 4, 5 | le document « LOAN » du candidat 10 | THÉMATIQUE | images uniques : avis d'expulsion, fiche de paie | c10 · t000019000 (document à droite), utilisée pour les deux éléments | oui : #00FF00 (papier beige, sceau doré) |

## Éléments faits en code (aucun prompt)
- Beat 1 : compteur « 12,1 millions », icônes de ménages.
- Beat 2 : jauge ou barre « presque la moitié, 49 % », étiquette « record ».
- Beat 3 : flèches et barres comparatives « loyers +30 % / revenus +9 % », étiquette « depuis 2001 ».
- Beat 4 : compteur « 1,23 million de dossiers », icônes « un pour treize », étiquettes Atlanta et Austin.
- Beat 5 : escalier et ascenseur (formes géométriques) sur lesquels montent la fiche de paie et la maison.
- Tous les cartons de texte, la carte « DATE », les badges et le logo de la chaîne.

## Décisions prises
- **Les frames des candidats 04 et 09 ne montrent qu'un carton de texte** (« BUT CAPITALISM IS A C… », « IT RARELY WORKS LIKE THAT THESE DAYS ») sur fond sombre : aucun élément à reprendre. Pour les beats 4 et 5, les références viennent donc des candidats 10 et 05, les deux seuls retenus qui ont des images d'éléments.
- **Les frames des candidats ne montrent pas les chiffres du speech** (expulsions, sans-abri) : les assets des beats 4 et 5 sont des objets du même style (porte, papier, décor) et non des reprises de leurs scènes.
- **Textes sur les objets** : « FOR RENT » (déjà sur la frame), « EVICTION NOTICE » et « PAYCHECK » (le speech parle d'expulsions et de fiche de paie) sont les seuls textes autorisés dans les prompts.
- **Non utilisés** : la scène des personnes aux yeux bandés devant le feu, l'homme au drapeau rouge, les trois panneaux (ouvrier, banquier, prêt) et la bombe, qui ne servent pas les points de l'idée.
- **Frames regardées** : toutes les planches-contact des candidats 10, 05, 04, 09, et en pleine taille les frames citées ci-dessus.
