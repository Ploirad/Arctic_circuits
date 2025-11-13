"""
🎮 RETO 10: TU MUNDO AUTOMÁTICO - PROYECTO FINAL
=================================================
💰 Recompensa: 2 Cervantes Dollars (C$)
🏆 PROYECTO FINAL - INTEGRA TODO LO APRENDIDO

🎯 OBJETIVO:
Crear un mundo automático personalizado que use TODOS los conceptos aprendidos

📚 CONCEPTOS A INTEGRAR:
✓ Print y variables (Reto 1)
✓ Input y tipos de datos (Reto 2)
✓ Operaciones matemáticas (Reto 3)
✓ Condicionales if/elif/else (Reto 4)
✓ Bucles for (Reto 5)
✓ Bucles while (Reto 6)
✓ Listas (Reto 7)
✓ Funciones (Reto 8)
✓ Funciones con parámetros (Reto 9)

⚠️ ANTES DE EMPEZAR:
1. Servidor arrancado
2. Jugador en el mundo
3. Ejecuta: python reto_10_mundo_automatico.py

═══════════════════════════════════════════════════════
🎨 PROYECTO: GENERADOR DE CIUDADES AUTOMÁTICO

Vas a crear un programa que:
1. Pregunte al usuario qué tipo de ciudad quiere
2. Genere automáticamente edificios, calles, parques
3. Use funciones para organizar el código
4. Permita personalizar colores y tamaños

¡Sé creativo y añade tus propias ideas!
═══════════════════════════════════════════════════════
"""

from mcpi.minecraft import Minecraft
from mcpi import block
import random
import time

mc = Minecraft.create()

print("\n" + "="*60)
print("🏆 RETO 10: TU MUNDO AUTOMÁTICO - PROYECTO FINAL")
print("="*60 + "\n")

# ============================================
# CONFIGURACIÓN INICIAL
# ============================================

# Lista de materiales disponibles
materiales_edificios = [
    block.STONE_BRICK.id,
    block.BRICK_BLOCK.id,
    block.SANDSTONE.id,
    block.QUARTZ_BLOCK.id
]

materiales_decoracion = [
    block.GLOWSTONE_BLOCK.id,
    block.GLASS.id,
    block.STAINED_GLASS.id
]

# ============================================
# FUNCIONES DEL PROYECTO
# ============================================

def mostrar_bienvenida():
    """Muestra el mensaje de bienvenida"""
    print("\n" + "="*60)
    print("    GENERADOR AUTOMÁTICO DE CIUDADES")
    print("    Preparación para Eurobot 2026")
    print("="*60)

    mc.postToChat("=" * 30)
    mc.postToChat("GENERADOR DE CIUDADES")
    mc.postToChat("Proyecto Final Eurobot")
    mc.postToChat("=" * 30)

def construir_edificio(x, y, z, ancho, alto, largo, material):
    """Construye un edificio personalizable"""

    # Construir estructura principal
    for i in range(ancho):
        for j in range(alto):
            for k in range(largo):
                # Crear paredes huecas
                if i == 0 or i == ancho-1 or k == 0 or k == largo-1:
                    mc.setBlock(x + i, y + j, z + k, material)
                elif j == 0 or j == alto-1:  # Suelo y techo
                    mc.setBlock(x + i, y + j, z + k, material)

    # Añadir ventanas
    for j in range(1, alto-1, 2):
        # Ventanas frontales
        for i in range(1, ancho-1, 2):
            mc.setBlock(x + i, y + j, z, block.GLASS.id)

    # Puerta
    mc.setBlock(x + ancho//2, y, z, block.AIR.id)
    mc.setBlock(x + ancho//2, y + 1, z, block.AIR.id)

def construir_calle(x, y, z, longitud, direccion):
    """Construye una calle"""
    material_calle = block.STONE.id

    for i in range(longitud):
        for ancho in range(3):
            if direccion == "horizontal":
                mc.setBlock(x + i, y, z + ancho, material_calle)
            else:  # vertical
                mc.setBlock(x + ancho, y, z + i, material_calle)

def construir_parque(x, y, z, tamaño):
    """Construye un pequeño parque"""

    # Césped
    for i in range(tamaño):
        for j in range(tamaño):
            mc.setBlock(x + i, y, z + j, block.GRASS.id)

    # Árboles (simples)
    for _ in range(3):
        ax = x + random.randint(1, tamaño-2)
        az = z + random.randint(1, tamaño-2)

        # Tronco
        for h in range(4):
            mc.setBlock(ax, y + 1 + h, az, block.WOOD.id)

        # Hojas
        for i in range(-1, 2):
            for j in range(-1, 2):
                mc.setBlock(ax + i, y + 5, az + j, block.LEAVES.id)

def construir_farola(x, y, z):
    """Construye una farola"""
    # Poste
    for h in range(4):
        mc.setBlock(x, y + h, z, block.FENCE.id)

    # Luz
    mc.setBlock(x, y + 4, z, block.GLOWSTONE_BLOCK.id)

def calcular_materiales(num_edificios, tamaño_promedio):
    """Calcula aproximadamente cuántos bloques se necesitan"""
    bloques_por_edificio = (tamaño_promedio ** 3) // 2  # Aproximado para huecos
    total = num_edificios * bloques_por_edificio
    return total

# ============================================
# 🎯 TU PROYECTO - COMPLETA ESTAS FUNCIONES
# ============================================

def construir_torre_vigilancia(x, y, z):
    """
    EJERCICIO 1: Construye una torre de vigilancia
    Debe incluir:
    - Base cuadrada
    - Torre alta
    - Plataforma de observación en la cima
    - Escalera interior (opcional)
    """

    # ESCRIBE TU CÓDIGO AQUÍ:
    pass




def construir_fuente(x, y, z):
    """
    EJERCICIO 2: Construye una fuente decorativa
    Debe incluir:
    - Base circular o cuadrada
    - Agua en el centro
    - Bloques decorativos alrededor
    """

    # ESCRIBE TU CÓDIGO AQUÍ:
    pass




def construir_puente(x, y, z, longitud):
    """
    EJERCICIO 3: Construye un puente
    Debe incluir:
    - Estructura de soporte
    - Camino para cruzar
    - Barandillas a los lados
    """

    # ESCRIBE TU CÓDIGO AQUÍ:
    pass




def construir_estadio(x, y, z):
    """
    EJERCICIO 4: Construye un estadio pequeño
    (Para practicar para Eurobot!)
    Debe incluir:
    - Campo rectangular en el centro
    - Gradas alrededor
    - Líneas del campo
    """

    # ESCRIBE TU CÓDIGO AQUÍ:
    pass




# ============================================
# MENÚ PRINCIPAL DEL PROYECTO
# ============================================

def menu_principal():
    """Menú interactivo para el generador de ciudades"""

    mostrar_bienvenida()
    time.sleep(1)

    print("\n🏗️  ¿QUÉ QUIERES CONSTRUIR HOY?")
    print("-" * 60)
    print("1. Ciudad pequeña (5 edificios)")
    print("2. Ciudad mediana (10 edificios)")
    print("3. Ciudad grande (20 edificios)")
    print("4. Construcción personalizada")
    print("5. Modo creativo libre")
    print("6. Salir")
    print("-" * 60)

    opcion = input("\nElige una opción (1-6): ")

    if opcion == "1":
        construir_ciudad_pequeña()
    elif opcion == "2":
        construir_ciudad_mediana()
    elif opcion == "3":
        construir_ciudad_grande()
    elif opcion == "4":
        construccion_personalizada()
    elif opcion == "5":
        modo_creativo_libre()
    elif opcion == "6":
        print("¡Hasta pronto!")
        mc.postToChat("¡Hasta pronto, constructor!")
        return False
    else:
        print("Opción no válida")

    return True

def construir_ciudad_pequeña():
    """Construye una ciudad pequeña con 5 edificios"""

    mc.postToChat("Construyendo ciudad pequeña...")
    print("\n🏘️  Construyendo ciudad pequeña...")

    pos = mc.player.getTilePos()
    x_inicial = pos.x + 10
    y_inicial = pos.y
    z_inicial = pos.z + 10

    # Construir 5 edificios
    print("Construyendo edificios...")
    for i in range(5):
        x = x_inicial + (i * 12)
        ancho = random.randint(5, 8)
        alto = random.randint(5, 10)
        largo = random.randint(5, 8)
        material = random.choice(materiales_edificios)

        construir_edificio(x, y_inicial, z_inicial, ancho, alto, largo, material)
        print(f"  Edificio {i+1}/5 completado")

    # Construir calles
    print("Construyendo calles...")
    construir_calle(x_inicial, y_inicial, z_inicial - 3, 60, "horizontal")

    # Añadir farolas
    print("Añadiendo farolas...")
    for i in range(0, 60, 10):
        construir_farola(x_inicial + i, y_inicial, z_inicial - 4)

    # Parque central
    print("Construyendo parque...")
    construir_parque(x_inicial + 25, y_inicial, z_inicial + 10, 10)

    mc.postToChat("¡Ciudad pequeña completada!")
    print("✅ ¡Ciudad pequeña completada!")

def construir_ciudad_mediana():
    """
    EJERCICIO 5: Construye una ciudad mediana
    Similar a ciudad_pequeña pero con:
    - 10 edificios
    - Más calles
    - 2 parques
    - Torre de vigilancia
    """

    # ESCRIBE TU CÓDIGO AQUÍ:
    pass

def construir_ciudad_grande():
    """
    EJERCICIO 6: Construye una ciudad grande
    Debe incluir:
    - 20 edificios de diferentes tamaños
    - Red de calles completa
    - Múltiples parques
    - Torre de vigilancia
    - Fuente central
    - Estadio
    """

    # ESCRIBE TU CÓDIGO AQUÍ:
    pass

def construccion_personalizada():
    """
    EJERCICIO 7: Construcción personalizada
    Pregunta al usuario:
    - Cuántos edificios quiere
    - Qué estructuras especiales (torre, fuente, etc.)
    - Materiales preferidos
    Y construye según sus preferencias
    """

    print("\n🎨 CONSTRUCCIÓN PERSONALIZADA")
    print("-" * 60)

    # ESCRIBE TU CÓDIGO AQUÍ:
    pass

def modo_creativo_libre():
    """
    EJERCICIO 8: Modo creativo libre
    Crea tu propio sistema de construcción
    ¡Usa tu imaginación!
    Algunas ideas:
    - Constructor de castillos
    - Generador de laberintos
    - Creador de pixel art
    - Sistema de trenes
    """

    print("\n💡 MODO CREATIVO LIBRE")
    print("-" * 60)
    print("¡Aquí puedes programar lo que quieras!")

    # ESCRIBE TU CÓDIGO AQUÍ:
    # ¡SÉ CREATIVO!
    pass

# ============================================
# PROGRAMA PRINCIPAL
# ============================================

def main():
    """Función principal del proyecto"""

    print("\n" + "="*60)
    print("     PROYECTO FINAL - EUROBOT 2026")
    print("     Programación Python con Minecraft")
    print("="*60)

    continuar = True
    while continuar:
        continuar = menu_principal()

        if continuar:
            print("\n¿Quieres construir algo más?")
            respuesta = input("(s/n): ")
            if respuesta.lower() != 's':
                continuar = False

    # Finalización
    print("\n" + "="*60)
    print("🎉 ¡PROYECTO COMPLETADO!")
    print("="*60)
    print("\n📊 ESTADÍSTICAS:")
    print("  ✓ Has completado todos los retos")
    print("  ✓ Has aprendido Python desde cero")
    print("  ✓ Has creado construcciones automáticas")
    print("  ✓ Estás preparado para Eurobot 2026")
    print("\n💰 RECOMPENSA FINAL: 2 Cervantes Dollars")
    print("💰 TOTAL FINAL: 4 C$")
    print("\n🏆 ¡FELICIDADES, PROGRAMADOR!")
    print("="*60)

    mc.postToChat("=" * 40)
    mc.postToChat("PROYECTO FINAL COMPLETADO")
    mc.postToChat("¡2 C$ GANADOS!")
    mc.postToChat("TOTAL FINAL: 4 C$")
    mc.postToChat("FELICIDADES, PROGRAMADOR!")
    mc.postToChat("=" * 40)

# ============================================
# EJECUTAR EL PROGRAMA
# ============================================

if __name__ == "__main__":
    main()

"""
═══════════════════════════════════════════════════════
🎓 LO QUE HAS APRENDIDO EN ESTE CURSO:

1. FUNDAMENTOS (Retos 1-3):
   ✓ Print y variables
   ✓ Input y tipos de datos
   ✓ Operaciones matemáticas

2. CONTROL DE FLUJO (Retos 4-6):
   ✓ Condicionales if/elif/else
   ✓ Bucle for
   ✓ Bucle while

3. ESTRUCTURAS DE DATOS (Reto 7):
   ✓ Listas
   ✓ Manipulación de colecciones

4. FUNCIONES (Retos 8-9):
   ✓ Definir funciones
   ✓ Parámetros y argumentos
   ✓ Return values
   ✓ Organización de código

5. PROYECTO INTEGRADOR (Reto 10):
   ✓ Aplicar todos los conceptos
   ✓ Resolver problemas complejos
   ✓ Crear programas completos

🤖 PRÓXIMOS PASOS PARA EUROBOT 2026:

Ahora que dominas Python básico, estás listo para:

1. PROGRAMACIÓN DE ROBOTS:
   - Controlar motores con Python
   - Leer sensores
   - Tomar decisiones automáticas
   - Implementar estrategias

2. CONCEPTOS AVANZADOS:
   - Clases y objetos
   - Manejo de errores (try/except)
   - Archivos y persistencia
   - Librerías de robótica

3. PRÁCTICA ESPECÍFICA:
   - Simuladores de robots
   - Programación de Arduino/Raspberry Pi
   - Visión por computadora
   - Comunicación entre robots

4. TRABAJO EN EQUIPO:
   - Git para control de versiones
   - Documentación de código
   - Revisión de código entre compañeros
   - División de tareas

═══════════════════════════════════════════════════════
💡 CONSEJOS FINALES:

- Sigue practicando: la programación mejora con la práctica
- Experimenta: prueba ideas nuevas, rompe cosas, aprende
- Colabora: programa con tus compañeros, aprende de ellos
- Investiga: busca tutoriales, lee documentación
- Diviértete: la programación es creativa y divertida

🚀 ¡MUCHA SUERTE EN EUROBOT 2026!

═══════════════════════════════════════════════════════
"""
