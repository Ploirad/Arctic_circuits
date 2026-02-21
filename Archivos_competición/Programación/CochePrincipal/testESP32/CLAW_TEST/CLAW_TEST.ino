#include "CLAW.h"
#include "PCA9685.h"

PCA9685 pca(0x40);
CLAW claw(pca, 0, 4, 4);

void setup() {
  Serial.begin(115200);
  Serial.println("CLAW TESTER");
  pca.begin();
  Serial.println("ACTIONS:");
  Serial.println("C 50 means compress at speed 50");
  Serial.println("U 50 2000 means uncompress at speed 50 for 2000 ms");
  Serial.println("T means turn");
  Serial.println("S means stop");
}

void loop() {
    if (Serial.available() > 0) {
        String input = Serial.readStringUntil('\n');
        input.trim();
        if (input.length() == 0) return;
    
        char command = input.charAt(0);
        if (command == 'C') {
        int speed = input.substring(1).toInt();
        claw.compress(speed);
        Serial.println("Compressing at speed " + String(speed));
        } else if (command == 'U') {
        int spaceIndex = input.indexOf(' ', 1);
        if (spaceIndex != -1) {
            int speed = input.substring(1, spaceIndex).toInt();
            int time = input.substring(spaceIndex + 1).toInt();
            claw.uncompress(speed, time);
            Serial.println("Uncompressing at speed " + String(speed) + " for " + String(time) + " ms");
        }
        } else if (command == 'T') {
        claw.turn();
        Serial.println("Turning");
        } else if (command == 'S') {
        claw.stop();
        Serial.println("Stopped");
        }
    }
}