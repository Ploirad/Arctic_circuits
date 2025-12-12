#include <Wire.h>

#define RUN_PIN 3
#define COLOR_PIN 4
#define OK_PIN 5
#define RESET_PIN 6

void setup(){
  Serial.begin(115200);
  Serial.println("Hola Mundo");

  pinMode(RUN_PIN, INPUT);
  pinMode(COLOR_PIN, INPUT);
  pinMode(OK_PIN, OUTPUT);
}

void loop(){
  int run = digitalRead(RUN_PIN);
  int color = digitalRead(COLOR_PIN);

  if (color == HIGH){
    Serial.print("Color: Blue   ; ");
  }else{
    Serial.print("Color: Yellow ; ");
  }

  if (run == HIGH){
    Serial.println("RUNNING");
    digitalWrite(OK_PIN, HIGH);
  }else{
    Serial.println("STOP");
    digitalWrite(OK_PIN, LOW);
  }

}
