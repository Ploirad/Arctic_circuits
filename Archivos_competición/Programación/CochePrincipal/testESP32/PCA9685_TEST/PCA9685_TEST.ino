#include "PCA9685.h"

PCA9685 servos(0x40);

void setup() {
  Serial.begin(115200);
  Serial.println("PCA TESTER");
  servos.begin();
}

void loop() {
  for (int angle = 0; angle < 180; angle++) {
    Serial.print("Servo 1: ");
    Serial.println(angle);
    servos.setDegrees(0, angle);
  }
  for (int vel = 0; vel < 100; vel++) {
    for (int i=4; i<8; i++) {
      Serial.print("Servo "); Serial.print(i); Serial.print(": ");
      Serial.println(vel);
      servos.setVelocity(i, vel);
    }
  }
  delay(1000);
  for (int angle = 180; angle > 0; angle--) {
    Serial.print("Servo 1:");
    Serial.println(angle);
    servos.setDegrees(0, angle);
  }
  for (int vel = 100; vel > 0; vel--) {
    for (int i=4; i<8; i++) {
      Serial.print("Servo "); Serial.print(i); Serial.print(": ");
      Serial.println(vel);
      servos.setVelocity(i, vel);
    }
  }

  delay(1000);
}