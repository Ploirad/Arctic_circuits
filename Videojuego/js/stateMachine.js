/* =========================================================================
 * stateMachine.js — Maquina de estados finita generica.
 * Cada estado es un objeto { enter, update, render, exit }.
 * Las transiciones se declaran por nombre y se disparan con send(evento).
 *
 * Flujo implementado (la gasolinera del diagrama es ahora un objeto fisico
 * al borde de la carretera: te acercas, frenas y "Stop at Station" abre la
 * tienda; eso unifica RoundComplete/RestPeriod/GasStation):
 *   MainMenu --Start Game--> Playing
 *   Playing  --Collision Detected--> Crashed
 *   Crashed  --Lives > 0--> Playing   |  --Lives = 0--> GameOver
 *   GameOver --Game Over--> MainMenu
 *   Playing  --Pause--> MainMenu
 *   Playing  --Stop at Station--> ShopMenu   (frenas junto a la gasolinera)
 *   ShopMenu --Exit Shop--> Playing
 * ====================================================================== */

class StateMachine {
  constructor() {
    this.states = {};        // nombre -> definicion de estado
    this.transitions = {};   // nombre -> { evento: nombreDestino }
    this.current = null;
    this.currentName = null;
    this.history = [];       // traza de transiciones (util para depurar)
  }

  addState(name, def, transitions) {
    this.states[name] = def || {};
    this.transitions[name] = transitions || {};
    return this;
  }

  start(name, payload) {
    this.currentName = name;
    this.current = this.states[name];
    this.history.push(name);
    if (this.current.enter) this.current.enter(payload);
  }

  // Dispara un evento; cambia de estado si existe la transicion.
  send(event, payload) {
    const map = this.transitions[this.currentName];
    const next = map && map[event];
    if (!next) return false; // evento ignorado en este estado
    this._transition(next, event, payload);
    return true;
  }

  _transition(nextName, event, payload) {
    if (this.current && this.current.exit) this.current.exit(nextName);
    this.history.push(`${this.currentName} --${event}--> ${nextName}`);
    this.currentName = nextName;
    this.current = this.states[nextName];
    if (this.current.enter) this.current.enter(payload);
  }

  update(dt) { if (this.current && this.current.update) this.current.update(dt); }
  render(ctx) { if (this.current && this.current.render) this.current.render(ctx); }

  is(name) { return this.currentName === name; }
}
