#ifndef L298N_h
#define L298N_h

#include "Arduino.h"

class L298N {
    public:
        L298N(int in1, int in2, int in3, int in4);
        bool isRunning();
        void stop();
        void runContinuous(bool CW);

    private:
        bool running;
        int IN1; int IN2; int IN3; int IN4;
};

#endif