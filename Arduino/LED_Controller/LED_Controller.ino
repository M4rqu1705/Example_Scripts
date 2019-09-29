#include "math.h"

// Define ports to use for program
#define X_JOY A0
#define Y_JOY A1
#define BUTTON 2
#define LED1 7
#define LED2 6
#define LED3 5
#define LED4 4

// Variable Inicialization
int magnitude = 0, x_input = 0, y_input = 0;
double angle = 0;
double led_positions[4] = {M_PI/4, M_PI*3/4, -M_PI*3/4, -M_PI/4};
double margin_error = M_PI/2;

// Function prototypes
bool isClose(double value, double desired_value, double range);

void setup() {
    // Serial.begin(9600);      // Begin serial monitor

    // Define inputs
    pinMode(X_JOY, INPUT);      // Define the joystick's x axis as input
    pinMode(Y_JOY, INPUT);      // Define the joystick's y axis as input
    pinMode(BUTTON, INPUT_PULLUP);      // Define joystick's button as input with pullup resistor

    // Define the four LED ports as outputs
    pinMode(LED1, OUTPUT);
    pinMode(LED2, OUTPUT);
    pinMode(LED3, OUTPUT);
    pinMode(LED4, OUTPUT);
}

void loop() {

    // Store manipulated joystick inputs in variables
    x_input = analogRead(X_JOY) - 500;
    y_input = 512 - analogRead(Y_JOY);

    // Interpret the joystick's values as a vector's components

    // Calculate the vector's magnitude
    magnitude = pow((pow(x_input,2) + pow(y_input,2)),0.5);
    // Calculate the vector's orientation with a smart inverse tangent
    angle = atan2(y_input,x_input);

    // Print variable's values for debugging purposes
    //* Serial.print("X = "); Serial.print(x_input);
    Serial.print("\t| Y = "); Serial.print(y_input);
    Serial.print("\t| Magnitude = "); Serial.print(magnitude);
    Serial.print("\t| Angle = "); Serial.println(angle/M_PI);//*/

    // Use 100 as a minimum threshold so noise doesn't activate the LEDs
    if(magnitude > 100){

        // Calculate a common margin error so various LED's light up with different magnitudes
        margin_error = (M_PI/4)*(magnitude/200);

        // Compare the current joystick direction with the position of each LED to determine if to turn it on or not
        // Also take into account the previously calculated margin error
        if(isClose(angle, led_positions[0], margin_error))
            digitalWrite(LED1, HIGH);
        else
            digitalWrite(LED1, LOW);

        // Repeat the same comparison as before
        // However, if we ignore that the readings go from positive to negative, and then jump back to positive, there
        // Won't be a smooth transition between LEDs. For this reason, also take into account the equivalent of the 
        // LED's position -2pi radians from its current position
        if(isClose(angle, led_positions[1], margin_error) || isClose(angle, led_positions[1] - 2*M_PI, margin_error))
            digitalWrite(LED2, HIGH);
        else
            digitalWrite(LED2, LOW);

        // Repeat the previous comparison, but instead of -2pi, +2pi
        if(isClose(angle, led_positions[2], margin_error) || isClose(angle, led_positions[2]+ 2*M_PI, margin_error))
            digitalWrite(LED3, HIGH);
        else
            digitalWrite(LED3, LOW);

        // Repeat the previous comparison
        if(isClose(angle, led_positions[3], margin_error) || isClose(angle, led_positions[3] - 2*M_PI, margin_error))
            digitalWrite(LED4, HIGH);
        else
            digitalWrite(LED4, LOW);

    }
    else if(!digitalRead(BUTTON)){
        // If the joystick's button is pressed, turn on all LEDs
        digitalWrite(LED1, HIGH);
        digitalWrite(LED2, HIGH);
        digitalWrite(LED3, HIGH);
        digitalWrite(LED4, HIGH);
    }
    else{
        // Turn of all LEDs if nothing is happening
        digitalWrite(LED1, LOW);
        digitalWrite(LED2, LOW);
        digitalWrite(LED3, LOW);
        digitalWrite(LED4, LOW);
    }

    // Wait 20 milliseconds to leave the processor some time to rest
    delay(20);
}


bool isClose(double value, double desired_value, double range){
    // Function to check if the current input is close to another value within some established range
    return(bool(desired_value-range <= value && value <=desired_value+range));
}
