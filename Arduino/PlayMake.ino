#include <Servo.h> 


int ledPin[] = {2,3,4};
int servoPin = 5;
Servo pinkRing;

void setup() {
    Serial.begin(9600); // set the baud rate
    pinMode(ledPin[0], OUTPUT);
    pinMode(ledPin[1], OUTPUT);
    pinMode(ledPin[2], OUTPUT);
    pinkRing.attach(servoPin);
    Serial.println("Ready"); // print "Ready" once
    }


void loop() {
    if (Serial.read() == 'r'){
        Serial.print("Nothing");
    }
    else if (Serial.read() == 'p'){
        pinkRing.write(-150);
        delay(2000);
        pinkRing.write(150);
    }
    else if (Serial.read() == 's'){
        pinkRing.write(-150);
        delay(2000);
        pinkRing.write(150);
    }
    else if (Serial.read() == '1'){
        analogWrite(ledPin[0], 255);
        analogWrite(ledPin[1], 0);
        analogWrite(ledPin[2], 0);
    }
    else if (Serial.read() == '2'){
        analogWrite(ledPin[0], 255);
        analogWrite(ledPin[1], 255);
        analogWrite(ledPin[2], 0);
    }
    else if (Serial.read() == '3'){
        analogWrite(ledPin[0], 255);
        analogWrite(ledPin[1], 255);
        analogWrite(ledPin[2], 255);
    }
}