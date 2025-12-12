"""
DC Motor Control Example for DFRobot Motor Driver

This example demonstrates how to control DC motors using the DFRobot motor expansion board.
Motors can run at variable speeds (0-255) in both directions (CW/CCW).
"""

from dfrobot_motor import DFRobot0548, Motors, Direction
from microbit import sleep, display, Image

# Create driver instance
driver = DFRobot0548()

# Display a happy face to show the program is running
display.show(Image.HAPPY)

# Example 1: Basic motor control - forward and backward
print("Example 1: Basic motor control")
driver.motor_run(Motors.M1, Direction.CW, 150)   # Run motor M1 clockwise at speed 150
sleep(2000)
driver.motor_stop(Motors.M1)                      # Stop motor M1
sleep(500)

driver.motor_run(Motors.M1, Direction.CCW, 150)  # Run motor M1 counter-clockwise at speed 150
sleep(2000)
driver.motor_stop(Motors.M1)
sleep(500)

# Example 2: Speed ramping - gradually increase and decrease speed
print("Example 2: Speed ramping")
# Ramp up
for speed in range(0, 256, 15):
    driver.motor_run(Motors.M1, Direction.CW, speed)
    sleep(100)

# Ramp down
for speed in range(255, -1, -15):
    driver.motor_run(Motors.M1, Direction.CW, speed)
    sleep(100)

driver.motor_stop(Motors.M1)
sleep(500)

# Example 3: Control multiple motors simultaneously
print("Example 3: Multiple motors")
driver.motor_run(Motors.M1, Direction.CW, 200)   # Motor 1 forward
driver.motor_run(Motors.M2, Direction.CW, 200)   # Motor 2 forward
sleep(2000)

driver.motor_run(Motors.M1, Direction.CCW, 200)  # Motor 1 backward
driver.motor_run(Motors.M2, Direction.CCW, 200)  # Motor 2 backward
sleep(2000)

driver.motor_stop_all()  # Stop all motors
sleep(500)

# Example 4: Differential drive (like a robot car)
print("Example 4: Differential drive")
# Turn left (right motor faster)
driver.motor_run(Motors.M1, Direction.CW, 100)
driver.motor_run(Motors.M2, Direction.CW, 200)
sleep(1500)

# Turn right (left motor faster)
driver.motor_run(Motors.M1, Direction.CW, 200)
driver.motor_run(Motors.M2, Direction.CW, 100)
sleep(1500)

# Spin in place (motors in opposite directions)
driver.motor_run(Motors.M1, Direction.CW, 180)
driver.motor_run(Motors.M2, Direction.CCW, 180)
sleep(1500)

driver.motor_stop_all()
sleep(500)

# Example 5: All four motors
print("Example 5: Four motor control")
# All motors forward
driver.motor_run(Motors.M1, Direction.CW, 180)
driver.motor_run(Motors.M2, Direction.CW, 180)
driver.motor_run(Motors.M3, Direction.CW, 180)
driver.motor_run(Motors.M4, Direction.CW, 180)
sleep(2000)

# All motors backward
driver.motor_run(Motors.M1, Direction.CCW, 180)
driver.motor_run(Motors.M2, Direction.CCW, 180)
driver.motor_run(Motors.M3, Direction.CCW, 180)
driver.motor_run(Motors.M4, Direction.CCW, 180)
sleep(2000)

# Emergency stop all motors
driver.motor_stop_all()

print("DC motor examples complete!")
display.show(Image.YES)
