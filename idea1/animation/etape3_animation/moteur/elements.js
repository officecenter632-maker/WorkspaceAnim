/* Éléments faits en code (cartes, compteurs, pictogrammes) : HTML / CSS / SVG dessinés ici, jamais en images.
   Ils ne zooment pas avec le décor : ils sont placés sur l'écran (calque « code »). */
(function () {
  var A = window.Anim, F = A.facile, TAU = 2 * Math.PI;
  var POLICE = "font-family:'Inter','Segoe UI','Helvetica Neue',Arial,sans-serif;font-weight:800;";

  /* compteur_menages : carte blanche, grand chiffre qui défile, 3e ligne qui se déplie.
     o = { x, y, w (px), entree {t0,d}, compte {t0,d,vers}, ligne3 {t0}, sortie {t0,d} } */
  A.creerCompteur = function (parent, o) {
    var carte = A.el('div', 'position:absolute;left:' + o.x + 'px;top:' + o.y + 'px;width:' + o.w + 'px;box-sizing:border-box;padding:12px 28px 12px;background:#fff;border-radius:24px;color:#1b2433;opacity:0;' + POLICE, parent);
    var nombre = A.el('div', 'font-size:76px;line-height:80px;letter-spacing:-1px;font-variant-numeric:tabular-nums;', carte);
    var unite = A.el('div', 'font-size:24px;line-height:28px;color:#4a5568;letter-spacing:.5px;', carte);
    unite.textContent = 'MILLION RENTER HOUSEHOLDS';
    var pli = A.el('div', 'overflow:hidden;height:0;', carte);
    var ligne3 = A.el('div', 'font-size:24px;line-height:30px;color:#d63a3a;padding-top:6px;letter-spacing:.3px;white-space:nowrap;', pli);
    ligne3.textContent = 'MORE THAN HALF OF INCOME ON RENT';
    var hLigne3 = 36;
    return {
      maj: function (t) {
        var ent = F.rebond(A.prog(t, o.entree.t0, o.entree.d)), sor = F.entree3(A.prog(t, o.sortie.t0, o.sortie.d));
        /* la carte glisse depuis le bord gauche, se pose avec un léger rebond ; à la sortie elle repart à gauche */
        var dx = -(o.x + o.w + 40) * (1 - ent) - (o.x + o.w + 40) * sor;
        /* vie : flotte d'environ 0,5 % de la hauteur de l'écran, lentement */
        var flotte = t > o.entree.t0 + o.entree.d ? 0.005 * A.H * Math.sin(TAU * t / 3.8) : 0;
        carte.style.opacity = t < o.entree.t0 ? 0 : 1 - sor;
        carte.style.transform = 'translate(' + dx + 'px,' + flotte + 'px)';
        carte.style.boxShadow = '0 ' + (10 + flotte) + 'px ' + (28 + flotte) + 'px rgba(0,0,0,.28)';
        /* le nombre défile vite puis ralentit, et s'arrête net sur la valeur */
        var c = F.sortie4(A.prog(t, o.compte.t0, o.compte.d));
        nombre.textContent = (o.compte.vers * c).toFixed(1);
        /* 3e ligne : la carte s'allonge vers le bas, le texte apparaît de gauche à droite */
        var u = A.prog(t, o.ligne3.t0, 0.9), pliP = F.sortie3(A.clamp(u / 0.4, 0, 1)), txt = A.clamp((u - 0.35) / 0.65, 0, 1);
        pli.style.height = (hLigne3 * pliP) + 'px';
        ligne3.style.clipPath = 'inset(0 ' + (100 - 100 * txt) + '% 0 0)';
      }
    };
  };

  /* icones_menages : pictogrammes maison, entrée en cascade de gauche à droite, balancement et pulsation.
     o = { x, y, pas, taille, t0, ecart, rouges:[indices], sortie {t0,d} } */
  var MAISON = '<svg viewBox="0 0 100 100" width="100%" height="100%"><path d="M50 8 L94 46 L84 46 L84 92 L16 92 L16 46 L6 46 Z" fill="FOND" stroke="#1b2433" stroke-width="6" stroke-linejoin="round"/><rect x="40" y="60" width="20" height="32" rx="3" fill="#1b2433"/><rect x="66" y="16" width="10" height="22" fill="FOND" stroke="#1b2433" stroke-width="6" stroke-linejoin="round"/></svg>';
  A.creerIcones = function (parent, o) {
    var n = o.n, items = [];
    for (var i = 0; i < n; i++) {
      var rouge = o.rouges.indexOf(i) >= 0;
      var cell = A.el('div', 'position:absolute;left:' + (o.x + i * o.pas) + 'px;top:' + o.y + 'px;width:' + o.taille + 'px;height:' + o.taille + 'px;opacity:0;transform-origin:50% 100%;', parent);
      cell.innerHTML = MAISON.replace(/FOND/g, rouge ? '#e0443e' : '#f5a623');
      items.push({ el: cell, rouge: rouge, i: i });
    }
    return {
      maj: function (t) {
        var sor = F.entree3(A.prog(t, o.sortie.t0, o.sortie.d));
        items.forEach(function (it) {
          var t0 = o.t0 + it.i * o.ecart, e = F.rebond(A.prog(t, t0, 0.5));
          var vu = t >= t0 ? 1 : 0;
          /* poussé du bas avec un petit rebond ; ensuite balancement de ±3° à son propre rythme */
          var y = (1 - e) * (o.taille * 0.7);
          var rot = t > t0 + 0.5 ? 3 * Math.sin(TAU * t / (2.6 + it.i * 0.37) + it.i * 1.3) : 0;
          var pulse = it.rouge && t > t0 + 0.5 ? 1 + 0.02 * Math.sin(TAU * t / 1.1 + it.i) : 1;
          /* à la sortie : tous se réduisent vers leur centre */
          var sc = pulse * (1 - sor);
          it.el.style.opacity = vu ? Math.min(1, e * 4) : 0;
          it.el.style.transform = 'translateY(' + y + 'px) rotate(' + rot + 'deg) scale(' + sc + ')';
          it.el.style.transformOrigin = sor > 0 ? '50% 50%' : '50% 100%';
        });
      }
    };
  };
})();
