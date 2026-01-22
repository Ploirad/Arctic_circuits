#include "I2C_SLAVE.h"
#include <Wire.h>

// Initialize static members
uint8_t I2C_SLAVE::_receivedData[MAX_BUFFER_SIZE];
volatile size_t I2C_SLAVE::_receivedBytes = 0;
volatile bool I2C_SLAVE::_newDataAvailable = false;

I2C_SLAVE::I2C_SLAVE(uint8_t address) {
    _address = address;
}

void I2C_SLAVE::begin() {
    Wire.begin(_address);
    Wire.onReceive(onReceiveHandler);
}

void I2C_SLAVE::onReceiveHandler(int numBytes) {
    _receivedBytes = 0;
    
    // Read all available bytes
    while (Wire.available() && _receivedBytes < MAX_BUFFER_SIZE) {
        _receivedData[_receivedBytes++] = Wire.read();
    }
    
    // Clear any remaining bytes if buffer is full
    while (Wire.available()) {
        Wire.read();
    }
    
    _newDataAvailable = true;
}

uint8_t* I2C_SLAVE::getData() {
    if (_newDataAvailable) {
        _newDataAvailable = false;
        return _receivedData;
    }
    return nullptr;
}

size_t I2C_SLAVE::getDataSize() {
    return _receivedBytes;
}

bool I2C_SLAVE::isDataAvailable() {
    return _newDataAvailable;
}
