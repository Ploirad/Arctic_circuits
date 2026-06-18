# -*- coding: utf-8 -*-
"""Pre-procesa los PNG de arte: recorta el fondo (flood-fill desde los bordes),
lo hace transparente, recorta al contenido y reescala. Genera assets listos
para usar en el juego (transparencia ya horneada -> funciona desde file://).

Uso:  python tools/process_assets.py
Salida: Videojuego/assets/*.png
"""
import os
from collections import deque
from PIL import Image

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "assets")
os.makedirs(OUT, exist_ok=True)

# (origen, destino, ancho_max, tolerancia_fondo)
JOBS = [
    ("delorean.png",            "player_delorean.png", 160, 70),
    ("cocheAzul.png",           "enemy_azul.png",      150, 60),
    ("cocheBlanco.png",         "enemy_blanco.png",    150, 60),
    ("cocheNegro.png",          "enemy_negro.png",     150, 60),
    ("furgon.png",              "enemy_furgon.png",    150, 60),
    ("ferrario.png",            "enemy_ferrario.png",  150, 60),
    ("cocheFantastico.png",     "enemy_fantastico.png",150, 60),
    ("GruasPaco.png",           "enemy_gruas.png",     150, 60),
    ("CazaFantasma.png",        "enemy_caza.png",       150, 60),
    ("EquipoA.png",             "enemy_equipoa.png",   150, 60),
    ("espanoil.png",            "gas_station.png",     360, 60),
    (u"SeñalGasolinera (1).png", "sign_gas.png",  200, 60),
]


def flood_remove_bg(im, tol):
    """Pone alpha=0 en el fondo conectado a los bordes (color ~ esquinas)."""
    im = im.convert("RGBA")
    w, h = im.size
    px = im.load()
    # Color de fondo de referencia: media de las 4 esquinas.
    cs = [px[0, 0], px[w - 1, 0], px[0, h - 1], px[w - 1, h - 1]]
    br = sum(c[0] for c in cs) // 4
    bg = sum(c[1] for c in cs) // 4
    bb = sum(c[2] for c in cs) // 4

    seen = bytearray(w * h)
    q = deque()

    def similar(c):
        return abs(c[0] - br) <= tol and abs(c[1] - bg) <= tol and abs(c[2] - bb) <= tol

    # Semillas: todos los pixeles del borde que parezcan fondo.
    for x in range(w):
        for y in (0, h - 1):
            i = y * w + x
            if not seen[i] and similar(px[x, y]):
                seen[i] = 1; q.append((x, y))
    for y in range(h):
        for x in (0, w - 1):
            i = y * w + x
            if not seen[i] and similar(px[x, y]):
                seen[i] = 1; q.append((x, y))

    while q:
        x, y = q.popleft()
        px[x, y] = (0, 0, 0, 0)
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h:
                i = ny * w + nx
                if not seen[i] and similar(px[nx, ny]):
                    seen[i] = 1; q.append((nx, ny))
    return im


def process(src, dst, max_w, tol):
    im = Image.open(os.path.join(BASE, src)).convert("RGBA")
    # Limitar la resolucion de trabajo (BFS rapido) sin perder nitidez de borde.
    work_w = 800
    if im.width > work_w:
        nh = round(im.height * work_w / im.width)
        im = im.resize((work_w, nh), Image.LANCZOS)
    # 1) Quitar el fondo en ALTA resolucion (bordes nitidos -> sin halo).
    im = flood_remove_bg(im, tol)
    # 2) Recortar al contenido.
    bbox = im.getbbox()
    if bbox:
        im = im.crop(bbox)
    # 3) Reescalar al tamaño final (los bordes se mezclan con transparencia).
    if im.width > max_w:
        nh = round(im.height * max_w / im.width)
        im = im.resize((max_w, nh), Image.LANCZOS)
    # 4) Limpiar el fleco semitransparente muy tenue.
    px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b, a = px[x, y]
            if a < 24:
                px[x, y] = (r, g, b, 0)
    im.save(os.path.join(OUT, dst))
    print(f"{src:28s} -> assets/{dst:22s} {im.size}")


for src, dst, mw, tol in JOBS:
    process(src, dst, mw, tol)


def make_background():
    """Fondo de horizonte (cielo + montañas + colinas) desde carretera3railes,
    recortando la parte de carretera inferior. Se usa como parallax."""
    im = Image.open(os.path.join(BASE, "carretera3railes.png")).convert("RGB")
    w, h = im.size
    # La carretera ocupa la parte baja; nos quedamos con el cielo y montañas.
    crop = im.crop((0, 0, w, int(h * 0.62)))
    # Ancho comodo para tilear/escalar en el juego.
    target_w = 480
    nh = round(crop.height * target_w / crop.width)
    crop = crop.resize((target_w, nh), Image.LANCZOS)
    crop.save(os.path.join(OUT, "bg_horizon.png"))
    print(f"carretera3railes.png         -> assets/bg_horizon.png        {crop.size}")


make_background()
print("OK")
