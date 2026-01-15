from microbit import *
import radio

class Radio:
    def __init__(self, Channel: int, Power=7):
        """
        Channel: Radio group between 0 and 255
        Power: Transmit power of the radio, between 0 and 7
        """
        radio.on()
        if Channel < 0:
            Channel = 0
            print("Invalid channel, changing to 0")
        elif Channel > 255:
            Channel = 255
            print("Invalid channel, changing to 255")
        if Power < 0:
            Power = 0
        elif Power > 7:
            Power = 7
        
        self.Channel = Channel
        self.Power = Power
        radio.config(group=self.Channel, power=self.Power)

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