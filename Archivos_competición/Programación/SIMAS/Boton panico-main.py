# Imports go at the top
from microbit import *
from wukong import *
import radio
radio.config(group=23)
wk = WUKONG()




while True:
    if 1 == pin8.read_digital():
        wk.set_motors(1, 0)
        wk.set_motors(2, 0)
        radio.config(group=255)






    

