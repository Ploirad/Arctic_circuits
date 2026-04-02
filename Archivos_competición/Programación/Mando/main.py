# Imports go at the top
from microbit import *
from Radio import *
from button import *
from joystick import joystick
from potentiometer import Potentiometer as Pot
carData = [0,0,"F","F","F","F","F",0,0]
simaData = [0, 0] # -> "0,0"
car_channel = 47
sima_channel = 50
radio_sys = Radio(car_channel)

display.off()

movementJoystick = joystick(pin0, pin1)
movementJoystick.setButton(pin5)
pot = Pot(pin2)
actionsJoystick = joystick(pin3, pin4)
actionsJoystick.setButton(pin6)
turn1 = button(pin7)
turn2 = button(pin8)
turn3 = button(pin9)
turn4 = button(pin10)
color = button(pin11)

def map_value(x, in_min, in_max, out_min, out_max):
    if in_min == in_max:
        return out_min
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
def listToStr(data):
    return str(data)[1:-2].replace(" ", "").replace("'", "").replace(",", "")
def listToStrSima(data):
    return str(data)[1:-2].replace(" ", "").replace("'", "")

class Directions:
    Stop = "00"
    Ahead = "01"
    Backwards = "02"
    Left = "03"
    Right = "04"
    Left_Ahead = "05"
    Right_Ahead = "06"
    Left_Backwards = "07"
    Right_Backwards = "08"
    CW = "09"
    CCW = "10"

def coordToDirection(x: int, y: int, b: int, base=400,ratio=150):
    maximum = base + ratio
    minimum = base - ratio
    if b == -1:
        b = 0

    if x >= maximum:
        if b == 1:
            return Directions.CW
        if y >= maximum:
            return Directions.Right_Ahead
        elif y <= minimum:
            return Directions.Right_Backwards
        else:
            return Directions.Right
    elif x <= minimum:
        if b == 1:
            return Directions.CCW
        if y >= maximum:
            return Directions.Left_Ahead
        elif y <= minimum:
            return Directions.Left_Backwards
        else:
            return Directions.Left
    else:
        if y >= maximum:
            return Directions.Ahead
        elif y <= minimum:
            return Directions.Backwards
        else:
            return Directions.Stop

move = False
moved = False
moveTemp = False
canChange = True

while True:

    # MAIN ROBOT
    x,y,btn = movementJoystick.getValues()
    direction = coordToDirection(x, y, btn)

    p = pot.read()
    # print(p)
    # sleep(100)
    potValue = min(max(int(map_value(p, 785, 832, 0, 255)), 0), 255)

    close,down,temp = actionsJoystick.getValues()
    if close > (400+150):
        carData[6] = "2"
    elif close < (400-150):
        carData[6] = "1"
    else:
        carData[6] = "0"

    if down > (400+150):
        carData[7] = "2"
    elif down < (400-150):
        carData[7] = "1"
    else:
        carData[7] = "0"

    potValueToSend = str(potValue)
    if len(potValueToSend) == 2:
        potValueToSend = "0"+potValueToSend
    elif len(potValueToSend) == 1:
        potValueToSend = "00"+potValueToSend

    turnValues = [turn1.getValue(), turn2.getValue(), turn3.getValue(), turn4.getValue()]
    
    carData[0] = direction
    carData[1] = potValueToSend
    for i in range(4):
        carData[i+2] = turnValues[i]

    if temp and canChange:
        print(moveTemp)
        moveTemp = not moveTemp
        canChange = False
        print("Pulsado")
        print(moveTemp)
    elif not temp:
        canChange = True
        print("Resteado")
        
    if moveTemp:
        carData[8] = "T"
    else:
        carData[8] = "F"
    
    data = listToStr(carData).replace("F", "0").replace("T", "1")
    # print(data)
    radio_sys.config(car_channel, 7)
    radio_sys.send(data)

    # SIMA'S
    for data in [carData[2], carData[3], carData[4], carData[5], carData[8]]:
        if not move and not moved and data != "F":
            move = True
            moved = True

    simaData[0] = color.getValue() # Color
    simaData[1] = moved # Start the count
    radio_sys.config(sima_channel, 7)
    # simaData structure to send: "Color,Start"
    radio_sys.send(listToStrSima(simaData))