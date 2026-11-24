/* Beat 1 : 0,0 à 5,3 s (+ 0,4 s de sortie des éléments en code, qui se fait au changement de beat).
   « Right now, 12.1 million American renter households spend more than half of their income on rent. »
   Placements : Liste_assets.md, « Mise en place par beat » ; gestes : pieces.json et elements_code.json (étape 2).
   Instants des mots : début du beat + rang du mot x 0,331 s. */
(function () {
  var A = window.Anim;
  var pere, mere, garcon, fille, compteur, icones, decor;
  A.ajouterScene({
    debut: 0, fin: 5.7,
    monter: function (monde, code) {
      decor = A.el('img', 'position:absolute;left:0;top:0;width:' + A.L + 'px;height:' + A.H + 'px;pointer-events:none;', monde);
      decor.src = 'decors/decor_maison_rose.svg'; decor.draggable = false;
      /* couche 1 : père (x 26 %, pieds à y 99 %, 78 % de l'écran) et mère (x 54 %, pieds à y 97 %, 72 %) */
      pere = A.creerPersonnage(monde, { asset: 'pere_locataire', prefixe: 'pere_', ancre: { x: 836, y: 886 }, hauteurSource: 874,
        place: { x: 0.26, y: 0.99, h: 0.78 }, repos: { bras_g: -38, bras_d: 38, coude_g: 6, coude_d: -6 }, phase: 0, clignement: { periode: 3.6, phase: 0.9 } });
      mere = A.creerPersonnage(monde, { asset: 'mere_locataire', prefixe: 'mere_', ancre: { x: 837, y: 897 }, hauteurSource: 880,
        place: { x: 0.54, y: 0.97, h: 0.72 }, repos: { bras_g: -16, bras_d: 16, coude_g: -8, coude_d: 8 }, phase: 2.1, clignement: { periode: 4.4, phase: 2.3 } });
      /* couche 2 : les enfants, devant la mère (garçon x 60 %, fille x 66 %, pieds à y 100 %) */
      garcon = A.creerBloc(monde, { asset: 'enfants_locataires', piece: 'garcon', ancre: { x: 628, y: 868 }, hauteurSource: 800,
        place: { x: 0.60, y: 1.0, h: 0.53 }, phase: 0.8 });
      fille = A.creerBloc(monde, { asset: 'enfants_locataires', piece: 'fille', ancre: { x: 1055, y: 868 }, hauteurSource: 798,
        place: { x: 0.66, y: 1.0, h: 0.56 }, phase: 3.4 });
      /* couche 5 : éléments en code (haut gauche : x 3 à 33 %, y 4 % ; haut droite : x 55 à 97 %, y 4 %) */
      compteur = A.creerCompteur(code, { x: 0.03 * A.L, y: 0.04 * A.H, w: 540,
        entree: { t0: 0.05, d: 0.61 },      /* arrive au mot « 12.1 » (0,66 s) */
        compte: { t0: 0.66, d: 1.8, vers: 12.1 },
        ligne3: { t0: 2.65 },               /* « more than half » */
        sortie: { t0: 5.3, d: 0.4 } });
      icones = A.creerIcones(code, { n: 7, x: 0.55 * A.L, y: 0.04 * A.H, pas: 100, taille: 96,
        t0: 1.99, ecart: 0.18,              /* premier picto au mot « households » (1,99 s) */
        rouges: [0, 1, 3, 5],
        sortie: { t0: 5.3, d: 0.3 } });
    },
    maj: function (t) {
      /* caméra : oscillation continue + poussée lente 105 % -> 109 %, sur le groupe décor + personnages */
      A.camera(t, 1.05 + 0.04 * A.clamp(t / 10, 0, 1));
      /* expressions : à « more than half » (2,65 s) l'inquiétude monte (0,2 s avant le mot) : tête qui s'incline de 3°, bouche qui se resserre ; retour au neutre à la sortie (5,3 s) */
      var inq = A.facile.sortie3(A.prog(t, 2.45, 0.35)) * (1 - A.facile.sortie3(A.prog(t, 5.3, 0.3)));
      pere.maj(t, { tete: 3 * inq, bouche: 1 - 0.35 * inq }); mere.maj(t, { tete: -3 * inq, bouche: 1 - 0.35 * inq }); garcon.maj(t); fille.maj(t);
      compteur.maj(t); icones.maj(t);
    }
  });
})();
