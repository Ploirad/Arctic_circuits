"""
🎮 RETO 4: BLOQUE DEL DÍA (CONDICIONALES)
=========================================

🎯 OBJETIVO DE PYTHON:
Aprender a usar if, elif, else para tomar decisiones

📚 CONCEPTOS QUE VAS A APRENDER:
- Condicionales: if, elif, else
- Operadores de comparación: ==, !=, <, >, <=, >=
- Operadores lógicos: and, or, not
- Indentación (espacios al inicio de línea)

⚠️ ANTES DE EMPEZAR:
1. Servidor arrancado
2. Jugador en el mundo
3. Ejecuta: python reto_04_bloque_del_dia.py

═══════════════════════════════════════════════════════
"""

from mcpi.minecraft import Minecraft
from mcpi import block
import datetime

mc = Minecraft.create()

print("\n" + "="*50)
print("🎮 RETO 4: BLOQUE DEL DÍA")
print("="*50 + "\n")

# ============================================
# PARTE 1: IF BÁSICO
# ============================================
print("PARTE 1: Condicional IF básico")
print("-" * 30)

# if sirve para ejecutar código SOLO si una condición es verdadera
edad = 17

if edad >= 18:
    print("Eres mayor de edad")
    mc.postToChat("Eres mayor de edad")

# Este código se ejecuta siempre (no depende del if)
print("Edad: " + str(edad))

# ============================================
# PARTE 2: IF-ELSE
# ============================================
print("\nPARTE 2: IF-ELSE (si no...)")
print("-" * 30)

# else se ejecuta cuando el if es FALSO
edad = 16

if edad >= 18:
    print("Eres mayor de edad")
    mc.postToChat("Eres mayor de edad")
else:
    print("Eres menor de edad")
    mc.postToChat("Eres menor de edad")

# ============================================
# PARTE 3: IF-ELIF-ELSE
# ============================================
print("\nPARTE 3: IF-ELIF-ELSE (múltiples condiciones)")
print("-" * 30)

# elif (else if) permite comprobar múltiples condiciones
puntuacion = 85

if puntuacion >= 90:
    print("Calificación: Sobresaliente")
    nota = "Sobresaliente"
elif puntuacion >= 70:
    print("Calificación: Notable")
    nota = "Notable"
elif puntuacion >= 50:
    print("Calificación: Aprobado")
    nota = "Aprobado"
else:
    print("Calificación: Suspenso")
    nota = "Suspenso"

mc.postToChat("Tu nota: " + nota)

# ============================================
# PARTE 4: OPERADORES DE COMPARACIÓN
# ============================================
print("\nPARTE 4: Operadores de Comparación")
print("-" * 30)

a = 10
b = 5

print("a = " + str(a) + ", b = " + str(b))
print("a == b (igual): " + str(a == b))  # False
print("a != b (diferente): " + str(a != b))  # True
print("a > b (mayor que): " + str(a > b))  # True
print("a < b (menor que): " + str(a < b))  # False
print("a >= b (mayor o igual): " + str(a >= b))  # True
print("a <= b (menor o igual): " + str(a <= b))  # False

# ============================================
# PARTE 5: OPERADORES LÓGICOS
# ============================================
print("\nPARTE 5: Operadores Lógicos")
print("-" * 30)

edad = 17
tiene_permiso = True

# AND (y): Ambas condiciones deben ser verdaderas
if edad >= 16 and tiene_permiso:
    print("Puedes conducir un ciclomotor")
    mc.postToChat("Puedes conducir un ciclomotor")

# OR (o): Al menos una condición debe ser verdadera
es_fin_de_semana = True
es_festivo = False

if es_fin_de_semana or es_festivo:
    print("¡No hay clase!")
    mc.postToChat("¡No hay clase!")

# NOT (no): Invierte el valor
llueve = False

if not llueve:
    print("Buen día para construir")
    mc.postToChat("Buen día para construir")

# ============================================
# PARTE 6: EJEMPLO PRÁCTICO - BLOQUE DEL DÍA
# ============================================
print("\nPARTE 6: Ejemplo Práctico - Bloque del Día")
print("-" * 30)

# Obtener el día de la semana actual
dia_semana = datetime.datetime.now().weekday()
# 0=Lunes, 1=Martes, 2=Miércoles, 3=Jueves, 4=Viernes, 5=Sábado, 6=Domingo

print("Día de la semana: " + str(dia_semana))

# Según el día, elegimos un bloque diferente
if dia_semana == 0:  # Lunes
    material = block.DIAMOND_BLOCK.id
    nombre_dia = "Lunes"
    nombre_bloque = "Diamante"
elif dia_semana == 1:  # Martes
    material = block.GOLD_BLOCK.id
    nombre_dia = "Martes"
    nombre_bloque = "Oro"
elif dia_semana == 2:  # Miércoles
    material = block.IRON_BLOCK.id
    nombre_dia = "Miércoles"
    nombre_bloque = "Hierro"
elif dia_semana == 3:  # Jueves
    material = block.EMERALD_BLOCK.id
    nombre_dia = "Jueves"
    nombre_bloque = "Esmeralda"
elif dia_semana == 4:  # Viernes
    material = block.LAPIS_LAZULI_BLOCK.id
    nombre_dia = "Viernes"
    nombre_bloque = "Lapislázuli"
elif dia_semana == 5:  # Sábado
    material = block.REDSTONE_BLOCK.id
    nombre_dia = "Sábado"
    nombre_bloque = "Redstone"
else:  # Domingo
    material = block.GLOWSTONE_BLOCK.id
    nombre_dia = "Domingo"
    nombre_bloque = "Piedra luminosa"

# Colocar el bloque del día junto al jugador
pos = mc.player.getTilePos()
mc.setBlock(pos.x + 2, pos.y, pos.z, material)

mc.postToChat("=" * 30)
mc.postToChat("Hoy es " + nombre_dia)
mc.postToChat("Bloque del dia: " + nombre_bloque)
mc.postToChat("=" * 30)

# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 1
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 1: Comprobador de edad")
print("="*50 + "\n")

# Pide al usuario su edad
# Si es menor de 13: "Eres un niño"
# Si tiene entre 13 y 17: "Eres adolescente"
# Si tiene 18 o más: "Eres adulto"
# Muestra el mensaje en Minecraft

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 2
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 2: Sistema de acceso")
print("="*50 + "\n")

# Pide al usuario:
# - Un nombre de usuario
# - Una contraseña
#
# Si el nombre es "admin" Y la contraseña es "1234":
#   - Construye un bloque de diamante
#   - Envía mensaje "Acceso concedido"
# Si no:
#   - Construye un bloque de obsidiana
#   - Envía mensaje "Acceso denegado"

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 3
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 3: Calculadora con menú")
print("="*50 + "\n")

# Pide al usuario:
# - Dos números
# - Una operación (1=suma, 2=resta, 3=multiplicación, 4=división)
#
# Según la operación elegida, realiza el cálculo
# Muestra el resultado en Minecraft

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 4
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 4: Detector de posición")
print("="*50 + "\n")

# Obtén la posición Y del jugador (altura)
# Según la altura, muestra un mensaje:
# - Si Y < 20: "Estás en las profundidades"
# - Si Y entre 20 y 60: "Estás a nivel del suelo"
# - Si Y > 60: "Estás volando alto"
#
# Además, coloca un bloque diferente según la altura:
# - Profundidades: Obsidiana
# - Suelo: Piedra
# - Alto: Nube (lana blanca)

# ESCRIBE TU CÓDIGO AQUÍ:
pos = mc.player.getTilePos()
altura = pos.y

# Completa el código aquí




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 5
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 5: Selector de estructura")
print("="*50 + "\n")

# Crea un menú que pregunte qué estructura construir:
# 1 = Columna de 5 diamantes
# 2 = Pared de 5 oro
# 3 = Suelo de 3x3 esmeraldas
#
# Según la opción, construye la estructura junto al jugador

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 RETO EXTRA (OPCIONAL)
# ============================================
# Crea un "sistema de clima" que:
# - Genere un número aleatorio entre 1 y 10 (import random, random.randint(1,10))
# - Si es 1-3: "Lluvia" (coloca agua arriba del jugador)
# - Si es 4-7: "Soleado" (coloca piedra luminosa)
# - Si es 8-10: "Tormenta" (coloca bloques oscuros)

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# COMPROBACIÓN FINAL
# ============================================
print("\n" + "="*50)
print("🎉 ¡FELICIDADES! Has completado el Reto 4")
print("="*50)
print("\n📚 HAS APRENDIDO:")
print("  ✓ Condicionales: if, elif, else")
print("  ✓ Operadores de comparación: ==, !=, <, >, <=, >=")
print("  ✓ Operadores lógicos: and, or, not")
print("  ✓ Tomar decisiones en el código")
print("\n🚀 Siguiente paso: reto_05_torre_automatica.py")
print("="*50)

mc.postToChat("=" * 30)
mc.postToChat("RETO 4 COMPLETADO")
mc.postToChat("Total acumulado: 1 C$")
mc.postToChat("=" * 30)

"""
═══════════════════════════════════════════════════════
📖 RESUMEN DE LO QUE HAS APRENDIDO:

1. Condicionales:
   if condicion:
       # código si es verdadero
   elif otra_condicion:
       # código si la otra es verdadera
   else:
       # código si todas son falsas

2. Operadores de Comparación:
   == : igual a
   != : diferente de
   >  : mayor que
   <  : menor que
   >= : mayor o igual
   <= : menor o igual

3. Operadores Lógicos:
   and : Y (ambas condiciones verdaderas)
   or  : O (al menos una verdadera)
   not : NO (invierte el valor)

4. Indentación:
   En Python, los espacios al inicio de línea son IMPORTANTES
   Todo el código dentro de un if debe estar indentado (4 espacios)

🤖 CONEXIÓN CON EUROBOT:
Los robots toman decisiones constantemente:
- Si sensor detecta obstáculo -> girar
- Si batería baja -> volver a base
- Si encuentra pieza -> recogerla
- Si tiempo < 10 seg -> estrategia rápida

═══════════════════════════════════════════════════════
"""
