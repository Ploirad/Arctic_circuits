from mcpi.minecraft import Minecraft
import time
import random

mc = Minecraft.create()

# Lista extensa de Pokémon (solo nombres)
pokemons = [
    "pikachu", "charmander", "bulbasaur", "squirtle", "eevee", "snorlax", "jigglypuff", "gengar", "psyduck", "machop",
    "onix", "mewtwo", "pidgey", "abra", "magikarp", "geodude", "rattata", "diglett", "zubat", "bellsprout",
    "gastly", "haunter", "lapras", "vulpix", "nidoran", "poliwag", "slowpoke", "krabby", "horsea", "goldeen",
    "scyther", "pinsir", "tauros", "ditto", "articuno", "zapdos", "moltres", "dratini", "dragonair", "dragonite",
    "togepi", "mareep", "wooper", "sudowoodo", "wobbuffet", "teddiursa", "phanpy", "larvitar", "mudkip", "torchic",
    "treecko", "ralts", "aron", "electrike", "trapinch", "bagon", "beldum", "gible", "riolu", "lucario",
    "snivy", "tepig", "oshawott", "zorua", "axew", "goomy", "greninja", "rowlet", "litten", "popplio",
    "rockruff", "lycanroc", "grookey", "scorbunny", "sobble", "yamper", "rookidee", "corviknight", "pawmi", "lechonk"
]

# Variables de juego
palabra = random.choice(pokemons)
errores = 0
aciertos = 0  # cantidad de Pokémon adivinados
letras_acertadas = set()
letras_intentadas = set()
fallos_seguidos = 0  # contador de fallos consecutivos sin aciertos

mc.postToChat("🎮 ¡Bienvenido al Ahorcado Pokémon!")
mc.postToChat(f"Un Pokémon ha sido elegido al azar ({len(palabra)} letras).")
mc.postToChat("💬 Escribe una letra en el chat para intentar adivinarlo.")

def mostrar_progreso():
    visible = " ".join([l if l in letras_acertadas else "_" for l in palabra])
    mc.postToChat(f"➡️ {visible}")

mostrar_progreso()

while True:
    mensajes = mc.events.pollChatPosts()
    for msg in mensajes:
        texto = msg.message.strip().lower()

        # Si ya ganó 5 Pokémon
        if aciertos >= 5:
            mc.postToChat("🏆 ¡GANASTE EL JUEGO! Adivinaste 5 Pokémon 🎉")
            aciertos = 0
            errores = 0
            letras_acertadas.clear()
            letras_intentadas.clear()
            palabra = random.choice(pokemons)
            fallos_seguidos = 0
            mc.postToChat(f"🎲 Nuevo ciclo: adivina el Pokémon ({len(palabra)} letras).")
            mostrar_progreso()
            continue

        # Si perdió
        if errores >= 7:
            mc.postToChat(f"💀 Perdiste. El Pokémon era '{palabra.upper()}'.")
            palabra = random.choice(pokemons)
            errores = 0
            letras_acertadas.clear()
            letras_intentadas.clear()
            fallos_seguidos = 0
            mc.postToChat(f"🎲 Nuevo Pokémon elegido ({len(palabra)} letras).")
            mostrar_progreso()
            continue

        # Evitar letras repetidas
        if texto in letras_intentadas:
            mc.postToChat("⚠️ Ya intentaste esa letra.")
            continue
        letras_intentadas.add(texto)

        # Verificar coincidencias
        acierto = False
        for letra in texto:
            if letra in palabra:
                letras_acertadas.add(letra)
                acierto = True

        if acierto:
            mc.postToChat("✅ ¡Acertaste una letra!")
            fallos_seguidos = 0
        else:
            errores += 1
            fallos_seguidos += 1
            mc.postToChat(f"❌ No hay letras. Intentos fallidos: {errores}/7 (Fallos seguidos: {fallos_seguidos}/3)")

            # Si falla 3 veces seguidas sin aciertos → reiniciar victorias
            if fallos_seguidos >= 3:
                if aciertos > 0:
                    aciertos = 0
                    mc.postToChat("💥 Has fallado 3 veces seguidas. ¡Tus victorias se reinician a 0!")
                fallos_seguidos = 0  # reiniciar contador de fallos seguidos

        mostrar_progreso()

        # Verificar si adivinó el Pokémon
        if all(l in letras_acertadas for l in set(palabra)):
            aciertos += 1
            mc.postToChat(f"🎉 ¡Has adivinado al Pokémon '{palabra.upper()}'! ({aciertos}/5)")
            palabra = random.choice(pokemons)
            errores = 0
            letras_acertadas.clear()
            letras_intentadas.clear()
            fallos_seguidos = 0
            mc.postToChat(f"🎲 Nuevo Pokémon elegido ({len(palabra)} letras).")
            mostrar_progreso()
            continue

    time.sleep(0.5)
