#include "L298N.h"

L298N::L298N(int in1, int in2, int in3, int in4)
: running(false),
IN1(in1), IN2(in2), IN3(in3), IN4(in4)
{
    pinMode(IN1, OUTPUT);
    pinMode(IN2, OUTPUT);
    pinMode(IN3, OUTPUT);
    pinMode(IN4, OUTPUT);
}

bool L298N::isRunning() { return running; }
void L298N::stop() {
    if (running) {
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, LOW);
        digitalWrite(IN3, LOW);
        digitalWrite(IN4, LOW);
        running = false;
    }
}

void L298N::runContinuous(bool CW) {
    if (CW) {
        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);
        digitalWrite(IN3, HIGH);
        digitalWrite(IN4, LOW);
    } else {
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, HIGH);
        digitalWrite(IN3, LOW);
        digitalWrite(IN4, HIGH);
    }
    running = true;
}