# Imports go at the top
from microbit import *
from Radio import *
from button import *
from joystick import joystick
data = [0,0,"F","F","F","F","F"]
radio_sys = Radio(47, 7)
TurnRightButton = button(pin2)
TurnLeftButton = button(pin8)
ColorButton = button(pin12)
CursorButton = button(pin13)
SystemButton = button(pin14)
ResetButton = button(pin15)
Joystick = joystick(pin0,pin1)

class Directions:
    Stop = 0
    Ahead = 1
    Backwards = 2
    Left = 3
    Right = 4
    Left_Ahead = 5
    Right_Ahead = 6
    Left_Backwards = 7
    Right_Backwards = 8

def coordToDirection(x: int, y: int, base=700,ratio=150):
    maximum = base + ratio
    minimum = base - ratio

    if x >= maximum:
        if y >= maximum:
            return Directions.Right_Ahead
        elif y <= minimum:
            return Directions.Right_Backwards
        else:
            return Directions.Right
    elif x <= minimum:
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

# Code in a 'while True:' loop repeats forever
while True:
    x,y,_ = Joystick.getValues()
    data[0] = coordToDirection(x, y, 400, 150)
    data[1] = TurnLeftButton.getValue()
    data[2] = TurnRightButton.getValue()
    data[3] = ColorButton.getValue()
    data[4] = CursorButton.getValue()
    data[5] = SystemButton.getValue()
    data[6] = ResetButton.getValue()
    radio_sys.send(str(data)[1:-2].replace(" ", "").replace("'", ""))