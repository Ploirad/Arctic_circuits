"""
🎮 RETO 8: MI PRIMERA FUNCIÓN
==============================

🎯 OBJETIVO DE PYTHON:
Aprender a crear y usar funciones para organizar y reutilizar código

📚 CONCEPTOS QUE VAS A APRENDER:
- Qué es una función
- Definir funciones con def
- Llamar (ejecutar) funciones
- Scope (alcance) de variables
- Por qué las funciones son útiles

⚠️ ANTES DE EMPEZAR:
1. Servidor arrancado
2. Jugador en el mundo
3. Ejecuta: python reto_08_primera_funcion.py

═══════════════════════════════════════════════════════
"""

from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

print("\n" + "="*50)
print("🎮 RETO 8: MI PRIMERA FUNCIÓN")
print("="*50 + "\n")

# ============================================
# PARTE 1: ¿QUÉ ES UNA FUNCIÓN?
# ============================================
print("PARTE 1: ¿Qué es una función?")
print("-" * 30)

# Una función es un bloque de código con un NOMBRE
# Puedes ejecutarla (llamarla) tantas veces como quieras
# Es como crear tu propio comando personalizado

# Ejemplo SIN función (código repetitivo):
print("\nSin función (código repetitivo):")
print("¡Hola!")
print("¡Bienvenido!")
print("---")
print("¡Hola!")
print("¡Bienvenido!")
print("---")
print("¡Hola!")
print("¡Bienvenido!")

# Ejemplo CON función (código reutilizable):
def saludar():
    print("¡Hola!")
    print("¡Bienvenido!")

print("\nCon función (código reutilizable):")
saludar()
print("---")
saludar()
print("---")
saludar()

# ============================================
# PARTE 2: DEFINIR FUNCIONES
# ============================================
print("\nPARTE 2: Definir funciones con def")
print("-" * 30)

# Sintaxis:
# def nombre_funcion():
#     código de la función

def mostrar_mensaje():
    print("Este es un mensaje desde una función")
    mc.postToChat("Mensaje desde función!")

# La función está definida, pero NO se ejecuta hasta que la llames
print("Función definida, pero aún no ejecutada")

# Llamar (ejecutar) la función:
mostrar_mensaje()
mostrar_mensaje()  # Podemos llamarla múltiples veces

# ============================================
# PARTE 3: FUNCIONES PARA CONSTRUCCIÓN
# ============================================
print("\nPARTE 3: Funciones para construcción")
print("-" * 30)

def construir_torre():
    """Construye una torre de 5 bloques de oro"""
    pos = mc.player.getTilePos()
    for i in range(5):
        mc.setBlock(pos.x + 3, pos.y + i, pos.z, block.GOLD_BLOCK.id)
    mc.postToChat("Torre de oro construida!")

def construir_cubo():
    """Construye un cubo de vidrio 3x3x3"""
    pos = mc.player.getTilePos()
    for x in range(3):
        for y in range(3):
            for z in range(3):
                mc.setBlock(pos.x + 6 + x, pos.y + y, pos.z + z, block.GLASS.id)
    mc.postToChat("Cubo de vidrio construido!")

def construir_pared():
    """Construye una pared de ladrillos 5x3"""
    pos = mc.player.getTilePos()
    for x in range(5):
        for y in range(3):
            mc.setBlock(pos.x + 10 + x, pos.y + y, pos.z, block.BRICK_BLOCK.id)
    mc.postToChat("Pared de ladrillos construida!")

# Ahora podemos construir todo fácilmente:
print("Construyendo estructuras...")
construir_torre()
construir_cubo()
construir_pared()

# ============================================
# PARTE 4: FUNCIONES CON RETURN
# ============================================
print("\nPARTE 4: Funciones que devuelven valores")
print("-" * 30)

# return devuelve un valor de la función
def calcular_bloques_cubo(tamaño):
    """Calcula cuántos bloques necesitas para un cubo"""
    return tamaño * tamaño * tamaño

# Usar el valor devuelto
bloques = calcular_bloques_cubo(5)
print("Bloques necesarios para cubo 5x5x5: " + str(bloques))

bloques = calcular_bloques_cubo(10)
print("Bloques necesarios para cubo 10x10x10: " + str(bloques))

def obtener_posicion_jugador():
    """Obtiene y devuelve la posición del jugador"""
    pos = mc.player.getTilePos()
    return pos

# Usar la posición
posicion = obtener_posicion_jugador()
print("Estás en: X=" + str(posicion.x) + " Y=" + str(posicion.y) + " Z=" + str(posicion.z))

# ============================================
# PARTE 5: SCOPE (ALCANCE) DE VARIABLES
# ============================================
print("\nPARTE 5: Scope de variables")
print("-" * 30)

# Variables FUERA de funciones son GLOBALES
variable_global = "Soy global"

def mi_funcion():
    # Variables DENTRO de funciones son LOCALES
    variable_local = "Soy local"
    print("Dentro de la función:")
    print("  " + variable_global)  # Puedo acceder a la global
    print("  " + variable_local)

mi_funcion()

print("\nFuera de la función:")
print("  " + variable_global)  # Funciona
# print("  " + variable_local)  # ERROR: no existe fuera de la función

# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 1
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 1: Tu función de saludo")
print("="*50 + "\n")

# Crea una función llamada "mi_saludo" que:
# - Muestre tu nombre en la consola
# - Muestre tu edad en la consola
# - Envíe un saludo al chat de Minecraft
# Luego llama a la función 3 veces

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 2
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 2: Función de cuenta atrás")
print("="*50 + "\n")

# Crea una función llamada "cuenta_atras" que:
# - Cuente desde 5 hasta 0
# - Muestre cada número en consola
# - Al llegar a 0, envíe "¡DESPEGUE!" al chat de Minecraft
# - Construya un bloque de TNT junto al jugador

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 3
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 3: Calculadora con funciones")
print("="*50 + "\n")

# Crea 4 funciones:
# - sumar(a, b): devuelve a + b
# - restar(a, b): devuelve a - b
# - multiplicar(a, b): devuelve a * b
# - dividir(a, b): devuelve a / b
#
# Luego prueba cada función con diferentes números
# y muestra los resultados

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 4
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 4: Menú de construcción")
print("="*50 + "\n")

# Crea 3 funciones de construcción:
# - construir_casa(): construye una casa simple
# - construir_castillo(): construye un castillo pequeño
# - construir_puente(): construye un puente
#
# Luego crea un menú que pregunte al usuario qué quiere construir
# y llame a la función correspondiente

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 5
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 5: Función es_par")
print("="*50 + "\n")

# Crea una función llamada "es_par" que:
# - Reciba un número como parámetro
# - Devuelva True si es par, False si es impar
# - Pista: usa el operador % (módulo)
#
# Prueba la función con varios números
# y muestra mensajes como "7 es impar" o "10 es par"

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 RETO EXTRA (OPCIONAL)
# ============================================
# Crea una función "dibujar_letra" que dibuje una letra
# en Minecraft usando bloques. Por ejemplo, la letra "T":
#
#   XXX
#    X
#    X
#    X
#
# Luego crea funciones para otras letras y escribe tu nombre

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# COMPROBACIÓN FINAL
# ============================================
print("\n" + "="*50)
print("🎉 ¡FELICIDADES! Has completado el Reto 8")
print("="*50)
print("\n📚 HAS APRENDIDO:")
print("  ✓ Qué es una función y por qué son útiles")
print("  ✓ Definir funciones con def")
print("  ✓ Llamar funciones")
print("  ✓ Devolver valores con return")
print("  ✓ Scope de variables (local vs global)")
print("\n🚀 Siguiente paso: reto_09_constructor_personalizable.py")
print("="*50)

mc.postToChat("=" * 30)
mc.postToChat("RETO 8 COMPLETADO")
mc.postToChat("Total acumulado: 2 C$")
mc.postToChat("=" * 30)

"""
═══════════════════════════════════════════════════════
📖 RESUMEN DE LO QUE HAS APRENDIDO:

1. Definir función:
   def nombre_funcion():
       # código
       # más código

2. Llamar función:
   nombre_funcion()

3. Función con return:
   def calcular(x):
       resultado = x * 2
       return resultado

4. Ventajas de las funciones:
   - Reutilizar código
   - Organizar mejor el programa
   - Facilitar mantenimiento
   - Dividir problemas grandes en pequeños

5. Scope:
   - Variables locales: solo existen dentro de la función
   - Variables globales: existen en todo el programa

🤖 CONEXIÓN CON EUROBOT:
Las funciones son FUNDAMENTALES en robótica:

def avanzar_distancia(cm):
    # código para avanzar

def girar_angulo(grados):
    # código para girar

def recoger_pieza():
    # código para recoger

# Programa principal:
avanzar_distancia(50)
girar_angulo(90)
recoger_pieza()

Ventajas:
- Código más legible
- Fácil de probar cada función por separado
- Reutilizar acciones comunes
- Trabajo en equipo (cada uno programa funciones diferentes)

═══════════════════════════════════════════════════════
"""
