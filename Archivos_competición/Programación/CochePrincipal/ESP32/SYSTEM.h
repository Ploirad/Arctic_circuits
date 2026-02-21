#ifndef SYSTEM_h
#define SYSTEM_h

#include "Arduino.h"
#include "CLAW.h"
#include "STEPPER.h"
#include "PCA9685.h"
#include "THREAD.h"

class SYSTEM {
    public:
        SYSTEM(
            int compressionChannel1, int turnChannel1, int endOfRacePin1,
            int compressionChannel2, int turnChannel2, int endOfRacePin2,
            int compressionChannel3, int turnChannel3, int endOfRacePin3,
            int compressionChannel4, int turnChannel4, int endOfRacePin4,
            uint8_t pcaAddress,
            int IN1, int IN2, int IN3, int IN4
        );
        ~SYSTEM();

        void begin();

        void turnClaw(int clawIndex);
        void compressClaws();
        void uncompressClaws();
        void stopClaws();
        void moveStepper(bool CW);
        void stopStepper();

        void setCompressionSpeed(int speed);
        void setStepperSpeed(float speed);
        void setStepperMaxSpeed(float maxSpeed);
        void setStepperAcceleration(float acceleration);

        void emergencyStop();
    private:
        STEPPER principalStepper;
        PCA9685 pca;
        CLAW claws[4];
        int compressionSpeed;

        float stepperSpeed;
        float stepperMaxSpeed;
        float stepperAcceleration;
        
        bool CW;
        bool move;

        Thread stepperThread;
        SemaphoreHandle_t _stepperMutex;
        static const uint32_t _stepperThread_stack;
        static const uint8_t _stepperThread_priority;
        static const char* _stepperThread_name;
        static void* stepperThreadFunc(void* parameter);
};

#endif