"""
Button.py - Librería simple para botones Microbit
Compatible con: button_a, button_b, pin0-pin19
"""
from microbit import *
import utime

class Button:
    """
    Clase wrapper para botones Microbit (A, B o pines digitales).
    
    Uso:
    btn = Button(button_a)      # Botón A
    btn = Button(button_b)      # Botón B  
    btn = Button(pin0)          # Pin digital 0
    btn = Button(16)            # Pin 16
    
    Métodos:
    - is_pressed() → True si presionado
    - was_pressed() → True si acaba de presionarse (edge)
    - is_held(duration_ms=1000) → True si mantenido X ms
    """
    
    def __init__(self, pin):
        """
        Inicializa botón.
        pin_or_button: button_a, button_b o Pin
        """
        self._pin = pin
        self._last_state = self._read_raw()
        self._last_press_time = 0
        
    def _read_raw(self):
        """Lee estado raw del pin (0=LIBRE, 1=PRESIONADO)."""
        return self._pin.read_digital()
    
    def is_pressed(self):
        """True si botón está presionado AHORA."""
        return self._read_raw() == 1
    
    def was_pressed(self):
        """
        True si botón ACABA de presionarse (flanco descendente).
        Útil para detectar pulsaciones únicas.
        """
        current = self._read_raw()
        pressed_now = (current == 1)
        was_released = (self._last_state == 0)
        
        self._last_state = current
        return pressed_now and was_released
    
    def is_held(self, duration_ms=1000):
        """
        True si botón está mantenido durante duration_ms.
        """
        current = self._read_raw()
        if current == 1:
            now = utime.ticks_ms()
            if utime.ticks_diff(now, self._last_press_time) >= duration_ms:
                return True
        else:
            self._last_press_time = utime.ticks_ms()
        return False
    
    def wait_for_press(self, timeout_ms=5000):
        """
        Espera a que se pulse el botón (bloqueante).
        timeout_ms: tiempo máximo de espera (default 5s)
        Retorna True si pulsado, False si timeout.
        """
        start = utime.ticks_ms()
        while utime.ticks_diff(utime.ticks_ms(), start) < timeout_ms:
            if self.was_pressed():
                return True
            sleep(10)
        return False
    
    @property
    def pin_number(self):
        """Número del pin (útil para debug)."""
        try:
            return int(str(self._pin)[-2:])
        except:
            return -1  # button_a/b
    
    def __repr__(self):
        state = "PRESSED" if self.is_pressed() else "RELEASED"
        return f"Button(pin{self.pin_number}: {state})"


# Ejemplos de uso (descomenta para test)
if __name__ == "__main__":
    print("=== Button Test ===")
    
    # Test botones A/B
    btn_a = Button(button_a)
    btn_b = Button(button_b)
    btn_p0 = Button(pin0)
    
    print("Presiona A, B o pin0 para test...")
    
    while True:
        if btn_a.was_pressed():
            print("¡A pulsado!")
        if btn_b.is_pressed():
            print("B presionado")
        if btn_p0.is_held(2000):
            print("pin0 mantenido 2s!")
        
        sleep(100)