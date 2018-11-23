// Tutorial from https://learn.sparkfun.com/tutorials/connecting-arduino-to-processing/all

import processing.serial.*;

Serial myPort; 

String val = "";
  String[] temp = {"","", ""};
  int[] values = {0, 0, 0};

int[] get_ints(){
  
  if (myPort.available() > 0) {  // If data is available,
    val = myPort.readStringUntil('\n');         // read it and store it in val
    if(val!=null){
      temp = val.split(",");
      for(int c = 0; c<temp.length; c++){
        try{
          values[c] = Integer.parseInt(temp[c].replaceAll("\\s",""));
        }
        catch(Exception e){
          print("**Error ");
          println(e);
        }    
      }
    }
  } 
  return(values);
}

void setup()
{
  String portName = Serial.list()[0]; // COM4 
  myPort = new Serial(this, portName, 9600);
  size(200,200);
}

void draw(){
  int[] colors = get_ints();
  fill(map(colors[0], 0, 1023, 0, 255), map(colors[1], 250, 800, 0, 255), map(colors[2], 500, 470, 0, 255));
  rect(25, 25, 150, 150);
}
