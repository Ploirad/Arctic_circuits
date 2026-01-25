#ifndef CLAW_h
#define CLAW_h

#include "Arduino.h"
#include "SERVOS.h"
#include "END_OF_RACE.h"
#include "THREAD.h"

class CLAW {
    public:
        CLAW(int compressionPin, int turnPin, int endOfRacePin);
        virtual ~CLAW();
        void compress(int speed);
        void uncompress(int speed, int time);
        void turn();
        void stop();
    private:
        int actual = 0;
        Servo360 compressionServo;
        Servo180 turnServo;
        EndOfRace endOfRace;

        // EORT means End Of Race Thread
        Thread EORT;
        Thread CompThread;
        
        bool compressed;
        int compressing;
        int compressingSpeed;
        int uncompressionTime;

        static const uint32_t _EORT_stack;
        static const uint8_t _EORT_priority;
        static const char* _EORT_name;

        static const uint32_t _CompThread_stack;
        static const uint8_t _CompThread_priority;
        static const char* _CompThread_name;

        static void* EORT_func(void* parameter);
        static void* CompThread_func(void* parameter);
        
};

#endif