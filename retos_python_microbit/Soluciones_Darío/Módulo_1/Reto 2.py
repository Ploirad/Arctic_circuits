# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    display.scroll("DARIO")
    sleep(1000)
    display.scroll(17)
    sleep(1000)
    display.show(Image.ASLEEP)
    sleep(1000)
    display.show(Image('00099:'
                       '99099:'
                       '00000:'
                       '09990:'
                       '00000'))
    sleep(1000)
    display.show(Image('00099:'
                       '99099:'
                       '09990:'
                       '90009:'
                       '09990'))
    sleep(400)
    display.show(Image('00099:'
                       '99099:'
                       '00000:'
                       '09990:'
                       '00000'))
    sleep(400)
    display.show(Image('00099:'
                       '99099:'
                       '09990:'
                       '90009:'
                       '09990'))
    sleep(400)
    display.show(Image('00099:'
                       '99099:'
                       '00000:'
                       '09990:'
                       '00000'))
    sleep(500)
    display.show(Image.ASLEEP)
    
    
    
