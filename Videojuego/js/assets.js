/* =========================================================================
 * assets.js — Carga las imagenes y las asigna a CONFIG.
 * Las imagenes se pintan en cuanto terminan de cargar (no bloquea el inicio).
 * Importante: los PNG ya vienen con transparencia "horneada" (ver
 * tools/process_assets.py), por eso funcionan tambien abriendo el index
 * directamente con file:// sin necesidad de servidor.
 * ====================================================================== */

const Assets = (() => {
  function load(entry) {
    if (!entry || !entry.src) return;
    const img = new Image();
    img.src = entry.src;
    entry.image = img;
  }

  function loadAll() {
    load(CONFIG.carSkins.player);
    CONFIG.carSkins.enemies.forEach(load);
    load(CONFIG.assets.horizon);
    load(CONFIG.assets.station);
    load(CONFIG.assets.sign);
  }

  return { loadAll };
})();
