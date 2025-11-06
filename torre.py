from mcpi.minecraft import Minecraft
from mcpi import block
import random
import time

mc = Minecraft.create()
mc.setBlocks(0,1,0,100,255,100,block.AIR.id)
mc.setBlocks(0,1,0,30,1,30,block.FENCE.id)
mc.setBlocks(1,1,1,29,1,29,block.AIR.id)
mc.player.setPos(1,1,1)
pos_block_x = 15
pos_block_y = 1
pos_block_z = 15
block_id = block.GLASS.id
mc.setBlock(pos_block_x ,pos_block_y ,pos_block_z , block_id,14)
points = 0
start_time = time.time()
tiempo_limite = 60  # segundos



while True:
    while mc.getBlock(pos_block_x ,pos_block_y ,pos_block_z) == block.AIR.id :
        pos_block_x = random.randint(1,29)
        pos_block_z = random.randint(1,29)
        pos_block_y = random.randint(1,3)
        mc.setBlock(pos_block_x ,pos_block_y ,pos_block_z , block_id,14)
        points += 1
        mc.postToChat(points)
    tiempo_transcurrido = time.time() - start_time
    tiempo_restante = tiempo_limite - tiempo_transcurrido

    # Ejecutar otras tareas aquí dentro del bucle
    # ...

    if tiempo_restante <= 0:
        if points >= 15:
            mc.postToChat("Ehnorabuena has ganado")
        else:
            mc.postToChat("Ehnorabuena has no ganado")
        break



    


    
#mc.postToChat(pos_arrow)