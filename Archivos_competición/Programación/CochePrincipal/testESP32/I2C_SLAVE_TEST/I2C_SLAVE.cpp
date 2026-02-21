#include "I2C_SLAVE.h"

I2C_SLAVE* I2C_SLAVE::_self = nullptr;

I2C_SLAVE::I2C_SLAVE(uint8_t address, int sdaPin, int sclPin) 
: _dataLen(0), _dataAvailable(false) {
    _self = this;
    Wire1.begin(address, sdaPin, sclPin, 100000);
    Wire1.onReceive(onReceiveHandler);
}

bool I2C_SLAVE::isDataAvailable() {
    return _dataAvailable;
}

uint8_t* I2C_SLAVE::getData(uint8_t &len) {
    len = _dataLen;
    _dataAvailable = false; // Marcar como leído
    return _buffer;
}

void I2C_SLAVE::clearData() {
    _dataLen = 0;
    _dataAvailable = false;
}

void I2C_SLAVE::onReceiveHandler(int numBytes) {
    if (_self == nullptr) return;

    _self->_dataLen = 0; // Reiniciar buffer
    while (Wire1.available() && _self->_dataLen < I2C_BUFFER_SIZE) {
        _self->_buffer[_self->_dataLen++] = Wire1.read();
    }
    _self->_dataAvailable = (_self->_dataLen > 0);
}