#include <AccelStepper.h>

// Definición de pines (conectados al ULN2003)
const int motorPin1 = 18;   // 28BYJ48 In1
const int motorPin2 = 33;   // 28BYJ48 In2
const int motorPin3 = 19;   // 28BYJ48 In3
const int motorPin4 = 32;   // 28BYJ48 In4

// Parámetros del motor
const int stepsPerRev = 4076;   // Pasos por revolución (medio paso)
int motorSpeed = 1200;          // Velocidad original en microsegundos/paso

// Crear objeto AccelStepper con interfaz HALF4WIRE
// Orden de pines: (In1, In3, In2, In4) para que coincida con la secuencia original
AccelStepper stepper(AccelStepper::HALF4WIRE, motorPin1, motorPin3, motorPin2, motorPin4);

void setup() {
  Serial.begin(115200);
  
  // Configurar velocidad máxima (en pasos/segundo) a partir del valor inicial
  // Convertimos de microsegundos/paso a pasos/segundo: 1e6 / motorSpeed
  stepper.setMaxSpeed(1000000.0 / motorSpeed);
  stepper.setSpeed(1000000.0 / motorSpeed);   // Velocidad constante positiva (horario)
  stepper.setAccel(200);
}

void loop() {
  // Leer comando serie para cambiar la velocidad
  if (Serial.available()) {
    String input = Serial.readStringUntil('\n');
    int newSpeed = input.toInt();
    if (newSpeed > 0) {   // Evitar velocidades no válidas
      motorSpeed = newSpeed;
      // Actualizar velocidad en pasos/segundo
      float stepsPerSec = 1000000.0 / motorSpeed;
      stepper.setMaxSpeed(stepsPerSec);
      stepper.setSpeed(stepsPerSec);
      Serial.print("Velocidad actual: ");
      Serial.println(motorSpeed);
    }
  }

  // Mover continuamente en sentido horario
  stepper.runSpeed();
}