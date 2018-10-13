const unsigned char RED_LED = 11, GREEN_LED = 10, BLUE_LED = 9;


void setup() {
  pinMode(RED_LED, OUTPUT);
  pinMode(GREEN_LED, OUTPUT);
  pinMode(BLUE_LED, OUTPUT);

  analogWrite(RED_LED, 0);
  analogWrite(GREEN_LED, 0);
  analogWrite(BLUE_LED, 0);

  Serial.begin(9600);
}

void loop() {
  byte red_intensity = 0, green_intensity = 0, blue_intensity = 0;

  for (int i = 0; i < 6; i++) {
    switch (i) {
      case 0:
        red_intensity = 255;
        green_intensity = 0;
        blue_intensity = 0;
        break;
      case 1:
        red_intensity = 235;
        green_intensity = 255;
        blue_intensity = 0;
        break;
      case 2:
        red_intensity = 200;
        green_intensity = 255;
        blue_intensity = 0;
        break;
      case 3:
        red_intensity = 0;
        green_intensity = 255;
        blue_intensity = 0;
        break;
      case 4:
        red_intensity = 0;
        green_intensity = 0;
        blue_intensity = 255;
        break;
      case 5:
        red_intensity = 150;
        green_intensity = 0;
        blue_intensity = 200;
        break;

    }

    analogWrite(RED_LED, red_intensity);
    analogWrite(GREEN_LED, green_intensity);
    analogWrite(BLUE_LED, blue_intensity);
    delay(1000);
  }
}
