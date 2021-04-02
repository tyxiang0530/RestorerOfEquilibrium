int rPin = 2;
int gPin = 3;

int dry = 540;
int wet = 250;
// 470 is dry soil, 301 is wet soil
// to get percent: ((input - min) * 100) / (max - min)
void setup() {   
    pinMode(rPin, OUTPUT);
    pinMode(gPin, OUTPUT);

    Serial.begin(9600); // open serial port, set the baud rate as 9600 bps 
    } 

void loop() {   
    int val;   
    val = get_percent(analogRead(0));  
    //connect sensor to Analog 0   
    Serial.print(val); //print the value to serial port   
    Serial.print("% |");

    if (val >= 50){
        analogWrite(gPin, 0);
        analogWrite(rPin, 255);
        analogWrite(rPin, 0);
    } 
    else{
        analogWrite(rPin, 0);
        analogWrite(gPin, 255);
        analogWrite(gPin, 0);
    }
    delay(60000); 
    }

int get_percent(int val_in){
    return 100 - (((val_in - wet) * 100) / (dry - wet));
}
// void RGB_color(int red_light_value, int green_light_value, int blue_light_value)
// {
//     analogWrite(red_light_pin, red_light_value);
//     analogWrite(green_light_pin, green_light_value);
//     analogWrite(blue_light_pin, blue_light_value);
// }
