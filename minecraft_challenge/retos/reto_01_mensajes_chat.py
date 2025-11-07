"""
🎮 RETO 1: MOSTRANDO MENSAJES EN EL CHAT DE MINECRAFT
======================================================

🎯 OBJETIVO DE PYTHON:
Aprender a usar print() y variables básicas en Python

📚 CONCEPTOS QUE VAS A APRENDER:
- print(): mostrar mensajes en la consola
- Variables: guardar información con nombres
- Strings (texto): guardar palabras y frases
- mc.postToChat(): enviar mensajes al chat de Minecraft

⚠️ ANTES DE EMPEZAR:
1. Asegúrate de que el servidor está arrancado
2. Entra al mundo de Minecraft
3. Ejecuta: python reto_01_mensajes_chat.py

═══════════════════════════════════════════════════════
"""

# ============================================
# PARTE 1: IMPORTAR LIBRERÍAS
# ============================================
# Primero necesitamos importar las herramientas de Minecraft
from mcpi.minecraft import Minecraft
from mcpi import block

# Conectar al servidor de Minecraft
mc = Minecraft.create()

print("¡Conectado al servidor de Minecraft!")
print("Ahora vamos a aprender Python...")

# ============================================
# PARTE 2: TU PRIMER PRINT
# ============================================
# print() sirve para mostrar mensajes en la CONSOLA (terminal)
# La consola es donde ejecutaste el script

print("¡Hola mundo!")
print("Este mensaje aparece en la consola")
print("No en Minecraft, sino en la terminal")

# ============================================
# PARTE 3: VARIABLES BÁSICAS
# ============================================
# Una variable es como una caja donde guardas información
# Se crea con: nombre_variable = valor

nombre = "Estudiante"
edad = 16
curso = "Robótica Eurobot 2026"
perico_el_de_los_palotes = "¡Hola!"
en_un_lugar_de_la_manchaaaa = "Erase una vez..."
# Ahora podemos usar esas variables
print(nombre)
print(edad)
print(curso)
print(perico_el_de_los_palotes)
print(en_un_lugar_de_la_manchaaaa)

# También podemos combinar texto y variables
print("Mi nombre es: " + nombre)
print("Mi edad es: " + str(edad))  # str() convierte número a texto

# ============================================
# PARTE 4: ENVIAR MENSAJES AL CHAT DE MINECRAFT
# ============================================
# mc.postToChat() envía mensajes al chat de Minecraft
# ¡Así todos los jugadores lo pueden ver!

mc.postToChat("¡Hola desde Python!")
mc.postToChat("Mi nombre es: " + nombre)

# También podemos guardar mensajes en variables
mensaje_bienvenida = "Bienvenido al Reto 1"
mensaje_despedida = "¡Hasta pronto!"

mc.postToChat(mensaje_bienvenida)
mc.postToChat(mensaje_despedida)

# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 1
# ============================================
# Crea las siguientes variables CON TU INFORMACIÓN:
# - tu_nombre (tu nombre real)
# - tu_edad (tu edad)
# - tu_comida_favorita (tu comida favorita)
#
# Luego usa print() para mostrarlas en la consola
# Y usa mc.postToChat() para mostrarlas en Minecraft

# ESCRIBE TU CÓDIGO AQUÍ:
tu_nombre = "Jose Luis"
tu_edad = 5
tu_comida_favorita = "Pizza con patatas fritas y cebolla"

mc.postToChat("Mi nombre es: " + tu_nombre)
mc.postToChat("Mi edad es: " + str(tu_edad))
mc.postToChat("Mi comida favorita es: " + tu_comida_favorita)


# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 2
# ============================================
# Crea un mensaje de presentación que incluya:
# - Tu nombre
# - Tu edad
# - Tu comida favorita
# Y envíalo al chat de Minecraft

# Ejemplo: "Hola, soy María, tengo 16 años y me encanta la pizza"

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 3
# ============================================
# Crea 5 variables con nombres de tus compañeros de clase
# Luego envía un saludo a cada uno al chat de Minecraft

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 RETO EXTRA (OPCIONAL)
# ============================================
# Investiga cómo hacer que los mensajes aparezcan con colores
# en la consola (pista: busca "ANSI colors Python")
# No es necesario para ganar los CC, pero es divertido

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# COMPROBACIÓN FINAL
# ============================================
print("\n" + "="*50)
print("🎉 ¡FELICIDADES! Has completado el Reto 1")
print("="*50)
print("\n📚 HAS APRENDIDO:")
print("  ✓ Usar print() para mostrar mensajes")
print("  ✓ Crear variables para guardar información")
print("  ✓ Combinar texto con variables")
print("  ✓ Enviar mensajes al chat de Minecraft")
print("\n🚀 Siguiente paso: reto_02_chat_interactivo.py")
print("="*50)

mc.postToChat("=" * 30)
mc.postToChat("RETO 1 COMPLETADO")
mc.postToChat("=" * 30)

"""
═══════════════════════════════════════════════════════
📖 RESUMEN DE LO QUE HAS APRENDIDO:

1. print()
   - Muestra mensajes en la consola/terminal
   - Sintaxis: print("tu mensaje")

2. Variables
   - Guardan información con un nombre
   - Se crean con: nombre = valor
   - Tipos: texto (string), números (int)

3. mc.postToChat()
   - Envía mensajes al chat de Minecraft
   - Sintaxis: mc.postToChat("tu mensaje")

4. Concatenación
   - Unir texto con +
   - Ejemplo: "Hola " + nombre

🤖 CONEXIÓN CON EUROBOT:
En robótica también necesitas variables para guardar:
- Posición del robot (x, y)
- Velocidad de los motores
- Estado de los sensores
- Puntuación del equipo

═══════════════════════════════════════════════════════
"""
