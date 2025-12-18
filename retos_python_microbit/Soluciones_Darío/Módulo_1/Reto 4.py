# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    dato = 0
    if button_b.was_pressed():
        while True:
            display.scroll(dato)
            if button_a.was_pressed():
                dato += 1
            sleep(100)
            if button_b.was_pressed():
                break
    else:
        display.scroll("Horas en una semana")
        display.scroll(24*7)
        display.scroll("Segundos en una hora")
        display.scroll(60*60)
        display.scroll("Tengo 100 caramelos entre 7 amigos")
        display.scroll("A cada amigo le doy")
        display.scroll(100//7)
        display.scroll("caramelos")
        display.scroll("Y sobran")
        display.scroll(100%7)
        display.scroll("caramelos")
        display.scroll("El nivel de luz actual es de:")
        luz = display.read_light_level()
        display.scroll(luz/255*100)
        display.scroll("%")
        display.scroll("El doble de la temperatura actual es de: ")
        display.show(2*temperature())
        