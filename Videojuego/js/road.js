/* =========================================================================
 * road.js — Carretera pseudo-3D estilo OutRun.
 * La pista es una lista de segmentos con curva (dx) y altura (y). Cada
 * fotograma se proyectan a pantalla y se dibujan de atras hacia delante.
 * Algoritmo clasico de "pseudo-3d racer" (proyeccion por escalas).
 * ====================================================================== */

const Road = (() => {
  const R = CONFIG.road;
  const segments = [];          // pista completa
  let trackLength = 0;          // longitud total en unidades z
  const cameraDepth = 1 / Math.tan((R.fieldOfView / 2) * Math.PI / 180);

  // --- Construccion de la pista -----------------------------------------

  function lastY() {
    return segments.length === 0 ? 0 : segments[segments.length - 1].p2.world.y;
  }

  function addSegment(curve, y) {
    const n = segments.length;
    segments.push({
      index: n,
      p1: { world: { y: lastY(), z: n * R.segmentLength }, camera: {}, screen: {} },
      p2: { world: { y: y, z: (n + 1) * R.segmentLength }, camera: {}, screen: {} },
      curve: curve,
      sprites: [],  // sprites (coches, gasolinera, carteles) en este segmento
      color: Math.floor(n / R.rumbleLength) % 2,  // 0/1 para alternar colores
    });
  }

  // Interpolacion suave (easeInOut) para entradas/salidas de curva y rampa.
  function easeInOut(a, b, pct) {
    return a + (b - a) * ((-Math.cos(pct * Math.PI) / 2) + 0.5);
  }

  function addRoad(enter, hold, leave, curve, height) {
    const startY = lastY();
    const endY = startY + height * R.segmentLength;
    const total = enter + hold + leave;
    for (let n = 0; n < enter; n++)
      addSegment(easeInOut(0, curve, n / enter), easeInOut(startY, endY, n / total));
    for (let n = 0; n < hold; n++)
      addSegment(curve, easeInOut(startY, endY, (enter + n) / total));
    for (let n = 0; n < leave; n++)
      addSegment(easeInOut(curve, 0, n / leave), easeInOut(startY, endY, (enter + hold + n) / total));
  }

  // Genera una pista variada: rectas, curvas y colinas. Base para ampliar.
  function build() {
    segments.length = 0;
    addRoad(50, 50, 50, 0, 0);        // recta inicial
    addRoad(40, 40, 40, 3, 30);       // curva derecha + subida
    addRoad(40, 40, 40, -4, -20);     // curva izquierda + bajada
    addRoad(60, 60, 60, 0, 40);       // colina
    addRoad(40, 40, 40, 5, 0);        // curva cerrada derecha
    addRoad(50, 50, 50, -3, -30);     // curva izquierda + bajada
    addRoad(80, 40, 80, 0, 0);        // recta larga (zona rapida)
    addRoad(40, 40, 40, -5, 50);      // curva izquierda + subida
    addRoad(50, 50, 50, 0, 0);        // recta final
    trackLength = segments.length * R.segmentLength;
  }

  function findSegment(z) {
    return segments[Math.floor(z / R.segmentLength) % segments.length];
  }

  // --- Proyeccion 3D -> 2D ----------------------------------------------

  function project(p, camX, camY, camZ, width, height) {
    p.camera.x = (p.world.x || 0) - camX;
    p.camera.y = (p.world.y || 0) - camY;
    p.camera.z = (p.world.z || 0) - camZ;
    p.screen.scale = cameraDepth / p.camera.z;
    p.screen.x = Math.round((width / 2) + (p.screen.scale * p.camera.x * width / 2));
    p.screen.y = Math.round((height / 2) - (p.screen.scale * p.camera.y * height / 2));
    p.screen.w = Math.round(p.screen.scale * R.roadWidth * width / 2);
  }

  function rumbleWidth(projectedW) { return projectedW / 5; }
  function laneWidth(projectedW) { return projectedW / 24; }

  // --- Dibujo ------------------------------------------------------------

  function polygon(ctx, x1, y1, x2, y2, x3, y3, x4, y4, color) {
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.moveTo(x1, y1); ctx.lineTo(x2, y2);
    ctx.lineTo(x3, y3); ctx.lineTo(x4, y4);
    ctx.closePath();
    ctx.fill();
  }

  function drawSegment(ctx, width, lanes, p1, p2, isDark) {
    const C = CONFIG.colors;
    const grass = isDark ? C.grassDark : C.grassLight;
    const rumble = isDark ? C.rumbleDark : C.rumbleLight;
    const road = isDark ? C.roadDark : C.roadLight;

    // Cesped (banda completa)
    ctx.fillStyle = grass;
    ctx.fillRect(0, p2.screen.y, width, p1.screen.y - p2.screen.y);

    const r1 = rumbleWidth(p1.screen.w);
    const r2 = rumbleWidth(p2.screen.w);
    const l1 = laneWidth(p1.screen.w);
    const l2 = laneWidth(p2.screen.w);

    // Arcenes
    polygon(ctx, p1.screen.x - p1.screen.w - r1, p1.screen.y, p1.screen.x - p1.screen.w, p1.screen.y,
                 p2.screen.x - p2.screen.w, p2.screen.y, p2.screen.x - p2.screen.w - r2, p2.screen.y, rumble);
    polygon(ctx, p1.screen.x + p1.screen.w + r1, p1.screen.y, p1.screen.x + p1.screen.w, p1.screen.y,
                 p2.screen.x + p2.screen.w, p2.screen.y, p2.screen.x + p2.screen.w + r2, p2.screen.y, rumble);

    // Asfalto
    polygon(ctx, p1.screen.x - p1.screen.w, p1.screen.y, p1.screen.x + p1.screen.w, p1.screen.y,
                 p2.screen.x + p2.screen.w, p2.screen.y, p2.screen.x - p2.screen.w, p2.screen.y, road);

    // Lineas de carril (solo en segmentos claros)
    if (!isDark) {
      for (let lane = 1; lane < lanes; lane++) {
        const lx1 = p1.screen.x - p1.screen.w + (2 * p1.screen.w / lanes) * lane;
        const lx2 = p2.screen.x - p2.screen.w + (2 * p2.screen.w / lanes) * lane;
        polygon(ctx, lx1 - l1 / 2, p1.screen.y, lx1 + l1 / 2, p1.screen.y,
                     lx2 + l2 / 2, p2.screen.y, lx2 - l2 / 2, p2.screen.y, CONFIG.colors.laneMarker);
      }
    }
  }

  /* Sprites: cada uno es { z, offset, draw(ctx, x, yBottom, screenScale) }.
   * x        = posicion horizontal en pantalla (ya con curva + offset lateral)
   * yBottom  = base inferior del sprite en pantalla
   * screenScale = escala de proyeccion (multiplicala por tu factor de tamaño)
   * Asi la carretera no necesita saber si es un coche, una gasolinera, etc. */
  function placeSprites(sprites) {
    for (const seg of segments) if (seg.sprites.length) seg.sprites.length = 0;
    if (!sprites) return;
    for (const s of sprites) findSegment(s.z).sprites.push(s);
  }

  function drawSpritesOf(ctx, seg, width) {
    if (!seg.sprites.length) return;
    for (const s of seg.sprites) {
      const pct = (s.z % R.segmentLength) / R.segmentLength;
      const scale = seg.p1.screen.scale + (seg.p2.screen.scale - seg.p1.screen.scale) * pct;
      const sx = seg.p1.screen.x + (seg.p2.screen.x - seg.p1.screen.x) * pct;
      const sy = seg.p1.screen.y + (seg.p2.screen.y - seg.p1.screen.y) * pct;
      const spriteX = sx + scale * s.offset * R.roadWidth * width / 2;
      if (scale <= 0) continue;
      s.draw(ctx, spriteX, sy, scale);
    }
  }

  // --- Fondo de horizonte (parallax) ------------------------------------
  // Se desplaza horizontalmente segun la curvatura proxima y el lateral
  // del jugador, dando sensacion de profundidad sin coste de proyeccion.
  function drawBackground(ctx, baseSegment, basePercent, playerX) {
    const img = CONFIG.assets.horizon.image;
    const horizonY = Math.round(CONFIG.height * 0.5);
    if (!img || !img.complete || img.naturalWidth === 0) return;

    // Estima la curvatura acumulada de los primeros segmentos.
    let curve = 0;
    for (let n = 0; n < 60; n++)
      curve += segments[(baseSegment.index + n) % segments.length].curve;
    const shift = -(curve * 4) - (playerX * 60);

    const w = CONFIG.width;
    const dh = Math.round(w * (img.naturalHeight / img.naturalWidth));
    const top = horizonY - dh;
    let ox = shift % w;
    if (ox > 0) ox -= w;
    // Tilea horizontalmente para cubrir todo el ancho con el desplazamiento.
    for (let x = ox; x < w; x += w) ctx.drawImage(img, x, top, w, dh);
  }

  /**
   * Renderiza el cielo/horizonte, la carretera y los sprites sobre ella.
   * @param sprites lista opcional de sprites (coches, gasolinera, carteles)
   */
  function render(ctx, position, playerX, sprites) {
    const width = CONFIG.width;
    const height = CONFIG.height;
    const baseSegment = findSegment(position);
    const basePercent = (position % R.segmentLength) / R.segmentLength;
    const playerY = baseSegment.p1.world.y +
      (baseSegment.p2.world.y - baseSegment.p1.world.y) * basePercent;
    const camY = playerY + R.cameraHeight;

    // Fondo (cielo degradado + montañas con parallax).
    const g = ctx.createLinearGradient(0, 0, 0, height * 0.55);
    g.addColorStop(0, CONFIG.colors.skyDark);
    g.addColorStop(1, CONFIG.colors.sky);
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, width, height);
    drawBackground(ctx, baseSegment, basePercent, playerX);

    placeSprites(sprites);

    let maxY = height;       // recorte: no dibujar segmentos tapados por colinas
    let x = 0;               // acumulador de desplazamiento por curva
    let dx = -(baseSegment.curve * basePercent);

    // 1) Asfalto: de cerca a lejos (con recorte por colinas).
    const visible = [];
    for (let n = 0; n < R.drawDistance; n++) {
      const seg = segments[(baseSegment.index + n) % segments.length];
      seg.looped = (baseSegment.index + n) >= segments.length;
      seg.fog = Math.pow(1 / Math.E, ((n / R.drawDistance) * (n / R.drawDistance) * R.fogDensity));
      seg.clipped = true;

      const camZ = position - (seg.looped ? trackLength : 0);
      project(seg.p1, (playerX * R.roadWidth) - x, camY, camZ, width, height);
      project(seg.p2, (playerX * R.roadWidth) - x - dx, camY, camZ, width, height);

      x += dx;
      dx += seg.curve;

      if (seg.p1.camera.z <= cameraDepth || seg.p2.screen.y >= maxY) continue;
      seg.clipped = false;

      drawSegment(ctx, width, R.lanes, seg.p1, seg.p2, seg.color === 1);

      if (seg.fog < 1) {
        ctx.save();
        ctx.globalAlpha = 1 - seg.fog;
        ctx.fillStyle = CONFIG.colors.fog;
        ctx.fillRect(0, seg.p2.screen.y, width, seg.p1.screen.y - seg.p2.screen.y);
        ctx.restore();
      }

      maxY = seg.p2.screen.y;
      visible.push(seg);
    }

    // 2) Sprites: de lejos a cerca para un solapado correcto.
    for (let i = visible.length - 1; i >= 0; i--) drawSpritesOf(ctx, visible[i], width);
  }

  return {
    build, render, findSegment,
    get segments() { return segments; },
    get trackLength() { return trackLength; },
    get segmentLength() { return R.segmentLength; },
  };
})();
