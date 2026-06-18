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
| Enter / Espacio | Aceptar / confirmar en menús |
| P | Pausa (vuelve al menú) |
| 1–4 | Comprar mejoras en la tienda |
| Abajo / Arriba | Navegar zona de descanso / gasolinera |

## Máquina de estados implementada

Cada nodo del diagrama es un estado real en [js/stateMachine.js](js/stateMachine.js) + [js/states.js](js/states.js):

```
MainMenu ──Start Game──> Playing
Playing  ──Collision Detected──> Crashed
Crashed  ──Lives > 0──> Playing      Crashed ──Lives = 0──> GameOver
GameOver ──Game Over──> MainMenu
Playing  ──Pause──> MainMenu
Playing  ──120 Seconds No Cars──> RoundComplete
RoundComplete ──Enter Safe Zone──> RestPeriod
RestPeriod ──Drive to Gas Station──> GasStation   RestPeriod ──Continue Driving──> Playing
GasStation ──Stop at Station──> ShopMenu          GasStation ──Continue Driving──> Playing
ShopMenu ──Buy X──> GasStation                    ShopMenu ──Exit Shop──> Playing
```

Acciones internas de `Playing` (auto-bucles del diagrama): *Use Turbo, Dodge Car, Move Lane, Earn Money* están implementadas dentro del propio estado.

## Estructura del código

| Archivo | Responsabilidad |
|---------|-----------------|
| [index.html](index.html) | Lienzo y carga de scripts |
| [css/style.css](css/style.css) | Escalado del canvas y look 16-bit |
| [js/config.js](js/config.js) | **Todas las constantes ajustables** (física, reglas, tienda, colores) |
| [js/input.js](js/input.js) | Teclado (estado mantenido + flancos de pulsación) |
| [js/sprites.js](js/sprites.js) | Dibujo procedural de coches (sin imágenes externas) |
| [js/road.js](js/road.js) | Carretera **pseudo-3D** (proyección por escalas estilo OutRun) |
| [js/stateMachine.js](js/stateMachine.js) | Máquina de estados genérica |
| [js/states.js](js/states.js) | Estados concretos + estado runtime + HUD/menús |
| [js/game.js](js/game.js) | Bootstrap, cableado de transiciones y bucle principal |

## Mecánicas clave

- **Dinero por distancia:** solo se gana dinero mientras el coche **avanza** (parado = 0). El **turbo duplica** la ganancia (`turboMoneyMultiplier`).
- **Gasolinera por distancia:** se llega tras recorrer una distancia objetivo, equivalente a unos **30 s a velocidad punta sin turbo** (`rules.gasStationSeconds`). El HUD muestra el progreso ⛽ %.
- **Invencibilidad tras choque:** al revivir hay ~2,8 s de gracia (`rules.invincibleSec`) en los que el coche **parpadea** y no puede chocar, para evitar colisiones encadenadas.
- **El rival contra el que chocas se destruye** y reaparece lejos.
- **Hitbox ajustada** al tamaño visual de los coches (`rules.collision`: solape lateral + alcance en z).

## Personalizar el aspecto de los coches

Los coches se pintan según *skins* definidas en `CONFIG.carSkins` ([js/config.js](js/config.js)):

- `carSkins.player` y `carSkins.enemies[]` describen los **colores** (carrocería, cabina, ruedas, luces…). Cambia esos valores para recolorear al instante.
- Para usar **arte real** en el futuro, asigna `skin.image = Sprites.loadImage('ruta.png')` (y opcional `frameW`/`frameH`): [js/sprites.js](js/sprites.js) dibujará la imagen en lugar de los rectángulos, sin tocar la lógica del juego.

## Qué falta (ideas para iterar)

- Sustituir los sprites procedurales por *spritesheets* reales (ya preparado el enganche).
- Sonido y música (Web Audio API).
- Modelo de gasolina/combustible que se consuma y se reposte en la gasolinera.
- Efecto visual de disparo de la torreta automática.
- Persistir el dinero/mejoras entre partidas (`localStorage`).
- Más variedad de pista y rivales con IA de carril.

## Depuración

En la consola del navegador tienes acceso a `window.ARTIC` (`fsm`, `GameState`, `Road`, `CONFIG`). Por ejemplo, `ARTIC.fsm.history` muestra la traza de transiciones de estado.
