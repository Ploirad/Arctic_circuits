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
    fogDensity: 4,        // densidad de la niebla en el horizonte
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

  /* --- Reglas de juego --------------------------------------------------
   * MEDIDAS TEORICAS DE DISTANCIA (ronda a ronda):
   *   roundTarget = maxSpeed * gasStationSeconds = 12000 * 30 = 360 000 ud.
   *   Escala: maxSpeed (12000 ud/s) equivale a 320 km/h => 88,9 m/s,
   *           luego 1 ud ≈ 0,00741 m.
   *   => Cada ronda son ~360 000 ud ≈ 2 667 m ≈ 2,67 km de conduccion.
   *   La pista mide 1310 segmentos * 200 = 262 000 ud ≈ 1,94 km (1 vuelta),
   *   asi que una ronda equivale a ~1,37 vueltas a la pista.
   * -------------------------------------------------------------------- */
  rules: {
    startLives: 3,

    // Llegar a la gasolinera se mide por DISTANCIA (no por tiempo):
    // equivale a ~N segundos a velocidad punta SIN turbo.
    gasStationSeconds: 30,

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

    // Gasolinera fisica al borde de la carretera (te acercas y frenas).
    station: {
      offset: 1.85,           // posicion lateral (>1 = fuera de la carretera, dcha)
      signLeadDistance: 9000, // a que distancia antes aparece el cartel
      signOffset: 1.5,        // posicion lateral del cartel
      interactSpeed: 2200,    // velocidad max para poder interactuar (hay que frenar)
      interactBefore: 4000,   // margen de distancia ANTES de la estacion
      interactAfter: 16000,   // margen DESPUES (zona generosa para frenar)
      roundBonus: 100,        // bonus de dinero por ronda al repostar
    },
  },

  // --- Catalogo de mejoras de la tienda (ShopMenu) ---
  // once:true  -> solo se puede comprar una vez.
  shop: [
    { id: 'engine',  name: 'Mejora de Motor',    cost: 500,   desc: '+ velocidad punta' },
    { id: 'armor',   name: 'Blindaje',           cost: 400,   desc: '+1 vida extra' },
    { id: 'turbo',   name: 'Capacidad de Turbo', cost: 350,   desc: '+ deposito de turbo' },
    { id: 'turret',  name: 'Torreta Automatica', cost: 5000,  desc: 'elimina 1 coche / 15s', once: true },
  ],

  /* --- Aspecto de los coches (skins) -----------------------------------
   * Cada skin referencia una imagen (src). assets.js la carga en skin.image.
   * Sprites dibuja la imagen; si aun no ha cargado usa el color de respaldo.
   * Para cambiar un coche: cambia su 'src' (o añade entradas a enemies[]).
   * -------------------------------------------------------------------- */
  carSkins: {
    player: { src: 'assets/player_delorean.png', image: null, fallback: '#d4342f' },
    enemies: [
      { name: 'Azul',       src: 'assets/enemy_azul.png',       image: null, fallback: '#3f7fff' },
      { name: 'Blanco',     src: 'assets/enemy_blanco.png',     image: null, fallback: '#e8e8e8' },
      { name: 'Negro',      src: 'assets/enemy_negro.png',      image: null, fallback: '#2a2a30' },
      { name: 'Furgon',     src: 'assets/enemy_furgon.png',     image: null, fallback: '#c8c8c8' },
      { name: 'Ferrario',   src: 'assets/enemy_ferrario.png',   image: null, fallback: '#e02020' },
      { name: 'Fantastico', src: 'assets/enemy_fantastico.png', image: null, fallback: '#202020' },
      { name: 'GruasPaco',  src: 'assets/enemy_gruas.png',      image: null, fallback: '#f0a020' },
      { name: 'Caza',       src: 'assets/enemy_caza.png',       image: null, fallback: '#d0d0d0' },
      { name: 'EquipoA',    src: 'assets/enemy_equipoa.png',    image: null, fallback: '#404040' },
    ],
  },

  // --- Otros assets de escena (cargados en assets.js) ---
  assets: {
    horizon: { src: 'assets/bg_horizon.png', image: null },
    station: { src: 'assets/gas_station.png', image: null },
    sign:    { src: 'assets/sign_gas.png',    image: null },
  },

  // --- Paleta 16-bit (terreno mas vivo, inspirado en la referencia) ---
  colors: {
    sky:      '#5aa0e0',
    skyDark:  '#2a6ec0',
    fog:      '#9ec8e8',
    grassLight: '#5fb83f',
    grassDark:  '#3f9e2c',
    roadLight:  '#5c5c66',
    roadDark:   '#525258',
    rumbleLight:'#f0f0f4',
    rumbleDark: '#d83232',
    laneMarker: '#f0f0f4',
    hud:        '#f0f0f0',
    hudShadow:  '#101018',
    accent:     '#ffd23f',
  },
};
