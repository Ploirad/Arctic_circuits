# Imports go at the top
from microbit import *

health_bar = 100

while True:
    if button_a.is_pressed():
        health_bar = health_bar - 10

    if button_b.is_pressed():
        if health_bar <= 95:
            health_bar = health_bar + 5

    if health_bar > 80:
        display.show(Image.HAPPY)
    elif health_bar == 0:
        display.show(Image.SKULL)

    print(health_bar)