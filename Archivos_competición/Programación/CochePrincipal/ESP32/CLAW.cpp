#include "CLAW.h"

const uint32_t CLAW::_EORT_stack  = 2048;
const uint8_t  CLAW::_EORT_priority = 1;
const char* CLAW::_EORT_name = "EORT";

CLAW::CLAW(PCA9685& pca,int compressionChannel, int turnChannel, int endOfRacePin)
: actual(0),
  _compressionChannel(compressionChannel),
  _turnChannel(turnChannel),
  _pca(pca),
  endOfRace(endOfRacePin),
  EORT( EORT_func, this, _EORT_stack, _EORT_priority, _EORT_name ),
  compressed(false)
{
    _stateMutex = xSemaphoreCreateMutex();
    if (_stateMutex == NULL) {
        Serial.println("[CLAW] ERROR: Mutex/Semaphore was not created");
    }
}

CLAW::~CLAW() {
    EORT.stop();
    if (_stateMutex != NULL) {
        vSemaphoreDelete(_stateMutex);
    }
}

void CLAW::begin() {
    EORT.start();
}

void CLAW::compress(int speed) {
    if (_stateMutex == NULL) return;
    xSemaphoreTake(_stateMutex, portMAX_DELAY);
    bool COMPRESSED = compressed;
    xSemaphoreGive(_stateMutex);
    if (COMPRESSED) return; // Already compressed, do nothing
    _pca.setVelocity(_compressionChannel, speed);
}
void CLAW::uncompress(int speed) {
    _pca.setVelocity(_compressionChannel, -speed);
}
void CLAW::stop() {
    _pca.setVelocity(_compressionChannel, 0);
}

void CLAW::turn() {
    if (_stateMutex == NULL) return;
    xSemaphoreTake(_stateMutex, portMAX_DELAY);
    if (actual == 0) { actual = 180; }
    else { actual = 0; }
    int currentActual = actual;
    xSemaphoreGive(_stateMutex);
    _pca.setDegrees(_turnChannel, currentActual);
}

void* CLAW::EORT_func(void* parameter) {
    CLAW* self = static_cast<CLAW*>(parameter);
    if (self->_stateMutex == NULL) return nullptr;
    while (true) {
        bool pressed = self->endOfRace.pressed();
        xSemaphoreTake(self->_stateMutex, portMAX_DELAY);
        self->compressed = pressed;
        xSemaphoreGive(self->_stateMutex);
        vTaskDelay(10 / portTICK_PERIOD_MS);
    }
    return nullptr;
}