/* Personnages articulés : chaque pièce est une balise <img src="chemin.svg">, aucun SVG brut dans la page.
   Structure : racine (position, échelle) > balancement (autour des pieds) > jambes, haut du corps
   (autour de la taille) > [bras haut > bras bas] x2, torse, tête (autour du cou).
   Les pivots viennent de pivots.json, les décalages de montage.json (planche -> personnage assemblé). */
(function () {
  var A = window.Anim, D = window.DONNEES;
  var PLEIN = 'position:absolute;left:0;top:0;width:' + A.L + 'px;height:' + A.H + 'px;';
  function origine(e, p) { e.style.transformOrigin = p.x + 'px ' + p.y + 'px'; }

  /* cfg : asset, prefixe, ancre {x,y} (les pieds, dans l'image assemblée), place {x,y,h} (pieds à l'écran, hauteur de l'écran),
     hauteurSource (hauteur du personnage dans l'image), repos {bras_g, bras_d} (angle de repos des bras, degrés),
     phase (décale la vie pour que deux personnages ne bougent pas ensemble) */
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
    img(haut, p + 'torse');
    var tete = groupe(haut, p + 'tete'); img(tete, p + 'tete');
    var ph = cfg.phase || 0, TAU = 2 * Math.PI, r = cfg.repos || { bras_g: 0, bras_d: 0 };
    return {
      racine: racine,
      /* t : secondes. extra : gestes ajoutés par la scène { torse, tete, bgh, bgb, bdh, bdb } en degrés */
      maj: function (t, extra) {
        var e = extra || {}, sin = Math.sin;
        haut.style.transform = 'rotate(' + (e.torse || 0) + 'deg)';
        tete.style.transform = 'rotate(' + (e.tete || 0) + 'deg)';
        bgh.style.transform = 'rotate(' + (r.bras_g + (e.bgh || 0) ) + 'deg)';
        bgb.style.transform = 'rotate(' + ((r.coude_g || 0) + (e.bgb || 0)) + 'deg)';
        bdh.style.transform = 'rotate(' + (r.bras_d + (e.bdh || 0) ) + 'deg)';
        bdb.style.transform = 'rotate(' + ((r.coude_d || 0) + (e.bdb || 0)) + 'deg)';
      }
    };
  };

  /* Image entière (enfants) : un seul bloc qui respire et se balance autour des pieds. */
  A.creerBloc = function (parent, cfg) {
    var s = cfg.place.h * A.H / cfg.hauteurSource, TAU = 2 * Math.PI, ph = cfg.phase || 0;
    var racine = A.el('div', PLEIN + 'transform-origin:0 0;transform:translate(' + (cfg.place.x * A.L - s * cfg.ancre.x) + 'px,' + (cfg.place.y * A.H - s * cfg.ancre.y) + 'px) scale(' + s + ');', parent);
    var corps = A.el('div', PLEIN, racine); origine(corps, cfg.ancre);
    var i = A.el('img', PLEIN + 'pointer-events:none;', corps); i.src = D.index[cfg.asset].pieces[cfg.piece]; i.draggable = false; i.alt = '';
    return {
      maj: function (t, extra) {
        var e = extra || {};
        corps.style.transform = 'rotate(' + (e.rot || 0) + 'deg)';
      }
    };
  };
})();
