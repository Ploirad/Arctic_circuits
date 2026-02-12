from microbit import *
from radioLib import Radio #radio con minuscula tienes que crear un archivo con el codigo de Radio.py esto en microbit python editor
r = Radio(50, 7)#r es el equivalente de radio




while True:
    recived_data = r.receive()
    print(recived_data)

    if  recived_data == "F,Tru":
        display.set_pixel(0, 0, 9)
        sleep(2000)
    elif recived_data == "T,Tru":
        display.set_pixel(0, 0, 9)
        display.set_pixel(1, 1, 9)
        sleep(2000)
        


        

