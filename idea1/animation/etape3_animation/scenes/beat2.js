/* Beat 2 : 5,3 à 10,0 s. « Nearly half of all renters are stretched past the thirty percent line. A record. »
   Même décor et mêmes personnages que le beat 1 (montés par beat1.js) ; ce fichier ajoute les gestes (A.gestesFamille) et les deux éléments en code.
   Instants des mots : début du beat + rang du mot x 0,336 s : « Nearly » 5,3 ; « stretched » 7,3 ; « thirty » 8,3 ; « percent » 8,33 ; « record » 9,67. */
(function () {
  var A = window.Anim, F = A.facile, TAU = 2 * Math.PI, donut, record;
  function lisse(x) { return x * x * (3 - 2 * x); }
  function pr(t, t0, d) { return A.prog(t, t0, d); }
  /* amplitudes de départ (degrés) : à régler en regardant l'image */
  var PRISE = { haut: 88, coude: 135, torse: 3, tete: 6 };       /* se prendre la tête */
  var LEVE = { haut: 125, coude: 10, torse: -4, tete: -4 };       /* lever les bras */
  var CROISE = { haut: 10, coude: 90 };                           /* croiser les bras */
  A.gestesFamille = function (t) {
    /* père : se prend la tête à 7,3 (« stretched »), relâche vers 9,2, puis lève les bras à 9,67 (« record ») */
    var prend = lisse(pr(t, 7.3, 0.5)) * (1 - lisse(pr(t, 9.15, 0.35)));
    var leve = F.rebond(pr(t, 9.67, 0.3));
    var h = PRISE.haut * prend + LEVE.haut * leve, c = PRISE.coude * prend + LEVE.coude * leve;
    var pere = { bgh: h, bgb: c, bdh: -h, bdb: -c, torse: PRISE.torse * prend + LEVE.torse * leve, tete: PRISE.tete * prend + LEVE.tete * leve,
      devant: prend > 0.02, bouche: 1 + 0.45 * prend + 0.6 * leve };
    /* mère : hoche la tête deux fois à partir de 6,0, puis croise les bras à 8,3 (« thirty ») jusqu'à la fin */
    var u = pr(t, 6.0, 1.2), nod = u > 0 && u < 1 ? Math.abs(Math.sin(TAU * u)) : 0;     /* deux hochements en 1,2 s */
    var cr = lisse(pr(t, 8.3, 0.5));
    var mere = { tdy: 12 * nod, tete: 4 * nod, bgh: -CROISE.haut * cr, bgb: -CROISE.coude * cr, bdh: CROISE.haut * cr, bdb: CROISE.coude * cr, devant: cr > 0.02 };
    /* enfants : se serrent l'un vers l'autre à 9,67 (« record ») */
    var se = F.sortie3(pr(t, 9.67, 0.4));
    return { pere: pere, mere: mere, garcon: { rot: 3 * se }, fille: { rot: -3 * se } };
  };
  A.ajouterScene({
    debut: 5.3, fin: 10.0,
    monter: function (monde, code) {
      /* carte_donut : x 71 à 98 %, y 10 à 56 % ; arrive à « nearly » (5,3), part rouge 49 %, titre à « thirty percent » (8,33) */
      donut = A.creerDonut(code, { x: 0.71 * A.L, y: 0.10 * A.H, w: 0.27 * A.L, h: 0.46 * A.H,
        entree: { t0: 5.3, d: 0.6 }, part: { t0: 5.5, d: 1.5, vers: 0.49 }, centre: { t0: 6.3, texte: ['NEARLY', 'HALF'] }, titre: { t0: 8.33, d: 0.8, texte: 'PAST THE 30% LINE' } });
      /* etiquette_record : x 72 à 97 %, y 62 à 72 % ; arrive à « record » (9,67) */
      record = A.creerEtiquette(code, { x: 0.72 * A.L, y: 0.62 * A.H, w: 0.25 * A.L, h: 0.10 * A.H, texte: 'A RECORD',
        entree: { t0: 9.67, d: 0.3 }, fleche: { t0: 9.75, d: 0.25 } });
    },
    maj: function (t) { donut.maj(t); record.maj(t); }
  });
})();
