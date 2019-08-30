// Include the library required for Servo Control.
#include <Servo.h>
// Include the library required to interpret the IR Receiver signals
#include <IRremote.h>

// Create constant integer that stores the digital port in which the servo will be connected.
#define SERVO_PIN 10
// Create constant integer that stores the digital port in which the IR Receiver will be connected.
#define IR_RECEIVER_PIN 11

// Instantiate objects
Servo servo;
IRrecv irrecv(IR_RECEIVER_PIN);
decode_results results;

void setup() {
    // Associate Servo object instance with the servo's pin
    servo.attach(SERVO_PIN);

    // Start the  IR Receiver
    irrecv.enableIRIn();

    Serial.begin(9600);
}

void loop() {

    if (irrecv.decode(&results)){
        switch(results.value){
            case 0xFF6897:    // 0 - Turn off
            case 0x6BC6597B:    // 1 - Turn off
                servo.write(45);
                delay(500);
                break;
            case 0xFF30CF:    // 1 - Turn on
            case 0x735B797E:    // 2 - Turn on
                servo.write(165);
                delay(500);
                break;
        }
        Serial.println(results.value, HEX);
        irrecv.resume(); // Receive the next value 
    }
    servo.write(90);

    // Wait some time between read
    delay(100);
}
