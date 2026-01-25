#include "SERVOS.h"

BasicServo::BasicServo() : pin(-1) {}
BasicServo::~BasicServo() {}
void BasicServo::attach(int pin) {
    servo.attach(pin);
}

Servo360::Servo360() {}
Servo360::~Servo360() {}
void Servo360::stop() { servo.writeMicroseconds(1500); }
void Servo360::run(int speed) {
    if (speed < -100) speed = -100;
    if (speed > 100) speed = 100;
    int pulseWidth = map(speed, -100, 100, 1000, 2000);
    servo.writeMicroseconds(pulseWidth);
}

Servo180::Servo180() {}
Servo180::~Servo180() {}
void Servo180::write(int angle) {
    if (angle < 0) angle = 0;
    if (angle > 180) angle = 180;
    servo.write(angle);
}
