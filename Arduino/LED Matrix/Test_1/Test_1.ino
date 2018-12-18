
// Wiring from tutorial at http://osoyoo.com/2017/01/03/arduino-16x16-matrix/
// Code from tutorial at https://www.hackster.io/Treebug842/16x16-led-matrix-display-012b1e
// Instructinal link to read at https://www.sparkfun.com/sparkx/blog/2650
//*

#include <Arduino.h>

#define MATRIX_LAT 2
#define MATRIX_CLK 3
#define MATRIX_DI 4
#define MATRIX_G 5
#define MATRIX_A 6
#define MATRIX_B 7
#define MATRIX_C 8
#define MATRIX_D 9


unsigned char Display_Buffer[2];
unsigned char Word1[32];
unsigned long initial_time = millis();

const bool SCENE_ALL_ON[16][16] = 
{
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
};

const bool SCENE_ALL_OFF[16][16] = 
{
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
};

bool Scene[16][16] = 
{
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
};

void Scan_Line(unsigned int m);
void Send(unsigned int dat);
void ClearWorld();
void SceneToWorld();
void Update();
void Draw(bool image[16][16], int time_millis);



void setup() {
    Serial.begin(9600);

    pinMode(MATRIX_LAT, OUTPUT);
    pinMode(MATRIX_CLK, OUTPUT);
    pinMode(MATRIX_DI, OUTPUT);
    pinMode(MATRIX_G, OUTPUT);
    pinMode(MATRIX_A, OUTPUT);
    pinMode(MATRIX_B, OUTPUT);
    pinMode(MATRIX_C, OUTPUT);
    pinMode(MATRIX_D, OUTPUT);

}

void loop() {
    Draw(SCENE_ALL_ON, 1000);
    Draw(SCENE_ALL_OFF, 1000);
    bool temp[16][16] =  
{
    {0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1},
    {1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
    {1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1},
    {0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0},
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1},
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1},
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1},
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1},
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1},
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1},
    {1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0}
};

    Draw(temp, 1000);




}


//-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=

void Draw(bool image[16][16], int time_millis){
  for(int row = 0; row<16; row++)
      for(int column = 0; column<16; column++)
        Scene[row][column] = image[row][column];
    Update();
    initial_time = millis();
    while(millis()-initial_time < time_millis){
      Display(Word1);
    }
}


void Update(){
    ClearWord();
    SceneToWord();
}

void ClearWord(){
    for(unsigned char i = 0; i < 32; i++)
        Word1[i] = 0;
}



void SceneToWord(){
    // Interpret each of the scene's row as bits of a byte and
    // turn them into a character

    //*
    unsigned char temp;
    for(unsigned char i = 0; i<16; i++){
        for(unsigned char k = 0; k<16; k++){
            if(i < 8){
                temp = Scene[i][k] << (7 - i);
                Word1[15 - k] += temp;
            } 
            else {
                temp = Scene[i][k] << (15 - i);
                Word1[31 - k] += temp;
            }
        }
    }
    //*/
}


void Display(unsigned char dat[]){

    // Dat is Word1

    for(unsigned char i = 0 ; i < 16 ; i++ ){
        digitalWrite(MATRIX_G, HIGH);   

        Display_Buffer[0] = dat[i];   
        Display_Buffer[1] = dat[i+16];

        Send(Display_Buffer[1]);
        Send(Display_Buffer[0]);

        digitalWrite(MATRIX_LAT, HIGH);          
        delayMicroseconds(1);

        digitalWrite(MATRIX_LAT, LOW);
        delayMicroseconds(1);

        Scan_Line(i);             

        digitalWrite(MATRIX_G, LOW);

        delayMicroseconds(100);   
    } 
}


void Scan_Line( unsigned char m) { 
    switch(m)
    {
        case 0:     
            digitalWrite(MATRIX_D, LOW);digitalWrite(MATRIX_C, LOW);digitalWrite(MATRIX_B, LOW);digitalWrite(MATRIX_A, LOW);          
            break;
        case 1:         
            digitalWrite(MATRIX_D, LOW);digitalWrite(MATRIX_C, LOW);digitalWrite(MATRIX_B, LOW);digitalWrite(MATRIX_A, HIGH);     
            break;
        case 2:         
            digitalWrite(MATRIX_D, LOW);digitalWrite(MATRIX_C, LOW);digitalWrite(MATRIX_B, HIGH);digitalWrite(MATRIX_A, LOW);     
            break;
        case 3:         
            digitalWrite(MATRIX_D, LOW);digitalWrite(MATRIX_C, LOW);digitalWrite(MATRIX_B, HIGH);digitalWrite(MATRIX_A, HIGH);    
            break;
        case 4:
            digitalWrite(MATRIX_D, LOW);digitalWrite(MATRIX_C, HIGH);digitalWrite(MATRIX_B, LOW);digitalWrite(MATRIX_A, LOW);     
            break;
        case 5:
            digitalWrite(MATRIX_D, LOW);digitalWrite(MATRIX_C, HIGH);digitalWrite(MATRIX_B, LOW);digitalWrite(MATRIX_A, HIGH);    
            break;
        case 6:
            digitalWrite(MATRIX_D, LOW);digitalWrite(MATRIX_C, HIGH);digitalWrite(MATRIX_B, HIGH);digitalWrite(MATRIX_A, LOW);    
            break;
        case 7:
            digitalWrite(MATRIX_D, LOW);digitalWrite(MATRIX_C, HIGH);digitalWrite(MATRIX_B, HIGH);digitalWrite(MATRIX_A, HIGH);     
            break;
        case 8:
            digitalWrite(MATRIX_D, HIGH);digitalWrite(MATRIX_C, LOW);digitalWrite(MATRIX_B, LOW);digitalWrite(MATRIX_A, LOW);     
            break;
        case 9:
            digitalWrite(MATRIX_D, HIGH);digitalWrite(MATRIX_C, LOW);digitalWrite(MATRIX_B, LOW);digitalWrite(MATRIX_A, HIGH);    
            break;  
        case 10:
            digitalWrite(MATRIX_D, HIGH);digitalWrite(MATRIX_C, LOW);digitalWrite(MATRIX_B, HIGH);digitalWrite(MATRIX_A, LOW);    
            break;
        case 11:
            digitalWrite(MATRIX_D, HIGH);digitalWrite(MATRIX_C, LOW);digitalWrite(MATRIX_B, HIGH);digitalWrite(MATRIX_A, HIGH);     
            break;
        case 12:
            digitalWrite(MATRIX_D, HIGH);digitalWrite(MATRIX_C, HIGH);digitalWrite(MATRIX_B, LOW);digitalWrite(MATRIX_A, LOW);    
            break;
        case 13:
            digitalWrite(MATRIX_D, HIGH);digitalWrite(MATRIX_C, HIGH);digitalWrite(MATRIX_B, LOW);digitalWrite(MATRIX_A, HIGH);     
            break;
        case 14:
            digitalWrite(MATRIX_D, HIGH);digitalWrite(MATRIX_C, HIGH);digitalWrite(MATRIX_B, HIGH);digitalWrite(MATRIX_A, LOW);     
            break;
        case 15:
            digitalWrite(MATRIX_D, HIGH);digitalWrite(MATRIX_C, HIGH);digitalWrite(MATRIX_B, HIGH);digitalWrite(MATRIX_A, HIGH);    
            break;
        default : break;  
    }
}


void Send( unsigned char dat) {

    digitalWrite(MATRIX_CLK, LOW);
    delayMicroseconds(1);  
    digitalWrite(MATRIX_LAT, LOW);
    delayMicroseconds(1);

    for(unsigned char i = 0 ; i < 8 ; i++ ){
        if( dat & 0x01 ){
            digitalWrite(MATRIX_DI, HIGH);  
        }
        else{
            digitalWrite(MATRIX_DI, LOW);
        }

        delayMicroseconds(1);
        digitalWrite(MATRIX_CLK, HIGH);         
        delayMicroseconds(1);
        digitalWrite(MATRIX_CLK, LOW);
        delayMicroseconds(1);   
        dat >>= 1;

    }     
}



//*/
