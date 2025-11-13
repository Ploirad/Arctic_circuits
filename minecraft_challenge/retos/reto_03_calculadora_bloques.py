"""
🎮 RETO 3: CALCULADORA DE BLOQUES
==================================
💰 Recompensa: 1 Cervantes Dollar (C$)

🎯 OBJETIVO DE PYTHON:
Aprender operaciones matemáticas en Python

📚 CONCEPTOS QUE VAS A APRENDER:
- Operadores aritméticos: +, -, *, /, //, %, **
- Orden de operaciones (como en matemáticas)
- Operaciones con variables
- Cálculos útiles para construcciones

⚠️ ANTES DE EMPEZAR:
1. Servidor arrancado
2. Jugador en el mundo
3. Ejecuta: python reto_03_calculadora_bloques.py

═══════════════════════════════════════════════════════
"""

from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

print("\n" + "="*50)
print("🎮 RETO 3: CALCULADORA DE BLOQUES")
print("="*50 + "\n")

# ============================================
# PARTE 1: OPERADORES BÁSICOS
# ============================================
print("PARTE 1: Operadores Básicos")
print("-" * 30)

# Suma (+)
bloques_dia_1 = 50
bloques_dia_2 = 75
total_bloques = bloques_dia_1 + bloques_dia_2
print("Bloques día 1: " + str(bloques_dia_1))
print("Bloques día 2: " + str(bloques_dia_2))
print("Total bloques: " + str(total_bloques))

# Resta (-)
bloques_necesarios = 200
bloques_que_tengo = 150
bloques_que_faltan = bloques_necesarios - bloques_que_tengo
print("\nNecesito: " + str(bloques_necesarios))
print("Tengo: " + str(bloques_que_tengo))
print("Me faltan: " + str(bloques_que_faltan))

# Multiplicación (*)
bloques_por_fila = 10
numero_filas = 5
total = bloques_por_fila * numero_filas
print("\nBloques por fila: " + str(bloques_por_fila))
print("Número de filas: " + str(numero_filas))
print("Total: " + str(total))

# División (/)
bloques_totales = 100
jugadores = 4
bloques_por_jugador = bloques_totales / jugadores
print("\nBloques totales: " + str(bloques_totales))
print("Jugadores: " + str(jugadores))
print("Bloques por jugador: " + str(bloques_por_jugador))

# ============================================
# PARTE 2: OPERADORES AVANZADOS
# ============================================
print("\n\nPARTE 2: Operadores Avanzados")
print("-" * 30)

# División entera (//)
# Devuelve solo la parte entera, sin decimales
print("\nDivisión normal: 17 / 5 = " + str(17 / 5))
print("División entera: 17 // 5 = " + str(17 // 5))

# Módulo (%)
# Devuelve el RESTO de una división
print("\nMódulo: 17 % 5 = " + str(17 % 5))
print("(17 dividido entre 5 es 3, y sobran 2)")

# El módulo es útil para saber si un número es par o impar
numero = 10
if numero % 2 == 0:
    print("\n" + str(numero) + " es PAR")
else:
    print("\n" + str(numero) + " es IMPAR")

# Potencia (**)
base = 2
exponente = 3
resultado = base ** exponente
print("\n" + str(base) + " elevado a " + str(exponente) + " = " + str(resultado))

# ============================================
# PARTE 3: ORDEN DE OPERACIONES
# ============================================
print("\n\nPARTE 3: Orden de Operaciones")
print("-" * 30)

# Python sigue las reglas matemáticas (PEMDAS)
# 1. Paréntesis
# 2. Exponentes
# 3. Multiplicación y División
# 4. Suma y Resta

resultado_1 = 5 + 3 * 2
print("5 + 3 * 2 = " + str(resultado_1))  # Resultado: 11 (primero 3*2, luego +5)

resultado_2 = (5 + 3) * 2
print("(5 + 3) * 2 = " + str(resultado_2))  # Resultado: 16 (primero 5+3, luego *2)

# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 1
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 1: Calculadora de cubos")
print("="*50 + "\n")

# Pide al usuario el tamaño de lado de un cubo
# Calcula cuántos bloques necesita para construirlo
# Fórmula: lado * lado * lado  (o lado ** 3)
# Muestra el resultado en consola y en Minecraft

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 2
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 2: Calculadora de pirámide")
print("="*50 + "\n")

# Una pirámide de altura 3 tiene:
# - Base: 3x3 = 9 bloques
# - Medio: 2x2 = 4 bloques
# - Cima: 1x1 = 1 bloque
# Total: 9 + 4 + 1 = 14 bloques
#
# Pide al usuario la altura de la pirámide
# Calcula cuántos bloques necesita para cada nivel
# Muestra el total en Minecraft

# PISTA: Para altura 4 sería: 16 + 9 + 4 + 1 = 30

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 3
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 3: División de tesoro")
print("="*50 + "\n")

# Has encontrado un cofre con bloques de diamante
# Tienes que repartirlos entre todos los jugadores
#
# Pide:
# - Cuántos diamantes hay en total
# - Cuántos jugadores hay
#
# Calcula:
# - Cuántos diamantes le tocan a cada uno (división entera)
# - Cuántos diamantes sobran (módulo)
#
# Muestra los resultados en Minecraft

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 4
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 4: Constructor de cuadrado")
print("="*50 + "\n")

# Pide al usuario el tamaño del lado de un cuadrado
# Construye un cuadrado HUECO de ese tamaño en Minecraft
# (solo los bordes, no relleno)
#
# Por ejemplo, para lado=5:
# XXXXX
# X   X
# X   X
# X   X
# XXXXX
#
# Calcula cuántos bloques necesitas:
# Perímetro = lado * 4 - 4 (se restan 4 porque las esquinas se cuentan dos veces)

# ESCRIBE TU CÓDIGO AQUÍ:
lado = int(input("¿Tamaño del lado del cuadrado? "))

# Calcular bloques necesarios
bloques_necesarios = lado * 4 - 4
print("Necesitas " + str(bloques_necesarios) + " bloques")
mc.postToChat("Cuadrado de lado " + str(lado) + " = " + str(bloques_necesarios) + " bloques")

# Obtener posición
pos = mc.player.getTilePos()

# Construir el cuadrado (solo bordes)
# Lado superior
for i in range(lado):
    mc.setBlock(pos.x + i, pos.y, pos.z, block.GOLD_BLOCK.id)

# Lado derecho
for i in range(lado):
    mc.setBlock(pos.x + lado - 1, pos.y, pos.z + i, block.GOLD_BLOCK.id)

# Lado inferior
for i in range(lado):
    mc.setBlock(pos.x + i, pos.y, pos.z + lado - 1, block.GOLD_BLOCK.id)

# Lado izquierdo
for i in range(lado):
    mc.setBlock(pos.x, pos.y, pos.z + i, block.GOLD_BLOCK.id)

mc.postToChat("¡Cuadrado construido!")

# ============================================
# 🎯 RETO EXTRA (OPCIONAL)
# ============================================
# Crea una calculadora de distancia entre dos puntos en 3D
# Pide las coordenadas (x1, y1, z1) y (x2, y2, z2)
# Usa la fórmula: √[(x2-x1)² + (y2-y1)² + (z2-z1)²]
# PISTA: import math, luego usa math.sqrt() para raíz cuadrada

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# COMPROBACIÓN FINAL
# ============================================
print("\n" + "="*50)
print("🎉 ¡FELICIDADES! Has completado el Reto 3")
print("="*50)
print("\n📚 HAS APRENDIDO:")
print("  ✓ Operadores básicos: +, -, *, /")
print("  ✓ Operadores avanzados: //, %, **")
print("  ✓ Orden de operaciones")
print("  ✓ Cálculos útiles para construcciones")
print("\n💰 RECOMPENSA: 1 Cervantes Dollar")
print("💰 TOTAL ACUMULADO: 1 C$")
print("\n🚀 Siguiente paso: reto_04_bloque_del_dia.py")
print("="*50)

mc.postToChat("=" * 30)
mc.postToChat("RETO 3 COMPLETADO")
mc.postToChat("Has ganado 1 C$")
mc.postToChat("Total: 1 C$")
mc.postToChat("=" * 30)

"""
═══════════════════════════════════════════════════════
📖 RESUMEN DE LO QUE HAS APRENDIDO:

1. Operadores Aritméticos:
   + : suma
   - : resta
   * : multiplicación
   / : división (con decimales)
   // : división entera (sin decimales)
   % : módulo (resto de la división)
   ** : potencia

2. Orden de operaciones (PEMDAS):
   1. Paréntesis ()
   2. Exponentes **
   3. Multiplicación * y División /
   4. Suma + y Resta -

3. Usos prácticos:
   - Calcular materiales para construcciones
   - Dividir recursos entre jugadores
   - Determinar posiciones y distancias
   - Crear patrones matemáticos

🤖 CONEXIÓN CON EUROBOT:
En robótica usas matemáticas constantemente:
- Calcular velocidad del robot (distancia / tiempo)
- Convertir ángulos (grados a radianes)
- Determinar posición con sensores
- Calcular trayectorias y movimientos
- Repartir tareas entre múltiples robots

═══════════════════════════════════════════════════════
"""
