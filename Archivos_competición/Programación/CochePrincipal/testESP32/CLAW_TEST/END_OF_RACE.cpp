#include "END_OF_RACE.h"

EndOfRace::EndOfRace(int pin) : _pin(-1) {
    _pin = pin;
    pinMode(_pin, INPUT_PULLDOWN);
}

bool EndOfRace::pressed() {
    return digitalRead(_pin) == HIGH;
}