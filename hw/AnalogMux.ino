int pin_Out_S0 = 5;
int pin_In_Mux1 = A0;
int in_pin = 2;
int Mux1_State[2] = {0};

void setup() {
  pinMode(in_pin, OUTPUT);
  pinMode(pin_Out_S0, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(in_pin, HIGH);
  updateMux1();
  Serial.println("IR HIGH");
  for(int i = 0; i < 2; i ++) {
    if(i == 1) {
      Serial.println(get_volt(Mux1_State[i]));
    } else {
      Serial.print(get_volt(Mux1_State[i]));
      Serial.print(",");
    }
  }
  delay(1000);              
  digitalWrite(in_pin, LOW);
  updateMux1();
  Serial.println("IR LOW");
  for(int i = 0; i < 2; i ++) {
    if(i == 1) {
      Serial.println(get_volt(Mux1_State[i]));
    } else {
      Serial.print(get_volt(Mux1_State[i]));
      Serial.print(",");
    }   
  }
  delay(1000);    
}

void updateMux1 () {
  for (int i = 0; i < 2; i++){
    digitalWrite(pin_Out_S0, HIGH);
    Mux1_State[i] = analogRead(pin_In_Mux1);
  }
}

double get_volt(double val_in){
//  return val_in;
  return (val_in / 1023) * 5;
  }
