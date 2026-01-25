#include "THREAD.h"

// Constructor - INICIALIZAR TODAS LAS VARIABLES
Thread::Thread(ThreadFunction function, void* parameter, 
               uint32_t stackSize, uint8_t priority, const char* name)
: _function(function), 
  _parameter(parameter), 
  _handle(nullptr), 
  _stackSize(stackSize), 
  _priority(priority),
  _state(ThreadState::DEAD),
  _result(nullptr),        // ¡IMPORTANTE!
  _hasResult(false) {      // ¡IMPORTANTE!
    
    strncpy(_name, name, sizeof(_name) - 1);
    _name[sizeof(_name) - 1] = '\0';

    _resultMutex = xSemaphoreCreateMutex();
    _endSemaphore = xSemaphoreCreateBinary();

    // Verificar que se crearon los semáforos
    if (!_resultMutex || !_endSemaphore) {
        Serial.printf("[THREAD] ERROR creating semaphores for '%s'\n", _name);
    }

    Serial.printf("[THREAD] Created thread '%s'\n", _name);
}

// Destructor
Thread::~Thread() {
    // Primero parar el thread si está corriendo
    if (_handle != nullptr) {
        // Cambiar estado primero
        _state = ThreadState::DEAD;
        
        // Intentar eliminar la tarea
        vTaskDelete(_handle);
        _handle = nullptr;
    }
    
    // Limpiar resultado
    clearResult();

    // Eliminar semáforos
    if (_resultMutex) {
        vSemaphoreDelete(_resultMutex);
        _resultMutex = nullptr;
    }
    if (_endSemaphore) {
        vSemaphoreDelete(_endSemaphore);
        _endSemaphore = nullptr;
    }

    Serial.printf("[THREAD] Destroyed thread '%s'\n", _name);
}

// Wrapper estático
void Thread::wrapper(void* parameter) {
    Thread* thread = static_cast<Thread*>(parameter);

    if (thread == nullptr || thread->_function == nullptr) {
        Serial.println("[WRAPPER] ERROR: Invalid thread or function");
        vTaskDelete(nullptr);
        return;
    }

    // Cambiar estado
    thread->_state = ThreadState::ALIVE;
    Serial.printf("[WRAPPER] Thread '%s' starting\n", thread->_name);

    // Ejecutar la función
    void* result = nullptr;
    
    // Proteger con try-catch si usas C++ exceptions
    result = thread->_function(thread->_parameter);
    
    Serial.printf("[WRAPPER] Thread '%s' function returned\n", thread->_name);

    // Guardar resultado
    if (thread->_resultMutex != nullptr) {
        if (xSemaphoreTake(thread->_resultMutex, portMAX_DELAY) == pdTRUE) {
            thread->_result = result;
            thread->_hasResult = (result != nullptr);
            xSemaphoreGive(thread->_resultMutex);
        }
    }
    
    // Cambiar estado y señalar fin
    thread->_state = ThreadState::FINISHED;
    
    if (thread->_endSemaphore != nullptr) {
        xSemaphoreGive(thread->_endSemaphore);
    }
    
    Serial.printf("[WRAPPER] Thread '%s' finished, state: %d\n", 
                  thread->_name, (int)thread->_state);
    
    vTaskDelete(nullptr);
}

// Iniciar thread
bool Thread::start() {
    if (_state != ThreadState::DEAD) {
        Serial.printf("[THREAD] Thread '%s' already alive (state: %d)\n", 
                      _name, (int)_state);
        return false;
    }

    // Verificar semáforos
    if (_resultMutex == nullptr || _endSemaphore == nullptr) {
        Serial.printf("[THREAD] ERROR: Semaphores not created for '%s'\n", _name);
        return false;
    }

    // Limpiar resultado anterior
    clearResult();
    
    // Resetear semáforo de fin
    while (xSemaphoreTake(_endSemaphore, 0) == pdTRUE) {
        // Vaciar el semáforo si estaba señalado
    }

    BaseType_t result = xTaskCreate(
        wrapper,
        _name,
        _stackSize,
        this,
        _priority,
        &_handle
    );

    if (result == pdPASS) {
        _state = ThreadState::ALIVE;
        Serial.printf("[THREAD] Started thread '%s' successfully\n", _name);
        return true;
    }

    Serial.printf("[THREAD] FAILED to start thread '%s' (xTaskCreate returned %d)\n", 
                  _name, result);
    return false;
}

// Resto de métodos (iguales pero con más logging)
bool Thread::hasResult() {
    if (_resultMutex == nullptr) return false;
    
    bool hasResult = false;
    if (xSemaphoreTake(_resultMutex, portMAX_DELAY) == pdTRUE) {
        hasResult = _hasResult;
        xSemaphoreGive(_resultMutex);
    }
    return hasResult;
}

void* Thread::getResult() {
    if (_resultMutex == nullptr) return nullptr;
    
    void* result = nullptr;
    if (xSemaphoreTake(_resultMutex, portMAX_DELAY) == pdTRUE) {
        if (_hasResult) {
            result = _result;
            // No limpiamos aquí, el usuario debe llamar clearResult()
        }
        xSemaphoreGive(_resultMutex);
    }
    return result;
}

void* Thread::waitForResult(uint32_t timeoutMs) {
    if (_state == ThreadState::DEAD || _state == ThreadState::FINISHED) {
        return getResult();
    }

    if (_endSemaphore == nullptr) return nullptr;
    
    TickType_t ticks = timeoutMs / portTICK_PERIOD_MS;
    if (xSemaphoreTake(_endSemaphore, ticks) == pdTRUE) {
        return getResult();
    }

    return nullptr;
}

void Thread::clearResult() {
    if (_resultMutex == nullptr) return;
    
    if (xSemaphoreTake(_resultMutex, portMAX_DELAY) == pdTRUE) {
        if (_result != nullptr) {
            free(_result);
            _result = nullptr;
        }
        _hasResult = false;
        xSemaphoreGive(_resultMutex);
    }
}

bool Thread::stop() {
    if (_handle == nullptr) {
        Serial.printf("[THREAD] Thread '%s' already stopped\n", _name);
        return false;
    }

    Serial.printf("[THREAD] Stopping thread '%s'\n", _name);
    vTaskDelete(_handle);
    _handle = nullptr;
    _state = ThreadState::DEAD;
    clearResult();
    
    Serial.printf("[THREAD] Thread '%s' stopped\n", _name);
    return true;
}

bool Thread::pause() {
    if (_handle == nullptr || _state != ThreadState::ALIVE) {
        Serial.printf("[THREAD] Cannot pause '%s' (handle: %p, state: %d)\n", 
                      _name, _handle, (int)_state);
        return false;
    }

    vTaskSuspend(_handle);
    _state = ThreadState::SLEEPING;
    Serial.printf("[THREAD] Thread '%s' paused\n", _name);
    return true;
}

bool Thread::resume() {
    if (_handle == nullptr || _state != ThreadState::SLEEPING) {
        Serial.printf("[THREAD] Cannot resume '%s' (handle: %p, state: %d)\n", 
                      _name, _handle, (int)_state);
        return false;
    }

    vTaskResume(_handle);
    _state = ThreadState::ALIVE;
    Serial.printf("[THREAD] Thread '%s' resumed\n", _name);
    return true;
}

ThreadState Thread::status() const {
    return _state;
}

const char* Thread::getName() const {
    return _name;
}