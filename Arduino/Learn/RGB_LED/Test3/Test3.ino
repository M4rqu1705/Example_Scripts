byte HSV_to_RGB(double h, double s, double v)
{
  byte r,g,b;
  int i;
  double f, p, q, t;

  // Clamp values
  h = max(0.0, min(360.0, h));
  s = max(0.0, min(100.0, s));
  v = max(0.0, min(100.0, v));

  s /= 100;
  v /= 100;

  if (s == 0) {
    // Achromatic (grey)
    r = g = b = byte(round(v * 255));
    //Serial.println(String(String(*r) + " " + String(*g) + " " + String(*b)));
    return;
  }

  h /= 60; // sector 0 to 5
  i = floor(h);
  f = h - i; // factorial part of h
  p = v * (1 - s);
  q = v * (1 - s * f);
  t = v * (1 - s * (1 - f));

  switch (i) {
    case 0:
      r = byte(round(255 * v));
      g = byte(round(255 * t));
      b = byte(round(255 * p));
      break;
    case 1:
      r = byte(round(255 * q));
      g = byte(round(255 * v));
      b = byte(round(255 * p));
      break;
    case 2:
      r = byte(round(255 * p));
      g = byte(round(255 * v));
      b = byte(round(255 * t));
      break;
    case 3:
      r = byte(round(255 * p));
      g = byte(round(255 * q));
      b = byte(round(255 * v));
      break;
    case 4:
      r = byte(round(255 * t));
      g = byte(round(255 * p));
      b = byte(round(255 * v));
      break;
    default: // case 5:
      r = byte(round(255 * v));
      g = byte(round(255 * p));
      b = byte(round(255 * q));
  }
  //Serial.println(String(String(*r) + " " + String(*g) + " " + String(*b)));
  byte rgb[] = {r, g, b};
  return *rgb;
}

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

  for (int hue = 0; hue < 256; hue++) {
    byte *rgb = HSV_to_RGB(hue, 255, 127);
    
    Serial.println(String(String(rgb[0]) + " " + String(rgb[1]) + " " + String(rgb[2])));

    analogWrite(RED_LED, rgb[0]);
    analogWrite(GREEN_LED, rgb[1]);
    analogWrite(BLUE_LED, rgb[2]);
    delay(10);
  }
}
