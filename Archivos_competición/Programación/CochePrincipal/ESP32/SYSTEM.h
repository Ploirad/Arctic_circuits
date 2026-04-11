#ifndef SYSTEM_h
#define SYSTEM_h

#include "Arduino.h"
#include "CLAW.h"
#include "L298N.h"
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
        void moveL298N(bool CW);
        void stopL298N();

        void setCompressionSpeed(int speed);
        
        void emergencyStop();
    private:
        L298N motors;
        PCA9685 pca;
        CLAW claws[4];
        int compressionSpeed;
        
        bool CW;
        bool move;

        Thread l298nThread;
        SemaphoreHandle_t _l298nMutex;
        static const uint32_t _l298nThread_stack;
        static const uint8_t _l298nThread_priority;
        static const char* _l298nThread_name;
        static void* l298nThreadFunc(void* parameter);
};

#endif