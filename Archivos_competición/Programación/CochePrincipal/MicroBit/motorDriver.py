from microbit import *
from dfrobot_motor import *

driver = DFRobot0548()

class Motor:
    def __init__(self, motor):
        """
        motor: Motors.M1, Motors.M2, Motors.M3 or Motors.M4
        """
        self.motor = motor
        driver.motor_stop(self.motor)

    def move(self, direction, velocity):
        """
        Direction: Direction.CW or Direction.CCW
        Velocity: 0 - 255
        """
        driver.motor_run(self.motor, direction, velocity)

    def stop(self):
        driver.motor_stop(self.motor)

class Servo:
    def __init__(self, servo):
        """
        servo: from Servos.S1 to Servos.S8
        """
        self.servo = servo
    
    def move(self, angle):
        """
        angle: from 0 to 180 degrees in case it is a 180 degrees's servo
        else, it is velocity instead of degrees
        """
        driver.servo(self.servo, angle)