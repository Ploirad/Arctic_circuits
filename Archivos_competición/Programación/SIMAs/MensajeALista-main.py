# Imports go at the top
#Falta pulirlo
from microbit import *
from Radio import Radio
r = Radio(48, 7)
Booleano = True
Booleano2 = True
r.on()
while True:
    message = r.receive
    if message == ("FF"):
        lista = message.split(',')

        if lista[1] == "F":
            Booleano = False
            display.scroll('Hola')

        if lista[0] == "F":
            Booleano2 = False
            display.scroll('Hola')