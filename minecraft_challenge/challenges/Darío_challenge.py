from mcpi.minecraft import Minecraft
import mcpi.block as block
import laberinto
import random
import math
import time
mc = Minecraft.create()
d_x = 0
d_y = 0
d_z = 0
d = 0
mc.setBlocks(0,1,0,100,255,100,block.AIR.id)
mc.player.setPos(50,1,50)
mc.setBlocks(0,0,0,100,0,100, block.WOOL.id, 14)
mc.setBlocks(1,0,1,99,0,99, block.WOOL.id, 0)
for i in range(1,100):
    for j in range(1,100):
        if (i+j)%2 == 1:
            mc.setBlock(i,0,j,block.WOOL.id, 15)
pos = mc.player.getTilePos()
bloque_x = random.randint(pos.x-49,pos.x+49)
bloque_z = random.randint(pos.z-49,pos.z+49)
while True:
    pos = mc.player.getTilePos()
    d_x = pos.x-bloque_x;
    d_z = pos.z-bloque_z;
    d = math.sqrt(d_x**2 + d_z**2);
    mc.postToChat(f"Te encuentras a {d} bloques")
    if (d == 0):
        mc.postToChat("Te has encontrado con el bloque objetivo")
        break
    time.sleep(5)

m=49
n=49
laberinto.laberinto_csv(n, m)

GAP = block.AIR.id
WALL = block.BEDROCK.id
FLOOR = block.BEDROCK.id
FILENAME = "mazel.csv"
f = open(FILENAME, "r")
origin_x = 0
origin_y = 0
origin_z = 0
z = origin_z
for line in f.readlines():
    data = line.split(",")
    x = origin_x
    for cell in data:
        if cell == "0":
            b = GAP
        else:
            b = WALL
        mc.setBlock(x, origin_y, z, b)
        mc.setBlock(x, origin_y+1, z, b)
        mc.setBlock(x, origin_y-1, z, FLOOR)
        x= x+1
    z= z+1
mc.player.setPos(47,0,1)
while True:
    pos = mc.player.getTilePos()
    if pos.x == 0 and pos.z == 48:
        mc.postToChat("¡Felicidades! Has encontrado la salida del laberinto")
        break
    time.sleep(1)
    if pos.x > 48 or pos.z < 0 or pos.y > 1:
        mc.postToChat("Por ahi no se va tramposin")
        mc.player.setPos(47,0,1)
