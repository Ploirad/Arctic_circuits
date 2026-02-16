#ifndef STEPPER_h
#define STEPPER_h

#include "Arduino.h"
#include <AccelStepper.h>

class STEPPER {
    public:
        STEPPER(int IN1, int IN2, int IN3, int IN4);
        void setMaxSpeed(float speed);
        void setAcceleration(float acceleration);
        void setSpeed(float speed);
        int turnDegrees(int degrees, bool CW = true);
        int moveSteps(int steps, bool CW = true);
        bool isRunning();
        void stop();
        void setAsStartPosition();
        void moveToStartPosition();

    private:
        AccelStepper _stepper;
        long relativeStepsToStart;
        static const long STEPS_PER_REV;
};

#endif