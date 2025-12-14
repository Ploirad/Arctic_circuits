from microbit import *
from I2C_MASTER import I2C_MASTER
from motorDriver import *
from radio import *

ESP32_ADDRESS = 0x42
i2c_master = I2C_MASTER()

motors = []
motors.append(Motor(Motors.M1))
motors.append(Motor(Motors.M2))
motors.append(Motor(Motors.M3))
motors.append(Motor(Motors.M4))

servoSujector = Servo(Servos.S1)

radio = Radio()

while True:
    # success, error = i2c_master.write(ESP32_ADDRESS, [False, True, False])    
    for i in range(0, 180):
        servoSujector.move(i)
        sleep(10)

    for s in [direction.CW, direction.CCW]:
        for m in range(0, 3):
            print("Moving motor ", m)
            for v in range(0, 255):
                motors[s].move(m, v)
                sleep(1000)
            for v in range(255, 0):
                motors[s].move(m, v)
                sleep(1000)