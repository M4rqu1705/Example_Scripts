// https://www.arduino.cc/en/Tutorial/HelloWorld
// Include the LiquidCrystal Library; required for this project
#include <LiquidCrystal.h>

// LCD interface pins initialization
const int rs = 12, enable = 11, data4 = 5, data5 = 4, data6 = 3, data7 = 2;

// Instantiate LiquidCrystal object with the pre-selected pins
LiquidCrystal lcd(rs, enable, data4, data5, data6, data7);

void setup() {
  // Set up the LCD's number of columns and rows
  lcd.begin(16, 2);

  // Print message to the LCD
  lcd.print("Como de llamas?");
}

void loop() {
  // Set the to the appropriate column based on the number's width
  if(millis()<10000){
    lcd.setCursor(12,1);  
  }
  else if(millis()<100000){
    lcd.setCursor(11,1);  
  }
  else if(millis()<1000000){
    lcd.setCursor(10,1);  
  }
  
  // Print the number of seconds since arduino reset
  lcd.print(millis()/1000.0);

}
