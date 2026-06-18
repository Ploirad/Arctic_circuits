/* =========================================================================
 * states.js — Estados concretos del juego + estado runtime compartido.
 *
 * GameState : datos mutables de la partida (vidas, dinero, velocidad...).
 * States    : definiciones {enter,update,render} para la StateMachine.
 * UI        : helpers de dibujo (texto pixelado, paneles, HUD).
 *
 * `fsm` es la instancia global creada en game.js; los estados la usan para
 * disparar transiciones con fsm.send('evento').
 * ====================================================================== */

// --------------------------------------------------------------------------
// Estado runtime de la partida
// --------------------------------------------------------------------------
const GameState = {
  lives: 0,
  money: 0,
  speed: 0,          // velocidad actual (unidades/seg)
  position: 0,       // posicion z en la pista (envuelve con la longitud)
  distance: 0,       // distancia TOTAL recorrida (no envuelve) -> dinero y rondas
  roundStartDistance: 0, // distancia al empezar la ronda actual
  roundTarget: 0,    // distancia que hay que recorrer para llegar a la gasolinera
  playerX: 0,        // desplazamiento lateral (-1..1 ~ bordes)
  turbo: 100,        // deposito de turbo (0..maxTurbo)
  maxTurbo: 100,
  turboActive: false,
  invincible: 0,     // segundos de invencibilidad restantes tras un choque
  round: 1,
  enemies: [],
  upgrades: { engine: 0, armor: 0, turbo: 0, turret: false },
  turretTimer: 0,
  flicker: false,

  // Reinicia una partida nueva desde cero (las mejoras tambien se resetean).
  reset() {
    this.upgrades = { engine: 0, armor: 0, turbo: 0, turret: false };
    this.lives = CONFIG.rules.startLives;
    this.money = 0;
    this.speed = 0;
    this.position = 0;
    this.distance = 0;
    this.playerX = 0;
    this.maxTurbo = 100;
    this.turbo = this.maxTurbo;
    this.turboActive = false;
    this.invincible = 0;
    this.round = 1;
    this.startRound();
    this.turretTimer = 0;
    this.spawnEnemies();
  },

  // Marca el inicio de una ronda: fija el objetivo de distancia a recorrer.
  startRound() {
    this.roundStartDistance = this.distance;
    // Distancia ~= velocidad punta (sin turbo) * segundos objetivo.
    this.roundTarget = CONFIG.player.maxSpeed * CONFIG.rules.gasStationSeconds;
  },

  // Progreso hacia la gasolinera de la ronda actual (0..1).
  roundProgress() {
    return Math.min(1, (this.distance - this.roundStartDistance) / this.roundTarget);
  },

  // Limite de velocidad efectivo segun mejoras de motor y turbo.
  maxSpeed() {
    const base = CONFIG.player.maxSpeed * (1 + this.upgrades.engine * 0.15);
    return this.turboActive ? base * CONFIG.player.turboMultiplier : base;
  },

  spawnEnemies() {
    this.enemies = [];
    const skins = CONFIG.carSkins.enemies;
    for (let i = 0; i < CONFIG.rules.enemyCount; i++) {
      this.enemies.push({
        z: (i + 2) * Road.segmentLength * 30,
        offset: (Math.random() * 1.6) - 0.8,
        speed: CONFIG.player.maxSpeed * (0.25 + Math.random() * 0.25),
        skin: skins[i % skins.length],
        alive: true,
      });
    }
  },

  // Reaparece un rival lejos del jugador (tras destruirlo o adelantarlo).
  respawnEnemy(car) {
    car.z = (this.position + Road.trackLength * (0.45 + Math.random() * 0.4)) % Road.trackLength;
    car.offset = (Math.random() * 1.6) - 0.8;
    car.alive = true;
  },
};

// --------------------------------------------------------------------------
// Helpers de UI (texto/paneles estilo 16-bit)
// --------------------------------------------------------------------------
const UI = {
  text(ctx, str, x, y, size, color, align) {
    ctx.save();
    ctx.font = `${size}px "Courier New", monospace`;
    ctx.textAlign = align || 'left';
    ctx.textBaseline = 'top';
    // Sombra dura (look pixel)
    ctx.fillStyle = CONFIG.colors.hudShadow;
    ctx.fillText(str, x + 1, y + 1);
    ctx.fillStyle = color || CONFIG.colors.hud;
    ctx.fillText(str, x, y);
    ctx.restore();
  },

  panel(ctx, x, y, w, h) {
    ctx.save();
    ctx.fillStyle = 'rgba(10,12,24,0.82)';
    ctx.fillRect(x, y, w, h);
    ctx.strokeStyle = CONFIG.colors.accent;
    ctx.lineWidth = 2;
    ctx.strokeRect(x + 1, y + 1, w - 2, h - 2);
    ctx.restore();
  },

  // Cielo con degradado simple
  sky(ctx) {
    const g = ctx.createLinearGradient(0, 0, 0, CONFIG.height * 0.6);
    g.addColorStop(0, CONFIG.colors.skyDark);
    g.addColorStop(1, CONFIG.colors.sky);
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, CONFIG.width, CONFIG.height);
  },

  hud(ctx) {
    const W = CONFIG.width;
    const C = CONFIG.colors;
    // Velocidad (km/h "de pega")
    const kmh = Math.round((GameState.speed / CONFIG.player.maxSpeed) * 320);
    UI.text(ctx, `${kmh} KM/H`, 8, 6, 14, C.accent);
    if (GameState.turboActive) UI.text(ctx, 'TURBO!', 8, 22, 10, '#ff7b1f');

    // Vidas
    UI.text(ctx, 'VIDAS ' + '♥'.repeat(Math.max(0, GameState.lives)), 8, CONFIG.height - 18, 12, '#ff5b6b');

    // Dinero
    UI.text(ctx, `$${Math.floor(GameState.money)}`, W - 8, 6, 14, '#7bff8f', 'right');

    // Progreso de DISTANCIA hacia la gasolinera (sustituye al cronometro)
    const prog = GameState.roundProgress();
    UI.text(ctx, `RONDA ${GameState.round}  ⛽ ${Math.floor(prog * 100)}%`, W - 8, 22, 10, C.hud, 'right');
    const px = W - 88, py = 36, pw = 80, ph = 5;
    ctx.fillStyle = '#202030'; ctx.fillRect(px, py, pw, ph);
    ctx.fillStyle = C.accent; ctx.fillRect(px, py, pw * prog, ph);

    // Barra de turbo
    const bx = W - 88, by = CONFIG.height - 16, bw = 80, bh = 8;
    ctx.fillStyle = '#202030'; ctx.fillRect(bx, by, bw, bh);
    ctx.fillStyle = '#ffae3f';
    ctx.fillRect(bx, by, bw * (GameState.turbo / GameState.maxTurbo), bh);
    ctx.strokeStyle = '#000'; ctx.strokeRect(bx, by, bw, bh);
    UI.text(ctx, 'TURBO', bx, by - 11, 8, C.hud);
  },
};

// --------------------------------------------------------------------------
// Render compartido de la escena de conduccion (carretera + coches)
// --------------------------------------------------------------------------
function renderDrivingScene(ctx) {
  UI.sky(ctx);
  // La carretera dibuja tambien los rivales situados sobre el asfalto.
  Road.render(ctx, GameState.position, GameState.playerX, GameState.enemies);

  // Coche del jugador (vista trasera, fijo abajo-centro)
  const steer = (Input.held('left') ? -1 : 0) + (Input.held('right') ? 1 : 0);
  const cx = CONFIG.width / 2;
  const cy = CONFIG.height - 18;
  if (GameState.turboActive) Sprites.turboFlames(ctx, cx, cy, 1, GameState.flicker);

  // Durante la invencibilidad el coche parpadea (se atenua en flancos).
  const blink = GameState.invincible > 0 && GameState.flicker;
  Sprites.playerCar(ctx, cx, cy, 1, steer, CONFIG.carSkins.player, blink);
}

// --------------------------------------------------------------------------
// Definicion de los estados
// --------------------------------------------------------------------------
const States = {

  // ---- MainMenu (estado inicial) ----
  MainMenu: {
    enter() { Input.flush(); },
    update() {
      if (Input.pressed('accept')) { GameState.reset(); fsm.send('Start Game'); }
    },
    render(ctx) {
      UI.sky(ctx);
      Road.render(ctx, 0, 0);
      UI.panel(ctx, 60, 60, CONFIG.width - 120, 150);
      UI.text(ctx, 'ARTIC CIRCUITS', CONFIG.width / 2, 80, 28, CONFIG.colors.accent, 'center');
      UI.text(ctx, 'Prototipo 16-bit · OutRun / F-Zero', CONFIG.width / 2, 112, 11, CONFIG.colors.hud, 'center');
      UI.text(ctx, '> PULSA ENTER PARA EMPEZAR <', CONFIG.width / 2, 150,
        14, GameState.flicker ? '#7bff8f' : CONFIG.colors.hud, 'center');
      UI.text(ctx, 'Flechas/WASD conducir · Shift turbo · P pausa', CONFIG.width / 2, 178, 9, '#9aa0c0', 'center');
    },
  },

  // ---- Playing (jugando) ----
  Playing: {
    enter() { Input.flush(); },
    update(dt) {
      const P = CONFIG.player;
      const G = GameState;

      // Pausa -> vuelve al menu (segun diagrama)
      if (Input.pressed('pause')) { fsm.send('Pause'); return; }

      // --- Invencibilidad (frames de gracia tras un choque) ---
      if (G.invincible > 0) G.invincible = Math.max(0, G.invincible - dt);

      // --- Turbo ---
      G.turboActive = Input.held('turbo') && G.turbo > 0;
      if (G.turboActive) G.turbo = Math.max(0, G.turbo - P.turboBurnPerSec * dt);
      else G.turbo = Math.min(G.maxTurbo, G.turbo + P.turboRegenPerSec * dt);

      // --- Aceleracion / frenado ---
      const max = G.maxSpeed();
      if (Input.held('up')) G.speed += P.accel * max * dt;
      else if (Input.held('down')) G.speed += P.breaking * max * dt;
      else G.speed += P.decel * max * dt;

      // Penalizacion fuera de carretera
      const offRoad = Math.abs(G.playerX) > 1;
      if (offRoad && G.speed > P.offRoadLimit)
        G.speed += P.offRoadDecel * max * dt;

      G.speed = Math.max(0, Math.min(G.speed, max));

      // --- Direccion ---
      const speedPct = G.speed / CONFIG.player.maxSpeed;
      const dx = dt * P.steerResponse * speedPct;
      if (Input.held('left')) G.playerX -= dx;
      if (Input.held('right')) G.playerX += dx;

      // Fuerza centrifuga de la curva actual
      const seg = Road.findSegment(G.position);
      G.playerX -= dx * speedPct * seg.curve * P.centrifugal;
      G.playerX = Math.max(-2, Math.min(2, G.playerX));

      // --- Avance en la pista (distancia para dinero/rondas) ---
      const moved = G.speed * dt;            // distancia recorrida este frame
      G.position = (G.position + moved) % Road.trackLength;
      G.distance += moved;

      // --- Rivales ---
      this.updateEnemies(dt);

      // --- Torreta automatica (mejora): destruye un rival cada 15s ---
      if (G.upgrades.turret) {
        G.turretTimer += dt;
        if (G.turretTimer >= 15) {
          G.turretTimer = 0;
          if (G.enemies.length) G.respawnEnemy(G.enemies[0]); // lo "elimina" y reaparece lejos
        }
      }

      // --- Economia: dinero por DISTANCIA (x2 con turbo, 0 si no avanzas) ---
      let earn = moved * CONFIG.rules.moneyPerDistance;
      if (G.turboActive) earn *= CONFIG.rules.turboMoneyMultiplier;
      G.money += earn;

      // --- Llegada a la gasolinera por DISTANCIA -> RoundComplete ---
      if (G.distance - G.roundStartDistance >= G.roundTarget) {
        fsm.send('Reached Gas Station');
        return;
      }
    },

    updateEnemies(dt) {
      const G = GameState;
      const COL = CONFIG.rules.collision;
      const invincible = G.invincible > 0;

      for (const car of G.enemies) {
        car.z = (car.z + car.speed * dt) % Road.trackLength;

        // Distancia relativa al jugador (con wrap de pista)
        let rel = car.z - G.position;
        if (rel < -Road.trackLength / 2) rel += Road.trackLength;
        if (rel > Road.trackLength / 2) rel -= Road.trackLength;

        // Colision con hitbox ajustada al tamaño visual de los coches.
        if (!invincible) {
          const inZ = rel <= COL.zAhead * Road.segmentLength &&
                      rel >= -COL.zBehind * Road.segmentLength;
          const overlap = Math.abs(car.offset - G.playerX) < COL.lateral;
          if (inZ && overlap) {
            G.respawnEnemy(car);            // el rival contra el que chocas se destruye
            fsm.send('Collision Detected');
            return;
          }
        }

        // Reaparece por delante si quedo muy atras
        if (rel < -Road.segmentLength * 40) G.respawnEnemy(car);
      }
    },

    render(ctx) {
      renderDrivingScene(ctx);
      UI.hud(ctx);
    },
  },

  // ---- Crashed (choque) ----
  Crashed: {
    timer: 0,
    enter() {
      this.timer = 0;
      GameState.lives -= 1;
      GameState.speed *= CONFIG.rules.crashSpeedPenalty;
      Input.flush();
    },
    update(dt) {
      this.timer += dt;
      if (this.timer < 1.4) return;            // breve pausa dramatica
      // Decision segun vidas (Lives > 0  vs  Lives = 0)
      if (GameState.lives > 0) {
        GameState.playerX = 0;
        GameState.invincible = CONFIG.rules.invincibleSec; // frames de gracia
        fsm.send('Lives > 0');
      } else {
        fsm.send('Lives = 0');
      }
    },
    render(ctx) {
      renderDrivingScene(ctx);
      UI.hud(ctx);
      ctx.save();
      ctx.fillStyle = `rgba(200,40,40,${0.35 + 0.25 * Math.sin(this.timer * 20)})`;
      ctx.fillRect(0, 0, CONFIG.width, CONFIG.height);
      ctx.restore();
      UI.text(ctx, '¡CHOQUE!', CONFIG.width / 2, CONFIG.height / 2 - 16, 28, '#fff', 'center');
    },
  },

  // ---- GameOver ----
  GameOver: {
    enter() { Input.flush(); },
    update() { if (Input.pressed('accept')) fsm.send('Game Over'); },
    render(ctx) {
      UI.sky(ctx);
      UI.panel(ctx, 70, 70, CONFIG.width - 140, 130);
      UI.text(ctx, 'GAME OVER', CONFIG.width / 2, 92, 30, '#ff5b6b', 'center');
      UI.text(ctx, `Dinero final: $${Math.floor(GameState.money)}`, CONFIG.width / 2, 130, 12, CONFIG.colors.hud, 'center');
      UI.text(ctx, 'ENTER para volver al menu', CONFIG.width / 2, 160, 11, '#9aa0c0', 'center');
    },
  },

  // ---- RoundComplete ----
  RoundComplete: {
    enter() { GameState.speed *= 0.5; Input.flush(); },
    update() { if (Input.pressed('accept')) fsm.send('Enter Safe Zone'); },
    render(ctx) {
      renderDrivingScene(ctx);
      UI.panel(ctx, 70, 80, CONFIG.width - 140, 110);
      UI.text(ctx, '¡RONDA COMPLETADA!', CONFIG.width / 2, 100, 20, CONFIG.colors.accent, 'center');
      UI.text(ctx, `Bonus: $${GameState.round * 100}`, CONFIG.width / 2, 132, 12, '#7bff8f', 'center');
      UI.text(ctx, 'ENTER: Entrar a Zona Segura', CONFIG.width / 2, 158, 11, '#9aa0c0', 'center');
    },
  },

  // ---- RestPeriod (zona de descanso) ----
  RestPeriod: {
    enter() {
      GameState.money += GameState.round * 100; // bonus de ronda
      GameState.round += 1;
      GameState.startRound();                   // nuevo objetivo de distancia
      Input.flush();
    },
    update() {
      if (Input.pressed('accept')) fsm.send('Continue Driving');
      if (Input.held('down') || Input.pressed('opt1')) fsm.send('Drive to Gas Station');
    },
    render(ctx) {
      UI.sky(ctx);
      Road.render(ctx, GameState.position, 0);
      UI.panel(ctx, 60, 70, CONFIG.width - 120, 130);
      UI.text(ctx, 'ZONA DE DESCANSO', CONFIG.width / 2, 86, 18, CONFIG.colors.accent, 'center');
      UI.text(ctx, 'ENTER: Seguir conduciendo', CONFIG.width / 2, 124, 12, '#7bff8f', 'center');
      UI.text(ctx, 'ABAJO: Ir a la Gasolinera', CONFIG.width / 2, 146, 12, CONFIG.colors.hud, 'center');
    },
  },

  // ---- GasStation ----
  GasStation: {
    enter() { Input.flush(); },
    update() {
      if (Input.pressed('accept')) fsm.send('Stop at Station');
      if (Input.held('up') || Input.pressed('back')) fsm.send('Continue Driving');
    },
    render(ctx) {
      UI.sky(ctx);
      ctx.fillStyle = '#2a2a3a';
      ctx.fillRect(0, CONFIG.height * 0.6, CONFIG.width, CONFIG.height * 0.4);
      UI.panel(ctx, 60, 60, CONFIG.width - 120, 150);
      UI.text(ctx, '⛽ GASOLINERA', CONFIG.width / 2, 80, 20, CONFIG.colors.accent, 'center');
      UI.text(ctx, `Dinero: $${Math.floor(GameState.money)}`, CONFIG.width / 2, 112, 12, '#7bff8f', 'center');
      UI.text(ctx, 'ENTER: Parar en la Tienda', CONFIG.width / 2, 140, 12, CONFIG.colors.hud, 'center');
      UI.text(ctx, 'ARRIBA: Seguir conduciendo', CONFIG.width / 2, 162, 11, '#9aa0c0', 'center');
    },
  },

  // ---- ShopMenu (tienda de mejoras) ----
  ShopMenu: {
    enter() { Input.flush(); },
    update() {
      // Compras: "Buy X" -> vuelve a GasStation (segun diagrama)
      const buy = (idx) => {
        const item = CONFIG.shop[idx];
        if (GameState.money >= item.cost) {
          GameState.money -= item.cost;
          this.applyUpgrade(item.id);
          fsm.send('Buy ' + item.name);  // -> GasStation
        }
      };
      if (Input.pressed('opt1')) buy(0);
      else if (Input.pressed('opt2')) buy(1);
      else if (Input.pressed('opt3')) buy(2);
      else if (Input.pressed('opt4')) buy(3);
      else if (Input.pressed('accept')) fsm.send('Exit Shop'); // -> Playing
    },
    applyUpgrade(id) {
      const G = GameState;
      if (id === 'engine') G.upgrades.engine += 1;
      else if (id === 'armor') { G.upgrades.armor += 1; G.lives += 1; }
      else if (id === 'turbo') { G.upgrades.turbo += 1; G.maxTurbo += 50; G.turbo = G.maxTurbo; }
      else if (id === 'turret') G.upgrades.turret = true;
    },
    render(ctx) {
      UI.sky(ctx);
      UI.panel(ctx, 30, 24, CONFIG.width - 60, CONFIG.height - 48);
      UI.text(ctx, 'TIENDA', CONFIG.width / 2, 34, 20, CONFIG.colors.accent, 'center');
      UI.text(ctx, `Dinero: $${Math.floor(GameState.money)}`, CONFIG.width / 2, 58, 11, '#7bff8f', 'center');

      CONFIG.shop.forEach((item, i) => {
        const y = 84 + i * 32;
        const afford = GameState.money >= item.cost;
        UI.text(ctx, `[${i + 1}] ${item.name}`, 50, y, 13, afford ? CONFIG.colors.hud : '#666');
        UI.text(ctx, `$${item.cost}`, CONFIG.width - 50, y, 13, afford ? '#7bff8f' : '#aa5555', 'right');
        UI.text(ctx, item.desc, 60, y + 14, 9, '#9aa0c0');
      });

      UI.text(ctx, 'ENTER: Salir de la tienda (volver a conducir)',
        CONFIG.width / 2, CONFIG.height - 34, 10, CONFIG.colors.accent, 'center');
    },
  },
};
