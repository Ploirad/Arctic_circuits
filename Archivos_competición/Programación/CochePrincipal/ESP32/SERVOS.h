#ifndef SERVOS_h
#define SERVOS_h

#include "Arduino.h"
#include <ESP32Servo.h>

class BasicServo {
    protected:
        Servo servo;
        int pin;
    public:
        BasicServo();
        virtual ~BasicServo();
        void attach(int pin);
};

class Servo360 : public BasicServo {
    public:
        Servo360();
        virtual ~Servo360();
        void run(int speed);
        void stop();
};

class Servo180 : public BasicServo {
    public:
        Servo180();
        virtual ~Servo180();
        void write(int angle);
};

#endif