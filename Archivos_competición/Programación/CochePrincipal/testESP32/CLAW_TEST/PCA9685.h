#ifndef PCA9685_h
#define PCA9685_h

#include "Arduino.h"
#include <Wire.h>
#include "Adafruit_PWMServoDriver.h"

class PCA9685 {
    public:
        PCA9685(uint8_t address = 0x40);
        void begin();
        void setVelocity(int channel, int velocity);
        void setDegrees(int channel, int degrees);
        
    private:
        Adafruit_PWMServoDriver pca;
        
        static const int MIN_PULSE_180;
        static const int MAX_PULSE_180;
        static const int MIN_PULSE_360;
        static const int MAX_PULSE_360;
        static const int STOP_PULSE_360; // Para motores continuos
};

#endif