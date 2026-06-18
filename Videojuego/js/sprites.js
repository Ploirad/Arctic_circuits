/* =========================================================================
 * sprites.js — Dibujo de sprites (imagenes con transparencia + respaldos).
 *
 * Los coches usan las imagenes de CONFIG.carSkins (DeLorean para el jugador,
 * arte real para los rivales). Si una imagen aun no ha cargado se pinta un
 * coche de respaldo con el color de la skin, asi nunca hay huecos.
 * ====================================================================== */

const Sprites = {
  _ready(skin) {
    return skin && skin.image && skin.image.complete && skin.image.naturalWidth > 0;
  },

  // Dibuja una imagen centrada en x, con la BASE inferior en yBottom.
  _img(ctx, img, cx, yBottom, widthPx) {
    const h = widthPx * (img.naturalHeight / img.naturalWidth);
    ctx.drawImage(img, cx - widthPx / 2, yBottom - h, widthPx, h);
  },

  /**
   * Coche del jugador (DeLorean) en vista trasera, fijo abajo-centro.
   * @param widthPx ancho en pixeles de pantalla
   * @param dim atenua el sprite (parpadeo de invencibilidad)
   * @param turret si true, dibuja la torreta automatica sobre el coche
   */
  playerCar(ctx, cx, cy, widthPx, dim, turret) {
    const skin = CONFIG.carSkins.player;
    ctx.save();
    if (dim) ctx.globalAlpha = 0.4;

    // Sombra bajo el coche
    ctx.fillStyle = 'rgba(0,0,0,0.3)';
    ctx.fillRect(cx - widthPx / 2, cy - 3, widthPx, 5);

    if (this._ready(skin)) this._img(ctx, skin.image, cx, cy, widthPx);
    else this._fallbackCar(ctx, cx, cy, widthPx, skin.fallback);

    if (turret) this._turret(ctx, cx, cy - widthPx * 0.55, widthPx * 0.5);
    ctx.restore();
  },

  /** Coche rival en vista trasera situado sobre la carretera. */
  enemyCar(ctx, cx, yBottom, widthPx, skin) {
    if (widthPx < 1) return;
    ctx.save();
    if (this._ready(skin)) this._img(ctx, skin.image, cx, yBottom, widthPx);
    else this._fallbackCar(ctx, cx, yBottom, widthPx, (skin && skin.fallback) || '#888');
    ctx.restore();
  },

  // Coche simple de respaldo (mientras carga la imagen).
  _fallbackCar(ctx, cx, yBottom, w, color) {
    const h = w * 0.6, x = cx - w / 2, y = yBottom - h;
    ctx.fillStyle = color; ctx.fillRect(x, y + h * 0.25, w, h * 0.6);
    ctx.fillStyle = '#1a2a3a'; ctx.fillRect(x + w * 0.2, y, w * 0.6, h * 0.35);
    ctx.fillStyle = '#101014';
    ctx.fillRect(x - 2, y + h * 0.55, w * 0.16, h * 0.45);
    ctx.fillRect(x + w - w * 0.16 + 2, y + h * 0.55, w * 0.16, h * 0.45);
  },

  // Torreta automatica dibujada sobre el coche del jugador.
  _turret(ctx, cx, cy, w) {
    const h = w * 0.55;
    ctx.save();
    // Base
    ctx.fillStyle = '#3a3a44'; ctx.fillRect(cx - w * 0.28, cy, w * 0.56, h * 0.5);
    // Torreta
    ctx.fillStyle = '#5a5a66'; ctx.fillRect(cx - w * 0.2, cy - h * 0.45, w * 0.4, h * 0.55);
    // Cañon
    ctx.fillStyle = '#22222a'; ctx.fillRect(cx - w * 0.05, cy - h * 0.7, w * 0.1, h * 0.5);
    // Luz
    ctx.fillStyle = '#ff3b3b'; ctx.fillRect(cx - w * 0.04, cy - h * 0.35, w * 0.08, w * 0.08);
    ctx.restore();
  },

  /** Imagen generica al borde de la carretera (gasolinera, cartel...). */
  prop(ctx, img, cx, yBottom, widthPx) {
    if (!img || !img.complete || img.naturalWidth === 0 || widthPx < 1) return;
    this._img(ctx, img, cx, yBottom, widthPx);
  },

  /** Llamas del turbo bajo el coche del jugador. */
  turboFlames(ctx, cx, cy, widthPx, flicker) {
    const w = widthPx * 0.5;
    ctx.save();
    ctx.globalAlpha = 0.85;
    ctx.fillStyle = flicker ? '#ffd23f' : '#ff7b1f';
    ctx.fillRect(cx - w / 2, cy, w, 6);
    ctx.fillStyle = '#fff';
    ctx.fillRect(cx - w / 4, cy, w / 2, 3);
    ctx.restore();
  },
};
