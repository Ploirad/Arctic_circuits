from microbit import i2c

class I2C_MASTER:
    def __init__(self, freq=100000):
        """Initialize I2C as master with specified frequency"""
        i2c.init(freq=freq)
    
    def write(self, slave_address, data):
        """
        Send data to an I2C slave device.
        
        Args:
            slave_address: I2C address of the slave device (e.g., 0x42)
            data: List of integers (0-255) or booleans to send
        
        Returns:
            tuple: (success: bool, error: Exception or 0)
        """
        # Convert data to bytearray
        payload = bytearray()
        for item in data:
            if isinstance(item, bool):
                payload.append(1 if item else 0)
            elif isinstance(item, int):
                # Keep only the lowest 8 bits (0-255)
                payload.append(item & 0xFF)
        
        # Send data via I2C
        try:
            i2c.write(slave_address, payload)
            return True, 0
        except Exception as e:
            return False, e
