/*

Tai Xiang

Fake shift register takes in bytes as strings and applies same patterning
as a regular shift register would to a set of eight LEDs

 */
// Pin connected arduino
int ledPins[] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11};

// array that will hold 'bytes'
String dataArray[10];

void setup() {

  // set pins to output because they are addressed in the main loop

  Serial.begin(9600);

// instantiate the patterns
  dataArray[0] = "FF"; //0b11111111

  dataArray[1] = "FE"; //0b11111110

  dataArray[2] = "FC"; //0b11111100

  dataArray[3] = "F8"; //0b11111000

  dataArray[4] = "F0"; //0b11110000

  dataArray[5] = "E0"; //0b11100000

  dataArray[6] = "C0"; //0b11000000

  dataArray[7] = "80"; //0b10000000
}

void loop() {
    // main loop
    shiftRegisterReplicator(dataArray);
}

// unitHexTrans takes in a char and converts it to its binary pattern
const char* unitHexTrans(char c)
{
    switch(toupper(c))
    {
        case '0': return "0000";
        case '1': return "0001";
        case '2': return "0010";
        case '3': return "0011";
        case '4': return "0100";
        case '5': return "0101";
        case '6': return "0110";
        case '7': return "0111";
        case '8': return "1000";
        case '9': return "1001";
        case 'A': return "1010";
        case 'B': return "1011";
        case 'C': return "1100";
        case 'D': return "1101";
        case 'E': return "1110";
        case 'F': return "1111";
    }
}


/* 
hexToBin takes in a string of hexadecimals and translates 
them to a concatenated binary number
*/
String hexToBin(String hexa){
    String binOut = "";
    for (int i = 0; i < hexa.length(); i++){
        binOut +=  unitHexTrans(hexa[i]);
    }
    return binOut;
}

// binToVal takes in a character and returns its HIGH/LOW correspondance
int binToVal(char i){
    if (i == '1'){
        return 255;
    }
    return 0;
}

// shiftRegisterReplicator takes in an array of hexadecimals and performs the function of the shift register
void shiftRegisterReplicator(String arrIn[]){
    String fakeBin[8];
    for (int i = 0; i < 8; i++){
        fakeBin[i] = hexToBin(arrIn[i]);
    }

    for (String bin : fakeBin){
        Serial.print("Binary In: ");
        Serial.println(bin);
        for (int i = 0; i < bin.length(); i++){
            Serial.print("255 or 0: ");
            Serial.print(bin[i]);
            Serial.println(binToVal(bin[i]));
            analogWrite(ledPins[i], binToVal((bin[i])));
        }
        }
    }



