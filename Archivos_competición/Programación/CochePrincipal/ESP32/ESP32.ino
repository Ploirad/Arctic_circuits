#include "I2C_SLAVE.h"

const uint8_t ESP32_I2C_ADDRESS = 0x42;
I2C_SLAVE MicroBit(ESP32_I2C_ADDRESS);

void setup() {
  // Serial for debugging
  Serial.begin(115200);
  Serial.println("ESP32 I2C Slave ready");
  MicroBit.begin();
}

void loop() {
  if (MicroBit.isDataAvailable()) {
    uint8_t* data = MicroBit.getData();
    size_t size = MicroBit.getDataSize();
    Serial.print("Received data: ");
    for (size_t i = 0; i < size; i++) {
      Serial.print(data[i]);
      Serial.print(" ");
    }
    Serial.println();
  }
}
