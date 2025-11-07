"""
🎮 RETO 7: PALETA DE COLORES (LISTAS)
======================================

🎯 OBJETIVO DE PYTHON:
Aprender a trabajar con listas para guardar múltiples valores

📚 CONCEPTOS QUE VAS A APRENDER:
- Listas: colecciones ordenadas de elementos
- Acceder a elementos por índice [0], [1], [2]...
- Añadir elementos: append()
- Eliminar elementos: remove(), pop()
- Recorrer listas con for
- Longitud de listas: len()

⚠️ ANTES DE EMPEZAR:
1. Servidor arrancado
2. Jugador en el mundo
3. Ejecuta: python reto_07_paleta_colores.py

═══════════════════════════════════════════════════════
"""

from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

print("\n" + "="*50)
print("🎮 RETO 7: PALETA DE COLORES")
print("="*50 + "\n")

# ============================================
# PARTE 1: CREAR LISTAS
# ============================================
print("PARTE 1: Creando listas")
print("-" * 30)

# Una lista se crea con corchetes []
numeros = [1, 2, 3, 4, 5]
print("Lista de números: " + str(numeros))

nombres = ["Ana", "Carlos", "María", "Pedro"]
print("Lista de nombres: " + str(nombres))

mixta = [1, "dos", 3.0, True]
print("Lista mixta: " + str(mixta))

# Lista de materiales de Minecraft
materiales = [
    block.DIAMOND_BLOCK.id,
    block.GOLD_BLOCK.id,
    block.IRON_BLOCK.id,
    block.EMERALD_BLOCK.id
]
print("Lista de materiales: " + str(materiales))

# ============================================
# PARTE 2: ACCEDER A ELEMENTOS
# ============================================
print("\nPARTE 2: Acceder a elementos de la lista")
print("-" * 30)

# Los índices empiezan en 0 (no en 1)
colores = ["rojo", "azul", "verde", "amarillo"]

print("Primer color (índice 0): " + colores[0])
print("Segundo color (índice 1): " + colores[1])
print("Tercer color (índice 2): " + colores[2])
print("Cuarto color (índice 3): " + colores[3])

# Índices negativos: empiezan desde el final
print("\nÚltimo color (índice -1): " + colores[-1])
print("Penúltimo color (índice -2): " + colores[-2])

# Usar elementos de la lista
pos = mc.player.getTilePos()
mc.setBlock(pos.x + 2, pos.y, pos.z, materiales[0])  # Diamante
mc.setBlock(pos.x + 3, pos.y, pos.z, materiales[1])  # Oro
mc.postToChat("Bloques colocados desde la lista!")

# ============================================
# PARTE 3: LONGITUD DE LISTAS
# ============================================
print("\nPARTE 3: Longitud de listas con len()")
print("-" * 30)

print("Cantidad de colores: " + str(len(colores)))
print("Cantidad de materiales: " + str(len(materiales)))

# len() es útil para bucles
print("\nRecorriendo la lista de colores:")
for i in range(len(colores)):
    print("  Índice " + str(i) + ": " + colores[i])

# ============================================
# PARTE 4: RECORRER LISTAS CON FOR
# ============================================
print("\nPARTE 4: Recorrer listas directamente")
print("-" * 30)

# Forma más simple: for elemento in lista
print("Colores disponibles:")
for color in colores:
    print("  - " + color)

# Construir una fila de bloques con todos los materiales
mc.postToChat("Construyendo fila de materiales...")
for i in range(len(materiales)):
    mc.setBlock(pos.x + 5 + i, pos.y, pos.z, materiales[i])

print("Fila de " + str(len(materiales)) + " bloques construida")

# ============================================
# PARTE 5: AÑADIR Y ELIMINAR ELEMENTOS
# ============================================
print("\nPARTE 5: Modificar listas")
print("-" * 30)

mi_lista = [1, 2, 3]
print("Lista inicial: " + str(mi_lista))

# append() añade al final
mi_lista.append(4)
print("Después de append(4): " + str(mi_lista))

mi_lista.append(5)
print("Después de append(5): " + str(mi_lista))

# remove() elimina un elemento específico
mi_lista.remove(3)
print("Después de remove(3): " + str(mi_lista))

# pop() elimina el último elemento (y lo devuelve)
ultimo = mi_lista.pop()
print("Último eliminado: " + str(ultimo))
print("Lista final: " + str(mi_lista))

# ============================================
# PARTE 6: EJEMPLO COMPLETO - ARCOÍRIS
# ============================================
print("\nPARTE 6: Construyendo un arcoíris")
print("-" * 30)

# Lana de colores para el arcoíris
lanas = [
    14,  # Rojo
    1,   # Naranja
    4,   # Amarillo
    5,   # Verde lima
    11,  # Azul
    10,  # Morado
]

mc.postToChat("Construyendo arcoiris...")

# Construir arco con cada color
for i in range(len(lanas)):
    # Cada color es una columna de 5 bloques de alto
    for altura in range(5):
        mc.setBlock(pos.x + 10 + i, pos.y + altura, pos.z, 35, lanas[i])

mc.postToChat("¡Arcoiris completado!")

# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 1
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 1: Tu lista de favoritos")
print("="*50 + "\n")

# Crea una lista con 5 de tus cosas favoritas
# (pueden ser comidas, juegos, películas, etc.)
# Recorre la lista y muestra cada elemento en:
# - La consola (con print)
# - El chat de Minecraft (con postToChat)

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 2
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 2: Construcción desde lista")
print("="*50 + "\n")

# Crea una lista con 6 tipos de bloques diferentes
# Pide al usuario un número del 1 al 6
# Construye una torre de 10 bloques usando el material elegido
# (Recuerda: las listas empiezan en 0, no en 1)

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 3
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 3: Inventario de bloques")
print("="*50 + "\n")

# Crea una lista vacía llamada "inventario"
# Pide al usuario que añada 5 nombres de bloques
# Añade cada bloque a la lista con append()
# Al final, muestra todo el inventario numerado:
# 1. Diamante
# 2. Oro
# 3. Hierro
# ...

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 4
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 4: Pared multicolor")
print("="*50 + "\n")

# Crea una lista con al menos 5 tipos de bloques
# Construye una pared de 5 (ancho) x 5 (alto)
# Cada columna debe ser de un color diferente de tu lista
# Usa bucles anidados y accede a la lista

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 5
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 5: Patrón alternado")
print("="*50 + "\n")

# Crea dos listas:
# - materiales_1 = [diamante, oro, esmeralda]
# - materiales_2 = [hierro, piedra, madera]
#
# Construye una fila de 12 bloques alternando entre las dos listas:
# Bloque 0: materiales_1[0]
# Bloque 1: materiales_2[0]
# Bloque 2: materiales_1[1]
# Bloque 3: materiales_2[1]
# ...
#
# Pista: usa el operador % para alternar

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 RETO EXTRA (OPCIONAL)
# ============================================
# Crea una "galería de arte" en Minecraft
# - Lista con 10 bloques diferentes
# - Construye 10 marcos (cuadrados de 3x3)
# - Cada marco debe tener un bloque diferente en el centro
# - Organízalos en dos filas de 5

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# COMPROBACIÓN FINAL
# ============================================
print("\n" + "="*50)
print("🎉 ¡FELICIDADES! Has completado el Reto 7")
print("="*50)
print("\n📚 HAS APRENDIDO:")
print("  ✓ Crear listas con []")
print("  ✓ Acceder a elementos por índice [0], [1]...")
print("  ✓ Usar len() para saber el tamaño")
print("  ✓ Recorrer listas con for")
print("  ✓ Añadir y eliminar elementos")
print("\n🚀 Siguiente paso: reto_08_primera_funcion.py")
print("="*50)

mc.postToChat("=" * 30)
mc.postToChat("RETO 7 COMPLETADO")
mc.postToChat("Total acumulado: 2 C$")
mc.postToChat("=" * 30)

"""
═══════════════════════════════════════════════════════
📖 RESUMEN DE LO QUE HAS APRENDIDO:

1. Crear listas:
   lista = [elemento1, elemento2, elemento3]

2. Acceder a elementos:
   lista[0]   # Primer elemento
   lista[-1]  # Último elemento

3. Longitud:
   len(lista)  # Número de elementos

4. Recorrer listas:
   for elemento in lista:
       # usar elemento

   for i in range(len(lista)):
       # usar lista[i]

5. Modificar listas:
   lista.append(elemento)  # Añadir al final
   lista.remove(elemento)  # Eliminar elemento
   lista.pop()             # Eliminar último

🤖 CONEXIÓN CON EUROBOT:
Las listas son esenciales en robótica:

- Posiciones a visitar:
  puntos = [(0,0), (10,5), (20,10)]

- Secuencia de movimientos:
  movimientos = ["avanzar", "girar", "avanzar", "recoger"]

- Lecturas de sensores:
  distancias = [15.2, 14.8, 14.5, 14.1]

- Estrategias múltiples:
  estrategias = [estrategia_A, estrategia_B, estrategia_C]

- Gestión de piezas recogidas:
  piezas = []
  piezas.append(nueva_pieza)

═══════════════════════════════════════════════════════
"""
