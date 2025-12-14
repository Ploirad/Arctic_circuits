# Imports go at the top
from microbit import *

puntos = 0
while True:
    display.show(puntos)

    if button_a.is_pressed() and button_b.is_pressed():
        puntos = 0
    elif button_a.is_pressed():
        puntos += 1
    elif button_b.is_pressed():
        if puntos > 0:
            puntos -= 1