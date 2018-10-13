#include <Servo.h>
#include <MedianFilter.h>

const int x_axis = A0, y_axis = A1, button = 2, servo_pin = 3;
int x_position = 0;
int offset = 0;
Servo servo;
MedianFilter filter(3, 0);

void setup() {
  pinMode(x_axis, INPUT);
  pinMode(y_axis, INPUT);
  pinMode(button, INPUT_PULLUP);
  servo.attach(servo_pin);

  Serial.begin(9600);
}

void loop() {
  x_position = analogRead(x_axis) + offset;
  x_position = filter.in(x_position);
  Serial.print("Joystick X: ");
  Serial.println(x_position);
  servo.write(map(x_position, 1023, 0, 0, 180));

  delay(10);
}
