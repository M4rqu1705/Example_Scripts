// Wiring:
// https://www.behind-the-scenes.co.za/connecting-the-esp8266-to-a-breadboard-and-ftdi-programmer/
// Install accordingly: 
// https://create.arduino.cc/projecthub/luciorocha/ai-thinker-ai-cloud-inside-esp8266-update-firmware-reviewed-3e306c
// Setup commands:
// https://www.youtube.com/watch?v=9QZkCQSHnko
// More commands:
// https://room-15.github.io/blog/2015/03/26/esp8266-at-command-reference/#AT+CWJAP
// AT+CWJAP="ARRIS-F542","9CB37D4AF0314AB1"

void setup() {
  // initialize LED_BUILTIN as an output pin.
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off
  delay(1000);
}
