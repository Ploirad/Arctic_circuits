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

  // --- Cablear la maquina de estados segun el diagrama ---
  fsm = new StateMachine();

  // Transiciones de compra: cada "Buy X" vuelve a la gasolinera.
  const buyTransitions = {};
  for (const item of CONFIG.shop) buyTransitions['Buy ' + item.name] = 'GasStation';

  fsm.addState('MainMenu', States.MainMenu, {
    'Start Game': 'Playing',
  });
  fsm.addState('Playing', States.Playing, {
    'Collision Detected': 'Crashed',
    'Pause': 'MainMenu',
    'Reached Gas Station': 'RoundComplete', // ahora por distancia, no por tiempo
  });
  fsm.addState('Crashed', States.Crashed, {
    'Lives > 0': 'Playing',
    'Lives = 0': 'GameOver',
  });
  fsm.addState('GameOver', States.GameOver, {
    'Game Over': 'MainMenu',
  });
  fsm.addState('RoundComplete', States.RoundComplete, {
    'Enter Safe Zone': 'RestPeriod',
  });
  fsm.addState('RestPeriod', States.RestPeriod, {
    'Continue Driving': 'Playing',
    'Drive to Gas Station': 'GasStation',
  });
  fsm.addState('GasStation', States.GasStation, {
    'Stop at Station': 'ShopMenu',
    'Continue Driving': 'Playing',
  });
  fsm.addState('ShopMenu', States.ShopMenu, Object.assign({
    'Exit Shop': 'Playing',
  }, buyTransitions));

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
