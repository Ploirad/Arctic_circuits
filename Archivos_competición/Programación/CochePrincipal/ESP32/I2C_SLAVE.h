#ifndef I2C_SLAVE_h
#define I2C_SLAVE_h

#include "Arduino.h"
#include <Wire.h>

#define I2C_BUFFER_SIZE 32  // Tamaño máximo del buffer

class I2C_SLAVE {
public:
    I2C_SLAVE(uint8_t address, int sdaPin, int sclPin);
    
    bool isDataAvailable();           // ¿Hay nuevos datos?
    uint8_t* getData(uint8_t &len);   // Devuelve puntero al buffer y la longitud
    void clearData();                  // Limpia el buffer manualmente
    
private:
    static void onReceiveHandler(int numBytes);
    
    uint8_t _buffer[I2C_BUFFER_SIZE];
    uint8_t _dataLen;
    volatile bool _dataAvailable;      // volatile porque se modifica en ISR
    
    static I2C_SLAVE* _self;
};

#endif