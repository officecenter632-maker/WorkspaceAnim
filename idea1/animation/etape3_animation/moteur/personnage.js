/* Personnages articulés : chaque pièce est une balise <img src="chemin.svg">, aucun SVG brut dans la page.
   Structure : racine (position, échelle) > balancement (autour des pieds) > jambes, haut du corps
   (autour de la taille) > [bras haut > bras bas] x2, torse, tête (autour du cou).
   Les pivots viennent de pivots.json, les décalages de montage.json (planche -> personnage assemblé). */
(function () {
  var A = window.Anim, D = window.DONNEES;
  var PLEIN = 'position:absolute;left:0;top:0;width:' + A.L + 'px;height:' + A.H + 'px;';
  function origine(e, p) { e.style.transformOrigin = p.x + 'px ' + p.y + 'px'; }

  /* Clignement : 0 (yeux ouverts) à 1 (fermés), fonction du temps seulement. Régulier : exactement un clignement par période (pas de double
     clignement, pas de variation), fermeture 0,06 s, yeux clos 0,04 s, réouverture 0,10 s (0,2 s au total). */
  A.clignement = function (t, periode, phase) {
    var v = (t + phase) % periode;
    return v < 0.06 ? v / 0.06 : v < 0.10 ? 1 : v < 0.20 ? 1 - (v - 0.10) / 0.10 : 0;
  };
  /* Visage : applique clignement (yeux écrasés vers leur centre) et ouverture de bouche (1 = neutre) aux pièces présentes. */
  function majVisage(visage, t, cli, bouche) {
    var sy = 1 - 0.9 * A.clignement(t, cli.periode, cli.phase);
    if (visage.oeil_g) visage.oeil_g.style.transform = 'scale(1,' + sy + ')';
    if (visage.oeil_d) visage.oeil_d.style.transform = 'scale(1,' + sy + ')';
    if (visage.bouche) visage.bouche.style.transform = 'scale(1,' + (bouche == null ? 1 : bouche) + ')';
  }

  /* cfg : asset, prefixe, ancre {x,y} (les pieds, dans l'image assemblée), place {x,y,h} (pieds à l'écran, hauteur de l'écran),
     hauteurSource (hauteur du personnage dans l'image), repos {bras_g, bras_d} (angle de repos des bras, degrés),
     phase (décale la vie pour que deux personnages ne bougent pas ensemble),
     clignement {periode, phase} (secondes ; propre à chaque personnage, jamais synchrone avec un autre) */
  A.creerPersonnage = function (parent, cfg) {
    var idx = D.index[cfg.asset], piv = D.pivots[cfg.asset], mon = D.montage[cfg.asset] || {};
    function m(id) { return mon[id] || { dx: 0, dy: 0 }; }
    function pv(id) { return { x: piv[id].x + m(id).dx, y: piv[id].y + m(id).dy }; }
    function img(parentEl, id) {
      var i = A.el('img', PLEIN + 'transform:translate(' + m(id).dx + 'px,' + m(id).dy + 'px);pointer-events:none;', parentEl);
      i.src = idx.pieces[id]; i.draggable = false; i.alt = ''; return i;
    }
    function groupe(parentEl, id) { var g = A.el('div', PLEIN, parentEl); origine(g, pv(id)); return g; }
    var p = cfg.prefixe, s = cfg.place.h * A.H / cfg.hauteurSource;
    var racine = A.el('div', PLEIN + 'transform-origin:0 0;transform:translate(' + (cfg.place.x * A.L - s * cfg.ancre.x) + 'px,' + (cfg.place.y * A.H - s * cfg.ancre.y) + 'px) scale(' + s + ');', parent);
    var sway = A.el('div', PLEIN, racine); origine(sway, cfg.ancre);
    img(sway, p + 'jambes');
    var haut = groupe(sway, p + 'torse');
    var bgh = groupe(haut, p + 'bras_g_haut'); img(bgh, p + 'bras_g_haut');
    var bgb = groupe(bgh, p + 'bras_g_bas'); img(bgb, p + 'bras_g_bas');
    var bdh = groupe(haut, p + 'bras_d_haut'); img(bdh, p + 'bras_d_haut');
    var bdb = groupe(bdh, p + 'bras_d_bas'); img(bdb, p + 'bras_d_bas');
    var torseImg = img(haut, p + 'torse');
    var tete = groupe(haut, p + 'tete'); img(tete, p + 'tete');
    /* visage : yeux et bouche sont des pièces séparées, dans le groupe de la tête (elles suivent ses mouvements) */
    var visage = null;
    if (idx.pieces[p + 'oeil_g']) {
      visage = {};
      ['oeil_g', 'oeil_d', 'bouche'].forEach(function (k) { if (idx.pieces[p + k]) { var g = groupe(tete, p + k); img(g, p + k); visage[k] = g; } });
    }
    /* bras devant le torse (se prendre la tête, croiser les bras) : l'ordre des couches change seulement quand l'état change */
    var enAvant = false;
    function bras_devant(v) {
      if (v === enAvant) return; enAvant = v;
      if (v) { haut.appendChild(bgh); haut.appendChild(bdh); } else { haut.insertBefore(bgh, torseImg); haut.insertBefore(bdh, torseImg); }
    }
    var cli = cfg.clignement || { periode: 4, phase: 0 };
    var ph = cfg.phase || 0, TAU = 2 * Math.PI, r = cfg.repos || { bras_g: 0, bras_d: 0 };
    return {
      racine: racine,
      /* t : secondes. extra : gestes ajoutés par la scène { torse, tete, bgh, bgb, bdh, bdb } en degrés, bouche (facteur vertical, 1 = neutre), tdy (décalage vertical de la tête en px de l'image : hochement) et devant (vrai : les bras passent devant le torse et la tête) */
      maj: function (t, extra) {
        var e = extra || {}, sin = Math.sin;
        /* respiration : étirement vertical d'environ 1 %, pieds fixes ; la tête suit avec retard */
        var resp = 1 + 0.01 * sin(TAU * t / 3.6 + ph);
        haut.style.transform = 'scale(1,' + resp + ') rotate(' + (e.torse || 0) + 'deg)';
        tete.style.transform = 'translate(0,' + (e.tdy || 0) + 'px) rotate(' + ((e.tete || 0) + 1.2 * sin(TAU * t / 3.6 + ph - 0.7)) + 'deg)';
        bras_devant(!!e.devant);
        if (visage) majVisage(visage, t, cli, e.bouche);
        /* poids d'un pied à l'autre : tout le personnage pivote de ±1° autour des pieds */
        sway.style.transform = 'rotate(' + (1 * sin(TAU * t / 5.5 + ph * 1.7)) + 'deg)';
        /* bras relâchés : balancement par inertie, ±2° à l'épaule, ±3° au coude */
        bgh.style.transform = 'rotate(' + (r.bras_g + (e.bgh || 0) + 2 * sin(TAU * t / 4.1 + ph + 1)) + 'deg)';
        bgb.style.transform = 'rotate(' + (((r.coude_g || 0) + (e.bgb || 0)) + 3 * sin(TAU * t / 3.3 + ph + 1.6)) + 'deg)';
        bdh.style.transform = 'rotate(' + (r.bras_d + (e.bdh || 0) + 2 * sin(TAU * t / 4.1 + ph + 3)) + 'deg)';
        bdb.style.transform = 'rotate(' + (((r.coude_d || 0) + (e.bdb || 0)) + 3 * sin(TAU * t / 3.3 + ph + 3.6)) + 'deg)';
      }
    };
  };

  /* Image entière (enfants) : un seul bloc qui respire et se balance autour des pieds. */
  A.creerBloc = function (parent, cfg) {
    var s = cfg.place.h * A.H / cfg.hauteurSource, TAU = 2 * Math.PI, ph = cfg.phase || 0;
    var racine = A.el('div', PLEIN + 'transform-origin:0 0;transform:translate(' + (cfg.place.x * A.L - s * cfg.ancre.x) + 'px,' + (cfg.place.y * A.H - s * cfg.ancre.y) + 'px) scale(' + s + ');', parent);
    var corps = A.el('div', PLEIN, racine); origine(corps, cfg.ancre);
    var i = A.el('img', PLEIN + 'pointer-events:none;', corps); i.src = D.index[cfg.asset].pieces[cfg.piece]; i.draggable = false; i.alt = '';
    /* visage : yeux et bouche en pièces séparées (nom : <piece>_oeil_g, <piece>_oeil_d, <piece>_bouche), dans le bloc, donc ils suivent son mouvement */
    var visage = {}, nb = 0, cli = cfg.clignement || { periode: 3.2, phase: 0 };
    ['oeil_g', 'oeil_d', 'bouche'].forEach(function (k) {
      var id = cfg.piece + '_' + k; if (!D.index[cfg.asset].pieces[id]) return;
      var g = A.el('div', PLEIN, corps); origine(g, D.pivots[cfg.asset][id]);
      var im = A.el('img', PLEIN + 'pointer-events:none;', g); im.src = D.index[cfg.asset].pieces[id]; im.draggable = false; im.alt = '';
      visage[k] = g; nb++;
    });
    return {
      maj: function (t, extra) {
        var e = extra || {};
        if (nb) majVisage(visage, t, cli, e.bouche);
        corps.style.transform = 'rotate(' + ((e.rot || 0) + 1.5 * Math.sin(TAU * t / 4.8 + ph)) + 'deg) scale(1,' + (1 + 0.01 * Math.sin(TAU * t / 3.6 + ph + 0.5)) + ')';
      }
    };
  };
})();
