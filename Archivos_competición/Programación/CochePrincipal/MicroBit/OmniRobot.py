from microbit import *
from motorDriver import *

class Directions:
    Stop = "stop"
    Ahead = "ahead"
    Right = "right"
    Left = "left"
    Backwards = "backwards"
    Left_Ahead = "left_ahead"
    Right_Ahead = "right_ahead"
    Right_Backwards = "right_backwards"
    Left_Backwards = "left_backwards"
    CW = "cw"
    CCW = "ccw"

class OmniRobot:
    def __init__(self):
        self.motors = []
        self.motors.append(Motor(Motors.M1))
        self.motors.append(Motor(Motors.M2))
        self.motors.append(Motor(Motors.M3))
        self.motors.append(Motor(Motors.M4))
        
        self.movements = {
            "stop": [0, 0, 0, 0],
            "ahead": [1, 1, 1, 1],
            "left": [-1, 1, 1, -1],
            "right": [1, -1, -1, 1],
            "backwards": [-1, -1, -1, -1],
            "right_ahead": [1, 0, 0, 1],
            "left_ahead": [0, 1, 1, 0],
            "left_backwards": [-1, 0, 0, -1],
            "right_backwards": [0, -1, -1, 0],
            "cw": [1, -1, 1, -1],
            "ccw": [-1, 1, -1, 1]
        }
        self.prints = {
            "stop": Image.HAPPY,
            "ahead": Image.ARROW_N,
            "right": Image.ARROW_E,
            "left": Image.ARROW_W,
            "backwards": Image.ARROW_S,
            "left_ahead": Image.ARROW_NW,
            "right_ahead": Image.ARROW_NE,
            "right_backwards": Image.ARROW_SE,
            "left_backwards": Image.ARROW_SW,
            "cw": Image.CHESSBOARD,
            "ccw": Image.SQUARE
        }

    def move(self, direction: str, velocity=255, prints=False):
        """
        direction must be a Directions value (Directions.Stop, Directions.Ahead, etc.)
        """
        direction = direction.lower()
        direction = direction.replace(" ", "_")
        for i in range(0, 4):
            if self.movements[direction][i] == 0:
                self.motors[i].stop()
            elif self.movements[direction][i] == 1:
                self.motors[i].move(Direction.CW, velocity)
            elif self.movements[direction][i] == -1:
                self.motors[i].move(Direction.CCW, velocity)
        if prints:
            display.show(self.prints[direction])

    def stop(self):
        """
        Stop all the movements
        """
        self.move(Directions.Stop)