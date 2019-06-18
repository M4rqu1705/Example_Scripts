// Tutorial from https://playground.arduino.cc/Learning/PhotoResistor

// This is a very simple sensor to use
/* Connection

       PhotoResistor  10K
 +5 -------/\/\/--.--/\/\/------- GND
                  |
                  --------------- Pin A0
*/
// Values range from 0 to 1023, but practically this range is much lower


const unsigned char photo_pin = A0;   // Create constant to store photoresistor pin

void setup() {
  Serial.begin(9600);   // Initialize serial monitor on 9600 baud
}

void loop() {
  unsigned short amount_of_light = analogRead(photo_pin);   // Initialize variable to store sensor reading
  Serial.println(amount_of_light);                          // Print sensor reading to the serial monitor
}
