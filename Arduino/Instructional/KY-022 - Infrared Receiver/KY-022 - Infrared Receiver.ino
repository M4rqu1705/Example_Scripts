// https://arduinomodules.info/ky-022-infrared-receiver-module/

#include <IRremote.h>

const unsigned char RECV_PIN = 11;  // Define input pin on Arduino 
IRrecv irrecv(RECV_PIN);            // Instantiate IRrecv object
decode_results results;             // Instantiate decode_results class which is defined in IRremote.h

void setup() { 
  Serial.begin(9600);   // Create serial port for communication
  irrecv.enableIRIn();  // Start the receiver 
} 

void loop() { 
  if (irrecv.decode(&results)){
    //Serial.println(results.value, HEX); 
    if (results.value == 0xE318261B || results.value == 0xFFA25D){
      Serial.println("On/OFF");
    }
    else if (results.value == 0xFF629D){
      Serial.println("Volume Up");
    }
    else if (results.value == 0xFFE21D || results.value == 0xEE886D7F){
      Serial.println("Func/Stop");
    }
    else if (results.value == 0xFF22DD){
      Serial.println("Back");
    }
    else if (results.value == 0xFF02FD || results.value == 0xD7E84B1B){
      Serial.println("Play/Pause");
    }
    else if (results.value == 0xFFC23D){
      Serial.println("Forward");
    }
    else if (results.value == 0xFFE01F){
      Serial.println("Down Arrow");
    }
    else if (results.value == 0xFFA857){
      Serial.println("Volume Down");
    }
    else if (results.value == 0xFF906F){
      Serial.println("Up arrow");
    }
    else if (results.value == 0xFF6897){
      Serial.println("Number 0");
    }
    else if (results.value == 0xFF9867){
      Serial.println("EQ");
    }
    else if (results.value == 0xFFB05F || results.value == 0xFFB04F){
      Serial.println("ST/Rept");
    }
    else if (results.value == 0xFF30CF){
      Serial.println("Number 1");
    }
    else if (results.value == 0xFF18E7){
      Serial.println("Number 2");
    }
    else if (results.value == 0xFF7A85){
      Serial.println("Number 3");
    }
    else if (results.value == 0xFF10EF){
      Serial.println("Number 4");
    }
    else if (results.value == 0xFF38C7){
      Serial.println("Number 5");
    }
    else if (results.value == 0xFF5AA5){
      Serial.println("Number 6");
    }
    else if (results.value == 0xFF42BD){
      Serial.println("Number 7");
    }
    else if (results.value == 0xFF4AB5){
      Serial.println("Number 8");
    }
    else if (results.value == 0xFF52AD){
      Serial.println("Number 9");
    }
    else if (results.value == 0xFFFFFF){
      Serial.println("Repeat");
    }
    irrecv.resume(); // Receive the next value 
  }
  delay (10); // small delay to prevent reading errors
}
