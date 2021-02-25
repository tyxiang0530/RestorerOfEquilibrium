    /*
      Module 2 sketch 
      @author Tai Xiang
      module that turns LED ON if sensorValue over 512ms, off if otherwise
     */
     
    // designate pins
    const int analogInPin = A0;
    int led = 5;
     
    void setup() {                
      // initialize pins and serial monitor
      pinMode(led, OUTPUT);
      Serial.begin(9600);
    }
     
    void loop() {
      if (analogRead(analogInPin) > 512){
        // sensorvalue is high
        Serial.print("LED ON");
        digitalWrite(led, HIGH);   // turn LED on
      }

      else{
        // sensorvalue is low
        Serial.print("LED OFF");
        digitalWrite(led, LOW);    // turn LED off
      }
    }
