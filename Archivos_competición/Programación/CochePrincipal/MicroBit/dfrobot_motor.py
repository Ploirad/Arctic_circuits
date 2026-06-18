"""
DFRobot Motor Driver for micro:bit (MicroPython)

This module provides control for the DFRobot motor expansion board using the PCA9685 PWM controller.
Supports:
- 8 servo channels (S1-S8): 0° to 180°
- 4 DC motors (M1-M4): Speed 0-255, bidirectional (CW/CCW)

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
