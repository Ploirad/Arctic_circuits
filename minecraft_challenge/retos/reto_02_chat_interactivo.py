"""
🎮 RETO 2: CHAT INTERACTIVO CON EL JUGADOR
===========================================

🎯 OBJETIVO DE PYTHON:
Aprender a usar input() y trabajar con diferentes tipos de datos

📚 CONCEPTOS QUE VAS A APRENDER:
- input(): pedir información al usuario
- Tipos de datos: string (texto), int (enteros), float (decimales)
- Conversión de tipos: str(), int(), float()
- Concatenación avanzada

⚠️ ANTES DE EMPEZAR:
1. Asegúrate de que el servidor está arrancado
2. Entra al mundo de Minecraft
3. Ejecuta: python reto_02_chat_interactivo.py

═══════════════════════════════════════════════════════
"""

from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

print("\n" + "="*50)
print("🎮 RETO 2: CHAT INTERACTIVO")
print("="*50 + "\n")

# ============================================
# PARTE 1: ENTENDIENDO INPUT()
# ============================================
# input() sirve para PEDIR información al usuario
# El programa se DETIENE y espera a que escribas algo

print("EJEMPLO 1: Input básico")
print("-" * 30)

nombre_usuario = input("¿Cómo te llamas? ")
print("¡Hola, " + nombre_usuario + "!")

# Ahora enviamos ese nombre a Minecraft
mc.postToChat("¡Hola, " + nombre_usuario + "!")

# ============================================
# PARTE 2: TIPOS DE DATOS
# ============================================
# En Python hay diferentes TIPOS de datos:
# - string (str): texto, ejemplo "Hola"
# - integer (int): números enteros, ejemplo 42
# - float: números con decimales, ejemplo 3.14

print("\nEJEMPLO 2: Tipos de datos")
print("-" * 30)

# IMPORTANTE: input() SIEMPRE devuelve un STRING (texto)
# Aunque escribas un número, Python lo ve como texto

edad_texto = input("¿Cuántos años tienes? ")
print("Tipo de dato: " + str(type(edad_texto)))  # Muestra: <class 'str'>

# Para hacer operaciones matemáticas necesitas convertirlo a int
edad_numero = int(edad_texto)
print("Ahora es un número: " + str(type(edad_numero)))  # Muestra: <class 'int'>

# ============================================
# PARTE 3: CONVERSIÓN DE TIPOS
# ============================================
print("\nEJEMPLO 3: Conversión de tipos")
print("-" * 30)

# str() convierte cualquier cosa a texto
numero = 42
texto = str(numero)
print("Número convertido a texto: " + texto)

# int() convierte texto a número entero
texto_numero = "100"
numero_entero = int(texto_numero)
print("Texto convertido a número: " + str(numero_entero))

# float() convierte a número decimal
texto_decimal = "3.14"
numero_decimal = float(texto_decimal)
print("Texto convertido a decimal: " + str(numero_decimal))

# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 1
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 1: Tu presentación completa")
print("="*50 + "\n")

# Pide al usuario:
# 1. Su nombre
# 2. Su edad (conviértela a int)
# 3. Su ciudad
# 4. Su robot favorito (o superhéroe)
#
# Luego envía un mensaje a Minecraft con toda esa información

# ESCRIBE TU CÓDIGO AQUÍ:
# nombre =
# edad =
# ciudad =
# favorito =




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 2
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 2: Calculando edades")
print("="*50 + "\n")

# Pide al usuario su año de nacimiento
# Calcula su edad (2026 - año_nacimiento)
# Muestra el resultado en Minecraft

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 3
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 3: Teletransporte personalizado")
print("="*50 + "\n")

# Pide al usuario tres números:
# - coordenada X
# - coordenada Y
# - coordenada Z
#
# Luego teletransporta al jugador a esas coordenadas
# Pista: usa mc.player.setTilePos(x, y, z)

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 4
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 4: Constructor de bloques personalizados")
print("="*50 + "\n")

# Pide al usuario:
# - Cuántos bloques quiere construir en vertical (altura)
# - Qué tipo de bloque (1=piedra, 2=madera, 3=oro, 4=diamante)
#
# Luego construye una torre de ese tamaño con ese material
# junto al jugador

# PISTA: Necesitarás un bucle for (pero aún no lo hemos aprendido bien)
# Por ahora, construye solo 3 bloques de ejemplo

# ESCRIBE TU CÓDIGO AQUÍ:
altura = int(input("¿Qué altura quieres? (solo construiremos 3 por ahora): "))
tipo_bloque = int(input("Tipo de bloque (1=piedra, 2=madera, 3=oro): "))

# Obtener posición del jugador
pos = mc.player.getTilePos()

# Decide qué bloque usar
if tipo_bloque == 1:
    material = block.STONE.id
elif tipo_bloque == 2:
    material = block.WOOD.id
elif tipo_bloque == 3:
    material = block.GOLD_BLOCK.id
else:
    material = block.DIAMOND_BLOCK.id

# Construir 3 bloques de ejemplo
mc.setBlock(pos.x + 2, pos.y, pos.z, material)
mc.setBlock(pos.x + 2, pos.y + 1, pos.z, material)
mc.setBlock(pos.x + 2, pos.y + 2, pos.z, material)

mc.postToChat("¡Torre de 3 bloques construida!")

# ============================================
# 🎯 RETO EXTRA (OPCIONAL)
# ============================================
# Crea un "generador de mensajes personalizados"
# que pida:
# - Un saludo (Hola, Hey, Buenos días...)
# - Un nombre
# - Una despedida (Adiós, Hasta luego, Nos vemos...)
#
# Y envíe todo junto al chat de Minecraft

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# COMPROBACIÓN FINAL
# ============================================
print("\n" + "="*50)
print("🎉 ¡FELICIDADES! Has completado el Reto 2")
print("="*50)
print("\n📚 HAS APRENDIDO:")
print("  ✓ Usar input() para pedir información al usuario")
print("  ✓ Entender los tipos de datos (string, int, float)")
print("  ✓ Convertir entre tipos con str(), int(), float()")
print("  ✓ Interactuar con el usuario desde Python")
print("\n🚀 Siguiente paso: reto_03_calculadora_bloques.py")
print("="*50)

mc.postToChat("=" * 30)
mc.postToChat("RETO 2 COMPLETADO")
mc.postToChat("=" * 30)

"""
═══════════════════════════════════════════════════════
📖 RESUMEN DE LO QUE HAS APRENDIDO:

1. input()
   - Pide información al usuario
   - El programa espera a que escribas
   - SIEMPRE devuelve un string (texto)
   - Sintaxis: variable = input("pregunta")

2. Tipos de datos
   - str: texto ("Hola")
   - int: números enteros (42)
   - float: números decimales (3.14)

3. Conversión de tipos
   - int("42") convierte "42" a número 42
   - str(42) convierte 42 a texto "42"
   - float("3.14") convierte "3.14" a decimal 3.14

4. ¿Por qué es importante?
   - input() da texto, pero a veces necesitas números
   - Para hacer matemáticas necesitas int o float
   - Para mostrar números con texto necesitas str

🤖 CONEXIÓN CON EUROBOT:
En robótica necesitas leer valores de sensores (input):
- Distancia medida por sensor ultrasónico (float)
- Estado del botón (True/False)
- Ángulo del servo (int)
Y convertirlos al tipo correcto para procesarlos

═══════════════════════════════════════════════════════
"""
