"""
🎮 RETO 5: TORRE AUTOMÁTICA (BUCLE FOR)
========================================
💰 Recompensa: 1 Cervantes Dollar (C$)

🎯 OBJETIVO DE PYTHON:
Aprender a usar bucles for para repetir código

📚 CONCEPTOS QUE VAS A APRENDER:
- Bucle for: repetir código un número fijo de veces
- range(): generar secuencias de números
- Iteración: recorrer elementos uno por uno
- Bucles anidados: un bucle dentro de otro

⚠️ ANTES DE EMPEZAR:
1. Servidor arrancado
2. Jugador en el mundo
3. Ejecuta: python reto_05_torre_automatica.py

═══════════════════════════════════════════════════════
"""

from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create()

print("\n" + "="*50)
print("🎮 RETO 5: TORRE AUTOMÁTICA")
print("="*50 + "\n")

# ============================================
# PARTE 1: FOR BÁSICO CON RANGE
# ============================================
print("PARTE 1: Bucle FOR básico")
print("-" * 30)

# range(5) genera los números: 0, 1, 2, 3, 4
print("\nContando del 0 al 4:")
for i in range(5):
    print("Número: " + str(i))

# range(inicio, fin) genera números desde inicio hasta fin-1
print("\nContando del 1 al 5:")
for i in range(1, 6):
    print("Número: " + str(i))

# range(inicio, fin, paso) genera números con un salto específico
print("\nContando de 2 en 2:")
for i in range(0, 10, 2):
    print("Número: " + str(i))

# ============================================
# PARTE 2: CONSTRUYENDO UNA TORRE
# ============================================
print("\nPARTE 2: Construyendo una torre")
print("-" * 30)

# Obtener posición del jugador
pos = mc.player.getTilePos()

# Construir una torre de 10 bloques de altura
mc.postToChat("Construyendo torre de 10 bloques...")
for altura in range(10):
    mc.setBlock(pos.x + 3, pos.y + altura, pos.z, block.BRICK_BLOCK.id)
    print("Bloque colocado a altura: " + str(altura))

mc.postToChat("¡Torre completada!")

# ============================================
# PARTE 3: TORRE MULTICOLOR
# ============================================
print("\nPARTE 3: Torre multicolor")
print("-" * 30)

# Lista de materiales para alternar
materiales = [
    block.DIAMOND_BLOCK.id,
    block.GOLD_BLOCK.id,
    block.EMERALD_BLOCK.id,
    block.IRON_BLOCK.id
]

mc.postToChat("Construyendo torre multicolor...")
for altura in range(12):
    # Usar el operador módulo (%) para alternar entre materiales
    material_index = altura % len(materiales)
    material = materiales[material_index]

    mc.setBlock(pos.x + 5, pos.y + altura, pos.z, material)
    time.sleep(0.1)  # Pausa breve para ver la construcción

mc.postToChat("¡Torre multicolor completada!")

# ============================================
# PARTE 4: BUCLES ANIDADOS (PARED)
# ============================================
print("\nPARTE 4: Bucles anidados - Construcción de pared")
print("-" * 30)

# Un bucle dentro de otro para hacer estructuras 2D
mc.postToChat("Construyendo pared de 5x5...")

for y in range(5):  # Altura (5 bloques)
    for x in range(5):  # Ancho (5 bloques)
        mc.setBlock(pos.x + 7 + x, pos.y + y, pos.z, block.STONE_BRICK.id)
        print("Bloque en posición: (" + str(x) + ", " + str(y) + ")")

mc.postToChat("¡Pared completada!")

# ============================================
# PARTE 5: BUCLES ANIDADOS TRIPLE (CUBO)
# ============================================
print("\nPARTE 5: Triple bucle anidado - Cubo")
print("-" * 30)

# Tres bucles anidados para estructuras 3D
mc.postToChat("Construyendo cubo de 4x4x4...")

for x in range(4):  # Ancho
    for y in range(4):  # Alto
        for z in range(4):  # Profundidad
            mc.setBlock(pos.x + 13 + x, pos.y + y, pos.z + z, block.GLASS.id)

mc.postToChat("¡Cubo de vidrio completado!")

# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 1
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 1: Torre personalizada")
print("="*50 + "\n")

# Pide al usuario:
# - La altura de la torre
# - El tipo de material (1=piedra, 2=madera, 3=ladrillo, 4=oro)
#
# Construye la torre con esas especificaciones

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 2
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 2: Escalera automática")
print("="*50 + "\n")

# Construye una escalera de 10 escalones
# Cada escalón debe estar:
# - 1 bloque más alto que el anterior (Y + 1)
# - 1 bloque más adelante que el anterior (X + 1)
#
# Pista: usa el mismo número (i) para ambas coordenadas

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 3
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 3: Suelo de tablero de ajedrez")
print("="*50 + "\n")

# Crea un suelo de 8x8 con patrón de ajedrez
# Alterna entre bloques blancos (lana blanca) y negros (obsidiana)
#
# Pista: usa (x + z) % 2 para determinar el color
# Si es 0: blanco, si es 1: negro

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 4
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 4: Pirámide creciente")
print("="*50 + "\n")

# Construye una pirámide de 5 niveles
# Nivel 1 (base): 5x5 bloques
# Nivel 2: 4x4 bloques (centrado)
# Nivel 3: 3x3 bloques (centrado)
# Nivel 4: 2x2 bloques (centrado)
# Nivel 5 (cima): 1x1 bloque
#
# Pista: El tamaño de cada nivel es (altura_total - nivel_actual)

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 5
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 5: Túnel automático")
print("="*50 + "\n")

# Crea un túnel de 20 bloques de longitud
# El túnel debe ser hueco: 3 bloques de ancho, 3 de alto
# Solo construye el techo, suelo y paredes (no el interior)

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 RETO EXTRA (OPCIONAL)
# ============================================
# Crea un "espiral ascendente"
# Construye bloques que suban en espiral alrededor de un punto central
# Pista: usa matemáticas (sin(ángulo), cos(ángulo)) para el círculo
# import math, luego math.sin() y math.cos()

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# COMPROBACIÓN FINAL
# ============================================
print("\n" + "="*50)
print("🎉 ¡FELICIDADES! Has completado el Reto 5")
print("="*50)
print("\n📚 HAS APRENDIDO:")
print("  ✓ Bucle for para repetir código")
print("  ✓ range() para generar secuencias")
print("  ✓ Bucles anidados para estructuras 2D y 3D")
print("  ✓ Construir automáticamente en Minecraft")
print("\n💰 RECOMPENSA: 1 Cervantes Dollar")
print("💰 TOTAL ACUMULADO: 2 C$")
print("\n🚀 Siguiente paso: reto_06_constructor_infinito.py")
print("="*50)

mc.postToChat("=" * 30)
mc.postToChat("RETO 5 COMPLETADO")
mc.postToChat("Has ganado 1 C$")
mc.postToChat("Total: 2 C$")
mc.postToChat("=" * 30)

"""
═══════════════════════════════════════════════════════
📖 RESUMEN DE LO QUE HAS APRENDIDO:

1. Bucle FOR:
   for variable in range(numero):
       # código a repetir

   Se repite el número de veces especificado

2. range():
   range(5)        → 0, 1, 2, 3, 4
   range(1, 6)     → 1, 2, 3, 4, 5
   range(0, 10, 2) → 0, 2, 4, 6, 8

3. Bucles anidados:
   for i in range(5):
       for j in range(5):
           # Este código se ejecuta 5*5 = 25 veces

4. Usos prácticos:
   - Construir torres (1D)
   - Construir paredes (2D)
   - Construir cubos (3D)
   - Crear patrones y diseños

🤖 CONEXIÓN CON EUROBOT:
Los bucles son fundamentales en robótica:
- Repetir movimientos (avanzar 10 veces)
- Buscar objetos (mirar en todas direcciones)
- Seguir líneas (leer sensor constantemente)
- Ejecutar estrategias (repetir secuencia de acciones)

En Eurobot, muchas tareas se repiten:
- Recoger múltiples piezas
- Visitar varios puntos del tablero
- Comprobar sensores continuamente

═══════════════════════════════════════════════════════
"""
