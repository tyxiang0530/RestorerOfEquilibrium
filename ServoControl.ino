#include <Servo.h> 
// Declare the Servo pin 
int servoPin = 3; 
// Create a servo object 
Servo Servo1; 
void setup() { 
   // We need to attach the servo to the used pin number 
   Servo1.attach(servoPin); 
}
void loop(){ 
   moveServo(randomNum())
}

void moveServo(int emoVal){
    // neutral emotion
    if (emoVal == 0){
        Servo1.write(90); 
    }

    // happy
    else if (emoVal == 1){
        Servo1.write(180); 
    }

    // sadness, anger, fear
    else if (emoVal == 2 || emoVal == 3 || emoVal == 4){
        Servo1.write(0); 
    }
}

int randomNum(){
    return random(0,4)
}