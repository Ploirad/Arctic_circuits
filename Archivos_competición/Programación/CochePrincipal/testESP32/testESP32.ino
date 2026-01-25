#include <Arduino.h>
#include "THREAD.h"

// Función mejorada con verificación
void* led(void* parameter) {
    if (parameter == nullptr) {
        Serial.println("[LED] ERROR: Parameter is NULL!");
        return nullptr;
    }
    
    int pin = (int)parameter;;
    
    // Verificar pin válido para ESP32
    if (pin < 0 || pin > 39) {
        Serial.printf("[LED] ERROR: Invalid pin %d\n", pin);
        return nullptr;
    }
    
    pinMode(pin, OUTPUT);
    Serial.printf("[LED] Starting on pin %d\n", pin);
    
    int counter = 0;
    const int MAX_ITERATIONS = 1000;  // Límite de seguridad
    
    while (counter < MAX_ITERATIONS) {
        digitalWrite(pin, HIGH);
        vTaskDelay(500 / portTICK_PERIOD_MS);
        digitalWrite(pin, LOW);
        vTaskDelay(500 / portTICK_PERIOD_MS);
        
        counter++;
        
        // Debug cada 10 iteraciones
        if (counter % 10 == 0) {
            // Verificar stack
            UBaseType_t watermark = uxTaskGetStackHighWaterMark(NULL);
            Serial.printf("[LED] Iteration %d, Stack free: %u\n", 
                         counter, watermark);
        }
        
        // Permitir que otras tareas se ejecuten
        taskYIELD();
    }
    
    Serial.printf("[LED] Finished after %d iterations\n", counter);
    return nullptr;
}

Thread* thread2 = nullptr;
bool stopped = false;

void setup() {
    Serial.begin(115200);
    
    // Esperar MUCHO para que se abra el monitor serial
    delay(5000);
    
    Serial.println("\n\n=== THREAD TEST START ===");
    Serial.printf("Free Heap: %d\n", ESP.getFreeHeap());
    Serial.printf("CPU Frequency: %d MHz\n", ESP.getCpuFreqMHz());
    Serial.printf("Reset reason: %d\n", esp_reset_reason());
    
    int ledPin = 2;  // GPIO18 (cambia si tu ESP32 tiene LED en otro pin)
    
    Serial.printf("Creating thread for pin %d...\n", ledPin);
    
    // Crear thread con stack grande
    thread2 = new Thread(
        led,
        (void*)ledPin,
        8192,  // 8KB stack para seguridad
        1,     // Prioridad baja
        "LEDThread"
    );
    
    if (thread2 == nullptr) {
        Serial.println("ERROR: Failed to create thread object!");
        return;
    }
    
    Serial.println("Thread object created, starting...");
    
    if (thread2->start()) {
        Serial.println("Thread started successfully");
    } else {
        Serial.println("ERROR: Failed to start thread!");
        delete thread2;
        thread2 = nullptr;
        return;
    }
    
    Serial.println("Setup complete, entering loop...");
}

void loop() {
    static int ciclo = 0;
    
    if (thread2 == nullptr) {
        Serial.println("ERROR: Thread is null!");
        delay(5000);
        return;
    }
    
    Serial.printf("\n============ Ciclo %d ============\n", ciclo);
    Serial.printf("Free Heap: %d\n", ESP.getFreeHeap());
    
    ThreadState state = thread2->status();
    Serial.printf("Thread state: %d\n", (int)state);
    
    // Controlar thread cada 5 ciclos
    if (ciclo % 5 == 0) {
        if (!stopped && state == ThreadState::ALIVE) {
            Serial.println("Pausing LED thread...");
            if (thread2->pause()) {
                stopped = true;
                Serial.println("LED thread paused");
            } else {
                Serial.println("Failed to pause LED thread");
            }
        } 
        else if (stopped && state == ThreadState::SLEEPING) {
            Serial.println("Resuming LED thread...");
            if (thread2->resume()) {
                stopped = false;
                Serial.println("LED thread resumed");
            } else {
                Serial.println("Failed to resume LED thread");
            }
        }
    }

    ciclo++;
    
    // Delay más largo para ver mejor
    delay(3000);
}