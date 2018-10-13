// Code based from https://howtomechatronics.com/tutorials/arduino/ultrasonic-sensor-hc-sr04/

const unsigned char echo_pin = 9, trig_pin = 10;  // Defines pins numbers

// defines variables
unsigned long duration;
unsigned int distance;

void setup() {
  pinMode(trig_pin, OUTPUT);  // Sets the tigger pin as an Output
  pinMode(echo_pin, INPUT);   // Sets the echo pin as an Input
  Serial.begin(9600);         // Starts the serial communication
}
void loop() {
  // Clears the trigPin
  digitalWrite(trig_pin, LOW);
  delayMicroseconds(2);

  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trig_pin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig_pin, LOW);

  duration = pulseIn(echo_pin, HIGH);   // Reads the echoPin, returns the sound wave travel time in microseconds

  distance = duration * 0.034 / 2;      // Calculating the distance
  distance = round(distance * 0.393701);

  if (distance < 859){
    // Prints the distance on the Serial Monitor
    String output = "Distance: " + String(distance) + " inches";
    Serial.println(output);
  }
  else{
    Serial.println("Unknown");  
  }

  delay(10);
}
