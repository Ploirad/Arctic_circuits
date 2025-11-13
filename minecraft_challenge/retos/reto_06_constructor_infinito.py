"""
🎮 RETO 6: CONSTRUCTOR INFINITO (BUCLE WHILE)
==============================================

🎯 OBJETIVO DE PYTHON:
Aprender a usar bucles while para repetir código mientras se cumpla una condición

📚 CONCEPTOS QUE VAS A APRENDER:
- Bucle while: repetir mientras una condición sea verdadera
- Diferencia entre for y while
- break: salir de un bucle
- continue: saltar a la siguiente iteración
- Bucles infinitos (y cómo evitarlos)

⚠️ ANTES DE EMPEZAR:
1. Servidor arrancado
2. Jugador en el mundo
3. Ejecuta: python reto_06_constructor_infinito.py

═══════════════════════════════════════════════════════
"""

from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create()

print("\n" + "="*50)
print("🎮 RETO 6: CONSTRUCTOR INFINITO")
print("="*50 + "\n")

# ============================================
# PARTE 1: WHILE BÁSICO
# ============================================
print("PARTE 1: Bucle WHILE básico")
print("-" * 30)

# while repite el código MIENTRAS la condición sea verdadera
contador = 0

while contador < 5:
    print("Contador: " + str(contador))
    contador = contador + 1  # MUY IMPORTANTE: incrementar el contador
    # Si no incrementamos, el bucle sería INFINITO

print("Bucle terminado. Contador final: " + str(contador))

# ============================================
# PARTE 2: FOR vs WHILE
# ============================================
print("\nPARTE 2: Diferencia entre FOR y WHILE")
print("-" * 30)

# FOR: cuando sabes CUÁNTAS VECES repetir
print("\nCon FOR (sabemos que son 5 veces):")
for i in range(5):
    print("  Iteración: " + str(i))

# WHILE: cuando repites HASTA QUE algo ocurra
print("\nCon WHILE (hasta que contador sea 5):")
contador = 0
while contador < 5:
    print("  Contador: " + str(contador))
    contador += 1  # Forma corta de: contador = contador + 1

# ============================================
# PARTE 3: BREAK - SALIR DEL BUCLE
# ============================================
print("\nPARTE 3: Palabra clave BREAK")
print("-" * 30)

# break sale INMEDIATAMENTE del bucle
pos = mc.player.getTilePos()

mc.postToChat("Construyendo torre hasta encontrar obstáculo...")

altura = 0
while altura < 20:
    # Comprobar si hay un bloque
    bloque_actual = mc.getBlock(pos.x + 3, pos.y + altura, pos.z)

    if bloque_actual != 0:  # 0 = aire
        print("¡Obstáculo encontrado en altura " + str(altura) + "!")
        mc.postToChat("Obstaculo encontrado!")
        break  # Salir del bucle

    # Colocar bloque
    mc.setBlock(pos.x + 3, pos.y + altura, pos.z, block.STONE.id)
    altura += 1

print("Torre final: " + str(altura) + " bloques")

# ============================================
# PARTE 4: CONTINUE - SALTAR ITERACIÓN
# ============================================
print("\nPARTE 4: Palabra clave CONTINUE")
print("-" * 30)

# continue salta el resto del código y va a la siguiente iteración
mc.postToChat("Construyendo torre con huecos...")

altura = 0
while altura < 10:
    # Saltar los niveles 3 y 7 (dejar huecos)
    if altura == 3 or altura == 7:
        print("Saltando altura " + str(altura))
        altura += 1
        continue  # Salta el resto y vuelve al inicio del while

    mc.setBlock(pos.x + 5, pos.y + altura, pos.z, block.BRICK_BLOCK.id)
    print("Bloque colocado en altura " + str(altura))
    altura += 1

mc.postToChat("¡Torre con huecos completada!")

# ============================================
# PARTE 5: BUCLE CONTROLADO POR USUARIO
# ============================================
print("\nPARTE 5: Bucle controlado por usuario")
print("-" * 30)

# Construir bloques hasta que el usuario diga "stop"
print("\n¡Construiremos bloques hasta que escribas 'stop'!")
print("(Simulación - en el ejercicio real usarás input)")

# Simulación
intentos = 0
while intentos < 3:  # Solo 3 para la demo
    mc.setBlock(pos.x + 7, pos.y + intentos, pos.z, block.GOLD_BLOCK.id)
    print("Bloque " + str(intentos + 1) + " colocado")
    intentos += 1

# ============================================
# ⚠️ CUIDADO: BUCLES INFINITOS
# ============================================
print("\nADVERTENCIA: Bucles infinitos")
print("-" * 30)
print("Este bucle sería INFINITO (NO lo ejecutes):")
print("contador = 0")
print("while contador < 5:")
print("    print(contador)")
print("    # ¡ERROR! Olvidamos incrementar contador")
print("\nSi te encuentras en un bucle infinito:")
print("- Pulsa Ctrl+C en la consola para detener el programa")

# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 1
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 1: Cuenta atrás")
print("="*50 + "\n")

# Pide al usuario un número
# Haz una cuenta atrás desde ese número hasta 0
# Muestra cada número en la consola y en Minecraft
# Al llegar a 0, coloca un bloque de TNT

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 2
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 2: Adivinanza de número")
print("="*50 + "\n")

# Piensa en un número secreto (por ejemplo, 7)
# Pide al usuario que adivine números
# Mientras no acierte, sigue pidiendo números
# Da pistas: "más alto" o "más bajo"
# Cuando acierte, construye un bloque de diamante y sal del bucle

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 3
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 3: Constructor con presupuesto")
print("="*50 + "\n")

# El jugador tiene un presupuesto de 50 "monedas"
# Cada bloque de diamante cuesta 10 monedas
# Construye bloques de diamante mientras haya presupuesto
# Muestra el presupuesto restante después de cada bloque
# Cuando se agote el presupuesto, muestra mensaje y termina

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 4
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 4: Torre hasta cierta altura")
print("="*50 + "\n")

# Pregunta al usuario a qué altura Y del mundo quiere llegar
# Construye una torre desde la posición del jugador
# hasta alcanzar esa altura Y
# Usa while para comprobar la altura actual

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 AHORA TE TOCA A TI - EJERCICIO 5
# ============================================
print("\n" + "="*50)
print("🎯 EJERCICIO 5: Menú interactivo")
print("="*50 + "\n")

# Crea un menú que se repita hasta que el usuario elija "salir"
#
# Menú:
# 1. Construir torre de 5 bloques
# 2. Construir pared de 3x3
# 3. Construir cubo de 2x2x2
# 4. Salir
#
# Usa while True y break cuando elijan opción 4

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# 🎯 RETO EXTRA (OPCIONAL)
# ============================================
# Crea un "reloj" que cuente segundos
# Usa while True (infinito)
# Cada segundo, coloca un bloque de redstone
# Muestra el tiempo transcurrido en el chat
# Para detenerlo tendrás que pulsar Ctrl+C
#
# Pista: usa time.sleep(1) para esperar 1 segundo

# ESCRIBE TU CÓDIGO AQUÍ:




# ============================================
# COMPROBACIÓN FINAL
# ============================================
print("\n" + "="*50)
print("🎉 ¡FELICIDADES! Has completado el Reto 6")
print("="*50)
print("\n📚 HAS APRENDIDO:")
print("  ✓ Bucle while para condiciones")
print("  ✓ Diferencia entre for y while")
print("  ✓ break para salir de bucles")
print("  ✓ continue para saltar iteraciones")
print("  ✓ Evitar bucles infinitos")
print("\n🚀 Siguiente paso: reto_07_paleta_colores.py")
print("="*50)

mc.postToChat("=" * 30)
mc.postToChat("RETO 6 COMPLETADO")
mc.postToChat("Total acumulado: 2 C$")
mc.postToChat("=" * 30)

"""
═══════════════════════════════════════════════════════
📖 RESUMEN DE LO QUE HAS APRENDIDO:

1. Bucle WHILE:
   while condicion:
       # código a repetir
       # IMPORTANTE: modificar la condición

2. FOR vs WHILE:
   - FOR: cuando sabes cuántas veces repetir
   - WHILE: cuando repites hasta que algo ocurra

3. BREAK:
   Sal inmediatamente del bucle

4. CONTINUE:
   Salta el resto del código y va a la siguiente iteración

5. Cuidado con bucles infinitos:
   Asegúrate de que la condición pueda volverse falsa

🤖 CONEXIÓN CON EUROBOT:
El while es fundamental en robótica:

- while sensor_distancia > 10:
      avanzar()
  (Avanzar hasta estar cerca de un obstáculo)

- while not pieza_detectada:
      buscar_pieza()
  (Buscar hasta encontrar)

- while tiempo_restante > 0:
      ejecutar_estrategia()
  (Jugar hasta que se acabe el tiempo)

- while True:
      leer_sensores()
      tomar_decisiones()
      ejecutar_acciones()
  (Bucle principal del robot)

═══════════════════════════════════════════════════════
"""
