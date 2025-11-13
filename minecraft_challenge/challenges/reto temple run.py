from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

# Coordenadas de meta
META_X, META_Y, META_Z = 1322, 72, 508
TIEMPO_LIMITE = 50  # segundos

cuentas_regresivas = {}  # jugador: tiempo final
jugadores_en_desafio = set()  # Para evitar reiniciar el desafío si ya juega

while True:
    # Obtener todos los jugadores conectados
    try:
        jugadores = mc.getPlayerEntityIds()
    except:
        jugadores = []

    for jugador in jugadores:
        if jugador not in jugadores_en_desafio:
            cuentas_regresivas[jugador] = time.time() + TIEMPO_LIMITE
            jugadores_en_desafio.add(jugador)
            mc.postToChat(f"Reto iniciado para jugador {jugador}! Llega a la meta en {TIEMPO_LIMITE} segundos.")

    # Revisar estado de cada jugador
    for jugador in list(cuentas_regresivas):
        pos = mc.entity.getTilePos(jugador)
        if (
            abs(pos.x - META_X) <= 1 and
            abs(pos.y - META_Y) <= 1 and
            abs(pos.z - META_Z) <= 1
        ):
            cuentas_regresivas.pop(jugador)
            jugadores_en_desafio.remove(jugador)
            mc.postToChat(f"Jugador {jugador} ha llegado a la meta! Reto completado.")
        elif time.time() >= cuentas_regresivas[jugador]:
            cuentas_regresivas.pop(jugador)
            jugadores_en_desafio.remove(jugador)
            try:
                mc.entity.setHealth(jugador, 0)
            except:
                mc.postToChat(f"No se pudo matar a {jugador}; función no soportada.")
            mc.postToChat(f"El jugador {jugador} no llegó a la meta a tiempo.")

    time.sleep(0.2)
