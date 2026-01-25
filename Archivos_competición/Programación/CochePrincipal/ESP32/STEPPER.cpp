#include "STEPPER.h"
#include <AccelStepper.h>

const long STEPPER::STEPS_PER_REV = 2038;

STEPPER::STEPPER(int IN1, int IN2, int IN3, int IN4, bool halfStep)
 : _stepper(
    halfStep ? AccelStepper::HALF4WIRE : AccelStepper::FULL4WIRE,
    IN1, IN2, IN3, IN4
 ), relativeStepsToStart(0) {
    _stepper.setMaxSpeed(500.0);
    _stepper.setAcceleration(200.0);
}

void STEPPER::setSpeed(float speed) { _stepper.setSpeed(speed); }
void STEPPER::setMaxSpeed(float speed) { _stepper.setMaxSpeed(speed); }
void STEPPER::setAcceleration(float acceleration) { _stepper.setAcceleration(acceleration); }

bool STEPPER::isRunning() { return _stepper.isRunning(); }
void STEPPER::stop() { _stepper.stop(); }

int STEPPER::turnDegrees(int degrees, bool CW) {
    long steps = (degrees * STEPS_PER_REV) / 360L;
    if (!CW) { steps = -steps; }

    _stepper.move(steps);
    _stepper.runToPosition();

    relativeStepsToStart += steps;
    return steps;
}

int STEPPER::moveSteps(int steps, bool CW) {
    if (!CW) { steps = -steps; }

    _stepper.move(steps);
    _stepper.runToPosition();

    relativeStepsToStart += steps;
    return steps;
}

void STEPPER::setAsStartPosition() { relativeStepsToStart = 0; }
void STEPPER::moveToStartPosition() {
    _stepper.move(-relativeStepsToStart);
    _stepper.runToPosition();
    relativeStepsToStart = 0;
}