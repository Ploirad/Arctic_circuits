#include "CLAW.h" 

CLAW garra1(16, 17, 5);

void setup() {
  Serial.begin(115200);
  Serial.println("============= CLAW TEST SYSTEM =============");
}

void loop() {
  if (Serial.available()) {
    char command = Serial.read();
    switch (command) {
      case 'c':
        Serial.println("Compressing");
        garra1.compress(100);
        break;
      case 'u':
        Serial.println("Uncompressing");
        garra1.uncompress(100, 5000);
        break;
      case 't':
        Serial.println("Turning");
        garra1.turn();
        break;
      case 's':
        Serial.println("Stopping");
        garra1.stop();
        break;
      case '\n':
      case '\r':
        break;
      default:
        Serial.println("Unknown command");
        break;
    }
  }
}