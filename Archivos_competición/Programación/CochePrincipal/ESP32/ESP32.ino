#include "SYSTEM.h"
#include "I2C_SLAVE.h"

// CONSTANTS AND CONFIGURATION PARAMETERS
const int compression_servo_channels[4] = {4, 5, 6, 7};
const int turn_servo_channels[4] = {0, 1, 2, 3};
const int end_of_race_pins[4] = {4, 5, 23, 13};
const int stepper_pins[4] = {32, 19, 33, 18};
const uint8_t pca_address = 0x40;

const int microbit_I2C_pins[2] = {16, 17}; // SDA, SCL
const uint8_t microbit_address = 0x42;

// OBJECTS
I2C_SLAVE microbit(microbit_address, microbit_I2C_pins[0], microbit_I2C_pins[1]);
SYSTEM sys(
    compression_servo_channels[0], turn_servo_channels[0], end_of_race_pins[0],
    compression_servo_channels[1], turn_servo_channels[1], end_of_race_pins[1],
    compression_servo_channels[2], turn_servo_channels[2], end_of_race_pins[2],
    compression_servo_channels[3], turn_servo_channels[3], end_of_race_pins[3],
    pca_address,
    stepper_pins[0], stepper_pins[1], stepper_pins[2], stepper_pins[3]
);

// VARIABLES
int microbit_data[6] = {0, 0, 0, 0, 0, 0};
uint8_t len;
int lastTurn[4] = {0, 0, 0, 0};

void setup() {
    Serial.begin(115200);
    sys.begin();
    sys.setCompressionSpeed(80); // Percentage (0-100)
    sys.setStepperSpeed(1000); // In steps/second
    sys.setStepperMaxSpeed(10000); // In steps/second
    sys.setStepperAcceleration(200); // In steps/second²
}

void loop() {
    if (microbit.isDataAvailable()) {
        uint8_t* data = microbit.getData(len);
        for (uint8_t i = 0; i < len; i++) {
            microbit_data[i] = data[i];
        }
    } else if (Serial.available()) {
        String data = Serial.readStringUntil('\n');  // read() → readString()
        if (data.length() >= 6) {
            
            for (int i = 0; i < ( sizeof(microbit_data) / sizeof(microbit_data[0]) ); i++) {
                microbit_data[i] = data.charAt(i) - '0';  // Convertir char a int
            }
        }
    }

    int size = sizeof(microbit_data)/sizeof(microbit_data[0]);

    Serial.println(size);
    for (int i = 0; i < size; i++) {
        Serial.print("Data ");
        Serial.print(i);
        Serial.print(": ");
        Serial.println(microbit_data[i]);
    }

    if (size == 6) {
        for (int i = 0; i<4; i++) {
            if ((microbit_data[i] == 1) && (microbit_data[i] != lastTurn[i])) {
                sys.turnClaw(i);
            }
            lastTurn[i] = microbit_data[i];
        }
        if (microbit_data[4] == 1) {
            sys.moveStepper(false);
        } else if (microbit_data[4] == 2) {
            sys.moveStepper(true);
        } else {
            sys.stopStepper();
        }

        if (microbit_data[5] == 1) {
            sys.compressClaws();
        } else if (microbit_data[5] == 2) {
            sys.uncompressClaws();
        } else {
            sys.stopClaws();
        }
    }
    delay(100);
}