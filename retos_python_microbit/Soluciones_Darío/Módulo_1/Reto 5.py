# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
puntos = 0
estado = 0
health_bar = 100
while True:
    if estado == 0:
        Nombre = "Dario"
        Edad = 17
        Ciudad = "Guadalajara"
        Hobby_favorito = "Videojuegos"
        display.scroll("Mi nombre es")
        display.scroll(Nombre)
        display.scroll("Mi edad es")
        display.scroll(Edad)
        display.scroll("Mi ciudad es")
        display.scroll(Ciudad)
        display.scroll("Mi hobbie favorito es")
        display.scroll(Hobby_favorito)
        if accelerometer.was_gesture("shake"):
            estado = 1
    if estado == 1:
        display.scroll(puntos)
        if button_a.was_pressed() and button_b.was_pressed():
            puntos = 0
        if button_a.was_pressed():
            puntos += 1
        if button_b.was_pressed() and puntos > 0:
            puntos -= 1
        if accelerometer.was_gesture("shake"):
            estado = 2
    if estado == 2:
        display.scroll("Vamos a calcular valores con las temperaturas")
        temp1 = temperature()
        sleep(2000)
        temp2 = temperature()
        sleep(2000)
        temp3 = temperature()
        display.scroll("El valor total es de:")
        display.scroll(temp1+temp2+temp3)
        display.scroll("El valor medio es de:")
        display.scroll((temp1+temp2+temp3)/3)
        display.scroll("El valor más alto es de:")
        if temp1>=temp2 and temp1>=temp3:
            display.scroll("Temperatura 1 de")
            display.scroll(temp1)
        elif temp2>=temp1 and temp2>=temp3:
            display.scroll("Temperatura 2 de")
            display.scroll(temp2)
        elif temp3>=temp2 and temp3>=temp1:
            display.scroll("Temperatura 3 de")
            display.scroll(temp3)
        if accelerometer.was_gesture("shake"):
            estado = 3
    if estado == 3:
        display.scroll(health_bar)
        if health_bar >= 80:
            display.show(Image.HAPPY)
            sleep(900)
        elif health_bar == 0:
            display.show(Image.SKULL)
            sleep(900)
        if button_a.was_pressed():
            health_bar -= 10
        if button_b.was_pressed() and health_bar < 100:
            health_bar += 5
        if accelerometer.was_gesture("shake"):
            estado = 0
    sleep(100)
        
        
        
