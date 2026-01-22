# DFRobot Motor Driver for micro:bit (MicroPython)

Port de la extensión MakeCode de DFRobot para controlar la placa de expansión de motores en MicroPython.

## 🎯 Características

- **8 canales de servomotores** (S1-S8): Control de 0° a 180°
- **4 motores DC** (M1-M4): Velocidad 0-255, bidireccional (CW/CCW)
- **2 controladores de motores paso a paso**: Soporta 28BYJ-48 y 42BYGH1861A-C
- **Control dual de steppers**: Controla dos motores paso a paso simultáneamente

## 🔧 Hardware Requerido

- **micro:bit** (v1 o v2)
- **DFRobot Motor Driver Expansion Board**
- **Fuente de alimentación**: 3.5V ~ 5.5V
- **Motores** (según necesites):
  - Servomotores (0-180°)
  - Motores DC
  - Motores paso a paso 28BYJ-48 o 42BYGH1861A-C

## 📦 Instalación

### Opción 1: Copiar archivo directamente

1. Descarga `dfrobot_motor.py`
2. Abre el editor de MicroPython para micro:bit (https://python.microbit.org/)
3. Copia el contenido de `dfrobot_motor.py` en un nuevo archivo
4. Guarda el archivo en tu micro:bit como `dfrobot_motor.py`

### Opción 2: Usar herramientas de línea de comandos

```bash
# Usando uflash (si tienes Python instalado)
pip install uflash
uflash dfrobot_motor.py
```

## 🚀 Inicio Rápido

### Inicialización

```python
from dfrobot_motor import DFRobot0548

# Crear instancia del driver
driver = DFRobot0548()
```

### Control de Servomotores

```python
from dfrobot_motor import DFRobot0548, Servos
from microbit import sleep

# Crear driver
driver = DFRobot0548()

# Mover servo S1 a 90 grados
driver.servo(Servos.S1, 90)
sleep(1000)

# Hacer un barrido de 0 a 180 grados
for angle in range(0, 181, 10):
    driver.servo(Servos.S1, angle)
    sleep(50)
```

### Control de Motores DC

```python
from dfrobot_motor import DFRobot0548, Motors, Direction
from microbit import sleep

# Crear driver
driver = DFRobot0548()

# Motor M1 hacia adelante a velocidad 200
driver.motor_run(Motors.M1, Direction.CW, 200)
sleep(2000)

# Motor M1 hacia atrás a velocidad 150
driver.motor_run(Motors.M1, Direction.CCW, 150)
sleep(2000)

# Detener motor
driver.motor_stop(Motors.M1)
```

### Control de Motores Paso a Paso

```python
from dfrobot_motor import DFRobot0548, Steppers, Direction
from microbit import sleep

# Crear driver
driver = DFRobot0548()

# Rotar motor 28BYJ-48 90 grados en sentido horario
driver.stepper_degree_28(Steppers.M1_M2, Direction.CW, 90)
sleep(500)

# Rotar motor 42BYGH 2 vueltas completas en sentido antihorario
driver.stepper_turn_42(Steppers.M1_M2, Direction.CCW, 2)
```


## 📚 Referencia de API

### Clase Principal

```python
from dfrobot_motor import DFRobot0548

# Crear instancia del driver
driver = DFRobot0548()  # Usa dirección I2C por defecto (0x40)

# O especificar dirección I2C personalizada
driver = DFRobot0548(i2c_address=0x40)
```

### Constantes de Dirección

```python
from dfrobot_motor import Direction

Direction.CW   # Sentido horario (Clockwise)
Direction.CCW  # Sentido antihorario (Counter-Clockwise)
```

### Canales de Servos

```python
Servos.S1  # Servo canal 1
Servos.S2  # Servo canal 2
# ... hasta S8
```

### Motores DC

```python
Motors.M1  # Motor DC 1
Motors.M2  # Motor DC 2
Motors.M3  # Motor DC 3
Motors.M4  # Motor DC 4
```

### Controladores de Steppers

```python
Steppers.M1_M2  # Stepper usando motores M1 y M2
Steppers.M3_M4  # Stepper usando motores M3 y M4
```

### Tipos de Steppers

```python
StepperType.STEPPER_42  # Motor 42BYGH1861A-C
StepperType.STEPPER_28  # Motor 28BYJ-48
```

---

### Funciones de Control

#### `driver.servo(index, degree)`

Controla un servomotor.

**Parámetros:**
- `index`: Canal del servo (Servos.S1 a Servos.S8)
- `degree`: Ángulo en grados (0-180)

**Ejemplo:**
```python
driver.servo(Servos.S1, 90)  # Mover servo S1 a 90 grados
```

---

#### `driver.motor_run(index, direction, speed)`

Ejecuta un motor DC.

**Parámetros:**
- `index`: Número de motor (Motors.M1 a Motors.M4)
- `direction`: Dirección (Direction.CW o Direction.CCW)
- `speed`: Velocidad (0-255)

**Ejemplo:**
```python
driver.motor_run(Motors.M1, Direction.CW, 200)  # Motor M1 a velocidad 200 en sentido horario
```

---

#### `driver.stepper_degree_28(index, direction, degree)`

Rota un motor paso a paso 28BYJ-48 por grados.

**Parámetros:**
- `index`: Controlador (Steppers.M1_M2 o Steppers.M3_M4)
- `direction`: Dirección (Direction.CW o Direction.CCW)
- `degree`: Grados a rotar

**Ejemplo:**
```python
driver.stepper_degree_28(Steppers.M1_M2, Direction.CW, 180)  # Rotar 180 grados
```

---

#### `driver.stepper_turn_28(index, direction, turns)`

Rota un motor paso a paso 28BYJ-48 por vueltas completas.

**Parámetros:**
- `index`: Controlador (Steppers.M1_M2 o Steppers.M3_M4)
- `direction`: Dirección (Direction.CW o Direction.CCW)
- `turns`: Número de vueltas completas

**Ejemplo:**
```python
driver.stepper_turn_28(Steppers.M1_M2, Direction.CW, 2)  # Rotar 2 vueltas completas
```

---

#### `driver.stepper_degree_42(index, direction, degree)`

Rota un motor paso a paso 42BYGH1861A-C por grados.

**Parámetros:**
- `index`: Controlador (Steppers.M1_M2 o Steppers.M3_M4)
- `direction`: Dirección (Direction.CW o Direction.CCW)
- `degree`: Grados a rotar

**Ejemplo:**
```python
driver.stepper_degree_42(Steppers.M1_M2, Direction.CCW, 90)  # Rotar 90 grados antihorario
```

---

#### `driver.stepper_turn_42(index, direction, turns)`

Rota un motor paso a paso 42BYGH1861A-C por vueltas completas.

**Parámetros:**
- `index`: Controlador (Steppers.M1_M2 o Steppers.M3_M4)
- `direction`: Dirección (Direction.CW o Direction.CCW)
- `turns`: Número de vueltas completas

**Ejemplo:**
```python
driver.stepper_turn_42(Steppers.M3_M4, Direction.CW, 3)  # Rotar 3 vueltas completas
```

---

#### `driver.dual_stepper(stepper_type, dir1, deg1, dir2, deg2)`

Controla dos motores paso a paso simultáneamente.

**Parámetros:**
- `stepper_type`: Tipo de motor (StepperType.STEPPER_42 o StepperType.STEPPER_28)
- `dir1`: Dirección para M1_M2 (Direction.CW o Direction.CCW)
- `deg1`: Grados para M1_M2
- `dir2`: Dirección para M3_M4 (Direction.CW o Direction.CCW)
- `deg2`: Grados para M3_M4

**Ejemplo:**
```python
driver.dual_stepper(StepperType.STEPPER_42, Direction.CW, 90, Direction.CCW, 180)
```

---

#### `driver.motor_stop(index)`

Detiene un motor DC específico.

**Parámetros:**
- `index`: Número de motor (Motors.M1 a Motors.M4)

**Ejemplo:**
```python
driver.motor_stop(Motors.M1)  # Detener motor M1
```

---

#### `driver.motor_stop_all()`

Detiene todos los motores (parada de emergencia).

**Ejemplo:**
```python
driver.motor_stop_all()  # Detener todos los motores
```

---

## 📖 Ejemplos

Consulta la carpeta `examples/` para ver ejemplos completos:

- **`servo_example.py`**: Control de servos con barridos y patrones
- **`dc_motor_example.py`**: Control de motores DC con rampa de velocidad
- **`stepper_example.py`**: Control de motores paso a paso (28BYJ-48 y 42BYGH)

## 🔌 Conexiones Hardware

### Servos
- Conecta los servos a los puertos S1-S8
- Asegúrate de que la alimentación externa esté conectada (3.5V-5.5V)

### Motores DC
- Conecta los motores DC a los puertos M1-M4
- Respeta la polaridad para el control de dirección correcto

### Motores Paso a Paso
- **28BYJ-48**: Conecta a M1+M2 o M3+M4
- **42BYGH1861A-C**: Conecta a M1+M2 o M3+M4
- Cada motor paso a paso usa 2 puertos de motor DC

## ⚠️ Notas Importantes

1. **Alimentación Externa**: La placa requiere alimentación externa (3.5V-5.5V) para los motores
2. **Dirección I2C**: El controlador PCA9685 usa la dirección I2C 0x40
3. **Límites de Velocidad**: Los motores DC aceptan valores de 0-255
4. **Ángulos de Servo**: Los servos están limitados a 0-180 grados
5. **Timing de Steppers**: 
   - 28BYJ-48: ~1000ms por 360°
   - 42BYGH: ~500ms por 360°

## 🐛 Solución de Problemas

### Los motores no se mueven
- Verifica la alimentación externa
- Comprueba las conexiones I2C
- Asegúrate de que `dfrobot_motor.py` esté en el micro:bit

### Los servos no alcanzan el rango completo
- Algunos servos tienen rangos limitados (ej: 0-170°)
- Ajusta los valores de grado según tu servo específico

### Los steppers se mueven de forma irregular
- Verifica que estés usando el tipo correcto (STEPPER_28 vs STEPPER_42)
- Asegúrate de que la alimentación sea suficiente
- Comprueba las conexiones del motor

## 📄 Licencia

GNU Lesser General Public License

Basado en la extensión original de MakeCode: https://github.com/DFRobot/pxt-motor

## 🤝 Contribuciones

Este es un port de la extensión MakeCode original de DFRobot. Para reportar problemas o contribuir, por favor abre un issue o pull request.

## 📞 Soporte

Para preguntas sobre el hardware, visita: http://www.dfrobot.com.cn/goods-1577.html