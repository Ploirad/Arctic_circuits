# Imports go at the top
from microbit import *
from wukong import WUKONG

wk = WUKONG()
while True:
    if button_a.was_pressed():
        sleep(2000)
        wk.set_motors(1,100)
        wk.set_motors(2,100)
        sleep(185)
        wk.set_motors(1,0)
        wk.set_motors(2,0)