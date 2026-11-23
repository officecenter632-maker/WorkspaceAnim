# Idée 1 : speech adapté

**Idée d'origine** : « Millions of American families are now spending more than half of their income on rent, and eviction rates are rising fast as wages fail to keep up with housing costs. »

Durée cible : **30 s maximum** (valeur par défaut, aucune durée imposée) | Candidat de référence : candidat10 (score 0.6217, « Hook: families spending half their paycheck on housing », 0.2–32.2 s, 96 mots, 2.99 mots/s)
Mots maximum : 89 (30 s × 2.99) | Mots minimum conseillés : 80 (90 %) | Mots obtenus : 86 | Durée du speech : 28.7 s | Langue : anglais (celle de `idea.json`)

Plan, candidats choisis et rejetés : voir `plan_scenario.md`. Faits et sources : voir `recherches.md`.

## Points de l'idée
1. Des millions de familles américaines dépensent plus de la moitié de leur revenu en loyer.
2. Les expulsions augmentent vite.
3. Les salaires ne suivent pas les coûts du logement.

## Beats
| # | Début (s) | Fin (s) | Candidat (frames) | Point | Texte |
|---|---|---|---|---|---|
| 1 | 0.0 | 5.3 | 10 | 1 | Right now, 12.1 million American renter households spend more than half of their income on rent. |
| 2 | 5.3 | 10.0 | 10 | 1 | Nearly half of all renters are stretched past the thirty percent line. A record. |
| 3 | 10.0 | 16.0 | 05 | 3 | Why? Paychecks aren't keeping pace. Since 2001, after inflation, rents are up 30 percent. Renter incomes, just 9. |
| 4 | 16.0 | 26.1 | 04 | 2 | And when the squeeze breaks, it ends in court. Last year, landlords filed 1.23 million eviction cases in the places Princeton's Eviction Lab tracks. Around Austin, thirty percent above normal. |
| 5 | 26.1 | 28.7 | 09 | 3 | Paychecks take the stairs. Housing takes the elevator. |

Fenêtres calculées avec le débit du candidat de référence. L'alignement avec les frames (candidats 10, 05, 04, 09) reste à faire à l'étape 2.

## Décisions prises
- **Durée : 30 s maximum**, valeur par défaut tant qu'aucune durée n'est précisée. Elle remplace la règle « 100 % à 130 % du candidat ».
- **Candidat de référence : 10.** Sa durée (32.1 s) est proche de 30 s et il parle de la même chose que le point 1 de l'idée (familles à plus de 50 % du revenu). Il donne le débit (2.99 mots/s), donc le plafond de 89 mots. Le candidat 05, utilisé avant (69 s), est trop long pour 30 s.
- **Ordre 1 → 3 → 2 → chute** : « beaucoup paient plus de la moitié, parce que les salaires ne suivent pas, et ça finit au tribunal ». Les trois points sont présents.
- **Faits gardés : les plus forts seulement.** Retirés pour tenir en 30 s : le chiffre de 210 $ restants, les sans-abri (HUD), le 31 % contre 27 %, le ratio prix/revenu.
- **« Les expulsions augmentent vite » n'est pas confirmé au niveau national** (dépôts 2025 légèrement sous 2024, selon l'Eviction Lab). Le speech cite le volume (1,23 M de dossiers) et la hausse locale (Austin, +30 % vs la normale) sans affirmer une hausse générale.
- **Faits réutilisés** de la recherche déjà recoupée : pas de nouvelle recherche web.
- **Les frames n'ont pas été regardées.**

## Speech complet

Right now, 12.1 million American renter households spend more than half of their income on rent. Nearly half of all renters are stretched past the thirty percent line. A record. Why? Paychecks aren't keeping pace. Since 2001, after inflation, rents are up 30 percent. Renter incomes, just 9. And when the squeeze breaks, it ends in court. Last year, landlords filed 1.23 million eviction cases in the places Princeton's Eviction Lab tracks. Around Austin, thirty percent above normal. Paychecks take the stairs. Housing takes the elevator.

## Vérifications
- [x] Les 3 points de l'idée sont présents.
- [x] Un plan existe et le speech le suit (`plan_scenario.md`).
- [x] 86 mots, sous le plafond de 89 ; durée 28.7 s ≤ 30 s.
- [x] Chaque fait est sourcé (`recherches.md`) et sert un point de l'idée.
- [x] Les beats se suivent sans trou et finissent à 28.7 s.
- [x] Aucune phrase recopiée du speech d'un candidat.
