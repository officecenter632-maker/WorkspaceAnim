/* Moteur commun : une seule horloge (secondes), une scène 1672 x 941 mise à l'échelle de la fenêtre.
   Aucune bibliothèque externe. Tout est fonction du temps t : on peut donc glisser le curseur librement. */
(function () {
  var L = 1672, H = 941;
  var Anim = window.Anim = {
    L: L, H: H, t: 0, duree: 0, lecture: false, scenes: [],
    clamp: function (x, a, b) { return Math.max(a, Math.min(b, x)); },
    /* progression 0..1 d'un geste qui commence à t0 et dure d secondes */
    prog: function (t, t0, d) { return Anim.clamp((t - t0) / d, 0, 1); },
    facile: {
      sortie3: function (x) { return 1 - Math.pow(1 - x, 3); },
      sortie4: function (x) { return 1 - Math.pow(1 - x, 4); },
      entree3: function (x) { return x * x * x; },
      /* dépasse un peu puis se pose : le petit rebond */
      rebond: function (x) { var c1 = 1.4, c3 = c1 + 1; return 1 + c3 * Math.pow(x - 1, 3) + c1 * Math.pow(x - 1, 2); }
    },
    el: function (tag, css, parent) {
      var e = document.createElement(tag);
      if (css) e.style.cssText = css;
      if (parent) parent.appendChild(e);
      return e;
    },
    ajouterScene: function (s) {
      Anim.scenes.push(s);
      Anim.duree = Math.max(Anim.duree, s.fin);
    },
    demarrer: function () {
      var scene = document.getElementById('scene');
      var monde = Anim.el('div', 'position:absolute;left:0;top:0;width:' + L + 'px;height:' + H + 'px;transform-origin:836px 660px', scene);
      var code = Anim.el('div', 'position:absolute;left:0;top:0;width:' + L + 'px;height:' + H + 'px', scene);
      Anim.monde = monde; Anim.code = code;
      Anim.scenes.forEach(function (s) { s.monter(monde, code); });
      Anim.cadrer(); window.addEventListener('resize', Anim.cadrer);
      Anim.brancher(); Anim.aller(0);
      var dernier = null;
      function boucle(ms) {
        if (Anim.lecture) {
          if (dernier !== null) Anim.aller(Anim.t + (ms - dernier) / 1000);
          if (Anim.t >= Anim.duree) { Anim.aller(Anim.duree); Anim.pause(); }
        }
        dernier = ms; requestAnimationFrame(boucle);
      }
      requestAnimationFrame(boucle);
      Anim.jouer();
    },
    cadrer: function () {
      var f = document.getElementById('fenetre'), s = document.getElementById('scene');
      var k = Math.min(f.clientWidth / L, f.clientHeight / H);
      s.style.transform = 'translate(' + ((f.clientWidth - L * k) / 2) + 'px,' + ((f.clientHeight - H * k) / 2) + 'px) scale(' + k + ')';
    },
    aller: function (t) {
      Anim.t = Anim.clamp(t, 0, Anim.duree);
      Anim.scenes.forEach(function (s) { s.maj(Anim.t); });
      var c = Anim.curseur, tx = Anim.texteTemps;
      if (c) c.value = Anim.t;
      if (tx) tx.textContent = Anim.t.toFixed(2) + ' / ' + Anim.duree.toFixed(2) + ' s';
    },
    jouer: function () {
      if (Anim.t >= Anim.duree) Anim.aller(0);
      Anim.lecture = true; if (Anim.bouton) Anim.bouton.textContent = 'Pause';
    },
    pause: function () { Anim.lecture = false; if (Anim.bouton) Anim.bouton.textContent = 'Lecture'; },
    brancher: function () {
      Anim.bouton = document.getElementById('bouton'); Anim.curseur = document.getElementById('curseur');
      Anim.texteTemps = document.getElementById('temps');
      Anim.curseur.max = Anim.duree; Anim.curseur.step = 0.01;
      Anim.bouton.onclick = function () { Anim.lecture ? Anim.pause() : Anim.jouer(); };
      Anim.curseur.oninput = function () { Anim.pause(); Anim.aller(parseFloat(Anim.curseur.value)); };
      document.addEventListener('keydown', function (e) {
        if (e.code === 'Space') { e.preventDefault(); Anim.bouton.click(); }
        if (e.code === 'ArrowRight') { Anim.pause(); Anim.aller(Anim.t + 0.1); }
        if (e.code === 'ArrowLeft') { Anim.pause(); Anim.aller(Anim.t - 0.1); }
      });
    }
  };
})();
