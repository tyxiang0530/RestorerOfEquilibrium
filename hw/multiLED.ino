/*
Tai Xiang HW4  MultiRed blinking LED
pure red led replaced with rg led with green value set to 0
*/ 


int ledPins[] = {2, 3, 4, 5, 6, 7, 8, 9};
int delayTime = 1000;
 
// using weird RG LED - set G to 0 for red
 
void setup()
{
for (int i = 0; i < 8; i++){
  pinMode(ledPins[i], OUTPUT);  
    }
}
 
void loop()
{
  rgbColorAll();
  // makeColor();  // red pin blinks in loop
}
 
void rgbColor(int red_light_value, int green_light_value, int blue_light_value)
 {
  analogWrite(ledPins[5], red_light_value);
  analogWrite(ledPins[6], green_light_value);
  analogWrite(ledPins[7], blue_light_value);
}
void rgbColorAll(){
  rgbColor(0, 0, 0);
  delay(delayTime);   
  rgbColor(255, 0, 0);
  delay(delayTime);  
  rgbColor(0, 255, 0);
  delay(delayTime);  
  rgbColor(0, 0, 255);
  delay(delayTime);  
  rgbColor(255, 255, 0);
  delay(delayTime);  
  rgbColor(255, 0, 255);
  delay(delayTime);  
  rgbColor(0, 255, 255);
  delay(delayTime);  
  rgbColor(255, 255, 255);
}


void makeColor()
{


  // turn all the LEDs on:

  digitalWrite(ledPins[0], HIGH);  //Turns on LED #0 (pin 4)
  delay(delayTime);                //wait delayTime milliseconds
  digitalWrite(ledPins[1], HIGH);  //Turns on LED #1 (pin 5)
  delay(delayTime);                //wait delayTime milliseconds
  digitalWrite(ledPins[2], HIGH);  //Turns on LED #2 (pin 6)
  delay(delayTime);                //wait delayTime milliseconds
  digitalWrite(ledPins[3], HIGH);  //Turns on LED #3 (pin 7)
  delay(delayTime);                //wait delayTime milliseconds
  digitalWrite(ledPins[4], HIGH);  //Turns on LED #4 (pin 8)
  delay(delayTime);                //wait delayTime milliseconds


  // turn all the LEDs off:

  digitalWrite(ledPins[7], LOW);   //Turn off LED #5 (pin 9)
  delay(delayTime);                //wait delayTime milliseconds
  digitalWrite(ledPins[6], LOW);   //Turn off LED #4 (pin 8)
  delay(delayTime);                //wait delayTime milliseconds
  digitalWrite(ledPins[5], LOW);   //Turn off LED #3 (pin 7)
  delay(delayTime);                //wait delayTime milliseconds
  digitalWrite(ledPins[4], LOW);   //Turn off LED #2 (pin 6)
  delay(delayTime);                //wait delayTime milliseconds
  digitalWrite(ledPins[3], LOW);   //Turn off LED #1 (pin 5)
  delay(delayTime);                //wait delayTime milliseconds
}