// Include the library required for Servo Control.
#include <Servo.h>
 
// Create constant integer that stores the digital port in which the servo will be connected.
const int servo_pin = 6;

// Instantiate Servo object with the name servo_1.
Servo servo_1;

void setup() {
  // Associate Servo object instance with the servo's pin
  servo_1.attach(6);

  // Begin the serial monitor at 9600 baud frequency
  Serial.begin(9600);

}

void loop() {
  // Create variable destination_position which stores a random integer between 0 and 180
  int destination_position = random(0, 180);

  // Print serial messages to indicate the position the servo will move to
  Serial.print("Servo Position: ");
  Serial.println(destination_position);

  // Move servo to the random position
  servo_1.write(destination_position);

  // Wait a second to give the servo time to move
  delay(1000);
}
