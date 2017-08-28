# Arduino Robot Controller [ARC]
An arduino program controlles a 4-wheel robot. 

## This robot has the following specifications:  
1.	A joystick consisting of 7push buttons :
     - 4 push buttons for the directions 
     - 1 for the mode of operation
     - 1 to stop the robot
     - 1 to choose to mode of the speed
2. There are two modes of operation:
	- Manual-mode: In this mode the robot is controlled using the joystick
	- Automatic-mode: In this mode the robot must avoid any obstacle in its way, and when found, it must choose clearest way to go.
3.	Three speed modes (60-125-255)
4.	 Each wheel is coupled to a DC Motor. The motors are controlled by 2 Dual Channel Cytron motor drivers, each driver can control both motor RPM and direction of rotation. The RPM is controlled by applying a PWM signal to the PWM pin of the corresponding motor. The direction of rotation is controlled by either applying a logic HIGH(1) or a logic LOW(0) to the direction pin of the corresponding motor.  
5. For the Automatic mode, the robot has a servo motor and an ultra-sonic sensor mounted above it.
6. For manual mode, if no push button is pressed, the robot must stop. 
   
## How to use it
- Just compile the code using arduino IDE and upload it to your KIT.
- Don't forget to connect the pins correctly as showed in the code comments.
 
## Algorithm
1. By default the robot is set in manual mode so it'll not move until direction button is pressed.
2. First we are checking for speed change and toggeling it.
3. Then we check the mod and run the moving function depending on the mode [manual 0 / auto 1]
4. In the manual mode we check for the direction push button press and move depending on it.
	- Forward :  all motor move forward [CW].
	- Backward : all motors move backward [CCW].
	- Right : right motors move backward [CCW] and left motors move farward [CW].
	- Left : left motors move backward [CCW] and right motors move farward [CW].
5. In the automatic mode we use the servo and ultrasonic sensor to check for barriers around us.
	- we check the distance in all 3 direction [front - right - left] then compare them and choose the direction depending on them.
6. Using two interrupts to Stop and toggle the mode.	
	
	
##### [ARDUINO UNO] Sketch uses 3496 bytes (10%) of program storage space. Maximum is 32256 bytes.

- You can get the source code and build it using any arduino IDE at [src](src/robot) directory.
- You can get a compiled hex file [bin](bin) directory.

###### * NOTE * this code is not tested physically.

###### Have any question or request .. 
Contact ME: Ahmad Hegazy <ahegazipro@gmail.com>
