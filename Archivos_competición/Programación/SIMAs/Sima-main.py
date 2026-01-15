from microbit import *
from radio import Radio #radio con minuscula tienes que crear un archivo con el codigo de Radio.py esto en microbit python editor
r = Radio(48, 7)#r es el equivalente de radio

r.on()
while True:
    cadena = r.receive()
    if  cadena == [0, "T"]:
        display.scroll("Amarillo, empezar")
        break
    elif cadena == [1, "T"]:
        display.scroll("Azul, empezar")
        break
    else:
        display.scroll("Estar parado")
    

        

