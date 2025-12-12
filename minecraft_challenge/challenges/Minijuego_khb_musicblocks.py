from mcpi.minecraft import Minecraft
import time
import random

# --- Conexión a Minecraft ---
try:
    mc = Minecraft.create()
    print("✅ Conectado a Minecraft")
except Exception as e:
    print("❌ No se pudo conectar a Minecraft:", e)
    input("Pulsa Enter para salir...")
    exit()

# --- Configuración del juego ---
LANES = 4
NOTE_SPEED = 1.0 # tiempo entre movimientos de notas
NOTE_INTERVAL = 2.0    # tiempo entre notas nuevas
NOTE_START_Y = 10

# IDs de bloques
NOTE_BLOCK_ID = 25     # Nota base
NOTE_ID = 35           # Lana (usaremos diferentes colores)
BEDROCK_ID = 7         # Suelo seguro
OBSIDIAN_ID = 49
RED_WOOL_ID = 14
BLUE_WOOL_ID = 11
AIR_ID = 0
GLOWSTONE_ID = 89

score = 0
misses = 0
notes = []

# --- Área y escenario ---
player_pos = mc.player.getTilePos()
BASE_X = player_pos.x
BASE_Y = player_pos.y
BASE_Z = player_pos.z + 5

def setup_stage():
    global BASE_X, BASE_Y, BASE_Z

    # Limpiar área
    mc.setBlocks(BASE_X - 6, BASE_Y, BASE_Z - 3,
                 BASE_X + LANES + 6, BASE_Y + NOTE_START_Y + 8, BASE_Z + 5, AIR_ID)

    # Suelo del escenario (ahora Bedrock)
    mc.setBlocks(BASE_X - 5, BASE_Y - 1, BASE_Z - 3,
                 BASE_X + LANES + 5, BASE_Y - 1, BASE_Z + 5, BEDROCK_ID)

    # Pared de fondo
    mc.setBlocks(BASE_X - 5, BASE_Y, BASE_Z + 3,
                 BASE_X + LANES + 5, BASE_Y + NOTE_START_Y + 5, BASE_Z + 3, OBSIDIAN_ID)

    # Columnas laterales decorativas
    mc.setBlocks(BASE_X - 6, BASE_Y, BASE_Z - 3,
                 BASE_X - 6, BASE_Y + NOTE_START_Y + 5, BASE_Z + 5, RED_WOOL_ID)
    mc.setBlocks(BASE_X + LANES + 6, BASE_Y, BASE_Z - 3,
                 BASE_X + LANES + 6, BASE_Y + NOTE_START_Y + 5, BASE_Z + 5, BLUE_WOOL_ID)

    # Bordes con luces (Glowstone)
    for i in range(LANES + 4):
        mc.setBlock(BASE_X - 2 + i, BASE_Y + NOTE_START_Y + 5, BASE_Z, GLOWSTONE_ID)

    # Bloques base de los carriles
    for lane in range(LANES):
        x = BASE_X + lane
        mc.setBlock(x, BASE_Y, BASE_Z, NOTE_BLOCK_ID)

    mc.postToChat("🎵 Escenario listo. ¡Que comience el show!")

# --- Generar notas ---
def generate_note():
    lane = random.randint(0, LANES - 1)
    x = BASE_X + lane
    y = BASE_Y + NOTE_START_Y
    z = BASE_Z
    color = lane * 4  # colores distintos por carril
    mc.setBlock(x, y, z, NOTE_ID, color)
    notes.append((x, y, z, lane))
    mc.postToChat(f"🎶 Nueva nota en carril {lane+1}")

# --- Mover notas ---
def move_notes():
    global misses
    if not notes:
        return True

    new_notes = []
    for (x, y, z, lane) in notes:
        mc.setBlock(x, y, z, AIR_ID)
        next_y = y - 1
        if next_y > BASE_Y:
            mc.setBlock(x, next_y, z, NOTE_ID)
            new_notes.append((x, next_y, z, lane))
        else:
            misses += 1
            mc.postToChat(f"❌ Fallo ({misses}/10)")
            if misses >= 10:
                mc.postToChat("💀 Demasiados fallos. Fin del juego.")
                return False
    notes[:] = new_notes
    return True

# --- Leer chat ---
def check_chat_hits():
    global score
    events = mc.events.pollChatPosts()
    for e in events:
        message = e.message.lower()
        if message == "stop":
            mc.postToChat("🎮 Juego terminado.")
            return False
        if message in ["1", "2", "3", "4"]:
            lane = int(message) - 1
            for note in notes[:]:
                x, y, z, l = note
                # Detecta la nota si está un poco arriba del suelo
                if l == lane and BASE_Y + 1 <= y <= BASE_Y + 2:
                    mc.setBlock(x, y, z, AIR_ID)
                    notes.remove(note)
                    score += 1
                    mc.postToChat(f"✅ ¡Acierto en carril {lane+1}! Puntos: {score}")
    return True

# --- Main ---
def main():
    setup_stage()
    mc.postToChat("🎶 Escribe 1-4 en el chat para tocar la nota.")
    mc.postToChat("🛑 Escribe 'stop' para salir.")

    last_note_time = time.time()
    generate_note()

    while True:
        if not move_notes():
            break
        if not check_chat_hits():
            break
        now = time.time()
        if now - last_note_time >= NOTE_INTERVAL:
            generate_note()
            last_note_time = now
        time.sleep(NOTE_SPEED)

    mc.postToChat(f"🏁 Fin. Puntos: {score} | Fallos: {misses}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error durante el juego:", e)
        input("Pulsa Enter para cerrar...")
