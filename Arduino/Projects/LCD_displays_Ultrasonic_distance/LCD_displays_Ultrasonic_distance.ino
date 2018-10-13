// Include the LiquidCrystal Library required for the LCD
#include <LiquidCrystal.h>

// Include the Median Filter libary required to filter the noisy values of the Ultrasonic Range finder
#include <MedianFilter.h>

// LCD interface pin assignment
const unsigned char rs = 12, enable = 11, data_4 = 5, data_5 = 4, data_6 = 3, data_7 = 2;

// Utrasonic range finder pin assignment
const unsigned char echo_pin = 10, trig_pin = 9;

// Variable definitions for the ultrasonic range finder
unsigned long duration;
float distance, previous_distance, _speed;

// Instantiate LiquidCrystal object with the pre-selected pins
LiquidCrystal lcd(rs, enable, data_4, data_5, data_6, data_7);

// Instantiate MedianFilter object with filter size of 9 elements and preset of 0
MedianFilter distance_filter(11, 0);
MedianFilter _speed_filter(7, 0);

void setup() {
  // Set the trigger pin as an output
  pinMode(trig_pin, OUTPUT);
  // Set the echo pin as input
  pinMode(echo_pin, INPUT);
  
  // Set up the LCD's number of columns and rows
  lcd.begin(16, 2);

  Serial.begin(9600);

  // Print a string to make the intention of the display clear
  lcd.print("Distancia - Vel");
}

void loop() {

  
  // Clears the trigPin
  digitalWrite(trig_pin, LOW);
  delayMicroseconds(2);

  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trig_pin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig_pin, LOW);

  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echo_pin, HIGH); 

  // Calculating the distance
  distance = duration * 0.034 / 2;
  distance = distance * 0.393701; //Convert to inches

  // Filter distance
  distance_filter.in(distance*10.0);

    // Calculating the speed
  _speed = ((distance_filter.out()/10.0) - (previous_distance))/0.05;
  _speed_filter.in(_speed*10.0);
  
  lcd.setCursor(0,1); 
  
  if(distance_filter.out()/10.0<10){ 
    lcd.print("     ");
    lcd.print(round(distance_filter.out()/10.0));
    lcd.print("   ");
  }
  else if(distance_filter.out()/10.0<100){
    lcd.print("    ");
    lcd.print(round(distance_filter.out()/10.0));
    lcd.print("   ");
  }
  else if(distance_filter.out()/10.0<859){
    lcd.print("   ");
    lcd.print(round(distance_filter.out()/10.0));
    lcd.print("   ");
  }
  else{
    lcd.print("Unknown  ");
  }

  lcd.setCursor(11,1);
  if(fabs(_speed_filter.out()/10.0) < 10.0){
    lcd.print("  ");
    lcd.print(fabs(_speed_filter.out()/10.0));  
    lcd.print("      ");
  } 
  else if(fabs(_speed_filter.out()/10.0) < 100.0){
    lcd.print(" ");
    lcd.print(fabs(_speed_filter.out()/10.0));  
    lcd.print("      ");  } 
  else if(fabs(_speed_filter.out()/10.0) < 1000.0){
    lcd.print(fabs(_speed_filter.out()/10.0));  
    lcd.print("      ");
  }
  
  

  previous_distance = distance_filter.out()/10.0;
  delay(50);
}
