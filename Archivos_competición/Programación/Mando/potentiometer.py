from microbit import *

class Potentiometer:
    def __init__(self, pin):
        self.pin = pin

    def read(self):
        value = self.pin.read_analog()
        return value