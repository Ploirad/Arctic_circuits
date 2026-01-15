#ifndef I2C_SLAVE_h
#define I2C_SLAVE_h

#include "Arduino.h"
#include <Wire.h>

class I2C_SLAVE {
    public:
        I2C_SLAVE(uint8_t address);
        void begin();
        uint8_t* getData();
        size_t getDataSize();
        bool isDataAvailable();
        
    private:
        static const size_t MAX_BUFFER_SIZE = 32;
        uint8_t _address;
        static uint8_t _receivedData[MAX_BUFFER_SIZE];
        static volatile size_t _receivedBytes;
        static volatile bool _newDataAvailable;
        static void onReceiveHandler(int numBytes);
};

#endif