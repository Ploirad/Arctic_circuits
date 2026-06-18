#include <Wire.h>

#define I2C_SLAVE_ADDR 0x42
#define I2C_SDA 16
#define I2C_SCL 17

// Led opcional en el pin 2 (muchas placas ESP32 lo tienen incorporado)
#define LED_PIN 2

void setup() {
  Serial.begin(115200);
  Serial.println("Iniciando ESP32 como esclavo I2C...");
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW); // Asegurar led apagado

  // Inicializar I2C como esclavo en pines 16 (SDA) y 17 (SCL) con dirección 0x42
  Wire1.begin(I2C_SLAVE_ADDR, I2C_SDA, I2C_SCL, 100000);
  
  Wire1.onReceive(receiveEvent);
  Wire1.onRequest(requestEvent);

  Serial.println("Esclavo I2C listo. Dirección: 0x42, Pines: SDA=16, SCL=17");
  Serial.println("Esperando datos...");
}

void loop() {
  // Pequeño parpadeo cada 2 segundos para indicar que el ESP32 está vivo
  digitalWrite(LED_PIN, HIGH);
  delay(100);
  digitalWrite(LED_PIN, LOW);
  delay(1900);
}

void receiveEvent(int howMany) {
  // Indicar recepción con el LED
  digitalWrite(LED_PIN, HIGH);
  
  Serial.print("📥 Recibidos ");
  Serial.print(howMany);
  Serial.println(" bytes:");

  int index = 0;
  while (Wire1.available()) {
    byte b = Wire1.read();  // Leer como byte (valor 0-255)
    Serial.print("  Byte[");
    Serial.print(index++);
    Serial.print("] = ");
    Serial.print(b);        // Decimal
    Serial.print(" (0x");
    Serial.print(b, HEX);   // Hexadecimal
    Serial.println(")");
  }
  
  digitalWrite(LED_PIN, LOW);
}

void requestEvent() {
  // Esta función se llama cuando el maestro solicita datos
  // Por ahora solo enviamos un acuse simple
  const char* respuesta = "OK";
  Wire1.write((const uint8_t*)respuesta, 2);
  Serial.println("📤 Solicitud recibida - Enviado 'OK'");
}