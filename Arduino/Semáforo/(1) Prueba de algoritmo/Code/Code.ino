// Define LED and button port constants
#define RED_LED 10
#define YELLOW_LED 9
#define GREEN_LED 8

#define RED_BUTTON 7
#define YELLOW_BUTTON 6
#define GREEN_BUTTON 5
#define NEUTRAL_BUTTON 4

// Define the time the streetlights will be on
#define GREEN_LED_TIME 1000
#define YELLOW_LED_TIME 200 + GREEN_LED_TIME
#define RED_LED_TIME 1000 + YELLOW_LED_TIME

// Initialize variables
bool red_was_pressed = 0,
     yellow_was_pressed = 0,
     green_was_pressed = 0,
     neutral_was_pressed = 1;
long begin_time = millis();

// Function prototypes
void check_buttons();
bool color_button_pressed();
void turn_LED_on(bool red, bool yellow, bool green);


void setup() {
    // Prepare the LED pins as outputs
    pinMode(RED_LED, OUTPUT);
    pinMode(YELLOW_LED, OUTPUT);
    pinMode(GREEN_LED, OUTPUT);

    // Prepare the button pins as inputs
    pinMode(RED_BUTTON, INPUT);
    pinMode(YELLOW_BUTTON, INPUT);
    pinMode(GREEN_BUTTON, INPUT);
    pinMode(NEUTRAL_BUTTON, INPUT);

}

void loop() {

    // Check if either of the buttons were pressed
    check_buttons();

    // Used later for the delay operation
    begin_time = millis();

    // Light up the LEDs accordingly
    // === === === === === === === Red light on === === === === === === === === ==
    if(red_was_pressed)
        turn_LED_on(true, false, false);

    // === === === === === === === Yellow light on === === === === === === === ===
    else if(yellow_was_pressed)
        turn_LED_on(false, true, false);

    // === === === === === === === Green light on === === === === === === === ====
    else if(green_was_pressed)
        turn_LED_on(false, false, true);

    // === === === === === === === Automatic Street light  === === === === === ===

    else if(neutral_was_pressed){
        // Turn green on for 10 seconds
        while(millis() < begin_time + GREEN_LED_TIME && !(color_button_pressed())){
            turn_LED_on(false, false, true);
            delay(10);
        } 

        // Turn yellow on for 2 seconds
        while(millis() < begin_time + YELLOW_LED_TIME && !(color_button_pressed())){
            turn_LED_on(false, true, false);
            delay(10);
        } 

        // Turn red on for 10 seconds
        while(millis() < begin_time + RED_LED_TIME && !(color_button_pressed())){
            turn_LED_on(true, false, false);
            delay(10);
        } 

    }


    begin_time = millis();

    // Delay exactly 15 milliseconds
    while(millis() < begin_time + 15) 0;

}


void check_buttons(){

    if(digitalRead(RED_BUTTON)){
        red_was_pressed = true;
        yellow_was_pressed = false;
        green_was_pressed = false;
        neutral_was_pressed = false;
    }

    if(digitalRead(YELLOW_BUTTON)){
        red_was_pressed = false;
        yellow_was_pressed = true;
        green_was_pressed = false;
        neutral_was_pressed = false;
    }

    if(digitalRead(GREEN_BUTTON)){
        red_was_pressed = false;
        yellow_was_pressed = false;
        green_was_pressed = true;
        neutral_was_pressed = false;
    }

    if(digitalRead(NEUTRAL_BUTTON)){
        red_was_pressed = false;
        yellow_was_pressed = false;
        green_was_pressed = false;
        neutral_was_pressed = true;
    }
}

bool color_button_pressed(){
    check_buttons();
    return (red_was_pressed || yellow_was_pressed || green_was_pressed);
}

void turn_LED_on(bool red, bool yellow, bool green){

    if(red)
        digitalWrite(RED_LED, HIGH);
    else
        digitalWrite(RED_LED, LOW);

    if(yellow)
        digitalWrite(YELLOW_LED, HIGH);
    else
        digitalWrite(YELLOW_LED, LOW);

    if(green)
        digitalWrite(GREEN_LED, HIGH);
    else
        digitalWrite(GREEN_LED, LOW);
}
