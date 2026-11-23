# Idée 1 : speech adapté

**Idée d'origine** : « Millions of American families are now spending more than half of their income on rent, and eviction rates are rising fast as wages fail to keep up with housing costs. »

Candidat de référence : candidat05 (score 0.6317, « Housing and living costs rose faster than wages », 953.4–1022.5 s) | Mots de référence : 187
Fourchette autorisée : 187 à 243 mots | Mots obtenus : 240 (128 %) | Durée du speech : 88.7 s (débit de référence 2.71 mots/s) | Langue : anglais (celle de `idea.json`)

Plan, candidats choisis et rejetés : voir `plan_scenario.md`. Faits et sources : voir `recherches.md`.

## Points de l'idée
1. Des millions de familles américaines dépensent plus de la moitié de leur revenu en loyer.
2. Les expulsions augmentent vite.
3. Les salaires ne suivent pas les coûts du logement.

## Beats
| # | Début (s) | Fin (s) | Candidat (frames) | Point | Texte |
|---|---|---|---|---|---|
| 1 | 0.0 | 8.9 | 10 | 1 | Right now, 12.1 million American renter households are handing over more than half of their income just to keep a roof over their heads. |
| 2 | 8.9 | 12.6 | 10 | 1 | That's one in four. It should be a red flag. |
| 3 | 12.6 | 21.1 | 10 | 1 | And it's not only the poorest. Nearly half of all renters, 22.7 million households, are stretched past the thirty percent line. A record. |
| 4 | 21.1 | 25.1 | 05 | 3 | So what gives? The answer is simple: paychecks aren't keeping pace. |
| 5 | 25.1 | 32.5 | 05 | 3 | Since 2001, after inflation, the median rent has climbed 30 percent, while the median renter's income has risen just 9. |
| 6 | 32.5 | 38.8 | 05 | 3 | The typical renter now hands over 31 percent of income for rent and utilities, up from 27. |
| 7 | 38.8 | 48.4 | 05 | 1 | And for families earning under thirty thousand dollars, what's left after housing is two hundred and ten dollars a month. For food, transport, medicine, everything else. |
| 8 | 48.4 | 55.4 | 04 | 2 | When the squeeze breaks, it ends in court. In a typical year, landlords file about 3.6 million eviction cases. |
| 9 | 55.4 | 65.8 | 04 | 2 | Last year, in the places tracked by Princeton's Eviction Lab, they filed 1.23 million. Roughly one case for every thirteen renter households. In Atlanta, one for every four. |
| 10 | 65.8 | 71.3 | 04 | 2 | Overall filings eased slightly, but in the Austin area they ran thirty percent above normal. |
| 11 | 71.3 | 84.6 | 04 | 2 | And at the very bottom, there's the street. In January 2024, the government counted 771,000 people without a home. The highest number ever recorded, up eighteen percent in one year. Almost 150,000 of them were children. |
| 12 | 84.6 | 88.7 | 09 | 3 | It's just arithmetic. Paychecks take the stairs. Housing takes the elevator. |

Les fenêtres de temps sont calculées avec le débit du candidat de référence. L'alignement fin avec les frames (candidats 10, 05, 04, 09) reste à faire à l'étape 2.

## Décisions prises
- **Candidat de référence : 05.** C'est le seul assez long (187 mots) pour porter les trois points ; il parle de coûts du logement qui montent plus vite que les salaires, donc du même sujet que l'idée. Son texte se coupe au milieu d'une phrase (« And »), la fin n'est donc pas visible : la chute vient du candidat 09.
- **Longueur : 240 mots, soit 128 % de la référence** (règle : 100 % à 130 %).
- **Ordre 1 → 3 → 2 → chute** au lieu de 1 → 2 → 3 : le raisonnement devient « beaucoup paient plus de la moitié, parce que les salaires ne suivent pas, et ça finit au tribunal ». L'ordre logique prime sur l'ordre de l'idée, tous les points restent présents.
- **« Les expulsions augmentent vite » n'est pas confirmé au niveau national.** Selon l'Eviction Lab, les dépôts de plaintes 2025 sont légèrement sous ceux de 2024. Le speech dit qu'ils restent massifs et dépassent la normale par endroits (Austin +30 %), sans affirmer une hausse générale rapide.
- **Candidat 01 écarté** (défend l'angle inverse : expulser serait plus dur que saisir). Autres écartés : voir `plan_scenario.md`.
- **Faits réutilisés** de la recherche déjà faite et recoupée dans cette conversation : pas de nouvelle recherche web. Le dernier chiffre de sans-abri disponible est de janvier 2024.
- **Les frames n'ont pas été regardées.** Le calage porte sur les textes, durées et résumés.

## Speech complet

Right now, 12.1 million American renter households are handing over more than half of their income just to keep a roof over their heads. That's one in four. It should be a red flag. And it's not only the poorest. Nearly half of all renters, 22.7 million households, are stretched past the thirty percent line. A record.

So what gives? The answer is simple: paychecks aren't keeping pace. Since 2001, after inflation, the median rent has climbed 30 percent, while the median renter's income has risen just 9. The typical renter now hands over 31 percent of income for rent and utilities, up from 27. And for families earning under thirty thousand dollars, what's left after housing is two hundred and ten dollars a month. For food, transport, medicine, everything else.

When the squeeze breaks, it ends in court. In a typical year, landlords file about 3.6 million eviction cases. Last year, in the places tracked by Princeton's Eviction Lab, they filed 1.23 million. Roughly one case for every thirteen renter households. In Atlanta, one for every four. Overall filings eased slightly, but in the Austin area they ran thirty percent above normal. And at the very bottom, there's the street. In January 2024, the government counted 771,000 people without a home. The highest number ever recorded, up eighteen percent in one year. Almost 150,000 of them were children.

It's just arithmetic. Paychecks take the stairs. Housing takes the elevator.

## Vérifications
- [x] Les 3 points de l'idée sont présents.
- [x] Un plan existe et le speech le suit (`plan_scenario.md`).
- [x] 240 mots, entre 187 et 243 (100 % à 130 % du candidat 05).
- [x] Chaque fait ajouté est sourcé (`recherches.md`) et sert un point de l'idée.
- [x] Les beats se suivent sans trou et finissent à 88.7 s.
- [x] Aucune phrase recopiée du speech d'un candidat.
