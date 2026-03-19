#ifndef CLAW_h
#define CLAW_h

#include "Arduino.h"
#include "PCA9685.h"
#include "END_OF_RACE.h"
#include "THREAD.h"

class CLAW {
    public:
        CLAW(PCA9685& pca, int compressionChannel, int turnChannel, int endOfRacePin);
        virtual ~CLAW();
        void begin();
        void compress(int speed);
        void uncompress(int speed);
        void turn();
        void stop();
    private:
        int actual = 0;
        uint8_t _compressionChannel;
        uint8_t _turnChannel;
        PCA9685& _pca;
        EndOfRace endOfRace;
        SemaphoreHandle_t _stateMutex;

        // EORT means End Of Race Thread
        Thread EORT;
        bool compressed;
        static const uint32_t _EORT_stack;
        static const uint8_t _EORT_priority;
        static const char* _EORT_name;
        static void* EORT_func(void* parameter);
};

#endif