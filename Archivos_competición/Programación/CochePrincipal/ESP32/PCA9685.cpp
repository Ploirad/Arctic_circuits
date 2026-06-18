#include "PCA9685.h"

const int PCA9685::MAX_PULSE_180 = 565;   // 180º
const int PCA9685::MIN_PULSE_180 = 172;   // 0°
const int PCA9685::MAX_PULSE_360 = 565;  // max vel CW
const int PCA9685::MIN_PULSE_360 = 172;  // min vel CCW
const int PCA9685::STOP_PULSE_360 = 400; // stop

PCA9685::PCA9685(uint8_t address) : pca(address) {}

void PCA9685::begin() {
    pca.begin();
    pca.setPWMFreq(60);
}

void PCA9685::setVelocity(int channel, int velocity) {
    if (channel < 0 || channel > 15) return;
    
    velocity = constrain(velocity, -100, 100);
    int pulse;
    
    if (velocity == 0) {
        // Parar el motor
        pulse = STOP_PULSE_360;
    } else if (velocity > 0) {
        // Sentido positivo
        pulse = map(velocity, 0, 100, STOP_PULSE_360, MAX_PULSE_360);
    } else {
        // Sentido negativo
        pulse = map(velocity, -100, 0, MIN_PULSE_360, STOP_PULSE_360);
    }
    
    pca.setPWM(channel, 0, pulse);
}

void PCA9685::setDegrees(int channel, int angle) {
    if (channel < 0 || channel > 15) return;
    
    angle = constrain(angle, 0, 180);
    int pulse = map(angle, 0, 180, MIN_PULSE_180, MAX_PULSE_180);
    pca.setPWM(channel, 0, pulse);
}