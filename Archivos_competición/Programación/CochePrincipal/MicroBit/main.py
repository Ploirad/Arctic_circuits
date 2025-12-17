from microbit import *
from I2C_MASTER import I2C_MASTER
from OmniRobot import *
from motorDriver import Servo
from Radio import Radio

ESP32_ADDRESS = 0x42
i2c_master = I2C_MASTER()

Robot = OmniRobot()
servoSujector = Servo(Servos.S1)

#moves = [Directions.Stop, Directions.Ahead, Directions.Backwards, Directions.Left, Directions.Right, Directions.Left_Ahead, Directions.Right_Ahead, Directions.Left_Backwards, Directions.Right_Backwards, Directions.CW, Directions.CCW]
PrincipalRadio = Radio(47, 7)
datas = [0, 0, 0, 0, 0]

def coordToDirection(x: float, y: float, ratio=30):
    n = ratio
    if x >= 850:
        if y >= 850:
            return Directions.Right_Ahead
        elif y <= 500:
            return Directions.Right_Backwards
        else:
            return Directions.Right
    elif x <= 500:
        if y >= 850:
            return Directions.Left_Ahead
        elif y <= 500:
            return Directions.Left_Backwards
        else:
            return Directions.Left
    else:
        if y >= 850:
            return Directions.Ahead
        elif y <= 500:
            return Directions.Backwards
        else:
            return Directions.Stop

last_2 = 0
last_3 = 0
last_4 = 0
while True:
    data = PrincipalRadio.receive()
    if data != -1:
                #X, Y, C, S, R        
        datas = [0, 0, 0, 0, 0]
        for n in data.split(","):
            if n[0] == "[":
                n = n[1:]
            if n[-1] == "]":
                n = n[:-2]

            if "F" in n.upper():
                datas.append(0)
            elif "T" in n.upper():
                datas.append(1)
            else:
                try:
                    datas.append(int(n))
                except:
                    print(n)
        datas = datas[5:]
        print(datas)

    dir = coordToDirection(datas[0], datas[1])
    Robot.move(dir, True)

    if last_2 != datas[2]:
        if datas[2] == 1:
            servoSujector.move(90)
        else:
            servoSujector.move(0)

    if last_3 != datas[3]:
        i2c_master.write(ESP32_ADDRESS, [datas[3]])
        last_3 = datas[3]

    if last_4 != datas[4]:
        if datas[4] == 1:
            display.scroll("Resetting")
        last_4 = datas[4]

    # sleep(1000)