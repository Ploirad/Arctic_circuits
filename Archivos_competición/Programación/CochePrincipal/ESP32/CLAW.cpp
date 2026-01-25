#include "CLAW.h"

const uint32_t CLAW::_EORT_stack  = 4096;
const uint8_t  CLAW::_EORT_priority = 1;
const char* CLAW::_EORT_name = "EORT";

const uint32_t CLAW::_CompThread_stack = 4096;
const uint8_t CLAW::_CompThread_priority = 1;
const char* CLAW::_CompThread_name = "CompThread";

CLAW::CLAW(int compressionPin, int turnPin, int endOfRacePin)
: actual(0),
  endOfRace(endOfRacePin),
  EORT( EORT_func, this, _EORT_stack, _EORT_priority, _EORT_name ),
  CompThread( CompThread_func, this, _CompThread_stack, _CompThread_priority, _CompThread_name ),
  uncompressionTime(0),
  compressing(0),
  compressingSpeed(0),
  compressed(false)
{
    compressionServo.attach(compressionPin);
    turnServo.attach(turnPin);
    EORT.start();
    CompThread.start();
    CompThread.pause();
}

CLAW::~CLAW() {
    EORT.stop();
    CompThread.stop();
}

void CLAW::compress(int speed) {
    if (!compressed) {
        compressing = 1;
        compressingSpeed = speed;
        if (CompThread.status() == ThreadState::SLEEPING) CompThread.resume();
    }
}
void CLAW::uncompress(int speed, int time) {
    if (compressed) {
        if (CompThread.status() == ThreadState::ALIVE) {
            CompThread.pause();
            delay(50);
        }
        
        compressing = -1;
        compressingSpeed = speed;
        uncompressionTime = time;
        
        if (CompThread.status() == ThreadState::SLEEPING) {
            CompThread.resume();
        }
    }
}
void CLAW::stop() {
    compressing = 0;
    compressingSpeed = 0;
    CompThread.pause();
    compressionServo.stop();
}

void CLAW::turn() {
    if (actual == 0) { actual = 180; }
    else { actual = 0; }
    turnServo.write(actual);
}

void* CLAW::EORT_func(void* parameter) {
    CLAW* self = static_cast<CLAW*>(parameter);
    while (true) {
        self->compressed = self->endOfRace.pressed();
        vTaskDelay(10 / portTICK_PERIOD_MS);
    }
    return nullptr;
}
void* CLAW::CompThread_func(void* parameter) {
    CLAW* self = static_cast<CLAW*>(parameter);
    while (true) {
        if (self->compressing == 1 && !self->compressed) {
            self->compressionServo.run(self->compressingSpeed);
        } 
        else if (self->compressing == 1 && self->compressed) {
            self->compressionServo.stop();
            self->compressing = 0;
            self->compressingSpeed = 0;
            self->CompThread.pause();
        } 
        else if (self->compressing == -1) {
            if (self->compressed) {
                while (self->compressed) {
                    self->compressionServo.run(-self->compressingSpeed);
                    vTaskDelay(20 / portTICK_PERIOD_MS);
                }
            }
            if (self->uncompressionTime > 0) {
                unsigned long start = millis();
                while (millis() - start < self->uncompressionTime) {
                    self->compressionServo.run(-self->compressingSpeed);
                    vTaskDelay(20 / portTICK_PERIOD_MS);
                }
            }
            self->compressionServo.stop();
            self->compressing = 0;
            self->compressingSpeed = 0;
            self->uncompressionTime = 0;
            self->CompThread.pause();
        } 
        else if (self->compressing == 0) {
            self->compressionServo.stop();
            self->CompThread.pause();
            vTaskSuspend(nullptr);
        } 
        else {
            self->compressionServo.stop();
            self->compressing = 0;
            self->CompThread.pause();
        }
        
        vTaskDelay(50 / portTICK_PERIOD_MS);  // Delay más largo para ver logs
    }
    return nullptr;
}