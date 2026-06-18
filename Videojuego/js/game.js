/* =========================================================================
 * game.js — Bootstrap: cablea la maquina de estados, monta el bucle
 * principal (requestAnimationFrame con delta-time) y arranca en MainMenu.
 * ====================================================================== */

let fsm; // instancia global usada por los estados

(function main() {
  const canvas = document.getElementById('game');
  const ctx = canvas.getContext('2d');
  ctx.imageSmoothingEnabled = false; // pixeles duros (look 16-bit)

  // Construir la pista una sola vez.
  Road.build();

  // Cargar imagenes (coches, gasolinera, cartel, fondo).
  Assets.loadAll();

  /* --- Cablear la maquina de estados ------------------------------------
   * La gasolinera/zona de descanso del diagrama original (RoundComplete ->
   * RestPeriod -> GasStation) se ha unificado en una GASOLINERA FISICA: la
   * estacion aparece al borde de la carretera durante Playing y, al frenar
   * junto a ella, "Stop at Station" abre la tienda. Por eso Playing conecta
   * directamente con ShopMenu y al salir vuelve a Playing.
   * -------------------------------------------------------------------- */
  fsm = new StateMachine();

  fsm.addState('MainMenu', States.MainMenu, {
    'Start Game': 'Playing',
  });
  fsm.addState('Playing', States.Playing, {
    'Collision Detected': 'Crashed',
    'Pause': 'MainMenu',
    'Stop at Station': 'ShopMenu',   // frenar junto a la gasolinera
  });
  fsm.addState('Crashed', States.Crashed, {
    'Lives > 0': 'Playing',
    'Lives = 0': 'GameOver',
  });
  fsm.addState('GameOver', States.GameOver, {
    'Game Over': 'MainMenu',
  });
  fsm.addState('ShopMenu', States.ShopMenu, {
    'Exit Shop': 'Playing',
  });

  fsm.start('MainMenu');

  // --- Bucle principal ---
  let last = performance.now();
  let flickerAcc = 0;

  function frame(now) {
    let dt = (now - last) / 1000; // segundos
    last = now;
    if (dt > 0.05) dt = 0.05;     // clamp (evita saltos tras perder foco)

    // Parpadeo compartido para textos/llamas
    flickerAcc += dt;
    if (flickerAcc > 0.4) { GameState.flicker = !GameState.flicker; flickerAcc = 0; }

    fsm.update(dt);

    ctx.clearRect(0, 0, CONFIG.width, CONFIG.height);
    fsm.render(ctx);

    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);

  // Exponer para depurar desde la consola del navegador.
  window.ARTIC = { fsm, GameState, Road, CONFIG };
})();
