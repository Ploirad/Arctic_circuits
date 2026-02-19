from microbit import *
from wukong import *
wk = WUKONG()

def Avance(Velocidad, Tiempo):
    wk.set_motors(1, Velocidad - 1)
    wk.set_motors(2, -1 * Velocidad)
    sleep(Tiempo)


def Giro(Color):#Color -1 es amarillo es decir lo contrario
    wk.set_motors(1, 30 * Color)
    wk.set_motors(2, -15 * Color)
    sleep(1000)

def Parar():
    wk.set_motors(1, 0)
    wk.set_motors(2, 0)
        
        
        
        
    
while True:
    if button_a.is_pressed():
        sleep(5000)
        Avance(100, 2000)
        Giro(-1)
        Avance(100, 2000)
        Parar()
          

