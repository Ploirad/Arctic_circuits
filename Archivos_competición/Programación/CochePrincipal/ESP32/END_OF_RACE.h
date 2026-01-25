#ifndef END_OF_RACE_h
#define END_OF_RACE_h

#include "Arduino.h"

class EndOfRace {
    public:
        EndOfRace(int pin);
        bool pressed();
    private:
        int _pin;
};

#endif