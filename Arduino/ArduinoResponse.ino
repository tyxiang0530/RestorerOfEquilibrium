'''
Combinations needed:
Each finger: pinky, ring, middle, index
Rock: p, r, m, i
Scissors: p, r
Paper: Nothing

Initialization:
Blink LED on and off

Mouth Configurations
-         -
 -       -
  -------
 -       -
-         -

Smile: Top + middle
Neutral: Middle
Sad: Bottom + Middle


'''
#include <Servo.h> 


int init1 = 1;
int init2 = 2;
int pinky = 5;
int ring = 6;
int middle = 7;
int index = 9;

Servo pinkf;
Servo ringf;
Servo middlef;
Servo indexf;

void setup() {
    Serial.begin(9600); // set the baud rate
    pinMode(init1, OUTPUT);
    pinMode(init2, OUTPUT);
    pinkf.attach(pinky);
    ringf.attach(ring);
    middlef.attach(middle);
    indexf.attach(index);

    Serial.println("Ready"); // print "Ready" once
    }


void loop() {
    // rock: all curl in
    if (Serial.read() == 'r'){
        pinkf.write(-150)
        ringf.write(-150)
        middlef.write(-150)
        indexf.write(-150)
        delay(2000)
        Serial.print("rock");
        pinkf.write(150)
        ringf.write(150)
        middlef.write(150)
        indexf.write(150)
    }
    // paper: no change
    else if (Serial.read() == 'p'){
        Serial.print("paper");
    }
    // scissors: ring and pinky curl in
    else if (Serial.read() == 's'){
        pinkf.write(-150);
        ringf.write(-150);
        delay(2000);
        pinkf.write(150);
        ringf.write(150);
    }
    // initialization: receive byte "i"
    else if (Serial.read() == 'i'){
        digitalWrite(init1, HIGH)
        digitalWrite(init2, LOW)
        delay(100)
        digitalWrite(init1, LOW)
        digitalWrite(init2, HIGH)
    }
}
