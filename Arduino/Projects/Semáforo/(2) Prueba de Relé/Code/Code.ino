#define RELAY_PIN 8

int period = 1000;

void setup() {
    pinMode(RELAY_PIN, OUTPUT);
    digitalWrite(RELAY_PIN, HIGH);
    Serial.begin(9600);
}

void loop() {
    digitalWrite(RELAY_PIN, HIGH);
    delay(period/2);
    digitalWrite(RELAY_PIN, LOW);
    delay(period/2);
}
