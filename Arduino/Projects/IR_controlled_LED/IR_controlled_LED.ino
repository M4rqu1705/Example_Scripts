#include <IRremote.h>

const unsigned char LED = 13, IR_RECV = 11;
IRrecv irrecv(IR_RECV);
decode_results results;

unsigned int delay_time = 500;
bool led_on = false;
bool operating = true;


void setup() {
    irrecv.enableIRIn();
    pinMode(13, OUTPUT);
    digitalWrite(13, LOW);

    Serial.begin(9600);
}

void loop() {

    if (irrecv.decode(&results)){
        //Serial.println(results.value, HEX);
        if (results.value == 0xE318261B || results.value == 0xFFA25D){
            // On/Off
            if (!operating){
              operating = true;  
            }
            else if (operating){
              operating = false;
              led_on = false;
              digitalWrite(LED, LOW);
            }
        }
        else if (results.value == 0xFF629D){
            // Volume up
            delay_time += 50;

        }
        else if (results.value == 0xFFE21D || results.value == 0xEE886D7F){
            Serial.println("Func/Stop");
        }
        else if (results.value == 0xFF22DD){
            // Back
            delay_time *= 0.75;
        }
        else if (results.value == 0xFF02FD || results.value == 0xD7E84B1B){
            // Play/Pause
            operating = !operating;
        }
        else if (results.value == 0xFFC23D){
            // Forward
            delay_time *= 1.25;
        }
        else if (results.value == 0xFFE01F){
            Serial.println("Down Arrow");
        }
        else if (results.value == 0xFFA857){
            // Volume Down
            delay_time -= 50;
        }
        else if (results.value == 0xFF906F){
            Serial.println("Up arrow");
        }
        else if (results.value == 0xFF6897){
            // Number 0
            delay_time = 25;
        }
        else if (results.value == 0xFF9867){
            Serial.println("EQ");
        }
        else if (results.value == 0xFFB05F || results.value == 0xFFB04F){
            Serial.println("ST/Rept");
        }
        else if (results.value == 0xFF30CF){
            // Number 1
            delay_time = 50;
            
        }
        else if (results.value == 0xFF18E7){
            // Number 2
            delay_time = 150;
        }
        else if (results.value == 0xFF7A85){
            // Number 3
            delay_time = 250;
        }
        else if (results.value == 0xFF10EF){
            // Number 4
            delay_time = 350;
        }
        else if (results.value == 0xFF38C7){
            // Number 5
            delay_time = 500;
        }
        else if (results.value == 0xFF5AA5){
            // Number 6
            delay_time = 650;
        }
        else if (results.value == 0xFF42BD){
            // Number 7
            delay_time = 750;
        }
        else if (results.value == 0xFF4AB5){
            // Number 8
            delay_time = 850;
        }
        else if (results.value == 0xFF52AD){
            // Number 9
            delay_time = 1000;
        }
        else if (results.value == 0xFFFFFF){
            Serial.println("Repeat");
        }
        irrecv.resume(); // Receive the next value 
    }
    
    if (led_on && operating){
        digitalWrite(LED, HIGH);
        led_on = !led_on;
    }
    else if (!led_on && operating){
        digitalWrite(LED, LOW);
        led_on = !led_on;
    }

    // Serial.println(String(delay_time));
    delay (delay_time);
}
