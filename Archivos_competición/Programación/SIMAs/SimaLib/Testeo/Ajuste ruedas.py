# Imports go at the top
from microbit import *
from wukong import WUKONG

wk = WUKONG()
vel_der = -100
vel_izq = 100
estado = 1
# Code in a 'while True:' loop repeats forever
while True:
    sleep(500)
    if estado == -1:
        display.show("1:")
        display.scroll(vel_izq)
        display.show("2:")
        display.scroll(vel_der)
        estado = 0
    if button_a.was_pressed() and button_b.was_pressed():
        estado = 1
    elif button_a.is_pressed():
        vel_der += 1
        estado = 1
    elif button_b.is_pressed():
        vel_izq -= 1
        estado = 1
    if estado == 1:
        sleep(4000)
        wk.set_motors(1, vel_izq)
        wk.set_motors(2, vel_der)
        sleep(1000)
        wk.set_motors(1,0)
        wk.set_motors(2,0)
        estado = -1
