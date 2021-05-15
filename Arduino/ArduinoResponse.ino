#include <Servo.h> 

int incomingByte;
int pinkRing = 6;
int midInd = 7;
int latchPin = 4;
int clockPin = 3;
int dataPin = 5;

Servo pinkRin;
Servo midIndex;

void setup() {
    Serial.begin(9600); // set the baud rate
    pinkRin.attach(pinkRing);
    midIndex.attach(midInd);
    Serial.println("Ready"); // print "Ready" once
    pinMode(latchPin, OUTPUT);
    clear();
    }


void loop() {
    // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    if (incomingByte == 's') {
      scissors();
    }
    else if (incomingByte == 'r') {
      rock();
    }
  }
  // sad
    else if (incomingByte == 'a' || incomingByte == 'c' || incomingByte == 'e'){
        smile();
    }

    //joy
    else if (incomingByte == 'b'){
      frown();
    }

    //neutral
    else if (incomingByte == 'd'){
        neutral();
    }

    // rock: all curl in
    else if (incomingByte == 'r'){
        rock();
    }
    
    // scissors: ring and pinky curl in
    else if (incomingByte == 's'){
        scissors();
    }
}


void shiftOut(int myDataPin, int myClockPin, byte myDataOut) {
  int i=0;
  int pinState;
  pinMode(myClockPin, OUTPUT);
  pinMode(myDataPin, OUTPUT);
  digitalWrite(myDataPin, 0);
  digitalWrite(myClockPin, 0);
  for (i=7; i>=0; i--)  {
    digitalWrite(myClockPin, 0);
    if ( myDataOut & (1<<i) ) {
      pinState= 1;
    }
    else {
      pinState= 0;
    }
    digitalWrite(myDataPin, pinState);
    digitalWrite(myClockPin, 1);
    digitalWrite(myDataPin, 0);
  }
  digitalWrite(myClockPin, 0);
}


void smile(){
  byte data = 0x3F;
  digitalWrite(latchPin, 0);
  shiftOut(dataPin, clockPin,data);
  digitalWrite(latchPin, 1);
  delay(300);
}


void frown(){
  byte data = 0xFC;
  digitalWrite(latchPin, 0);
  shiftOut(dataPin, clockPin, data);
  digitalWrite(latchPin, 1);
  delay(300);
}


void neutral(){
  byte data = 0x3C;
  digitalWrite(latchPin, 0);
  shiftOut(dataPin, clockPin, data);
  digitalWrite(latchPin, 1);
  delay(300);
}


void clear(){
  byte data = 0x0;
  digitalWrite(latchPin, 0);
  shiftOut(dataPin, clockPin, data);
  digitalWrite(latchPin, 1);
  delay(300);
  
}


void rock(){
  pinkRin.write(0);
  midIndex.write(0);
  pinkRin.write(180);
  midIndex.write(180);
  delay(1000);
  pinkRin.write(0);
  midIndex.write(0);
}


void scissors(){
  pinkRin.write(0);
  pinkRin.write(180);
  delay(1000);
  pinkRin.write(0);
}
