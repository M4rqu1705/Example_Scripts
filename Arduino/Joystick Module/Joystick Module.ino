const int x_joy = A0;
const int y_joy = A1;
const int button_pin  = 2;

void setup() {
  Serial.begin(9600);
  pinMode(x_joy, INPUT);
  pinMode(y_joy, INPUT);

  pinMode(button_pin, INPUT_PULLUP);
  
}

void loop() {
  Serial.print("X Position: ");
  Serial.print((analogRead(x_joy)));
  Serial.print(" |\tY Position: ");
  Serial.print((1024-analogRead(y_joy)));
  Serial.print(" |\tButton: ");
  Serial.println(digitalRead(button_pin));

  delay(100);
}
