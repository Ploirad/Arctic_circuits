#ifndef THREAD_h
#define THREAD_h

#include "Arduino.h"
#include <freertos/FreeRTOS.h>
#include <freertos/task.h>
#include <freertos/semphr.h>

typedef void* (*ThreadFunction)(void*);

enum class ThreadState {
    DEAD = 0,
    ALIVE = 1,
    SLEEPING = 2,
    FINISHED = 3
};

class Thread {
    public:
        Thread(
            ThreadFunction function,
            void* parameter = nullptr,
            uint32_t stackSize = 4096,
            uint8_t priority = 1,
            const char* name = "Thread"
        );
        ~Thread();
        bool start();
        bool stop();
        bool pause();
        bool resume();

        bool hasResult();
        void* getResult();
        void* waitForResult(uint32_t timeoutMs = portMAX_DELAY);
        void clearResult();

        ThreadState status() const;
        const char* getName() const;

    private:
        static void wrapper(void* parameter);

        ThreadFunction _function;
        void* _parameter;
        TaskHandle_t _handle;
        char _name[32];
        ThreadState _state;
        uint32_t _stackSize;
        uint8_t _priority;

        void* _result;
        bool _hasResult;
        SemaphoreHandle_t _resultMutex;
        SemaphoreHandle_t _endSemaphore;
};

#endif