from microbit import *
from radio import Radio #radio con minuscula tienes que crear un archivo con el codigo de Radio.py esto en microbit python editor
import radio
wk = WUKONG()
r = Radio(48, 7)#r es el equivalente de radio
r.on()
while True:
    cadena = r.receive()
    if  cadena == [0, "T"]:
        movimiento(0)
        break
    elif cadena == [1, "T"]:
        display.scroll("Azul, empezar")
        break
    else:
        display.scroll("Estar parado")


radio.config(group=48)





while True:
    if 1 == pin8.read_digital():
        wk.set_motors(1, 0)
        wk.set_motors(2, 0)
        radio.config(group=255)
    

        

