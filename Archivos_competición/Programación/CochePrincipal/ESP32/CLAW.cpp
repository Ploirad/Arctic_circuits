#include "CLAW.h"

const uint32_t CLAW::_EORT_stack  = 2048;
const uint8_t  CLAW::_EORT_priority = 1;
const char* CLAW::_EORT_name = "EORT";

const uint32_t CLAW::_CompThread_stack = 4096;
const uint8_t CLAW::_CompThread_priority = 2;
const char* CLAW::_CompThread_name = "CompThread";

CLAW::CLAW(PCA9685& pca,int compressionChannel, int turnChannel, int endOfRacePin)
: actual(0),
  _compressionChannel(compressionChannel),
  _turnChannel(turnChannel),
  _pca(pca),
  endOfRace(endOfRacePin),
  EORT( EORT_func, this, _EORT_stack, _EORT_priority, _EORT_name ),
  CompThread( CompThread_func, this, _CompThread_stack, _CompThread_priority, _CompThread_name ),
  uncompressionTime(0),
  compressing(0),
  compressingSpeed(0),
  compressed(false)
{
    _stateMutex = xSemaphoreCreateMutex();
    _compSemaphore = xSemaphoreCreateBinary();
    if (_stateMutex == NULL || _compSemaphore == NULL) {
        Serial.println("[CLAW] ERROR: Mutex/Semaphore was not created");
    }
    EORT.start();
    CompThread.start();
}

CLAW::~CLAW() {
    EORT.stop();
    CompThread.stop();
    if (_stateMutex != NULL) {
        vSemaphoreDelete(_stateMutex);
    }
    if (_compSemaphore != NULL) {
        vSemaphoreDelete(_compSemaphore);
    }
}

void CLAW::compress(int speed) {
    if (_stateMutex == NULL) return;
    xSemaphoreTake(_stateMutex, portMAX_DELAY);
    if (!compressed) {
        compressing = 1;
        compressingSpeed = speed;
        xSemaphoreGive(_stateMutex);
        if (_compSemaphore != NULL) {
            while (xSemaphoreTake(_compSemaphore, 0) == pdTRUE) {}
            xSemaphoreGive(_compSemaphore);
        }
    } else {
        xSemaphoreGive(_stateMutex);
    }
}
void CLAW::uncompress(int speed, int time) {
    if (_stateMutex == NULL) return;
    xSemaphoreTake(_stateMutex, portMAX_DELAY);
    if (compressed) {
        compressing = -1;
        compressingSpeed = speed;
        uncompressionTime = time;
        xSemaphoreGive(_stateMutex);
        
        if (_compSemaphore != NULL) {
            while (xSemaphoreTake(_compSemaphore, 0) == pdTRUE) {}
            xSemaphoreGive(_compSemaphore);
        }
    } else {
        xSemaphoreGive(_stateMutex);
    }
}
void CLAW::stop() {
    if (_stateMutex == NULL) return;
    xSemaphoreTake(_stateMutex, portMAX_DELAY);
    compressing = 0;
    compressingSpeed = 0;
    xSemaphoreGive(_stateMutex);
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
void* CLAW::CompThread_func(void* parameter) {
    CLAW* self = static_cast<CLAW*>(parameter);
    if (self->_stateMutex == NULL || self->_compSemaphore == NULL) return nullptr;

    while (true) {
        xSemaphoreTake(self->_compSemaphore, portMAX_DELAY);
        xSemaphoreTake(self->_stateMutex, portMAX_DELAY);
        int8_t currentState = self->compressing;
        int8_t speed = self->compressingSpeed;
        bool compressed = self->compressed;
        int16_t uncompressionTime = self->uncompressionTime;
        xSemaphoreGive(self->_stateMutex);

        if (currentState == 1) {
            self->_pca.setVelocity(self->_compressionChannel, speed);
            uint32_t startTime = millis();
            while (!compressed && (millis() - startTime < 15000)) {
                vTaskDelay(50 / portTICK_PERIOD_MS);
                xSemaphoreTake(self->_stateMutex, portMAX_DELAY);
                compressed = self->compressed;
                xSemaphoreGive(self->_stateMutex);
            }
            self->_pca.setVelocity(self->_compressionChannel, 0);

            xSemaphoreTake(self->_stateMutex, portMAX_DELAY);
            self->compressing = 0;
            xSemaphoreGive(self->_stateMutex);
        } else if (currentState == -1) {
            self->_pca.setVelocity(self->_compressionChannel, -speed);

            uint32_t startTime = millis();
            while (compressed) {
                vTaskDelay(50/portTICK_PERIOD_MS);
                xSemaphoreTake(self->_stateMutex, portMAX_DELAY);
                compressed = self->compressed;
                xSemaphoreGive(self->_stateMutex);
            }

            while (millis() - startTime < uncompressionTime) {
                vTaskDelay(50 / portTICK_PERIOD_MS);
            }
            self->_pca.setVelocity(self->_compressionChannel, 0);
            xSemaphoreTake(self->_stateMutex, portMAX_DELAY);
            self->compressing = 0;
            xSemaphoreGive(self->_stateMutex);
        }
        xSemaphoreGive(self->_compSemaphore);
        vTaskDelay(10/portTICK_PERIOD_MS);
    }
    return nullptr;
}