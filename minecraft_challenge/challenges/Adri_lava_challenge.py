import mcpi.minecraft as minecraft
import mcpi.block as block
from time import sleep
from mcrcon import MCRcon

ip = "10.0.7.70"
player = "steve_chueco"

with open(r"D:\AcademiaCervantesMinecraft\MinecraftServer\logs\debug.log", "r+") as f:
    contenido = f.read()
    if player in contenido:
        f.seek(0)
        f.truncate()

mc = minecraft.Minecraft.create(ip, 4711)

def create_lava_floor(height, center_x, center_z):
    mc.setBlocks(center_x-5, height, center_z-5,
                 center_x+4, height, center_z+4, block.LAVA_STATIONARY.id)

def create_hollow_tower(height, block_id=block.STONE.id):
    pos = mc.player.getPos()
    x, y, z = int(pos.x), int(pos.y), int(pos.z)
    mc.setBlocks(x-6, y, z-6, x+6, y+height, z+6, block_id)
    mc.setBlocks(x-5, y, z-5, x+5, y+height, z+5, block.AIR.id)

def give_item_to_player(objeto, quantity):
    mc.postToChat(f"Dar {objeto} x{quantity}")

def is_player_alive():
    global player
    with open(r"D:\AcademiaCervantesMinecraft\MinecraftServer\logs\debug.log", "r+") as f:
        contenido = f.read()
        if player in contenido:
            f.seek(0)
            f.truncate()
            return False
    return True

def ejecutarComando(command):
    global ip
    PORT = 25575
    PASSWORD = "\"mcbest\""
    try:
        with MCRcon(ip, PASSWORD, port=PORT) as mcr:
            print(mcr.command(command))
    except Exception as e:
        print(f"error: {e}")

def verificar_bloques_prohibidos():
    pos = mc.player.getTilePos()
    x, y, z = int(pos.x), int(pos.y), int(pos.z)

    # Escanear un área pequeña alrededor del jugador
    for dx in range(-3, 4):
        for dy in range(-1, 4):
            for dz in range(-3, 4):
                bx, by, bz = x + dx, y + dy, z + dz
                bloque = mc.getBlock(bx, by, bz)

                # Solo revisar arena y madera
                if bloque in (block.SAND.id, block.WOOD_PLANKS.id):
                    if hay_adyacente_igual(bx, by, bz, bloque):
                        mc.setBlock(bx, by, bz, block.AIR.id)
                        mc.postToChat("❌ No puedes colocar bloques iguales pegados.")
                        return                        
def hay_adyacente_igual(x, y, z, bloque_id):
    adyacentes = [
        (x + 1, y, z),
        (x - 1, y, z),
        (x, y + 1, z),
        (x, y - 1, z),
        (x, y, z + 1),
        (x, y, z - 1)
    ]
    for ax, ay, az in adyacentes:
        if mc.getBlock(ax, ay, az) == bloque_id:
            return True
    return False

# --- Ejecución principal ---
pos = mc.player.getPos()
x, y, z = int(pos.x), int(pos.y), int(pos.z)

spawn_coords = "-138 63 286"
levels = 150

create_hollow_tower(levels)
# mc.postToChat("¡Torre creada! Prepárate...")
sleep(10)
win = True

for i in range(levels):
    verificar_bloques_prohibidos()
    if not is_player_alive():
        win = False
        break
    elif mc.player.getPos().y >= (y+levels):
        break

    ejecutarComando("/give @p sand 1")
    ejecutarComando("/give @p planks 1")
    
    with open(r"D:\AcademiaCervantesMinecraft\MinecraftServer\logs\debug.log", "r+") as f:
        contenido = f.read()
        if player in contenido:
            f.seek(0)
            f.truncate()

    for j in range(10, 0, -1):
        # mc.postToChat(f"{j}...")
        sleep(1)
    mc.postToChat("Lava is raising!!!")

    create_lava_floor(int(y) + i -1, x, z)
if win:
    mc.postToChat("Congratulations, you won")
    ejecutarComando("/give @p diamond")
    ejecutarComando(f"/tp @p {spawn_coords}")
else:
    mc.postToChat("You died! End of the game")