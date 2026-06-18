from microbit import *
import radio

class Radio:
    def __init__(self, channel: int, power=7):
        """
        Channel: Radio group between 0 and 255
        Power: Transmit power of the radio, between 0 and 7
        """
        radio.on()
        if channel < 0:
            channel = 0
            print("Invalid channel, changing to 0")
        elif channel > 255:
            channel = 255
            print("Invalid channel, changing to 255")
        if power < 0:
            power = 0
        elif power > 7:
            power = 7
        
        self.channel = channel
        self.power = power
        radio.config(group=self.channel, power=self.power)

    def on(self):
        """
        Turn on the radio
        """
        radio.on()
    def off(self):
        """
        Turn off the radio
        """
        radio.off()
    
    def send(self, message: str):
        """
        Send a message (string) onto the channel
        """
        self.on()
        radio.send(str(message))
        
    def receive(self):
        """
        Receive the message that is on the channel
        Returns:
            The message if it exists
            -1 if there is not message
        """
        message = radio.receive()
        if message:
            return message
        else:
            return -1