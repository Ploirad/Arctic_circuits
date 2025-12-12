"""
Servo Control Example for DFRobot Motor Driver

This example demonstrates how to control servo motors using the DFRobot motor expansion board.
Servos can be controlled from 0° to 180°.
"""

from dfrobot_motor import DFRobot0548, Servos
from microbit import sleep, display, Image

# Create driver instance
driver = DFRobot0548()

# Display a happy face to show the program is running
display.show(Image.HAPPY)

# Example 1: Move a single servo to specific positions
print("Example 1: Single servo control")
driver.servo(Servos.S1, 0)    # Move servo S1 to 0 degrees
sleep(1000)
driver.servo(Servos.S1, 90)   # Move servo S1 to 90 degrees (center)
sleep(1000)
driver.servo(Servos.S1, 180)  # Move servo S1 to 180 degrees
sleep(1000)

# Example 2: Sweep a servo back and forth
print("Example 2: Servo sweep")
for i in range(3):  # Repeat 3 times
    # Sweep from 0 to 180
    for angle in range(0, 181, 10):
        driver.servo(Servos.S1, angle)
        sleep(50)
    
    # Sweep from 180 to 0
    for angle in range(180, -1, -10):
        driver.servo(Servos.S1, angle)
        sleep(50)

# Example 3: Control multiple servos
print("Example 3: Multiple servo control")
driver.servo(Servos.S1, 45)
driver.servo(Servos.S2, 90)
driver.servo(Servos.S3, 135)
sleep(2000)

# Return all servos to center position
driver.servo(Servos.S1, 90)
driver.servo(Servos.S2, 90)
driver.servo(Servos.S3, 90)

# Example 4: Create a wave pattern with 4 servos
print("Example 4: Wave pattern")
for cycle in range(2):  # 2 cycles
    for offset in range(0, 180, 20):
        driver.servo(Servos.S1, offset)
        driver.servo(Servos.S2, (offset + 45) % 180)
        driver.servo(Servos.S3, (offset + 90) % 180)
        driver.servo(Servos.S4, (offset + 135) % 180)
        sleep(100)

print("Servo examples complete!")
display.show(Image.YES)
