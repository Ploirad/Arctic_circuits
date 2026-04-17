from microbit import *
import utime
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

    def _current_time(self):
        """Tiempo actual en segundos (float)."""
        return utime.ticks_ms() / 1000.0
         
    def setColor(self, color):
        self.color = color
        
    def _adelante(self, der, izq):
        self.wk.set_motors(1, izq)
        self.wk.set_motors(2, der)

    def start(self):
        self._stop()
        display.show(Image.ARROW_N)
        color = 0
        parar = True
        color, start = self.decode(self.radio.receive())
        while not start:
           color, start = self.decode(self.radio.receive())

        self.setColor(color)
        display.show(Image.YES)
        sleep(86 * 1000)
        self._last_odom_time = self._current_time()
        a = True
        while a:
            now = self._current_time()
            dt  = now - self._last_odom_time
            sleep(10)
            if self.go(dt) or self.emergencyBtn.is_pressed():
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

    def go(self, dt):
        if self.emergencyBtn.is_pressed():
            self._stop()
            display.show(Image.NO)
            return True # Break loop principal

        if dt <= 5000:
            self.wk.set_motors(1, 100)
            self.wk.set_motors(2, -100)
            return False
        else:    
            return True
                
                

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
        HC_SR04_pin = pin2, panic_pin = pin1,
        channel = 50, servo_pin=0
    )
    SIMA.start()
