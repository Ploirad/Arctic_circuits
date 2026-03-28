from microbit import *
from I2C_MASTER import I2C_MASTER
from OmniRobot import *
from motorDriver import Servo
from radioLib import Radio

ESP32_ADDRESS = 0x42
i2c_master = I2C_MASTER()

Robot = OmniRobot()
cursorServo1 = Servo(Servos.S8)
cursorServo2 = Servo(Servos.S7)

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
    elif d == 9:
        return Directions.CW
    elif d == 10:
        return Directions.CCW
    else:
        return -1

last_8 = 0
while True:
    #X, Y, TR,TL,C, Cs,S, R       
    values = []
    data = PrincipalRadio.receive()
    try:
        if data != -1:
            #00 0 0 0 0 0 0 0
            values = [int(data[0:2])]
            values.append(int(data[2:5]))
            for i in data[5:]:
                values.append(int(i))
            print(values)

            vel = values[1]
            
            direction = dataToDirection(values[0])
            if direction != -1:
                Robot.move(direction, vel, True)

            if last_8 != values[8]:
                if values[8] == 1:
                    cursorServo1.move(90)
                    cursorServo2.move(90)
                else:
                    cursorServo1.move(0)
                    cursorServo2.move(180)
                last_8 = values[8]

            i2c_master.write(ESP32_ADDRESS, [
                values[2], values[3], values[4], values[5],
                values[6], values[7]
            ])

    except IndexError:
        print("Index error")
    # # sleep(1000)