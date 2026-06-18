/* =========================================================================
 * input.js — Gestion de teclado.
 * Expone Input.held(action) para estado continuo y Input.pressed(action)
 * para eventos de una sola pulsacion (consumidos al leerlos).
 * ====================================================================== */

const Input = (() => {
  // Mapa: codigo de tecla -> accion logica
  const KEY_MAP = {
    ArrowUp: 'up', KeyW: 'up',
    ArrowDown: 'down', KeyS: 'down',
    ArrowLeft: 'left', KeyA: 'left',
    ArrowRight: 'right', KeyD: 'right',
    ShiftLeft: 'turbo', ShiftRight: 'turbo',
    Space: 'accept', Enter: 'accept',
    KeyP: 'pause', Escape: 'back',
    Digit1: 'opt1', Digit2: 'opt2', Digit3: 'opt3', Digit4: 'opt4',
  };

  const down = {};        // acciones mantenidas
  const edgeQueue = {};   // acciones recien pulsadas (pendientes de consumir)

  window.addEventListener('keydown', (e) => {
    const action = KEY_MAP[e.code];
    if (!action) return;
    e.preventDefault();
    if (!down[action]) edgeQueue[action] = true; // flanco de subida
    down[action] = true;
  });

  window.addEventListener('keyup', (e) => {
    const action = KEY_MAP[e.code];
    if (!action) return;
    down[action] = false;
  });

  return {
    held(action) { return !!down[action]; },

    // Devuelve true una sola vez por pulsacion (consume el evento).
    pressed(action) {
      if (edgeQueue[action]) { delete edgeQueue[action]; return true; }
      return false;
    },

    // Limpia eventos pendientes (util al cambiar de estado).
    flush() { for (const k in edgeQueue) delete edgeQueue[k]; },
  };
})();
