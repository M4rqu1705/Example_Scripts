#include <Wire.h>

#define ADDRESS 0x04

int number;

void setup() {
  Serial.begin(9600);         // Enable "printing" to serial monitor
  Wire.begin(ADDRESS);

  // Callback functions
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
}

void loop() {
  delay(100);
}

void receiveData(int byteCount) {
  while (Wire.available()) {
    number = Wire.read();
    Serial.println(char(number));
  }
}

void sendData(){
  Wire.write(number);
}

void sendStr(String data){
  for(int c=0; c<data.length(); c++){
    Wire.write(int(data.charAt(c)));  
  }
}
