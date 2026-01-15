from microbit import *

class button:
    def __init__(self, pin=pin2):
        self.pin = pin
        self.pin.set_pull(self.pin.PULL_UP)
    
    def getValue(self):
        """
        Returns the value 0/1 of the button
        """
        v = not self.pin.read_digital()
        if v:
            return "T"
        else:
            return "F"