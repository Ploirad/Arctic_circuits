from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()
mc.postToChat("¡Hola desde Python!")

pos = mc.player.getPos()
for i in range(10):
    mc.setBlock(pos.x + 3, pos.y + i, pos.z, block.DIAMOND_BLOCK.id)

mc.postToChat("¡Torre de diamante construida!")