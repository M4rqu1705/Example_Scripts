// Establish ports 
const unsigned char RED_LED = 11, GREEN_LED = 10, BLUE_LED = 9;

int r = 0, g = 0, b = 0;

void set_color(unsigned char red, unsigned char green, unsigned char blue) {
  while (red != r || green != g || blue != b) {
    if (r < red) r++;
    else if (r > red) r--;

    if (g < green) g++;
    else if (g > green) g--;

    if (b < blue) b++;
    else if (b > blue) b--;

    analogWrite(RED_LED, r);
    analogWrite(GREEN_LED, g);
    analogWrite(BLUE_LED, b);

    delay(10);
  }
  return;
}

void setup() {
  pinMode(RED_LED, OUTPUT);   // Initialize red led pin as an output
  pinMode(GREEN_LED, OUTPUT); // Initialize green led pin as output
  pinMode(BLUE_LED, OUTPUT);  // Initialize blue led pin as output

  analogWrite(RED_LED, r);    // Preset r pin
  analogWrite(GREEN_LED, g);  // Preset g pin
  analogWrite(BLUE_LED, b);   // Preset b pin
}

void loop() {
  set_color(255, 0, 0);     // Red
  set_color(185, 200, 0);   // Orange
  set_color(155, 200, 0);   // Yellow
  set_color(0, 255, 0);     // Green
  set_color(0, 0, 255);     // Blue
  set_color(150, 0, 200);   // Purple
}
