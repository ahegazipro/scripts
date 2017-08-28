#include <Servo.h>  //Load Servo Library
/* MOTORS */
//All motors should have the same speed so will connect All PWMs to one pin //pin 3
const byte pinPwm = 5;
//DIRECTION PIN // CW LOW , CCW HIGH
//motor 1 [TOP RIGHT] 
const byte m1Dir = 4;
//motor 1 [TOP LEFT] 
const byte m2Dir = 7;
//motor 1 [Bottom RIGHT] 
const byte m3Dir = 12;
//motor 1 [Bottom LEFT]
const byte m4Dir = 8;

/* PUSH BUTTONS */
const byte pbStop = 2;
const byte pbMod = 3; 
const byte pbSpeed = 0;
const byte pbUp = 1;
const byte pbDown = 11;
const byte pbLeft = 9;
const byte pbRight = 10;

/* ULTRA SONIC AND SERVO*/
const byte trigPin=13; //Sensor Trig pin connected to Arduino pin 13
const byte echoPin=A0;  //Sensor Echo pin connected to Arduino pin A0
const byte servoControlPin=6; //Servo control line is connected to pin 6

Servo Controller; //setting up a servo motor for moving the ultrasonic
byte servoAngle = 90; //Variable for the value we want to set servo to. DEFAULT looking forward

/* Available Speeds  */
//byte speeds[] = {60, 125, 255};
byte Cspeed = 60; //current speed //  [ 60 - 125 - 255 ] 
/* Available MODS */
byte mod = 0; //1: AUTO , 0: Manual default mod IS manual

/*******************************************************************************
 * FUNCTIONS                                                                    *
 *******************************************************************************/

// The setup routine runs once when you press reset.
void setup() {                
  // Initialize the PWM and DIR pins as digital outputs.
  pinMode(pinPwm, OUTPUT);
  pinMode(m1Dir, OUTPUT);
  pinMode(m2Dir, OUTPUT);
  pinMode(m3Dir, OUTPUT);
  pinMode(m4Dir, OUTPUT);
  //Initialize the Direction pins as inputs.
  pinMode(pbUp, INPUT);
  pinMode(pbDown, INPUT);
  pinMode(pbLeft, INPUT);
  pinMode(pbRight, INPUT);
  pinMode(pbSpeed, INPUT);
  
  pinMode(servoControlPin, OUTPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  
  //Iniyislize the Interrupt pins
  pinMode(pbStop, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(pbStop), stopMoving, RISING);
  pinMode(pbMod, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(pbMod), toggleMod, RISING);

//Attaching the SERVO
  Controller.attach(servoControlPin);
}



// The loop routine runs over and over again forever.
void loop() {
  
   byte spd = digitalRead(pbSpeed);
   if(spd == HIGH){
       changeSpeed();
   }
    if(mod == 1){
      autoMove();
    }else{
      manualMove();  
    }
}
  
void stopMoving(){
  //stopping the motors >> speed = 0;
  analogWrite(pinPwm,0);
  analogWrite(pinPwm,0);
  //stopping the Servo making it look forward
  servoAngle = 90;
  Controller.write(servoAngle);
  //CHANGING MOD TO MANUAL
  mod = 0;
  
}

void toggleMod(){
  if (mod == 0){
     mod = 1;
    }else{
     mod = 0;
    }
}

void changeSpeed(){
    switch (Cspeed) {
        case 60:
          Cspeed = 125;
          break;
        case 125:
          Cspeed = 255;
          break;
        case 255:
          Cspeed = 60;
          break;
        default: 
          Cspeed = 60;
          break;
      }
}

void autoMove(){
    short distF; //forward distance
    short distR; //right distance
    short distL; //left distance
    
  while (1){
    if(mod != 1 ){return;}
    servoAngle = 90; //setting the servo to look forward
    Controller.write(servoAngle); //write servoAngle to the servo
    distF = getDistance();      

/* RIGHT AND LEFT ANGLES SHOULD BE CHANGED DEPENDING ON THE HARDWARE RANGE .. EX: some servos only moves between 15 to 170 Degree */
    servoAngle = 0; //setting the servo to look Right
    Controller.write(servoAngle); //write servoAngle to the servo
    distR = getDistance();      

    servoAngle = 180; //setting the servo to look left
    Controller.write(servoAngle); //write servoAngle to the servo
    distL = getDistance();

    if(distF > distR && distF > distL){
            moveUp();
    }else if (distR > distF && distR > distL){
            moveRight();
    }else if (distL > distR && distL > distF){
            moveLeft();
    }else {
            moveBack();
    }
  }
}


short getDistance(){
    short pingTime;  //time for ping to travel from sensor to target and return
    short Distance;  //time for ping to travel from sensor to target and return
    const short speedOfSound=347; //Speed of sound in meter per second.

    //sending ultrasonic signal 
      digitalWrite(trigPin, LOW); //Set trigger pin low
      delayMicroseconds(2000); //Let signal settle
      digitalWrite(trigPin, HIGH); //Set trigPin high
      delayMicroseconds(15); //Delay in high state
      digitalWrite(trigPin, LOW); //ping has now been sent
      delayMicroseconds(10); //Delay in low state
      
      pingTime = pulseIn(echoPin, HIGH);  //pingTime is presented in microceconds
      pingTime=pingTime/1000000; //convert pingTime to seconds by dividing by 1000000 (microseconds in a second)
      Distance= speedOfSound * pingTime;  //This will be in miles, since speed of sound was miles per hour
      Distance=Distance/2; //Remember ping travels to target and back from target, so you must divide by 2 for actual target distance.
      return Distance;
  }
void manualMove(){
  while(1){
   if(mod != 0 ){return;}
   byte up = digitalRead(pbUp);
   byte down = digitalRead(pbDown);
   byte right = digitalRead(pbRight);
   byte left = digitalRead(pbLeft); 
  
    if( up == HIGH ){
      moveUp();
    }else if(down == HIGH ){
      moveBack();
    }else if( right == HIGH ){
      moveRight();
    }else if( left == HIGH ){
      moveLeft();
    }else {
      stopMoving();
    }
  }
}



void moveUp(){
//Speed 
  analogWrite(pinPwm, Cspeed);
//CW 
  digitalWrite(m1Dir,LOW);
  digitalWrite(m2Dir,LOW);
  digitalWrite(m3Dir,LOW);
  digitalWrite(m4Dir,LOW);  
}

void moveBack(){
  //Speed 
  analogWrite(pinPwm, Cspeed);
//CCW 
  digitalWrite(m1Dir,HIGH);
  digitalWrite(m2Dir,HIGH);
  digitalWrite(m3Dir,HIGH);
  digitalWrite(m4Dir,HIGH);

}

void moveRight(){
  //Speed 
  analogWrite(pinPwm, Cspeed);
//Right [top/bottom]  motors move CW 
//Left [top/bottom]  motors move CCW 
  digitalWrite(m1Dir,HIGH);
  digitalWrite(m2Dir,LOW);
  digitalWrite(m3Dir,HIGH);
  digitalWrite(m4Dir,LOW);
}

void moveLeft(){
    //Speed 
  analogWrite(pinPwm, Cspeed);
//Left [top/bottom]  motors move CW 
//Right [top/bottom]  motors move CCW 
  digitalWrite(m1Dir,LOW);
  digitalWrite(m2Dir,HIGH);
  digitalWrite(m3Dir,LOW);
  digitalWrite(m4Dir,HIGH);
}

