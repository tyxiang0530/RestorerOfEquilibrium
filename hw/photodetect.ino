int in_pin = 2;
int analog_in = 0;


void setup() {
    pinMode(in_pin, OUTPUT);
    Serial.begin(9600); // open serial port, set the baud rate as 9600 bps 

}


void loop() {
//    digitalWrite(in_pin, HIGH);  
//    int val;   
//    val = analogRead(analog_in);  
//    Serial.print(get_volt(val));
//    Serial.print("|");
//    delay(1000);              
//    digitalWrite(in_pin, LOW);   
    val = analogRead(analog_in);
    Serial.print(get_volt(val));
    Serial.print("|");  
    delay(300000);         
}

double get_volt(double val_in){
//  return val_in;
  return (val_in / 1023) * 5;
  }
