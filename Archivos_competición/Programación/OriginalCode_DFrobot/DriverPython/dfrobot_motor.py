"""
DFRobot Motor Driver for micro:bit (MicroPython)

This module provides control for the DFRobot motor expansion board using the PCA9685 PWM controller.
Supports:
- 8 servo channels (S1-S8): 0° to 180°
- 4 DC motors (M1-M4): Speed 0-255, bidirectional (CW/CCW)
- 2 stepper motor controllers: 28BYJ-48 and 42BYGH1861A-C

Hardware: DFRobot micro:bit Motor Driver Expansion Board (Model 0548)
I2C Address: 0x40 (PCA9685)

Author: MicroPython port from original MakeCode extension
License: GNU Lesser General Public License
"""

from microbit import i2c, sleep


# Direction constants
class Direction:
    """Motor direction constants"""
    CW = 1   # Clockwise
    CCW = -1  # Counter-clockwise


# Motor/Servo channel mappings
class Servos:
    """Servo channel identifiers (S1-S8)"""
    S1 = 0x08
    S2 = 0x07
    S3 = 0x06
    S4 = 0x05
    S5 = 0x04
    S6 = 0x03
    S7 = 0x02
    S8 = 0x01


class Motors:
    """DC Motor identifiers (M1-M4)"""
    M1 = 0x1
    M2 = 0x2
    M3 = 0x3
    M4 = 0x4


class Steppers:
    """Stepper motor controller identifiers"""
    M1_M2 = 0x1  # Uses motors M1 and M2
    M3_M4 = 0x2  # Uses motors M3 and M4


class StepperType:
    """Stepper motor type identifiers"""
    STEPPER_42 = 1  # 42BYGH1861A-C
    STEPPER_28 = 2  # 28BYJ-48


class DFRobot0548:
    """
    DFRobot Motor Driver Board (Model 0548) Controller
    
    This class provides a clean interface to control the DFRobot motor expansion board
    for micro:bit using the PCA9685 PWM controller.
    
    Example:
        driver = DFRobot0548()
        driver.servo(Servos.S1, 90)
        driver.motor_run(Motors.M1, Direction.CW, 200)
    """
    
    # PCA9685 Register addresses
    _PCA9685_ADDRESS = 0x40
    _MODE1 = 0x00
    _MODE2 = 0x01
    _PRESCALE = 0xFE
    _LED0_ON_L = 0x06
    _LED0_ON_H = 0x07
    _LED0_OFF_L = 0x08
    _LED0_OFF_H = 0x09
    
    # Stepper motor phase constants for 28BYJ-48
    _STP_CHA_L = 2047
    _STP_CHA_H = 4095
    _STP_CHB_L = 1
    _STP_CHB_H = 2047
    _STP_CHC_L = 1023
    _STP_CHC_H = 3071
    _STP_CHD_L = 3071
    _STP_CHD_H = 1023
    
    # Stepper motor phase constants for 42BYGH1861A-C
    _BYG_CHA_L = 3071
    _BYG_CHA_H = 1023
    _BYG_CHB_L = 1023
    _BYG_CHB_H = 3071
    _BYG_CHC_L = 4095
    _BYG_CHC_H = 2047
    _BYG_CHD_L = 2047
    _BYG_CHD_H = 4095
    
    def __init__(self, i2c_address=0x40):
        """
        Initialize the DFRobot motor driver
        
        Args:
            i2c_address: I2C address of the PCA9685 (default: 0x40)
        """
        self._address = i2c_address
        self._initialized = False
        self._init_pca9685()
    
    def _i2c_write(self, reg, value):
        """Write a single byte to a PCA9685 register"""
        i2c.write(self._address, bytes([reg, value]))
    
    def _i2c_read(self, reg):
        """Read a single byte from a PCA9685 register"""
        i2c.write(self._address, bytes([reg]))
        return i2c.read(self._address, 1)[0]
    
    def _set_freq(self, freq):
        """Set PWM frequency for PCA9685"""
        prescaleval = 25000000.0  # 25MHz
        prescaleval /= 4096.0
        prescaleval /= freq
        prescaleval -= 1.0
        prescale = int(prescaleval)
        
        oldmode = self._i2c_read(self._MODE1)
        newmode = (oldmode & 0x7F) | 0x10  # Sleep
        self._i2c_write(self._MODE1, newmode)  # Go to sleep
        self._i2c_write(self._PRESCALE, prescale)  # Set prescaler
        self._i2c_write(self._MODE1, oldmode)
        sleep(5)  # Wait 5ms
        self._i2c_write(self._MODE1, oldmode | 0xa1)
    
    def _set_pwm(self, channel, on, off):
        """Set PWM for a specific channel"""
        if channel < 0 or channel > 15:
            return
        
        buf = bytes([
            self._LED0_ON_L + 4 * channel,
            on & 0xFF,
            (on >> 8) & 0xFF,
            off & 0xFF,
            (off >> 8) & 0xFF
        ])
        i2c.write(self._address, buf)
    
    def _init_pca9685(self):
        """Initialize the PCA9685 PWM controller"""
        self._i2c_write(self._MODE1, 0x00)
        self._set_freq(50)  # 50Hz for servos
        self._initialized = True
    
    def _set_stepper_28(self, index, direction):
        """Set stepper motor 28BYJ-48 phase pattern"""
        if index == 1:
            if direction:
                self._set_pwm(4, self._STP_CHA_L, self._STP_CHA_H)
                self._set_pwm(6, self._STP_CHB_L, self._STP_CHB_H)
                self._set_pwm(5, self._STP_CHC_L, self._STP_CHC_H)
                self._set_pwm(7, self._STP_CHD_L, self._STP_CHD_H)
            else:
                self._set_pwm(7, self._STP_CHA_L, self._STP_CHA_H)
                self._set_pwm(5, self._STP_CHB_L, self._STP_CHB_H)
                self._set_pwm(6, self._STP_CHC_L, self._STP_CHC_H)
                self._set_pwm(4, self._STP_CHD_L, self._STP_CHD_H)
        else:
            if direction:
                self._set_pwm(0, self._STP_CHA_L, self._STP_CHA_H)
                self._set_pwm(2, self._STP_CHB_L, self._STP_CHB_H)
                self._set_pwm(1, self._STP_CHC_L, self._STP_CHC_H)
                self._set_pwm(3, self._STP_CHD_L, self._STP_CHD_H)
            else:
                self._set_pwm(3, self._STP_CHA_L, self._STP_CHA_H)
                self._set_pwm(1, self._STP_CHB_L, self._STP_CHB_H)
                self._set_pwm(2, self._STP_CHC_L, self._STP_CHC_H)
                self._set_pwm(0, self._STP_CHD_L, self._STP_CHD_H)
    
    def _set_stepper_42(self, index, direction):
        """Set stepper motor 42BYGH1861A-C phase pattern"""
        if index == 1:
            if direction:
                self._set_pwm(7, self._BYG_CHA_L, self._BYG_CHA_H)
                self._set_pwm(6, self._BYG_CHB_L, self._BYG_CHB_H)
                self._set_pwm(5, self._BYG_CHC_L, self._BYG_CHC_H)
                self._set_pwm(4, self._BYG_CHD_L, self._BYG_CHD_H)
            else:
                self._set_pwm(7, self._BYG_CHC_L, self._BYG_CHC_H)
                self._set_pwm(6, self._BYG_CHD_L, self._BYG_CHD_H)
                self._set_pwm(5, self._BYG_CHA_L, self._BYG_CHA_H)
                self._set_pwm(4, self._BYG_CHB_L, self._BYG_CHB_H)
        else:
            if direction:
                self._set_pwm(3, self._BYG_CHA_L, self._BYG_CHA_H)
                self._set_pwm(2, self._BYG_CHB_L, self._BYG_CHB_H)
                self._set_pwm(1, self._BYG_CHC_L, self._BYG_CHC_H)
                self._set_pwm(0, self._BYG_CHD_L, self._BYG_CHD_H)
            else:
                self._set_pwm(3, self._BYG_CHC_L, self._BYG_CHC_H)
                self._set_pwm(2, self._BYG_CHD_L, self._BYG_CHD_H)
                self._set_pwm(1, self._BYG_CHA_L, self._BYG_CHA_H)
                self._set_pwm(0, self._BYG_CHB_L, self._BYG_CHB_H)
    
    # Public API Methods
    
    def servo(self, index, degree):
        """
        Control a servo motor
        
        Args:
            index: Servo channel (use Servos.S1 to Servos.S8)
            degree: Angle in degrees (0-180)
        
        Example:
            driver.servo(Servos.S1, 90)  # Move servo S1 to 90 degrees
        """
        # Constrain degree to 0-180
        degree = max(0, min(180, degree))
        
        # Calculate pulse width: 0.6ms to 2.4ms for 0° to 180°
        v_us = (degree * 1800 // 180 + 600)  # microseconds
        value = v_us * 4096 // 20000  # Convert to 12-bit PWM value
        self._set_pwm(index + 7, 0, value)
    
    def motor_run(self, index, direction, speed):
        """
        Run a DC motor
        
        Args:
            index: Motor number (use Motors.M1 to Motors.M4)
            direction: Direction (Direction.CW or Direction.CCW)
            speed: Speed value (0-255)
        
        Example:
            driver.motor_run(Motors.M1, Direction.CW, 200)
        """
        # Map speed from 0-255 to 0-4095 and apply direction
        speed = speed * 16 * direction
        
        # Constrain speed
        if speed >= 4096:
            speed = 4095
        if speed <= -4096:
            speed = -4095
        
        if index > 4 or index <= 0:
            return
        
        # Calculate PWM channel numbers
        pn = (4 - index) * 2
        pp = (4 - index) * 2 + 1
        
        # Set motor direction and speed
        if speed >= 0:
            self._set_pwm(pp, 0, speed)
            self._set_pwm(pn, 0, 0)
        else:
            self._set_pwm(pp, 0, 0)
            self._set_pwm(pn, 0, -speed)
    
    def stepper_degree_42(self, index, direction, degree):
        """
        Rotate 42BYGH1861A-C stepper motor by degrees
        
        Args:
            index: Stepper controller (Steppers.M1_M2 or Steppers.M3_M4)
            direction: Direction (Direction.CW or Direction.CCW)
            degree: Degrees to rotate
        
        Example:
            driver.stepper_degree_42(Steppers.M1_M2, Direction.CW, 90)
        """
        if degree == 0:
            return
        
        self._set_stepper_42(index, direction > 0)
        degree_abs = abs(degree)
        
        # Timing: 50000 * degree / (360 * 100) ms at 100Hz
        pause_ms = (50000 * degree_abs) // (360 * 100)
        sleep(pause_ms)
        
        # Stop motors
        if index == 1:
            self.motor_stop(Motors.M1)
            self.motor_stop(Motors.M2)
        else:
            self.motor_stop(Motors.M3)
            self.motor_stop(Motors.M4)
    
    def stepper_turn_42(self, index, direction, turns):
        """
        Rotate 42BYGH1861A-C stepper motor by full turns
        
        Args:
            index: Stepper controller (Steppers.M1_M2 or Steppers.M3_M4)
            direction: Direction (Direction.CW or Direction.CCW)
            turns: Number of full rotations
        
        Example:
            driver.stepper_turn_42(Steppers.M1_M2, Direction.CCW, 2)
        """
        if turns == 0:
            return
        degree = turns * 360
        self.stepper_degree_42(index, direction, degree)
    
    def stepper_degree_28(self, index, direction, degree):
        """
        Rotate 28BYJ-48 stepper motor by degrees
        
        Args:
            index: Stepper controller (Steppers.M1_M2 or Steppers.M3_M4)
            direction: Direction (Direction.CW or Direction.CCW)
            degree: Degrees to rotate
        
        Example:
            driver.stepper_degree_28(Steppers.M1_M2, Direction.CW, 180)
        """
        if degree == 0:
            return
        
        degree_abs = abs(degree)
        degree_signed = degree_abs * direction
        
        self._set_stepper_28(index, degree_signed > 0)
        
        # Timing: 1000ms per 360 degrees
        pause_ms = (1000 * degree_abs) // 360
        sleep(pause_ms)
        
        # Stop motors
        if index == 1:
            self.motor_stop(Motors.M1)
            self.motor_stop(Motors.M2)
        else:
            self.motor_stop(Motors.M3)
            self.motor_stop(Motors.M4)
    
    def stepper_turn_28(self, index, direction, turns):
        """
        Rotate 28BYJ-48 stepper motor by full turns
        
        Args:
            index: Stepper controller (Steppers.M1_M2 or Steppers.M3_M4)
            direction: Direction (Direction.CW or Direction.CCW)
            turns: Number of full rotations
        
        Example:
            driver.stepper_turn_28(Steppers.M3_M4, Direction.CW, 1)
        """
        if turns == 0:
            return
        degree = turns * 360
        self.stepper_degree_28(index, direction, degree)
    
    def dual_stepper(self, stepper_type, dir1, deg1, dir2, deg2):
        """
        Control two stepper motors simultaneously
        
        Args:
            stepper_type: Type of stepper (StepperType.STEPPER_42 or StepperType.STEPPER_28)
            dir1: Direction for M1_M2 (Direction.CW or Direction.CCW)
            deg1: Degrees for M1_M2
            dir2: Direction for M3_M4 (Direction.CW or Direction.CCW)
            deg2: Degrees for M3_M4
        
        Example:
            driver.dual_stepper(StepperType.STEPPER_42, Direction.CW, 90, Direction.CCW, 180)
        """
        deg1_abs = abs(deg1)
        deg2_abs = abs(deg2)
        
        if stepper_type == StepperType.STEPPER_42:
            if deg1_abs == 0 and deg2_abs == 0:
                self._set_stepper_42(Steppers.M1_M2, dir1 > 0)
                self._set_stepper_42(Steppers.M3_M4, dir2 > 0)
            elif deg1_abs == 0 and deg2_abs > 0:
                timeout1 = (50000 * deg2_abs) // (360 * 100)
                self._set_stepper_42(Steppers.M1_M2, dir1 > 0)
                self._set_stepper_42(Steppers.M3_M4, dir2 > 0)
                sleep(timeout1)
                self.motor_stop(Motors.M3)
                self.motor_stop(Motors.M4)
            elif deg2_abs == 0 and deg1_abs > 0:
                timeout1 = (50000 * deg1_abs) // (360 * 100)
                self._set_stepper_42(Steppers.M1_M2, dir1 > 0)
                self._set_stepper_42(Steppers.M3_M4, dir2 > 0)
                sleep(timeout1)
                self.motor_stop(Motors.M1)
                self.motor_stop(Motors.M2)
            elif deg2_abs > deg1_abs:
                timeout1 = (50000 * deg1_abs) // (360 * 100)
                timeout2 = (50000 * (deg2_abs - deg1_abs)) // (360 * 100)
                self._set_stepper_42(Steppers.M1_M2, dir1 > 0)
                self._set_stepper_42(Steppers.M3_M4, dir2 > 0)
                sleep(timeout1)
                self.motor_stop(Motors.M1)
                self.motor_stop(Motors.M2)
                sleep(timeout2)
                self.motor_stop(Motors.M3)
                self.motor_stop(Motors.M4)
            else:  # deg1_abs >= deg2_abs
                timeout1 = (50000 * deg2_abs) // (360 * 100)
                timeout2 = (50000 * (deg1_abs - deg2_abs)) // (360 * 100)
                self._set_stepper_42(Steppers.M1_M2, dir1 > 0)
                self._set_stepper_42(Steppers.M3_M4, dir2 > 0)
                sleep(timeout1)
                self.motor_stop(Motors.M3)
                self.motor_stop(Motors.M4)
                sleep(timeout2)
                self.motor_stop(Motors.M1)
                self.motor_stop(Motors.M2)
        
        elif stepper_type == StepperType.STEPPER_28:
            if deg1_abs == 0 and deg2_abs == 0:
                self._set_stepper_28(Steppers.M1_M2, dir1 > 0)
                self._set_stepper_28(Steppers.M3_M4, dir2 > 0)
            elif deg1_abs == 0 and deg2_abs > 0:
                timeout1 = (50000 * deg2_abs) // (360 * 100)
                self._set_stepper_28(Steppers.M1_M2, dir1 > 0)
                self._set_stepper_28(Steppers.M3_M4, dir2 > 0)
                sleep(timeout1)
                self.motor_stop(Motors.M3)
                self.motor_stop(Motors.M4)
            elif deg2_abs == 0 and deg1_abs > 0:
                timeout1 = (50000 * deg1_abs) // (360 * 100)
                self._set_stepper_28(Steppers.M1_M2, dir1 > 0)
                self._set_stepper_28(Steppers.M3_M4, dir2 > 0)
                sleep(timeout1)
                self.motor_stop(Motors.M1)
                self.motor_stop(Motors.M2)
            elif deg2_abs > deg1_abs:
                timeout1 = (50000 * deg1_abs) // (360 * 100)
                timeout2 = (50000 * (deg2_abs - deg1_abs)) // (360 * 100)
                self._set_stepper_28(Steppers.M1_M2, dir1 > 0)
                self._set_stepper_28(Steppers.M3_M4, dir2 > 0)
                sleep(timeout1)
                self.motor_stop(Motors.M1)
                self.motor_stop(Motors.M2)
                sleep(timeout2)
                self.motor_stop(Motors.M3)
                self.motor_stop(Motors.M4)
            else:  # deg1_abs >= deg2_abs
                timeout1 = (50000 * deg2_abs) // (360 * 100)
                timeout2 = (50000 * (deg1_abs - deg2_abs)) // (360 * 100)
                self._set_stepper_28(Steppers.M1_M2, dir1 > 0)
                self._set_stepper_28(Steppers.M3_M4, dir2 > 0)
                sleep(timeout1)
                self.motor_stop(Motors.M3)
                self.motor_stop(Motors.M4)
                sleep(timeout2)
                self.motor_stop(Motors.M1)
                self.motor_stop(Motors.M2)
    
    def motor_stop(self, index):
        """
        Stop a specific DC motor
        
        Args:
            index: Motor number (use Motors.M1 to Motors.M4)
        
        Example:
            driver.motor_stop(Motors.M1)
        """
        self._set_pwm((4 - index) * 2, 0, 0)
        self._set_pwm((4 - index) * 2 + 1, 0, 0)
    
    def motor_stop_all(self):
        """
        Stop all motors (emergency stop)
        
        Example:
            driver.motor_stop_all()
        """
        for idx in range(1, 5):
            self.motor_stop(idx)


# Backward compatibility: Keep old constants at module level
CW = Direction.CW
CCW = Direction.CCW
