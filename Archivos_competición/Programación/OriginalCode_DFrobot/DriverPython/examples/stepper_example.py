"""
Stepper Motor Control Example for DFRobot Motor Driver

This example demonstrates how to control stepper motors using the DFRobot motor expansion board.
Supports both 28BYJ-48 and 42BYGH1861A-C stepper motors.
"""

from dfrobot_motor import DFRobot0548, Steppers, StepperType, Direction
from microbit import sleep, display, Image

# Create driver instance
driver = DFRobot0548()

# Display a happy face to show the program is running
display.show(Image.HAPPY)

print("=== 28BYJ-48 Stepper Motor Examples ===")

# Example 1: Basic stepper control - rotate by degrees
print("Example 1: Rotate 28BYJ-48 by degrees")
driver.stepper_degree_28(Steppers.M1_M2, Direction.CW, 90)   # Rotate 90 degrees clockwise
sleep(500)
driver.stepper_degree_28(Steppers.M1_M2, Direction.CCW, 90)  # Rotate 90 degrees counter-clockwise
sleep(500)

# Example 2: Rotate by full turns
print("Example 2: Rotate 28BYJ-48 by turns")
driver.stepper_turn_28(Steppers.M1_M2, Direction.CW, 1)   # Rotate 1 full turn clockwise
sleep(500)
driver.stepper_turn_28(Steppers.M1_M2, Direction.CCW, 1)  # Rotate 1 full turn counter-clockwise
sleep(500)

# Example 3: Precise positioning
print("Example 3: Precise positioning with 28BYJ-48")
driver.stepper_degree_28(Steppers.M1_M2, Direction.CW, 45)   # 45 degrees
sleep(500)
driver.stepper_degree_28(Steppers.M1_M2, Direction.CW, 45)   # Another 45 degrees (total 90)
sleep(500)
driver.stepper_degree_28(Steppers.M1_M2, Direction.CCW, 90)  # Return to start
sleep(1000)

print("=== 42BYGH1861A-C Stepper Motor Examples ===")

# Example 4: Basic 42 stepper control
print("Example 4: Rotate 42BYGH by degrees")
driver.stepper_degree_42(Steppers.M1_M2, Direction.CW, 180)   # Rotate 180 degrees clockwise
sleep(500)
driver.stepper_degree_42(Steppers.M1_M2, Direction.CCW, 180)  # Rotate 180 degrees counter-clockwise
sleep(500)

# Example 5: Multiple rotations with 42 stepper
print("Example 5: Multiple turns with 42BYGH")
driver.stepper_turn_42(Steppers.M1_M2, Direction.CW, 2)   # Rotate 2 full turns clockwise
sleep(500)
driver.stepper_turn_42(Steppers.M1_M2, Direction.CCW, 2)  # Rotate 2 full turns counter-clockwise
sleep(1000)

print("=== Dual Stepper Motor Examples ===")

# Example 6: Control two steppers simultaneously (28BYJ-48)
print("Example 6: Dual 28BYJ-48 steppers")
driver.dual_stepper(
    StepperType.STEPPER_28,
    Direction.CW, 180,   # M1_M2: 180 degrees clockwise
    Direction.CCW, 180   # M3_M4: 180 degrees counter-clockwise
)
sleep(1000)

# Example 7: Dual steppers with different angles
print("Example 7: Dual steppers - different angles")
driver.dual_stepper(
    StepperType.STEPPER_28,
    Direction.CW, 90,    # M1_M2: 90 degrees clockwise
    Direction.CW, 270    # M3_M4: 270 degrees clockwise
)
sleep(1000)

# Example 8: Dual 42BYGH steppers
print("Example 8: Dual 42BYGH steppers")
driver.dual_stepper(
    StepperType.STEPPER_42,
    Direction.CW, 360,   # M1_M2: 1 full turn clockwise
    Direction.CCW, 360   # M3_M4: 1 full turn counter-clockwise
)
sleep(1000)

# Example 9: Synchronized movement
print("Example 9: Synchronized stepper movement")
for i in range(4):
    driver.dual_stepper(
        StepperType.STEPPER_42,
        Direction.CW, 90,   # Both rotate 90 degrees
        Direction.CW, 90
    )
    sleep(500)

# Example 10: Using both stepper controllers independently
print("Example 10: Independent stepper control")
driver.stepper_degree_28(Steppers.M1_M2, Direction.CW, 180)   # First stepper
sleep(500)
driver.stepper_degree_28(Steppers.M3_M4, Direction.CCW, 180)  # Second stepper
sleep(500)

print("Stepper motor examples complete!")
display.show(Image.YES)
