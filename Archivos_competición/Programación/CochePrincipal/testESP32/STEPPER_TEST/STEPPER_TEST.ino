#include "STEPPER.h"

STEPPER stepper(18, 33, 19, 32);

void setup() {
    Serial.begin(115200);
    stepper.setSpeed(100.0);
    stepper.setMaxSpeed(1000.0);
    stepper.setAcceleration(200.0);
}

void loop() {
    if (Serial.available()) {
        String command = Serial.readStringUntil('\n');
        command.trim();
        if (command.startsWith("turn ")) {
            int degrees = command.substring(5).toInt();
            stepper.turnDegrees(degrees);
            Serial.println("Turned " + String(degrees) + " degrees.");
        } else if (command.startsWith("move ")) {
            int steps = command.substring(5).toInt();
            stepper.moveSteps(steps);
            Serial.println("Moved " + String(steps) + " steps.");
        } else if (command == "stop") {
            stepper.stop();
            Serial.println("Stepper stopped.");
        } else if (command == "start") {
            stepper.setAsStartPosition();
            Serial.println("Current position set as start.");
        } else if (command == "home") {
            stepper.moveToStartPosition();
            Serial.println("Moved to start position.");
        } else {
            Serial.println("Unknown command: " + command);
        }
    }
}