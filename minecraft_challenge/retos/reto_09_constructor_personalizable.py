"""
🎮 RETO 9: CONSTRUCTOR PERSONALIZABLE (FUNCIONES CON PARÁMETROS)
=================================================================

🎯 OBJETIVO DE PYTHON:
Aprender a crear funciones con parámetros para hacerlas más flexibles y potentes

📚 CONCEPTOS QUE VAS A APRENDER:
- Parámetros: valores que pasas a una función
- Argumentos: los valores reales que envías
- Funciones con múltiples parámetros
- Parámetros por defecto
- Return con funciones parametrizadas

⚠️ ANTES DE EMPEZAR:
1. Servidor arrancado
2. Jugador en el mundo
3. Ejecuta: python reto_09_constructor_personalizable.py

═══════════════════════════════════════════════════════
"""

from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

print("\n" + "="*50)
print("🎮 RETO 9: CONSTRUCTOR PERSONALIZABLE")
print("="*50 + "\n")

# ============================================
# PARTE 1: FUNCIONES CON UN PARÁMETRO
# ============================================
print("PARTE 1: Funciones con un parámetro")
print("-" * 30)

# Sin parámetro: siempre hace lo mismo
def saludar_simple():
    print("¡Hola!")

saludar_simple()
saludar_simple()  # Siempre igual

# Con parámetro: más flexible
def saludar_persona(nombre):
    print("¡Hola, " + nombre + "!")

saludar_persona("Ana")
saludar_persona("Carlos")
saludar_persona("María")  # Diferente cada vez

# ============================================
# PARTE 2: MÚLTIPLES PARÁMETROS
# ============================================
print("\nPARTE 2: Funciones con múltiples parámetros")
print("-" * 30)

def presentarse(nombre, edad, ciudad):
    mensaje = "Me llamo " + nombre + ", tengo " + str(edad) + " años y soy de " + ciudad
    print(mensaje)
    mc.postToChat(mensaje)

presentarse("Laura", 16, "Madrid")
presentarse("Pablo", 17, "Barcelona")

# ============================================
# PARTE 3: CONSTRUCCIÓN PARAMETRIZADA
# ============================================
print("\nPARTE 3: Construcción parametrizada")
print("-" * 30)

def construir_torre(altura, material):
    """Construye una torre de la altura y material especificados"""
    pos = mc.player.getTilePos()

    mc.postToChat("Construyendo torre de " + str(altura) + " bloques...")

    for i in range(altura):
        mc.setBlock(pos.x + 3, pos.y + i, pos.z, material)

    mc.postToChat("¡Torre completada!")

# Diferentes torres con la misma función
construir_torre(5, block.DIAMOND_BLOCK.id)  # Torre de 5 diamantes
construir_torre(10, block.GOLD_BLOCK.id)    # Torre de 10 oros
construir_torre(3, block.IRON_BLOCK.id)     # Torre de 3 hierros

# ============================================
# PARTE 4: CONSTRUCCIÓN DE CUBOS
# ============================================
print("\nPARTE 4: Constructor de cubos personalizable")
print("-" * 30)

def construir_cubo(tamaño, material, x_offset=5):
    """Construye un cubo del tamaño y material especificados"""
    pos = mc.player.getTilePos()

    mc.postToChat("Construyendo cubo " + str(tamaño) + "x" + str(tamaño) + "x" + str(tamaño))

    for x in range(tamaño):
        for y in range(tamaño):
            for z in range(tamaño):
                mc.setBlock(pos.x + x_offset + x, pos.y + y, pos.z + z, material)

    bloques_usados = tamaño ** 3
    mc.postToChat("Cubo completado! Bloques usados: " + str(bloques_usados))

construir_cubo(3, block.GLASS.id)
construir_cubo(4, block.EMERALD_BLOCK.id, 15)

# ============================================
# PARTE 5: PARÁMETROS POR DEFECTO
# ============================================
print("\nPARTE 5: Parámetros por defecto")
print("-" * 30)

def construir_pared(ancho=5, alto=3, material=block.BRICK_BLOCK.id):
    """Construye una pared con valores por defecto"""
    pos = mc.player.getTilePos()

    for x in range(ancho):
        for y in range(alto):
            mc.setBlock(pos.x + 20 + x, pos.y + y, pos.z, material)

    mc.postToChat("Pared: " + str(ancho) + "x" + str(alto))

# Usar valores por defecto
construir_pared()  # 5x3 de ladrillos

# Especificar solo algunos
construir_pared(10)  # 10x3 de ladrillos
construir_pared(7, 5)  # 7x5 de ladrillos
construir_pared(4, 4, block.GOLD_BLOCK.id)  # 4x4 de oro

# ============================================
# PARTE 6: FUNCIONES QUE DEVUELVEN VALORES
# ============================================
print("\nPARTE 6: Return con parámetros")
print("-" * 30)

def calcular_bloques_cubo(tamaño):
    """Calcula bloques necesarios para un cubo"""
    return tamaño ** 3

def calcular_bloques_pared(ancho, alto):
    """Calcula bloques necesarios para una pared"""
    return ancho * alto

def calcular_bloques_piramide(altura):
    """Calcula bloques necesarios para una pirámide"""
    total = 0
    for nivel in range(altura, 0, -1):
        total += nivel ** 2
    return total

# Usar las funciones
print("Cubo 5x5x5 necesita: " + str(calcular_bloques_cubo(5)) + " bloques")
print("Pared 10x5 necesita: " + str(calcular_bloques_pared(10, 5)) + " bloques")
print("Pirámide altura 4 necesita: " + str(calcular_bloques_piramide(4)) + " bloques")

# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 1
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 1: Función de multiplicación")
print("="*50 + "\n")

# Crea una función llamada "multiplicar" que:
# - Reciba dos parámetros: numero1 y numero2
# - Devuelva el resultado de multiplicarlos
# - Muestre el resultado en el chat de Minecraft
#
# Pruébala con diferentes valores

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 2
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 2: Escalera personalizada")
print("="*50 + "\n")

# Crea una función "construir_escalera" que reciba:
# - altura: número de escalones
# - material: tipo de bloque a usar
#
# La función debe construir una escalera donde cada escalón
# esté 1 bloque más alto y 1 bloque más adelante que el anterior

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 3
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 3: Rectángulo personalizado")
print("="*50 + "\n")

# Crea una función "construir_rectangulo" que reciba:
# - ancho: bloques de ancho
# - largo: bloques de largo
# - material: tipo de bloque
# - hueco: True para hacer rectángulo hueco, False para relleno
#
# La función debe construir el rectángulo en el suelo junto al jugador

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 4
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 4: Generador de patrones")
print("="*50 + "\n")

# Crea una función "construir_patron" que reciba:
# - longitud: longitud del patrón
# - material1: primer material
# - material2: segundo material
#
# La función debe construir una fila alternando entre los dos materiales

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 5
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 5: Constructor inteligente")
print("="*50 + "\n")

# Crea una función "construir_estructura" que reciba:
# - tipo: "torre", "cubo" o "pared"
# - tamaño: tamaño de la estructura
# - material: tipo de bloque (opcional, por defecto piedra)
#
# Según el tipo, debe construir la estructura correspondiente
# usando las funciones que ya has creado

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 RETO EXTRA (OPCIONAL)
# ============================================
# Crea una función "construir_casa" que reciba:
# - tamaño: tamaño de la casa
# - material_paredes: material para las paredes
# - material_techo: material para el techo
# - con_puerta: True/False para añadir puerta
# - con_ventanas: True/False para añadir ventanas
#
# La función debe construir una casa completa con todas estas opciones

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# COMPROBACIÓN FINAL
# ============================================
print("\n" + "="*50)
print("🎉 ¡FELICIDADES! Has completado el Reto 9")
print("="*50)
print("\n📚 HAS APRENDIDO:")
print("  ✓ Funciones con parámetros")
print("  ✓ Múltiples parámetros")
print("  ✓ Parámetros por defecto")
print("  ✓ Return con parámetros")
print("  ✓ Funciones flexibles y reutilizables")
print("\n🚀 Siguiente paso: reto_10_mundo_automatico.py")
print("🏆 ¡ÚLTIMO RETO! ¡Proyecto final!")
print("="*50)

mc.postToChat("=" * 30)
mc.postToChat("RETO 9 COMPLETADO")
mc.postToChat("Total acumulado: 2 C$")
mc.postToChat("ULTIMO RETO PROXIMO!")
mc.postToChat("=" * 30)

"""
═══════════════════════════════════════════════════════
📖 RESUMEN DE LO QUE HAS APRENDIDO:

1. Función con parámetros:
   def mi_funcion(parametro1, parametro2):
       # usar parametro1 y parametro2

2. Llamar con argumentos:
   mi_funcion(valor1, valor2)

3. Parámetros por defecto:
   def mi_funcion(param1, param2=10):
       # param2 tiene valor por defecto

4. Return con parámetros:
   def calcular(x, y):
       resultado = x + y
       return resultado

5. Ventajas:
   - Funciones más flexibles
   - Reutilizar código con diferentes valores
   - Código más limpio y mantenible

🤖 CONEXIÓN CON EUROBOT:
Las funciones con parámetros son LA BASE de la programación robótica:

def avanzar(distancia_cm, velocidad):
    # mover el robot

def girar(angulo, direccion):
    # girar el robot

def mover_servo(servo_id, angulo):
    # mover un servo específico

def recoger_pieza(tipo_pieza, posicion):
    # recoger pieza específica

Esto permite:
- Reutilizar código con diferentes valores
- Crear comportamientos complejos combinando funciones simples
- Ajustar estrategias sin reescribir código
- Probar y depurar más fácilmente

Ejemplo de estrategia completa:
avanzar(50, velocidad_media)
girar(90, "derecha")
avanzar(30, velocidad_lenta)
recoger_pieza("cubo", posicion_actual)
girar(180, "izquierda")
avanzar(80, velocidad_rapida)

═══════════════════════════════════════════════════════
"""
