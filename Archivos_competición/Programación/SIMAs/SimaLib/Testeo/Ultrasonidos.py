# Imports go at the top
from microbit import *
from wukong import *


wk = WUKONG()
# Code in a 'while True:' loop repeats forever
while True:
    ping = wk.read_sonar(pin2)
    print(ping)
    sleep(200)