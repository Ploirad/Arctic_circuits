# Artic Circuits — Prototipo de carreras 16-bit

Prototipo base de un videojuego de carreras con **vista trasera del coche**, estética **16 bits** e inspiración en **OutRun** y **F-Zero**. Está construido con **HTML5 Canvas + JavaScript puro** (sin dependencias ni paso de compilación) y sigue fielmente la **máquina de estados** del diseño.

## Cómo ejecutarlo

Abre [index.html](index.html) en cualquier navegador moderno (doble clic). No necesita servidor ni instalación.

> Opcional, para evitar restricciones de algunos navegadores con `file://`:
> ```bash
> cd Videojuego
> python -m http.server 8000
> # luego abre http://localhost:8000
> ```

## Controles

| Tecla | Acción |
|-------|--------|
| Flechas / WASD | Conducir (acelerar, frenar, girar) |
| Shift | Turbo |
| Enter / Espacio | Aceptar · repostar al frenar junto a la gasolinera |
| P | Pausa (vuelve al menú) |
| 1–4 | Comprar mejoras en la tienda |

## Máquina de estados implementada

Cada nodo del diagrama es un estado real en [js/stateMachine.js](js/stateMachine.js) + [js/states.js](js/states.js):

```
---
config:
  layout: elk
  theme: redux
---
stateDiagram-v2
    [*] --> MainMenu
    
    MainMenu --> Playing: Start Game
    
    Playing --> Playing: Move Lane
    Playing --> Playing: Dodge Car
    Playing --> Playing: Use Turbo
    Playing --> Playing: Earn Money
    Playing --> Crashed: Collision Detected
    Playing --> RoundComplete: 120 Seconds No Cars
    
    Crashed --> GameOver: Lives = 0
    Crashed --> Playing: Lives > 0
    
    RoundComplete --> RestPeriod: Enter Safe Zone
    
    RestPeriod --> GasStation: Drive to Gas Station
    RestPeriod --> Playing: Continue Driving
    
    GasStation --> ShopMenu: Stop at Station
    
    ShopMenu --> GasStation: Buy Engine Upgrade
    ShopMenu --> GasStation: Buy Armor
    ShopMenu --> GasStation: Buy Turbo Capacity
    ShopMenu --> GasStation: Buy Auto-Turret (Eliminates a car every 15s)
    ShopMenu --> Playing: Exit Shop
    
    GameOver --> MainMenu: Game Over
    
    Playing --> MainMenu: Pause
```

Acciones internas de `Playing` (auto-bucles del diagrama): *Use Turbo, Dodge Car, Move Lane, Earn Money* están implementadas dentro del propio estado.

## Estructura del código

| Archivo | Responsabilidad |
|---------|-----------------|
| [index.html](index.html) | Lienzo y carga de scripts |
| [css/style.css](css/style.css) | Escalado del canvas y look 16-bit |
| [js/config.js](js/config.js) | **Todas las constantes ajustables** (física, reglas, tienda, skins, colores) |
| [js/assets.js](js/assets.js) | Carga de las imágenes (coches, gasolinera, cartel, fondo) |
| [js/input.js](js/input.js) | Teclado (estado mantenido + flancos de pulsación) |
| [js/sprites.js](js/sprites.js) | Dibujo de sprites (imágenes con transparencia + respaldos) |
| [js/road.js](js/road.js) | Carretera **pseudo-3D** + fondo de horizonte + sprites de mundo |
| [js/stateMachine.js](js/stateMachine.js) | Máquina de estados genérica |
| [js/states.js](js/states.js) | Estados concretos + estado runtime + HUD/menús |
| [js/game.js](js/game.js) | Bootstrap, cableado de transiciones y bucle principal |
| [assets/](assets/) | PNG ya procesados (transparencia horneada) que usa el juego |
| [tools/process_assets.py](tools/process_assets.py) | Script que recorta el fondo de los PNG originales y genera `assets/` |

## Mecánicas clave

- **Dinero por distancia:** solo se gana dinero mientras el coche **avanza** (parado = 0). El **turbo duplica** la ganancia (`turboMoneyMultiplier`).
- **Gasolinera física:** aparece **a un lado de la carretera**. Te acercas, **frenas manualmente** y, cuando estás cerca y a baja velocidad, puedes pulsar **Enter para repostar y entrar a la tienda**. Un poco antes aparece un **cartel de servicios** al borde.
- **Tienda monocromática:** fondo blanco; eliges qué comprar con 1–4 y sales con Enter (comprar no te saca de la tienda).
- **Invencibilidad tras choque:** ~2,8 s de gracia (`rules.invincibleSec`) con el coche **parpadeando**, para evitar colisiones encadenadas.
- **El rival contra el que chocas se destruye** y reaparece lejos.
- **Torreta automática:** mejora cara (`$5000`) de **compra única**; al equiparla se ve **sobre el coche** y elimina al rival más cercano cada 15 s.
- **Hitbox ajustada** al tamaño visual de los coches (`rules.collision`).

## Distancias teóricas (ronda a ronda)

- `roundTarget = maxSpeed × gasStationSeconds = 12000 × 30 = 360 000 ud`.
- Escala: `maxSpeed` (12000 ud/s) ≈ 320 km/h ≈ 88,9 m/s ⟹ **1 ud ≈ 0,00741 m**.
- Cada ronda ≈ **360 000 ud ≈ 2 667 m ≈ 2,67 km** de conducción continua.
- La pista mide `1310 × 200 = 262 000 ud ≈ 1,94 km` (una vuelta) ⟹ una ronda ≈ **1,37 vueltas**.

## Personalizar el aspecto de los coches y la escena

El arte vive en `assets/` y se referencia desde `CONFIG.carSkins` / `CONFIG.assets` ([js/config.js](js/config.js)). El jugador es el DeLorean y los rivales usan las imágenes provistas (`cocheAzul`, `furgon`, `ferrario`, `GruasPaco`…).

Para cambiar un coche/escenario:
1. Sustituye o añade el PNG original en [Videojuego/](.) (fondo liso, blanco o gris).
2. Ejecuta `python tools/process_assets.py` para recortar el fondo, hacerlo transparente y generar el asset en `assets/`.
3. Apunta el `src` correspondiente en `CONFIG.carSkins`/`CONFIG.assets`.

> La transparencia se "hornea" en el PNG (no se hace en runtime), por eso el juego funciona también abriendo `index.html` con `file://` sin servidor.

## Qué falta (ideas para iterar)

- Sonido y música (Web Audio API).
- Modelo de gasolina/combustible que se consuma y se reposte.
- Efecto visual de disparo (rayo) de la torreta hacia el coche eliminado.
- Persistir el dinero/mejoras entre partidas (`localStorage`).
- Más variedad de pista y rivales con IA de carril.

## Depuración

En la consola del navegador tienes acceso a `window.ARTIC` (`fsm`, `GameState`, `Road`, `CONFIG`). Por ejemplo, `ARTIC.fsm.history` muestra la traza de transiciones de estado.
