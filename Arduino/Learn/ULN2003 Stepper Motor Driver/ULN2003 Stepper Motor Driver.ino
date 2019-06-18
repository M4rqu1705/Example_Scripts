#include <AccelStepper.h>
#define HALFSTEP 8

const int motorPin1 = 3;
const int motorPin2 = 4;
const int motorPin3 = 5;
const int motorPin4 = 6;

AccelStepper stepper1(HALFSTEP, motorPin1, motorPin3, motorPin2, motorPin4);

void setup() {
  stepper1.setMaxSpeed(2000);
  stepper1.setAcceleration(250  .0);
  stepper1.setSpeed(2000);
  stepper1.moveTo(2000);

}

void loop() {
  if (stepper1.distanceToGo() == 0) {
    stepper1.moveTo(-stepper1.currentPosition());
  }
  stepper1.run();
}
