/* =========================================================================
 * config.js — Constantes globales del prototipo.
 * Todo lo "ajustable" del juego vive aqui para iterar rapido.
 * ====================================================================== */

const CONFIG = {
  // --- Resolucion interna (look 16-bit). El CSS la escala a x2. ---
  width: 480,
  height: 270,

  // --- Render pseudo-3D de la carretera (estilo OutRun) ---
  road: {
    segmentLength: 200,   // longitud (z) de cada segmento de carretera
    rumbleLength: 3,      // nº de segmentos por banda de color del arcen
    roadWidth: 1100,      // mitad de la anchura de la carretera (unidades mundo)
    lanes: 3,             // nº de carriles
    drawDistance: 220,    // cuantos segmentos dibujar hacia delante
    fieldOfView: 100,     // grados
    cameraHeight: 1000,   // altura de la camara sobre la carretera
    fogDensity: 5,        // densidad de la niebla en el horizonte
  },

  // --- Fisica del coche del jugador ---
  player: {
    maxSpeed: 12000,        // velocidad punta (unidades/seg)
    accel: 0.85,            // fraccion de maxSpeed alcanzada por segundo
    breaking: -2.2,         // desaceleracion al frenar
    decel: -0.55,           // desaceleracion al soltar gas
    offRoadDecel: -0.9,     // desaceleracion fuera de la carretera
    offRoadLimit: 4000,     // velocidad maxima fuera de la carretera
    steerResponse: 2.4,     // respuesta de giro (carriles/seg a tope)
    centrifugal: 0.45,      // cuanto te empuja la curva hacia fuera
    turboMultiplier: 1.7,   // multiplicador de velocidad punta con turbo
    turboBurnPerSec: 28,    // gasto de turbo por segundo en uso
    turboRegenPerSec: 6,    // regeneracion de turbo por segundo
  },

  // --- Reglas de juego (ligadas a la maquina de estados) ---
  rules: {
    startLives: 3,

    // Llegar a la gasolinera se mide por DISTANCIA, no por tiempo.
    // El objetivo equivale a ~N segundos a velocidad punta SIN turbo.
    gasStationSeconds: 30,    // segundos de conduccion a tope para "llegar"

    crashSpeedPenalty: 0.25,  // velocidad que conservas tras chocar
    invincibleSec: 2.8,       // invencibilidad tras revivir (frames de gracia)

    // Dinero por DISTANCIA recorrida (si el coche no avanza, no se gana).
    moneyPerDistance: 0.003,  // dinero por unidad de distancia
    turboMoneyMultiplier: 2,  // x2 de dinero mientras el turbo esta activo

    enemyCount: 6,            // coches rivales en pista a esquivar

    // Hitbox de colision (calibrada al tamaño visual de los coches).
    collision: {
      lateral: 0.20,          // solape lateral max (suma de semianchos, en offset)
      zAhead: 1.1,            // alcance por delante (en segmentos)
      zBehind: 0.4,           // alcance por detras (en segmentos)
    },
  },

  // --- Catalogo de mejoras de la tienda (ShopMenu) ---
  shop: [
    { id: 'engine',  name: 'Mejora de Motor',     cost: 500,  desc: '+ velocidad punta' },
    { id: 'armor',   name: 'Blindaje',            cost: 400,  desc: '+1 vida extra' },
    { id: 'turbo',   name: 'Capacidad de Turbo',  cost: 350,  desc: '+ deposito de turbo' },
    { id: 'turret',  name: 'Torreta Automatica',  cost: 800,  desc: 'elimina 1 coche / 15s' },
  ],

  // --- Aspecto de los coches (preparado para ampliar/sustituir) ---
  // Cada "skin" describe los colores del coche dibujado por procedimiento.
  // Para usar arte real en el futuro, asigna skin.image = <HTMLImageElement>
  // (y opcionalmente frameW/frameH); Sprites lo dibujara en vez de los rects.
  carSkins: {
    // Coche del jugador
    player: {
      image: null, frameW: 0, frameH: 0,
      body: '#d4342f', shadow: '#a82723', cabin: '#1a2a3a',
      wing: '#2a2a30', wheel: '#101014',
      lightL: '#ffcf3f', lightR: '#ff3b3b',
    },
    // Pool de skins para los rivales (se reparten ciclicamente)
    enemies: [
      { image: null, body: '#3f7fff', shadow: '#2a5ad0', cabin: '#13243a', wing: '#1c1c24', wheel: '#101014', light: '#ff5050' },
      { image: null, body: '#ffae3f', shadow: '#d08a25', cabin: '#3a2a13', wing: '#241c1c', wheel: '#101014', light: '#ff5050' },
      { image: null, body: '#9b3fff', shadow: '#7325d0', cabin: '#2a133a', wing: '#1c1c24', wheel: '#101014', light: '#ff5050' },
      { image: null, body: '#3fffa0', shadow: '#25d07f', cabin: '#133a2a', wing: '#1c241c', wheel: '#101014', light: '#ff5050' },
      { image: null, body: '#ff3f8f', shadow: '#d0256f', cabin: '#3a1326', wing: '#241c20', wheel: '#101014', light: '#ffcf3f' },
      { image: null, body: '#cccccc', shadow: '#9a9a9a', cabin: '#222232', wing: '#1c1c24', wheel: '#101014', light: '#ff5050' },
    ],
  },

  // --- Paleta 16-bit ---
  colors: {
    sky:      '#3a6ea5',
    skyDark:  '#1c3a5e',
    fog:      '#80a0c0',
    grassLight: '#2e8b3d',
    grassDark:  '#1f6b2c',
    roadLight:  '#6b6b7b',
    roadDark:   '#5a5a6a',
    rumbleLight:'#e8e8f0',
    rumbleDark: '#c83232',
    laneMarker: '#e8e8f0',
    hud:        '#f0f0f0',
    hudShadow:  '#101018',
    accent:     '#ffd23f',
  },
};
