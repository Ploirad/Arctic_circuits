# Imports go at the top
from microbit import *

def calculadora():
    dato1 = 0
    dato2 = 0
    estado = 0
    operador = 0 #Si vale 0 se hará una suma, si vale 1 pondrá una resta, si pone 2 hará una multiplicación y si pone 3 hará una división
    resultado = 0.0
    while True:
        button_a.was_pressed()
        button_b.was_pressed()
        display.scroll("Quieres ver el tutorial?")
        display.scroll("Pulsa A si quieres verlo y pulsa B si no quieres verlo")
        if button_a.was_pressed():
            display.scroll("Bienvenido a mi calculadora, primero estableceras los dos numeros con el boton A para sumar uno al numero y el boton B para restar uno")
            display.scroll("Cuando termines un numero pulsa ambos para pasar al otro o al operador que se va a utilizar")
            display.scroll("Despues elegiras que operador usar pulsando A para el primero y B para el segundo, si pulsas A+B cambiaras a los otros dos operadores")
            break
        elif button_b.was_pressed():
            break
    
    display.scroll("Numero 1:")
    while True:
        display.scroll(dato1)
        if button_a.is_pressed() and button_b.is_pressed():
            break
        elif button_a.was_pressed():
            dato1 += 1
        elif button_b.was_pressed():
            dato1 -= 1
    display.scroll("Numero 2:")
    while True:
        display.scroll(dato2)
        if button_a.is_pressed() and button_b.is_pressed():
            break
        elif button_a.was_pressed():
            dato2 += 1
        elif button_b.was_pressed():
            dato2 -= 1
    display.scroll("Operador")
    #Esto es para reiniciar la función was_pressed de los botones y que cuenten a partir de ahora
    button_a.was_pressed()
    button_b.was_pressed()
    while True:
        if estado == 0:
            display.show(Image('00900:'
                               '00900:'
                               '99999:'
                               '00900:'
                               '00900'))
            sleep(500)
            display.show(Image('00000:'
                               '00000:'
                               '99999:'
                               '00000:'
                               '00000'))
            sleep(500)
        else:
            display.show(Image('90009:'
                               '09090:'
                               '00900:'
                               '09090:'
                               '90009'))
            sleep(500)
            display.show(Image('00900:'
                               '00000:'
                               '99999:'
                               '00000:'
                               '00900'))
            sleep(500)
        if button_a.was_pressed() and button_b.was_pressed():
            estado = 1 - estado
        elif estado == 0 and button_a.was_pressed():
            operador = 0
            break
        elif estado == 0 and button_b.was_pressed():
            operador = 1
            break
        elif estado == 1 and button_a.was_pressed():
            operador = 2
            break
        elif estado == 1 and button_b.was_pressed():
            operador = 3
            break
    if operador == 0:
        resultado = dato1+dato2
    if operador == 1:
        resultado = dato1-dato2
    if operador == 2:
        resultado = dato1*dato2
    if operador == 3:
        resultado = dato1/dato2
    display.scroll("El resultado es:")
    display.scroll(resultado)
def basic():
    display.scroll("Nombre:")
    display.scroll("Dario")
    display.scroll("Edad:")
    display.show(17)
    sleep(1000)
    display.scroll("Mascotas:")
    display.show(0)
    sleep(1000)
    display.scroll("Comida favorita:")
    display.scroll("Mac&cheese")
    display.scroll("Altura:")
    display.show(2.02)
    display.scroll("Temperatura")
    display.show(temperature())
    display.show(Image.DUCK)

# Code in a 'while True:' loop repeats forever
while True:
    if button_a.is_pressed():
        calculadora()
    elif button_b.is_pressed():
        basic()
    
