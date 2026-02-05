from microbit import *
import utime
import machine
import neopixel

# Constantes I2C
PCA9685_ADDRESS = 0x10
MODE1 = 0x00
PRESCALE = 0xFE
LED0_ON_L = 0x06

KC_ADDR = 0x6D
KC_MODE = 1
KC_READCOLOR = 21
KC_READCOLORRAW = 23
KC_LEDPWM = 24
KC_LEDONOFF = 25
KC_LEDBIT = 26
KC_PROXIMITY = 31
KC_GESTURE = 41

RFID_ADDR = 0x6B
RFID_VERSION = 0x00
RFID_READCMD = 0x01
RFID_READOUT = 0x02
RFID_WRITE = 0x03
RFID_STOP = 0x04
RFID_STATUS = 0x05
RFID_UUID = 0x06

COMMAND_I2C_ADDRESS = 0x24
DISPLAY_I2C_ADDRESS = 0x34
_SEG = [0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F, 0x77, 0x7C, 0x39, 0x5E, 0x79, 0x71]

# Enums simulados como clases
class Ports:
    PORT1 = 0
    PORT2 = 1
    PORT3 = 2
    PORT4 = 3
    PORT5 = 4
    PORT6 = 5
    PORT7 = 6

class PortsA:
    PORT1 = 0
    PORT2 = 1
    PORT3 = 2
    PORT5 = 4
    PORT6 = 5
    PORT7 = 6

class SerialPorts:
    PORT1 = 0
    PORT2 = 1
    PORT3 = 2
    PORT4 = 3

class Slots:
    A = 1
    B = 0

class Motors:
    M1 = 0x1
    M2 = 0x2

class Servos:
    S1 = 8
    S2 = 9
    S3 = 10
    S4 = 11
    S5 = 12
    S6 = 13
    S7 = 14
    S8 = 15

class DHT11Type:
    TemperatureC = 0
    TemperatureF = 1
    Humidity = 2

class NeoPixelColors:
    Red = 0xFF0000
    Orange = 0xFFA500
    Yellow = 0xFFFF00
    Green = 0x00FF00
    Blue = 0x0000FF
    Indigo = 0x4b0082
    Violet = 0x8a2be2
    Purple = 0xFF00FF
    White = 0xFFFFFF
    Black = 0x000000

class PowerBrick:
    def __init__(self):
        self.initialized = False
        self._intensity = 3
        self.dbuf = [0, 0, 0, 0]
        self.distanceBuf = 0
        self.rgb_np = None
        self.rgb_pin = None
        self.rgb_bright = 30
        self.RGB_PIX = 64
        self.RGB_M = 8
        self.on_rfid_present = None
        
        # Mapeo de pines (Digi: [PinHigh, PinLow/Info])
        self.PortDigi = [
            (pin8, pin0),   # PORT1
            (pin12, pin1),  # PORT2
            (pin13, pin2),  # PORT3
            (pin15, pin14), # PORT4
            (pin6, pin3),   # PORT5
            (pin7, pin4),   # PORT6
            (pin9, pin10)   # PORT7
        ]
        
        self.PortSerial = [
            (pin8, pin0),
            (pin12, pin1),
            (pin13, pin2),
            (pin15, pin14)
        ]
        
        self.PortAnalog = [
            pin0, pin1, pin2, None, pin3, pin4, pin10
        ]

        self.FontNum = [
            0xff81ff, 0x0000ff, 0x8f89f9, 0xff8989, 0xff080f,
            0xf9898f, 0xf989ff, 0xff0101, 0xff89ff, 0xff898f
        ]

    # --- Funciones I2C Helper ---
    def _i2c_write(self, addr, reg, value):
        i2c.write(addr, bytearray([reg, value]))

    def _i2c_read(self, addr, reg):
        i2c.write(addr, bytearray([reg]))
        return i2c.read(addr, 1)[0]
    
    def _i2c_write_buffer(self, addr, buf):
        i2c.write(addr, buf)

    # --- Inicialización PCA9685 ---
    def init_pca9685(self):
        self._i2c_write(PCA9685_ADDRESS, MODE1, 0x00)
        self.set_freq(50)
        for idx in range(16):
            self.set_pwm(idx, 0, 0)
        self.initialized = True

    def set_freq(self, freq):
        prescaleval = 25000000
        prescaleval /= 4096
        prescaleval /= freq
        prescaleval -= 1
        prescale = int(prescaleval)
        oldmode = self._i2c_read(PCA9685_ADDRESS, MODE1)
        newmode = (oldmode & 0x7F) | 0x10 # sleep
        self._i2c_write(PCA9685_ADDRESS, MODE1, newmode)
        self._i2c_write(PCA9685_ADDRESS, PRESCALE, prescale)
        self._i2c_write(PCA9685_ADDRESS, MODE1, oldmode)
        utime.sleep_us(5000)
        self._i2c_write(PCA9685_ADDRESS, MODE1, oldmode | 0xa1)

    def set_pwm(self, channel, on, off):
        if channel < 0 or channel > 15:
            return
        buf = bytearray(5)
        buf[0] = LED0_ON_L + 4 * channel
        buf[1] = on & 0xff
        buf[2] = (on >> 8) & 0xff
        buf[3] = off & 0xff
        buf[4] = (off >> 8) & 0xff
        self._i2c_write_buffer(PCA9685_ADDRESS, buf)

    # --- DHT11 ---
    def dht11(self, port, readtype):
        """
        Lectura del sensor DHT11. 
        Nota: En Python puro esto puede ser inestable debido a los tiempos estrictos.
        """
        pin = self.PortDigi[port][0]
        buffer = [0] * 40
        data = [0, 0, 0, 0, 0]
        
        # 1. Start signal
        pin.write_digital(0)
        utime.sleep_ms(18)
        
        # 2. Pull up
        pin.set_pull(pin.PULL_UP)
        pin.read_digital() # dummy read
        utime.sleep_us(40)
        
        # 3. Read data
        # Esperar respuesta del sensor (Low ~80us, High ~80us)
        # Nota: Usamos ticks_us para evitar bloqueos infinitos
        timeout = 1000
        start = utime.ticks_us()
        while pin.read_digital() == 0:
            if utime.ticks_diff(utime.ticks_us(), start) > timeout: return 0
            
        start = utime.ticks_us()
        while pin.read_digital() == 1:
             if utime.ticks_diff(utime.ticks_us(), start) > timeout: return 0
             
        # Leer los 40 bits
        for i in range(40):
            start = utime.ticks_us()
            while pin.read_digital() == 0: # Espera inicio bit
                if utime.ticks_diff(utime.ticks_us(), start) > timeout: break
            
            # Medir duración del pulso alto
            t_pulse_start = utime.ticks_us()
            while pin.read_digital() == 1:
                if utime.ticks_diff(utime.ticks_us(), t_pulse_start) > timeout: break
            
            # Si el pulso alto duró más de ~28us, es un 1, si no, es 0
            # 26-28us = '0', 70us = '1'
            if utime.ticks_diff(utime.ticks_us(), t_pulse_start) > 40:
                buffer[i] = 1
        
        # Decodificar
        for i in range(5):
            for j in range(8):
                if buffer[8 * i + j] == 1:
                    data[i] += 2 ** (7 - j)
                    
        dht11Humidity = 0
        dht11Temperature = 0

        # Checksum
        if ((data[0] + data[1] + data[2] + data[3]) & 0xff) == data[4]:
            dht11Humidity = data[0] + data[1] * 0.1
            dht11Temperature = data[2] + data[3] * 0.1
            
        if readtype == DHT11Type.TemperatureC:
            return round(dht11Temperature)
        elif readtype == DHT11Type.TemperatureF:
            return round(dht11Temperature * 1.8 + 32)
        elif readtype == DHT11Type.Humidity:
            return round(dht11Humidity)
        return 0

    # --- Ultrasonidos ---
    def ultrasonic(self, port):
        pin = self.PortDigi[port][0]
        pin.set_pull(pin.PULL_NONE)
        
        # Trigger
        pin.write_digital(0)
        utime.sleep_us(2)
        pin.write_digital(1)
        utime.sleep_us(10)
        pin.write_digital(0)
        
        # Echo
        # Usamos machine.time_pulse_us para medir
        pin.read_digital() # Set to input
        try:
            d = machine.time_pulse_us(pin, 1, 25000)
        except:
            d = 0
            
        if d <= 0 and self.distanceBuf != 0:
            ret = self.distanceBuf
        else:
            ret = d
            self.distanceBuf = d
            
        return int(ret * 10 / 6 / 58) # Cálculo original del TS

    # --- Sensores Analógicos/Digitales Simples ---
    def sound_sensor(self, port):
        pin = self.PortAnalog[port]
        return pin.read_analog()

    def tracer(self, port, slot):
        pin = self.PortDigi[port][slot]
        pin.set_pull(pin.PULL_UP)
        return pin.read_digital() == 1

    def bumper(self, port, slot):
        pin = self.PortDigi[port][slot]
        pin.set_pull(pin.PULL_UP)
        return pin.read_digital() == 0

    def soil(self, port):
        pin = self.PortAnalog[port]
        return pin.read_analog()
    
    def water_level(self, port):
        pin = self.PortAnalog[port]
        return pin.read_analog()

    # --- Infra Temp (I2C) ---
    def infra_temp(self):
        i2c.write(27, bytearray([1]))
        # Nota: read_number con float32 no es estándar en microbit py, aproximamos
        # Asumiendo que devuelve bytes que representan el float
        buf = i2c.read(27, 4) 
        # Aquí necesitaríamos struct.unpack para float exacto, pero devolveremos lectura raw
        # Simplificación: Devolvemos un entero aproximado si el sensor lo permite
        return buf[0] # Esto habría que ajustarlo según la hoja de datos exacta del sensor

    # --- Motores y Servos ---
    def servo(self, index, degree):
        if not self.initialized: self.init_pca9685()
        v_us = ((degree - 90) * 20 / 3 + 1500)
        value = int(v_us * 4096 / 20000)
        self.set_pwm(index, 0, value)

    def servo360(self, index, speed):
        if not self.initialized: self.init_pca9685()
        v_us = (200 / 51) * speed + 1500
        value = int(v_us * 4096 / 20000)
        self.set_pwm(index, 0, value)
        
    def servo2kg(self, index, degree):
        if not self.initialized: self.init_pca9685()
        v_us = (int((degree) * 2000 / 350) + 500)
        value = int(v_us * 4096 / 20000)
        self.set_pwm(index, 0, value)

    def motor_run(self, index, speed):
        if not self.initialized: self.init_pca9685()
        speed = speed * 16
        if speed >= 4096: speed = 4095
        if speed <= -4096: speed = -4095
        
        if index > 2 or index <= 0: return
        
        pp = (index - 1) * 2
        pn = (index - 1) * 2 + 1
        
        if speed >= 0:
            self.set_pwm(pp, 0, speed)
            self.set_pwm(pn, 0, 0)
        else:
            self.set_pwm(pp, 0, 0)
            self.set_pwm(pn, 0, -speed)

    def motor_stop(self, index):
        self.motor_run(index, 0)
        
    def motor_stop_all(self):
        self.motor_run(1, 0)
        self.motor_run(2, 0)

    # --- MP3 ---
    def mp3_connect(self, port):
        # pin0 = PortSerial[port][0] # No usado en UART init directo
        pin1 = self.PortSerial[port][1] # TX del microbit
        pin2 = self.PortSerial[port][0] # RX del microbit
        uart.init(baudrate=9600, tx=pin1, rx=pin2)

    def mp3_play(self, pn):
        buf = bytearray(5)
        buf[0] = 0x7e; buf[1] = 0x03; buf[2] = pn
        buf[3] = buf[1] + buf[2]
        buf[4] = 0xef
        uart.write(buf)
        
    def mp3_volumn(self, vol):
        buf = bytearray(6)
        buf[0] = 0x7e; buf[1] = 0x04; buf[2] = 0xae; buf[3] = vol
        buf[4] = (buf[1] + buf[2] + buf[3]) & 0xff # Simple checksum
        buf[5] = 0xef
        uart.write(buf)

    # --- Segment Display ---
    def seg_cmd(self, c):
        i2c.write(COMMAND_I2C_ADDRESS, bytearray([c]))

    def seg_dat(self, bit, d):
        i2c.write(DISPLAY_I2C_ADDRESS + (bit % 4), bytearray([d]))

    def seg_on(self):
        self.seg_cmd(self._intensity * 16 + 1)

    def seg_off(self):
        self._intensity = 0
        self.seg_cmd(0)

    def seg_digit(self, num, bit):
        val = _SEG[num % 16]
        self.dbuf[bit % 4] = val
        self.seg_dat(bit, val)

    def seg_show_number(self, num):
        if num < 0:
            self.seg_dat(0, 0x40) # '-'
            num = -num
        else:
            self.seg_digit((num // 1000) % 10, 0)
        
        self.seg_digit(num % 10, 3)
        self.seg_digit((num // 10) % 10, 2)
        self.seg_digit((num // 100) % 10, 1)

    # --- RGB (NeoPixel) ---
    def rgb_connect(self, port):
        self.rgb_pin = self.PortDigi[port][0]
        self.rgb_np = neopixel.NeoPixel(self.rgb_pin, self.RGB_PIX)
        self.rgb_clear()

    def rgb_show(self):
        if self.rgb_np:
            self.rgb_np.show()
    
    def rgb_clear(self):
        if self.rgb_np:
            self.rgb_np.clear()
            self.rgb_show()

    def set_pixel_rgb(self, pixel_offset, rgb_int):
        if not self.rgb_np or pixel_offset < 0 or pixel_offset >= self.RGB_PIX:
            return
        
        r = (rgb_int >> 16) & 0xFF
        g = (rgb_int >> 8) & 0xFF
        b = rgb_int & 0xFF
        
        # Aplicar brillo
        if self.rgb_bright < 255:
            r = (r * self.rgb_bright) >> 8
            g = (g * self.rgb_bright) >> 8
            b = (b * self.rgb_bright) >> 8
            
        self.rgb_np[pixel_offset] = (r, g, b)

    def show_color(self, rgb_int):
        if not self.rgb_np: return
        for i in range(self.RGB_PIX):
            self.set_pixel_rgb(i, rgb_int)
        self.rgb_show()

    # --- RFID ---
    def rfid_read_sector(self, sector, block):
        retry = 5
        buf = bytearray([RFID_READCMD, sector, block])
        i2c.write(RFID_ADDR, buf)
        
        while retry > 0:
            utime.sleep_ms(100)
            stat = self._i2c_read(RFID_ADDR, RFID_STATUS)
            if stat == 3: # READ_SUCC
                i2c.write(RFID_ADDR, bytearray([RFID_READOUT]))
                rxbuf = i2c.read(RFID_ADDR, 16)
                ret = ""
                for b in rxbuf:
                    if 0x20 <= b < 0x7f:
                        ret += chr(b)
                return ret
            retry -= 1
        return ""

    def rfid_uuid(self):
        i2c.write(RFID_ADDR, bytearray([RFID_UUID]))
        uuid = i2c.read(RFID_ADDR, 4)
        # Reverse and hex
        return "{:02x}{:02x}{:02x}{:02x}".format(uuid[3], uuid[2], uuid[1], uuid[0])

# Instancia global para facilitar uso si se desea (opcional)
# pb = PowerBrick()