from microbit import *
from I2C_MASTER import I2C_MASTER
from OmniRobot import *
from motorDriver import Servo
from radioLib import Radio

ESP32_ADDRESS = 0x42
i2c_master = I2C_MASTER()

Robot = OmniRobot()
cursorServo = Servo(Servos.S1)

#moves = [Directions.Stop, Directions.Ahead, Directions.Backwards, Directions.Left, Directions.Right, Directions.Left_Ahead, Directions.Right_Ahead, Directions.Left_Backwards, Directions.Right_Backwards, Directions.CW, Directions.CCW]
PrincipalRadio = Radio(47, 7)

def dataToDirection(d: int):
    if d == 0:
        return Directions.Stop
    elif d == 1:
        return Directions.Ahead
    elif d == 2:
        return Directions.Backwards
    elif d == 3:
        return Directions.Left
    elif d == 4:
        return Directions.Right
    elif d == 5:
        return Directions.Left_Ahead
    elif d == 6:
        return Directions.Right_Ahead
    elif d == 7:
        return Directions.Left_Backwards
    elif d == 8:
        return Directions.Right_Backwards
    else:
        return -1

color = "Yellow"
last_3 = 0
last_4 = 0
last_5 = 0
last_6 = 0
while True:
    #X, Y, TR,TL,C, Cs,S, R       
    values = []
    data = PrincipalRadio.receive()
    try:
        if data != -1:
            for n in data.split(","):
                if "F" in n.upper():
                    values.append(0)
                elif "T" in n.upper():
                    values.append(1)
                else:
                    try:
                        values.append(int(n))
                    except:
                        print(n)
            print(values, color)
    
            if values[1] == 1:
                Robot.move(Directions.CCW, True)
            elif values[2] == 1:
                Robot.move(Directions.CW, True)
            else:
                direction = dataToDirection(values[0])
                if direction != -1:
                    Robot.move(direction, True)

            if last_3 != values[3]:
                if values[3] == 1:
                    if color == "Yellow":
                        color = "Blue"
                    else:
                        color = "Yellow"
                last_3 = values[3]
        
            if last_4 != values[4]:
                i2c_master.write(ESP32_ADDRESS, [values[5], values[4]])
                last_5 = values[4]
        
            if last_5 != values[5]:
                if values[6] == 1:
                    cursorServo.move(90)
                else:
                    cursorServo.move(0)
                last_5 = values[5]
        
            if last_6 != values[6]:
                if values[6] == 1:
                    display.scroll("Resetting")
                last_6 = values[6]
    except IndexError:
        pass
    # # sleep(1000)