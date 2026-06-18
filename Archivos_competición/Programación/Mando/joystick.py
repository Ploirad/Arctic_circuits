from microbit import *

class joystick:
    def __init__(self, Xpin, Ypin):
        self.Xpin = Xpin
        self.Ypin = Ypin
        self.SWpin = None

    def setButton(self, SWpin):
        """
        Sets the button to use it on getValues function
        """
        self.SWpin = SWpin
        self.SWpin.set_pull(self.SWpin.PULL_UP)

    def getValues(self):
        """
        Returns:
            x: 0-1023
            y: 0-1023
            btn: 1(Pressed), 0(Not pressed), -1(Not configured)
        """
        if self.SWpin != None:
            btn = not self.SWpin.read_digital()
        else:
            btn = -1

        x = self.Xpin.read_analog()
        y = self.Ypin.read_analog()

        return x, y, btn