/* =========================================================================
 * sprites.js — Dibujo de sprites estilo 16-bit, dirigido por "skins".
 *
 * Cada coche se pinta segun un objeto "skin" (definido en CONFIG.carSkins).
 * Si la skin trae una imagen cargada (skin.image), se dibuja esa imagen;
 * si no, se pintan rectangulos con los colores de la skin. Asi se puede
 * cambiar el aspecto de los coches en el futuro sin tocar la logica.
 * ====================================================================== */

const Sprites = {
  /** Carga una imagen de sprite y la devuelve (asignala a skin.image). */
  loadImage(src) {
    const img = new Image();
    img.src = src;
    return img;
  },

  // ¿La skin tiene una imagen lista para dibujar?
  _hasImage(skin) {
    return skin && skin.image && skin.image.complete && skin.image.naturalWidth > 0;
  },

  // Dibuja la imagen de la skin centrada sobre (cx, cy = base inferior).
  _drawImage(ctx, skin, cx, cy, scale) {
    const fw = (skin.frameW || skin.image.naturalWidth);
    const fh = (skin.frameH || skin.image.naturalHeight);
    const w = fw * scale, h = fh * scale;
    ctx.drawImage(skin.image, 0, 0, fw, fh, cx - w / 2, cy - h, w, h);
  },

  /**
   * Coche del jugador visto desde atras.
   * @param skin objeto de CONFIG.carSkins.player (colores o imagen)
   * @param steer -1..1 para inclinar las ruedas al girar
   * @param dim si true, atenua (efecto de parpadeo de invencibilidad)
   */
  playerCar(ctx, cx, cy, scale, steer, skin, dim) {
    skin = skin || CONFIG.carSkins.player;
    ctx.save();
    if (dim) ctx.globalAlpha = 0.35;

    if (this._hasImage(skin)) { this._drawImage(ctx, skin, cx, cy, scale); ctx.restore(); return; }

    const w = 64 * scale, h = 36 * scale;
    const x = cx - w / 2, y = cy - h;

    // Sombra
    ctx.fillStyle = 'rgba(0,0,0,0.35)';
    ctx.fillRect(x - 2, cy - 3, w + 4, 5);

    // Ruedas traseras (se desplazan al girar)
    const tilt = (steer || 0) * 4 * scale;
    ctx.fillStyle = skin.wheel;
    ctx.fillRect(x - 4 + tilt, y + h * 0.45, 10 * scale, h * 0.55);
    ctx.fillRect(x + w - 6 * scale - 4 + tilt, y + h * 0.45, 10 * scale, h * 0.55);

    // Carroceria
    ctx.fillStyle = skin.body;
    ctx.fillRect(x, y + h * 0.2, w, h * 0.7);
    ctx.fillStyle = skin.shadow;
    ctx.fillRect(x, y + h * 0.7, w, h * 0.2);

    // Luneta / techo
    ctx.fillStyle = skin.cabin;
    ctx.fillRect(x + w * 0.18, y, w * 0.64, h * 0.32);

    // Aleron
    ctx.fillStyle = skin.wing;
    ctx.fillRect(x - 3, y + h * 0.12, w + 6, 4 * scale);

    // Pilotos traseros
    ctx.fillStyle = skin.lightL;
    ctx.fillRect(x + 4, y + h * 0.55, 8 * scale, 6 * scale);
    ctx.fillStyle = skin.lightR;
    ctx.fillRect(x + w - 12 * scale, y + h * 0.55, 8 * scale, 6 * scale);

    ctx.restore();
  },

  /** Coche rival (vista trasera). skin = objeto de CONFIG.carSkins.enemies. */
  enemyCar(ctx, cx, cy, scale, skin) {
    skin = skin || CONFIG.carSkins.enemies[0];
    if (scale < 0.01) return;
    ctx.save();

    if (this._hasImage(skin)) { this._drawImage(ctx, skin, cx, cy, scale); ctx.restore(); return; }

    const w = 60 * scale, h = 34 * scale;
    const x = cx - w / 2, y = cy - h;

    ctx.fillStyle = 'rgba(0,0,0,0.3)';
    ctx.fillRect(x, cy - 2, w, 4);

    ctx.fillStyle = skin.wheel;
    ctx.fillRect(x - 3, y + h * 0.5, 8 * scale, h * 0.5);
    ctx.fillRect(x + w - 5 * scale, y + h * 0.5, 8 * scale, h * 0.5);

    ctx.fillStyle = skin.body;
    ctx.fillRect(x, y + h * 0.2, w, h * 0.8);
    ctx.fillStyle = skin.shadow;
    ctx.fillRect(x, y + h * 0.78, w, h * 0.22);
    ctx.fillStyle = skin.cabin;
    ctx.fillRect(x + w * 0.2, y, w * 0.6, h * 0.34);

    ctx.fillStyle = skin.light;
    ctx.fillRect(x + 4, y + h * 0.6, 7 * scale, 5 * scale);
    ctx.fillRect(x + w - 11 * scale, y + h * 0.6, 7 * scale, 5 * scale);
    ctx.restore();
  },

  /** Llamas del turbo bajo el coche del jugador. */
  turboFlames(ctx, cx, cy, scale, flicker) {
    const w = 40 * scale;
    ctx.save();
    ctx.globalAlpha = 0.85;
    ctx.fillStyle = flicker ? '#ffd23f' : '#ff7b1f';
    ctx.fillRect(cx - w / 2, cy, w, 6 * scale);
    ctx.fillStyle = '#fff';
    ctx.fillRect(cx - w / 4, cy, w / 2, 3 * scale);
    ctx.restore();
  },
};
