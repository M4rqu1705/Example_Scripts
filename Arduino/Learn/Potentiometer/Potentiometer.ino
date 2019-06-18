// Tutorial from https://www.arduino.cc/en/tutorial/potentiometer

const unsigned char pot_pin = A0;
unsigned short pot_reading = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  pot_reading = analogRead(pot_pin);
  Serial.print("Potentiometer value: ");
  Serial.println(pot_reading);
}
