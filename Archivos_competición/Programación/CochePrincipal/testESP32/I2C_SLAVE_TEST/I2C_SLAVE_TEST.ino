#include "I2C_SLAVE.h"

I2C_SLAVE slave(0x42, 16, 17);

void setup() {
  Serial.begin(115200);
  Serial.println("Esclavo I2C listo");
}

void loop() {
  if (slave.isDataAvailable()) {
    uint8_t len;
    uint8_t* data = slave.getData(len);
    
    Serial.print("Datos recibidos ("); 
    Serial.print(len);
    Serial.print(" bytes): ");
    
    for (uint8_t i = 0; i < len; i++) {
      Serial.print("0x");
      Serial.print(data[i], HEX);
      Serial.print(" ");
    }
    Serial.println();
  } else {
    // Solo imprime "None" cada medio segundo para no saturar
    static unsigned long lastPrint = 0;
    if (millis() - lastPrint > 500) {
      Serial.println("None");
      lastPrint = millis();
    }
  }
  
  delay(10); // Pequeña pausa para evitar rebote del watchdog
}