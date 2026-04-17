from microbit import *
import utime
import math
from Button import Button
from wukong import *
from RadioLib import Radio as r

class Sima:
    def __init__(self, HC_SR04_pin, panic_pin, channel, servo_pin):
        self.HC_SR04_pin = HC_SR04_pin
        self.wk = WUKONG()
        self.emergencyBtn = Button(panic_pin)
        self.radio = r(channel, Power=7)
        self.servo_pin = servo_pin

    def decode(self, message):
        # MESSAGE STRUCTURE:
        # "Color,Start"
        if message == -1:
            return False, False
        try:
            color_str, start_str = message.split(',')
            color = self._dataToVal(color_str.strip().upper())
            start = self._dataToVal(start_str.strip().upper())
            return color, start
        except ValueError:
            print("Invalid message format:", message)
            return False, False
        
    def setColor(self, color):
        self.color = color
        
        
    def start(self):
        display.show(Image.ARROW_N)
        color = 0
        parar = True
        color, start = self.decode(self.radio.receive())
        while not start:
            color, start = self.decode(self.radio.receive())

        self.setColor(color)
        display.show(Image.YES)
        # sleep(86 * 1000)
        self._last_odom_time = self._current_time()
        a = True
        while a:
            sleep(10)
            if self.go() or self.emergencyBtn.is_pressed():
                self._stop()
                a = False
            if self.emergencyBtn.is_pressed():
                parar = False
        while True and parar:
            self.turnServo(180)
            sleep(500)
            self.turnServo(90)
            sleep(500)
            
            if self.emergencyBtn.is_pressed():
                break

    def turnServo(self, deg):
        self.wk.set_servo(self.servo_pin, deg)  # Gira el servo a 0 grados (ajusta según necesidad)

    def go(self):
        if self.emergencyBtn.is_pressed():
            self._stop()
            display.show(Image.NO)
            return True # Break loop principal

        self._update_odometry()
        distance_obst = self._read_ultrasonic()

        if self.state == "GO_TO_GOAL":
            if 0 < distance_obst < self.ULTRASONIC_THRESHOLD:
                # Obstáculo detectado → cambiar a modo esquiva
                self._stop()
                display.show(Image.SAD)
                self.state = "AVOID_OBSTACLE"
            else:
                reached_goal = self._follow_point(self.xf, self.yf)
                if reached_goal:
                    self._stop()
                    display.show(Image.HAPPY)
                    return True # Objetivo alcanzado, salir del loop principal

        elif self.state == "AVOID_OBSTACLE":
            self._avoid_obstacle_maneuver()
            # Tras la maniobra volvemos a navegar hacia el objetivo
            self.state = "GO_TO_GOAL"
            display.show(Image.ARROW_N)

        return False # Continuar el loop principal

    def _dataToVal(self, data):
        if data == "F" or data == 0:
            return False
        else:
            return True

    def _stop(self):
        self.wk.set_motors(1, 0)
        self.wk.set_motors(2, 0)

    
if __name__ == '__main__':
    SIMA = Sima(
        x0 = 50.0, y0 = 1950.0, firstAngle = 180.0,
        xf = 50.0, yf = 800.0,
        v = 40.816327, angularVelocity = 500.0,
        lin_regulation = 100.0, ang_regulation = 100.0,
        HC_SR04_pin = pin2, panic_pin = pin1,
        channel = 36, servo_pin=0
    )
    SIMA.start()
