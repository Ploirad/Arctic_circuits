from microbit import *
import utime
WUKONG_ADDR = 0x10
class WUKONG(object):
    def __init__(self):
        i2c.init()

    def set_motors(self, motor, speed):
        if speed < 0:
            i2c.write(WUKONG_ADDR, bytearray([motor, 0x02, speed * -1, 0]))
        else:
            i2c.write(WUKONG_ADDR, bytearray([motor, 0x01, speed, 0]))

    def set_servo(self, servo, angle):
        if servo == 7:
            i2c.write(WUKONG_ADDR, bytearray([0x10, angle, 0, 0]))
        else:
            i2c.write(WUKONG_ADDR, bytearray([servo + 3, angle, 0, 0]))

    def set_light(self, light):
        i2c.write(WUKONG_ADDR, bytearray([0x12, light, 0, 0]))
        sleep(100)
        i2c.write(WUKONG_ADDR, bytearray([0x11, 160, 0, 0]))

    def set_light_breath(self, br: bool):
        if br:
            i2c.write(WUKONG_ADDR, bytearray([0x11, 0, 0, 0]))
            sleep(100)
            i2c.write(WUKONG_ADDR, bytearray([0x12, 150, 0, 0]))
        else:
            i2c.write(WUKONG_ADDR, bytearray([0x12, 0, 0, 0]))
            sleep(100)
            i2c.write(WUKONG_ADDR, bytearray([0x11, 160, 0, 0]))

    def read_sonar(self, pin, unit='cm'):
        if unit not in ['mm', 'cm', 'inch']:
            raise ValueError("unit error, use 'mm', 'cm', or 'inch'")

        # 1. Emitir el pulso (Trigger)
        pin.write_digital(0)
        utime.sleep_us(2)
        pin.write_digital(1)
        utime.sleep_us(10)
        pin.write_digital(0)
        
        # 2. Cambiar a modo lectura (Input)
        # Hacemos un read dummy para asegurar que el pin escuche
        pin.read_digital()
        timeout = 30000 # 30ms de tiempo máximo de espera
        start_wait = utime.ticks_us()
        
        # Bucle 1: Esperar a que llegue la señal (pin suba a 1)
        while pin.read_digital() == 0:
            if utime.ticks_diff(utime.ticks_us(), start_wait) > timeout:
                return 0 # Timeout: El sensor no responde o no está conectado
        
        # ¡Señal recibida! Marcamos el tiempo de inicio
        pulse_start = utime.ticks_us()
        
        # Bucle 2: Esperar a que termine la señal (pin baje a 0)
        while pin.read_digital() == 1:
            if utime.ticks_diff(utime.ticks_us(), pulse_start) > timeout:
                return 0 # Timeout: Objeto demasiado lejos
                
        # ¡Señal terminada! Marcamos el tiempo final
        pulse_end = utime.ticks_us()
        
        # La duración es la resta del final menos el inicio
        duration = utime.ticks_diff(pulse_end, pulse_start)
        distance_cm = duration / 58

        # Si la distancia es mayor a 400cm o duration es 0, considerar que no hay objeto
        if distance_cm > 400 or duration == 0:
            return 0

        # Convertir a la unidad solicitada
        if unit == 'mm':
            return int(distance_cm * 10)
        elif unit == 'cm':
            return int(distance_cm)
        elif unit == 'inch':
            return int(distance_cm / 2.54)
