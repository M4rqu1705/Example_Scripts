// Tutorial from https://learn.sparkfun.com/tutorials/connecting-arduino-to-processing/all

const unsigned char pot_pin = A0, photo_pin = A1, thermo_pin = A2;

void setup() {
  Serial.begin(9600);
}

void loop(){
  Serial.print(analogRead(pot_pin));
  Serial.print(",");
  Serial.print(analogRead(photo_pin));
  Serial.print(",");
  Serial.println(analogRead(thermo_pin));
  delay(100);
}

