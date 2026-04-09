# Imports go at the top
from microbit import *
from wukong import WUKONG

wk = WUKONG()
while True:
    if button_a.was_pressed():
        sleep(5000)
        wk.set_motors(1, 99)
        wk.set_motors(2, -100)
        sleep(2316)
        wk.set_motors(1,0)
        wk.set_motors(2,0)
    if button_b.was_pressed():
        wk.set_motors(1,0)
        wk.set_motors(2,0)
