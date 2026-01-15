# Librería Wukong con Soporte para Sensor Sonarbit

Librería Python mejorada para la placa de expansión Wukong de Elecfreaks, ahora con soporte integrado para el sensor de ultrasonidos Sonarbit.

## 📋 Características

- ✅ Control de motores DC (2 motores)
- ✅ Control de servomotores (8 servos)
- ✅ Control de luces ambientales con modo respiración
- ✅ **NUEVO**: Lectura de sensor de ultrasonidos Sonarbit

## 🔧 Instalación

1. Copia el archivo `Wukong.py` a tu editor de MicroPython para micro:bit
2. Importa la librería en tu código:

```python
from Wukong import WUKONG
from microbit import *
```

## 📡 Sensor de Ultrasonidos Sonarbit

### Especificaciones Técnicas

- **Sensor**: HC-SR04 compatible
- **Rango de medición**: 2cm - 400cm
- **Precisión**: ±1cm
- **Ángulo de medición**: 15°
- **Conexión**: 1 pin digital (trigger + echo combinados)
- **Unidades soportadas**: milímetros (mm), centímetros (cm), pulgadas (inch)

### Conexión del Hardware

El sensor Sonarbit se conecta a cualquier pin digital del micro:bit:

```
Sensor Sonarbit → micro:bit
────────────────────────────
VCC (Rojo)      → 3V
GND (Negro)     → GND
SIG (Amarillo)  → Pin digital (P0, P1, P2, etc.)
```

### Uso del Método `read_sonar()`

#### Sintaxis

```python
wk.read_sonar(pin, unit='cm')
```

#### Parámetros

- **pin** (MicroBitDigitalPin): Pin donde está conectado el sensor
  - Ejemplos: `pin0`, `pin1`, `pin2`, `pin8`, `pin12`, `pin13`, `pin14`, `pin15`, `pin16`
- **unit** (str, opcional): Unidad de medida
  - `'mm'` - milímetros
  - `'cm'` - centímetros (por defecto)
  - `'inch'` - pulgadas

#### Retorno

- **int**: Distancia medida en la unidad especificada
- **0**: Si no se detecta ningún objeto (distancia > 400cm)

#### Ejemplos Básicos

**Ejemplo 1: Lectura simple en centímetros**

```python
from Wukong import WUKONG
from microbit import *

wk = WUKONG()

while True:
    distancia = wk.read_sonar(pin0, 'cm')
    print("Distancia:", distancia, "cm")
    sleep(500)
```

**Ejemplo 2: Lectura en diferentes unidades**

```python
from Wukong import WUKONG
from microbit import *

wk = WUKONG()

# Leer en centímetros
dist_cm = wk.read_sonar(pin0, 'cm')
print("Distancia:", dist_cm, "cm")

# Leer en milímetros
dist_mm = wk.read_sonar(pin0, 'mm')
print("Distancia:", dist_mm, "mm")

# Leer en pulgadas
dist_inch = wk.read_sonar(pin0, 'inch')
print("Distancia:", dist_inch, "pulgadas")
```

**Ejemplo 3: Mostrar distancia en pantalla LED**

```python
from Wukong import WUKONG
from microbit import *

wk = WUKONG()

while True:
    distancia = wk.read_sonar(pin0, 'cm')
    
    if distancia == 0:
        display.show('X')  # No hay objeto
    else:
        display.scroll(str(distancia))
    
    sleep(1000)
```

**Ejemplo 4: Alarma de proximidad**

```python
from Wukong import WUKONG
from microbit import *
import music

wk = WUKONG()

DISTANCIA_ALERTA = 20  # cm

while True:
    distancia = wk.read_sonar(pin0, 'cm')
    
    if distancia > 0 and distancia < DISTANCIA_ALERTA:
        # ¡Objeto muy cerca!
        display.show(Image.SKULL)
        music.play(music.POWER_DOWN)
        wk.set_light_breath(True)  # Luz parpadeante
    else:
        # Todo bien
        display.show(Image.HAPPY)
        wk.set_light_breath(False)
    
    sleep(200)
```

**Ejemplo 5: Control de motor según distancia**

```python
from Wukong import WUKONG
from microbit import *

wk = WUKONG()

while True:
    distancia = wk.read_sonar(pin0, 'cm')
    
    if distancia > 0 and distancia < 30:
        # Objeto cerca: retroceder
        wk.set_motors(1, -50)
        wk.set_motors(2, -50)
    elif distancia >= 30 and distancia < 100:
        # Distancia media: avanzar despacio
        wk.set_motors(1, 30)
        wk.set_motors(2, 30)
    else:
        # Camino libre: avanzar rápido
        wk.set_motors(1, 80)
        wk.set_motors(2, 80)
    
    sleep(100)
```

## 🎯 Métodos Disponibles

### Control de Motores

#### `set_motors(motor, speed)`

Controla la velocidad y dirección de los motores DC.

- **motor** (int): Número de motor (1 o 2)
- **speed** (int): Velocidad (-100 a 100)
  - Valores positivos: adelante
  - Valores negativos: atrás
  - 0: detener

```python
wk.set_motors(1, 50)   # Motor 1 al 50% adelante
wk.set_motors(2, -30)  # Motor 2 al 30% atrás
```

### Control de Servomotores

#### `set_servo(servo, angle)`

Controla la posición de los servomotores.

- **servo** (int): Número de servo (0-7)
- **angle** (int): Ángulo (0-180 grados)

```python
wk.set_servo(0, 90)   # Servo 0 a 90 grados
wk.set_servo(1, 180)  # Servo 1 a 180 grados
```

### Control de Iluminación

#### `set_light(light)`

Establece el brillo de la luz ambiental.

- **light** (int): Nivel de brillo

```python
wk.set_light(150)
```

#### `set_light_breath(br)`

Activa/desactiva el modo respiración de la luz.

- **br** (bool): True para activar, False para desactivar

```python
wk.set_light_breath(True)   # Activar modo respiración
wk.set_light_breath(False)  # Desactivar
```

### Sensor de Ultrasonidos

#### `read_sonar(pin, unit='cm')`

Lee la distancia del sensor de ultrasonidos Sonarbit.

- **pin** (MicroBitDigitalPin): Pin de conexión
- **unit** (str): Unidad ('mm', 'cm', 'inch')
- **Retorna**: Distancia medida o 0 si no hay objeto

```python
distancia = wk.read_sonar(pin0, 'cm')
```

## ⚠️ Solución de Problemas

### El sensor siempre devuelve 0

- Verifica que el sensor esté correctamente conectado
- Asegúrate de usar el pin correcto en el código
- Comprueba que haya un objeto dentro del rango (2-400cm)
- Verifica la alimentación del sensor (3V)

### Lecturas inconsistentes

- Asegúrate de que no haya interferencias cerca del sensor
- Evita superficies muy irregulares o que absorban sonido (tela, espuma)
- Aumenta el tiempo entre lecturas (mínimo 50ms recomendado)

### Error "unit error"

- Verifica que estés usando una unidad válida: `'mm'`, `'cm'` o `'inch'`
- Las unidades deben estar entre comillas

## 📚 Recursos Adicionales

- [Documentación oficial Elecfreaks Wukong](https://www.elecfreaks.com/learn-en/microbitExtensionModule/wukong.html)
- [Documentación Sonarbit](https://github.com/elecfreaks/pxt-sonarbit)
- [MicroPython para micro:bit](https://microbit-micropython.readthedocs.io/)

## 📄 Licencia

MIT License - Compatible con la licencia original de Elecfreaks

## 👥 Créditos

- **Librería original Wukong**: Elecfreaks
- **Implementación Sonarbit**: Basada en [pxt-sonarbit](https://github.com/elecfreaks/pxt-sonarbit) de Elecfreaks
- **Integración Python**: 2026
