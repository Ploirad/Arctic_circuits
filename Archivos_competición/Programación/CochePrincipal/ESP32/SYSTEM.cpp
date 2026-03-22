#include "SYSTEM.h"

const uint32_t SYSTEM::_stepperThread_stack = 2048;
const uint8_t SYSTEM::_stepperThread_priority = 1;
const char* SYSTEM::_stepperThread_name = "StepperThread";

SYSTEM::SYSTEM(int compressionChannel1, int turnChannel1, int endOfRacePin1,
            int compressionChannel2, int turnChannel2, int endOfRacePin2,
            int compressionChannel3, int turnChannel3, int endOfRacePin3,
            int compressionChannel4, int turnChannel4, int endOfRacePin4,
            uint8_t pcaAddress,
            int IN1, int IN2, int IN3, int IN4)
: principalStepper(IN1, IN2, IN3, IN4),
pca(pcaAddress),
claws{
    CLAW(pca, compressionChannel1, turnChannel1, endOfRacePin1),
    CLAW(pca, compressionChannel2, turnChannel2, endOfRacePin2),
    CLAW(pca, compressionChannel3, turnChannel3, endOfRacePin3),
    CLAW(pca, compressionChannel4, turnChannel4, endOfRacePin4)
}, compressionSpeed(150), CW(false), move(false),
stepperSpeed(300.0), stepperMaxSpeed(600.0), stepperAcceleration(200.0),
stepperThread(stepperThreadFunc, this, _stepperThread_stack, _stepperThread_priority, _stepperThread_name)
{
    _stepperMutex = xSemaphoreCreateMutex();
    if (_stepperMutex == NULL) {
        Serial.println("[SYSTEM] ERROR: Mutex/Semaphore was not created");
    }

    principalStepper.setMaxSpeed(stepperMaxSpeed); // STEPS PER SECOND (steps/s)
    principalStepper.setAcceleration(stepperAcceleration); // STEPS PER SECOND SQUARED (steps/s^2)
    principalStepper.stop();
    principalStepper.setAsStartPosition();
}

// Añadir destructor en SYSTEM.h y aquí:
SYSTEM::~SYSTEM() {
    stepperThread.stop();
    if (_stepperMutex != NULL) {
        vSemaphoreDelete(_stepperMutex);
    }
}

// ========================
//          PUBLICS
// ========================

void SYSTEM::begin() {
    pca.begin();
    for (int i = 0; i<4; i++){
        claws[i].begin();
    }
    stepperThread.start();
}

void SYSTEM::turnClaw(int clawIndex) {
    if (clawIndex < 0 || clawIndex > 3) return;
    claws[clawIndex].turn();
}
void SYSTEM::compressClaws() {
    for (int i=0; i<4; i++) {
        claws[i].compress(compressionSpeed);
    }
}
void SYSTEM::uncompressClaws() {
    for (int i=0; i<4; i++) {
        claws[i].uncompress(compressionSpeed);
    }
}
void SYSTEM::stopClaws() {
    for (int i=0; i<4; i++) {
        claws[i].stop();
    }
}
void SYSTEM::moveStepper(bool cw) {
    if (_stepperMutex == NULL) return;
    xSemaphoreTake(_stepperMutex, portMAX_DELAY);
    CW = cw;
    move = true;
    xSemaphoreGive(_stepperMutex);
}
void SYSTEM::stopStepper() {
    if (_stepperMutex == NULL) return;
    xSemaphoreTake(_stepperMutex, portMAX_DELAY);
    move = false;
    xSemaphoreGive(_stepperMutex);
    principalStepper.stop();
}

void SYSTEM::setCompressionSpeed(int speed) {
    if (speed < -100) speed = -100;
    if (speed > 100) speed = 100;
    compressionSpeed = speed;
}
void SYSTEM::setStepperSpeed(float speed) {
    if (speed < 0) speed = 0;
    stepperSpeed = speed;
}
void SYSTEM::setStepperMaxSpeed(float maxSpeed) {
    if (maxSpeed < 0) maxSpeed = 0;
    stepperMaxSpeed = maxSpeed;
    principalStepper.setMaxSpeed(stepperMaxSpeed);
}
void SYSTEM::setStepperAcceleration(float acceleration) {
    if (acceleration < 0) acceleration = 0;
    stepperAcceleration = acceleration;
    principalStepper.setAcceleration(stepperAcceleration);
}

void SYSTEM::emergencyStop() {
    // Detener las garras
    stopClaws();

    // Detener el motor paso a paso
    if (_stepperMutex == NULL) return;
    xSemaphoreTake(_stepperMutex, portMAX_DELAY);
    move = false;
    xSemaphoreGive(_stepperMutex);
    principalStepper.stop();
}

void* SYSTEM::stepperThreadFunc(void* parameter) {
    SYSTEM* self = static_cast<SYSTEM*>(parameter);
    if (self->_stepperMutex == NULL) return nullptr;
    while (true) {
        xSemaphoreTake(self->_stepperMutex, portMAX_DELAY);
        bool _shouldMove = self->move;
        bool _CW = self->CW;
        float _speed = self->stepperSpeed;
        xSemaphoreGive(self->_stepperMutex);
        if (_shouldMove) {
            // Aplicar dirección a la velocidad
            float currentSpeed = _CW ? _speed : -_speed;
            self->principalStepper.setSpeed(currentSpeed);
            self->principalStepper.runContinuous();  // genera pasos si es momento
        } else {
            self->principalStepper.stop();
        }

        vTaskDelay(pdMS_TO_TICKS(1));  // Pequeño retardo para no saturar la CPU
    }
    return nullptr;
}