#include "SYSTEM.h"

const uint32_t SYSTEM::_l298nThread_stack = 2048;
const uint8_t SYSTEM::_l298nThread_priority = 1;
const char* SYSTEM::_l298nThread_name = "l298nThread";

SYSTEM::SYSTEM(int compressionChannel1, int turnChannel1, int endOfRacePin1,
            int compressionChannel2, int turnChannel2, int endOfRacePin2,
            int compressionChannel3, int turnChannel3, int endOfRacePin3,
            int compressionChannel4, int turnChannel4, int endOfRacePin4,
            uint8_t pcaAddress,
            int IN1, int IN2, int IN3, int IN4)
: motors(IN1, IN2, IN3, IN4),
pca(pcaAddress),
claws{
    CLAW(pca, compressionChannel1, turnChannel1, endOfRacePin1),
    CLAW(pca, compressionChannel2, turnChannel2, endOfRacePin2),
    CLAW(pca, compressionChannel3, turnChannel3, endOfRacePin3),
    CLAW(pca, compressionChannel4, turnChannel4, endOfRacePin4)
}, compressionSpeed(150), CW(false), move(false),
l298nThread(l298nThreadFunc, this, _l298nThread_stack, _l298nThread_priority, _l298nThread_name)
{
    _l298nMutex = xSemaphoreCreateMutex();
    if (_l298nMutex == NULL) {
        Serial.println("[SYSTEM] ERROR: Mutex/Semaphore was not created");
    }

    motors.stop();
}

// Añadir destructor en SYSTEM.h y aquí:
SYSTEM::~SYSTEM() {
    l298nThread.stop();
    if (_l298nMutex != NULL) {
        vSemaphoreDelete(_l298nMutex);
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
    l298nThread.start();
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
void SYSTEM::moveL298N(bool cw) {
    if (_l298nMutex == NULL) return;
    xSemaphoreTake(_l298nMutex, portMAX_DELAY);
    CW = cw;
    move = true;
    xSemaphoreGive(_l298nMutex);
}
void SYSTEM::stopL298N() {
    if (_l298nMutex == NULL) return;
    xSemaphoreTake(_l298nMutex, portMAX_DELAY);
    move = false;
    xSemaphoreGive(_l298nMutex);
    motors.stop();
}

void SYSTEM::setCompressionSpeed(int speed) {
    if (speed < -100) speed = -100;
    if (speed > 100) speed = 100;
    compressionSpeed = speed;
}

void SYSTEM::emergencyStop() {
    // Detener las garras
    stopClaws();

    // Detener el motor paso a paso
    if (_l298nMutex == NULL) return;
    xSemaphoreTake(_l298nMutex, portMAX_DELAY);
    move = false;
    xSemaphoreGive(_l298nMutex);
    motors.stop();
}

void* SYSTEM::l298nThreadFunc(void* parameter) {
    SYSTEM* self = static_cast<SYSTEM*>(parameter);
    if (self->_l298nMutex == NULL) return nullptr;
    while (true) {
        xSemaphoreTake(self->_l298nMutex, portMAX_DELAY);
        bool _shouldMove = self->move;
        bool _CW = self->CW;
        xSemaphoreGive(self->_l298nMutex);
        if (_shouldMove) {
            // Aplicar dirección a la velocidad
            self->motors.runContinuous(_CW);  // genera pasos si es momento
        } else {
            self->motors.stop();
        }

        vTaskDelay(pdMS_TO_TICKS(1));  // Pequeño retardo para no saturar la CPU
    }
    return nullptr;
}