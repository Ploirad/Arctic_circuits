# Imports go at the top
from microbit import *
from wukong import WUKONG

wk = WUKONG()
tiempo = 180
while True:
    display.scroll(tiempo)
    sleep(2000)
    if button_a.was_pressed():
        sleep(2000)
        wk.set_motors(1,100)
        wk.set_motors(2,100)
        sleep(tiempo)
        wk.set_motors(1,0)
        wk.set_motors(2,0)
    if button_b.was_pressed():
        tiempo += 5
