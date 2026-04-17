from microbit import *
import utime

class Button:
    def __init__(self, pin):
        self._pin = pin
        self._last_state = self._read_raw()
        self._last_press_time = 0
        
    def _read_raw(self):
        if self._pin == button_a or self._pin == button_b:
            return 1 if self._pin.is_pressed() else 0
        return self._pin.read_digital()
    
    def is_pressed(self):
        return self._read_raw() == 1
    
    def was_pressed(self):
        current = self._read_raw()
        pressed_now = (current == 1)
        was_released = (self._last_state == 0)
        
        self._last_state = current
        return pressed_now and was_released
    
    def is_held(self, duration_ms=1000):
        current = self._read_raw()
        if current == 1:
            now = utime.ticks_ms()
            if utime.ticks_diff(now, self._last_press_time) >= duration_ms:
                return True
        else:
            self._last_press_time = utime.ticks_ms()
        return False
    
    def wait_for_press(self, timeout_ms=5000):
        start = utime.ticks_ms()
        while utime.ticks_diff(utime.ticks_ms(), start) < timeout_ms:
            if self.was_pressed():
                return True
            sleep(10)
        return False
    
    @property
    def pin_number(self):
        try:
            return int(str(self._pin)[-2:])
        except:
            return -1  # button_a/b
    
    def __repr__(self):
        state = "PRESSED" if self.is_pressed() else "RELEASED"
        return "Button({}: {})".format(self._pin, state)
