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

  /* carte_donut : carte blanche à droite, anneau bleu déjà tracé, part rouge qui se dessine dans le sens des aiguilles d'une montre depuis le haut,
     texte au centre, titre lettre par lettre. Ne zoome pas avec le décor (calque code).
     o = { x, y, w, h, entree {t0,d}, part {t0,d,vers (0..1)}, centre {t0,texte:[ligne1,ligne2]}, titre {t0,d,texte}, sortie {t0,d} (facultatif) } */
  A.creerDonut = function (parent, o) {
    var carte = A.el('div', 'position:absolute;left:' + o.x + 'px;top:' + o.y + 'px;width:' + o.w + 'px;height:' + o.h + 'px;box-sizing:border-box;background:#fff;border-radius:24px;opacity:0;' + POLICE, parent);
    var titre = A.el('div', 'position:absolute;left:0;right:0;top:26px;text-align:center;font-size:34px;line-height:40px;color:#1b2433;letter-spacing:.5px;white-space:nowrap;', carte);
    var lettres = o.titre.texte.split('').map(function (c) { var sp = A.el('span', 'opacity:0;', titre); sp.textContent = c === ' ' ? '\u00a0' : c; return sp; });
    var D = Math.min(o.w - 90, o.h - 130);
    var svg = A.el('div', 'position:absolute;left:' + (o.w - D) / 2 + 'px;top:' + (88 + (o.h - 88 - D) / 2 - 8) + 'px;width:' + D + 'px;height:' + D + 'px;', carte);
    svg.innerHTML = '<svg viewBox="0 0 200 200" width="100%" height="100%"><circle cx="100" cy="100" r="68" fill="none" stroke="#0b4f8f" stroke-width="44"/>' +
      '<circle id="part" cx="100" cy="100" r="68" fill="none" stroke="#d63a3a" stroke-width="44" pathLength="100" stroke-dasharray="0 100" transform="rotate(-90 100 100)"/></svg>';
    var part = svg.querySelector('#part');
    var centre = A.el('div', 'position:absolute;left:0;top:0;width:100%;height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:' + Math.round(D * 0.085) + 'px;line-height:1.1;color:#1b2433;text-align:center;opacity:0;', svg);
    centre.innerHTML = o.centre.texte.join('<br>');
    return {
      maj: function (t) {
        var ent = F.rebond(A.prog(t, o.entree.t0, o.entree.d)), sor = o.sortie ? F.entree3(A.prog(t, o.sortie.t0, o.sortie.d)) : 0;
        var dx = (A.L - o.x + 40) * (1 - ent) + (o.sortie ? (A.L - o.x + 40) * sor : 0);
        var flotte = t > o.entree.t0 + o.entree.d ? 0.005 * A.H * Math.sin(TAU * t / 3.8 + 1) : 0;
        carte.style.opacity = t < o.entree.t0 ? 0 : 1 - sor;
        carte.style.transform = 'translate(' + dx + 'px,' + flotte + 'px)';
        carte.style.boxShadow = '0 ' + (10 + flotte) + 'px ' + (28 + flotte) + 'px rgba(0,0,0,.28)';
        var p = 100 * o.part.vers * F.sortie3(A.prog(t, o.part.t0, o.part.d));
        part.setAttribute('stroke-dasharray', p + ' ' + (100 - p));
        var c = F.sortie3(A.prog(t, o.centre.t0, 0.4));
        centre.style.opacity = c; centre.style.transform = 'scale(' + (0.9 + 0.1 * c) + ')';
        var n = lettres.length, u = A.prog(t, o.titre.t0, o.titre.d) * n;
        lettres.forEach(function (sp, i) { sp.style.opacity = u > i ? 1 : 0; });
      }
    };
  };

  /* etiquette_record : étiquette blanche à droite avec une flèche rouge montante qui se dessine de sa base vers sa pointe (puis une pulsation de 8 %) et un texte sombre en capitales.
     o = { x, y, w, h, texte, entree {t0,d}, fleche {t0,d}, sortie {t0,d} (facultatif) } */
  A.creerEtiquette = function (parent, o) {
    var carte = A.el('div', 'position:absolute;left:' + o.x + 'px;top:' + o.y + 'px;width:' + o.w + 'px;height:' + o.h + 'px;box-sizing:border-box;padding:0 28px;display:flex;align-items:center;gap:18px;background:#fff;border-radius:20px;opacity:0;' + POLICE, parent);
    var ic = A.el('div', 'flex:none;width:' + Math.round(o.h * 0.9) + 'px;height:' + Math.round(o.h * 0.72) + 'px;', carte);
    ic.innerHTML = '<svg viewBox="0 0 100 80" width="100%" height="100%" overflow="visible"><path id="tige" d="M6 66 L34 40 L52 54 L82 22" fill="none" stroke="#d63a3a" stroke-width="11" stroke-linecap="round" stroke-linejoin="round" pathLength="100" stroke-dasharray="0 100"/>' +
      '<polygon id="tete" points="94,8 86,38 64,18" fill="#d63a3a" stroke="#d63a3a" stroke-width="4" stroke-linejoin="round" opacity="0" style="transform-origin:78px 22px"/></svg>';
    var tige = ic.querySelector('#tige'), tete = ic.querySelector('#tete');
    var tx = A.el('div', 'font-size:' + Math.round(o.h * 0.4) + 'px;color:#1b2433;letter-spacing:.5px;white-space:nowrap;', carte); tx.textContent = o.texte;
    return {
      maj: function (t) {
        var ent = F.rebond(A.prog(t, o.entree.t0, o.entree.d)), sor = o.sortie ? F.entree3(A.prog(t, o.sortie.t0, o.sortie.d)) : 0;
        var dx = (A.L - o.x + 40) * (1 - ent) + (o.sortie ? (A.L - o.x + 40) * sor : 0);
        var flotte = t > o.entree.t0 + o.entree.d ? 0.005 * A.H * Math.sin(TAU * t / 3.4 + 2) : 0;
        carte.style.opacity = t < o.entree.t0 ? 0 : 1 - sor;
        carte.style.transform = 'translate(' + dx + 'px,' + flotte + 'px)';
        carte.style.boxShadow = '0 ' + (10 + flotte) + 'px ' + (28 + flotte) + 'px rgba(0,0,0,.28)';
        var p = F.sortie3(A.prog(t, o.fleche.t0, o.fleche.d));
        tige.setAttribute('stroke-dasharray', (100 * p) + ' 100');
        tete.setAttribute('opacity', p > 0.97 ? 1 : 0);
        var u = A.prog(t, o.fleche.t0 + o.fleche.d, 0.3);
        tete.style.transform = 'scale(' + (1 + 0.08 * Math.sin(Math.PI * u)) + ')';
      }
    };
  };
})();
