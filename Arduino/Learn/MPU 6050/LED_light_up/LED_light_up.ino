// (c) Michael Schoeffler 2017, http://www.mschoeffler.de
// http://www.mschoeffler.de/2017/10/05/tutorial-how-to-use-the-gy-521-module-mpu-6050-breakout-board-with-the-arduino-uno/

#include "Wire.h" // This library allows you to communicate with I2C devices.
#include "math.h" // This library allows you to use trigonometric functions

const int MPU_ADDR = 0x68; // I2C address of the MPU-6050. If AD0 pin is set to HIGH, the I2C address will be 0x69.
const int LED1 = 4, LED2 = 5, LED3 = 6, LED4 = 7;

int16_t accelerometer_x, accelerometer_y, accelerometer_z; // variables for accelerometer raw data

char tmp_str[7]; // temporary variable used in convert function

double g_x = 0, g_y = 0, g_z = 0;
double roll = 0, pitch = 0, yaw = 0;

void setup_mpu();
void retrieve_data();

void setup() {
    setup_mpu();
    Serial.begin(9600);
    pinMode(LED1, OUTPUT);
    pinMode(LED2, OUTPUT);
    pinMode(LED3, OUTPUT);
    pinMode(LED4, OUTPUT);

}
void loop() {
    retrieve_data();

    // Calculate the real acceleration in G's of force
    g_x = accelerometer_x/16384;
    g_y = accelerometer_y/16384;
    g_z = accelerometer_z/16384;

    // Calculate the angle in which the system is in
    roll = asin(g_x);
    pitch = asin(g_y);
    yaw = acos(g_z);
    
    Serial.print("Roll = "); Serial.print(int(roll)); Serial.print("."); Serial.print(int(-int(roll)*1000 + roll*1000));
    Serial.print("\t| Pitch = "); Serial.print(int(pitch)); Serial.print("."); Serial.print(int(-int(pitch)*1000 + pitch*1000));
    Serial.print("\t| Yaw = "); Serial.print(int(yaw)); Serial.print("."); Serial.println(int(-int(yaw)*1000 + yaw*1000));
    //It is really g_y / 1, but the 1 can be ommited in each case

    // Light up the LEDs appropriately
    if(roll > M_PI/4){
        digitalWrite(LED1, LOW);
        digitalWrite(LED2, HIGH);
        digitalWrite(LED3, HIGH);
        digitalWrite(LED4, LOW);
    }
    else if(roll < -M_PI/4){
        digitalWrite(LED1, HIGH);
        digitalWrite(LED2, LOW);
        digitalWrite(LED3, LOW);
        digitalWrite(LED4, HIGH);
    }
    else if(pitch > M_PI/4){
        digitalWrite(LED1, LOW);
        digitalWrite(LED2, LOW);
        digitalWrite(LED3, HIGH);
        digitalWrite(LED4, HIGH);
    }
    else if(pitch < -M_PI/4){
        digitalWrite(LED1, HIGH);
        digitalWrite(LED2, HIGH);
        digitalWrite(LED3, LOW);
        digitalWrite(LED4, LOW);
    }
    else{
        digitalWrite(LED1, LOW);
        digitalWrite(LED2, LOW);
        digitalWrite(LED3, LOW);
        digitalWrite(LED4, LOW);
    }



    // delay
    delay(50);
}

void setup_mpu(){
    Wire.begin();
    Wire.beginTransmission(MPU_ADDR); // Begins a transmission to the I2C slave (GY-521 board)
    Wire.write(0x6B); // PWR_MGMT_1 register
    Wire.write(0); // set to zero (wakes up the MPU-6050)
    Wire.endTransmission(true);  
}

void retrieve_data(){
    Wire.beginTransmission(MPU_ADDR);
    Wire.write(0x3B); // starting with register 0x3B (ACCEL_XOUT_H) [MPU-6000 and MPU-6050 Register Map and Descriptions Revision 4.2, p.40]
    Wire.endTransmission(false); // the parameter indicates that the Arduino will send a restart. As a result, the connection is kept active.
    Wire.requestFrom(MPU_ADDR, 7*2, true); // request a total of 7*2=14 registers

    // "Wire.read()<<8 | Wire.read();" means two registers are read and stored in the same variable
    accelerometer_x = Wire.read()<<8 | Wire.read(); // reading registers: 0x3B (ACCEL_XOUT_H) and 0x3C (ACCEL_XOUT_L)
    accelerometer_y = Wire.read()<<8 | Wire.read(); // reading registers: 0x3D (ACCEL_YOUT_H) and 0x3E (ACCEL_YOUT_L)
    accelerometer_z = Wire.read()<<8 | Wire.read(); // reading registers: 0x3F (ACCEL_ZOUT_H) and 0x40 (ACCEL_ZOUT_L)

    // Signs based on arrows in sensor
    accelerometer_x = -accelerometer_x;
    accelerometer_y = -accelerometer_y;
    accelerometer_z = -accelerometer_z;
}
