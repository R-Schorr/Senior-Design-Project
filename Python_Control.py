import RPi.GPIO as GPIO
import math
import re
import sys
import select
import atexit
import termios
import optparse
import time
import re
import sys
import select
import atexit
import termios
import optparse
import os

from evdev import ecodes, list_devices, AbsInfo, InputDevice, categorize, events


#######################################################################################################################################################


# DEFINITIONS:
gamepad=InputDevice('/dev/input/event0')

running = True
 
GPIO_FM = 13
GPIO_FR = 15
GPIO_FL = 11
 
GPIO_MM = 31
GPIO_MR = 33
GPIO_ML = 29
 
GPIO_BM = 38
GPIO_BR = 40
GPIO_BL = 36
 

#######################################################################################################################################################


# ANGLE DETERMINATION FUNCTION:

def angleFromCoordinates(x,y):
 
   angle = 0.0
   
   if x==0 and y>0:

      angle = 90

   elif x==0 and y<0:

      angle = 180
      
   elif x<0:

      angle = math.degrees(math.atan(y/x))+180

   elif x>0 and y<0: 

        angle = math.degrees(math.atan(y/x))+360

   elif x>0 and y>0:

	angle = math.degrees(math.atan(y/x))

   return angle


#######################################################################################################################################################


# MAIN CODE:
if __name__ == '__main__':
    
    #ds=execfile("Xbox.py").read()
    i=1
    print(gamepad)
    running == True
        #print ds
    x=0
    y=0


    # WHILE RUNNING:
    for event in gamepad.read_loop():

           #print(categorize(event))
             #print(event.value)
             #print(event.code)
             print('\n')
             # print(event.code)
             # print(events.AbsEvent.event)
             absevent=categorize(event)
          #  print(ecodes.bytype[absevent.event.type][absevent.event.code],absevent.event.value)
             i=i+1


#######################################################################################################################################################


# X BUTTON (BREAKS CODE):
             if event.code==307 and event.value ==1:

                running=False
                break


#######################################################################################################################################################


# LEFT JOYSTICK (YAW AND PITCH [ATTITUDE]):
             if event.code == 0 and event.value != 0:

                    x_left = event.value-65000/2
                    
             if event.code ==1:
                 
                    y_left =65000/2-event.value

             angle_left = angleFromCoordinates(x_left,y_left)
	     mag_left = math.sqrt(math.pow(x_left,2)+math.pow(y_left,2))
             print(angle_left)
	     print(mag_left)

# Joystick neutral = do nothing
# Joystick forward = pitch forward (negative y moment) = fire both attitude thrusters into negative z axis
# Joystick backward = picth backward (positive y moment) = fire both attitude thrusters into positive z axis
# Joystick right = yaw right (positive z moment) = fire attitude thruster into positive y axis
# Joystick left = yaw left (negative z moment) = fire attitude thruster ionto negative y axis

        
             if angle_left == 0 or angle_left == 360:
            
                GPIO.output(GPIO_ML, GPIO.HIGH)

             elif angle_left != 0 or angle_left != 360:

               GPIO.output(GPIO_ML, GPIO.LOW)
            
             if angle_left == 90:
            
               GPIO.output(GPIO_ML, GPIO.HIGH)

             elif angle_left != 90:

               GPIO.output(GPIO_ML, GPIO.LOW)               
            
             if angle_left == 180:
            
               GPIO.output(GPIO_ML, GPIO.HIGH)

	     elif angle_left != 180:

                GPIO.output(GPIO_ML, GPIO.LOW)
            
             if angle_left == 270:
            
                  GPIO.output(GPIO_ML, GPIO.HIGH)

      	     elif angle_left != 270:

                   GPIO.output(GPIO_ML, GPIO.LOW)
            
             if angle_left > 0 and angle_left < 90:
            
                  GPIO.output(GPIO_ML, GPIO.HIGH)
               
             elif angle_left < 0 and angle_left > 90:
            
                  GPIO.output(GPIO_ML, GPIO.LOW)

             if angle_left > 90 and angle_left < 180:
            
                  GPIO.output(GPIO_ML, GPIO.HIGH)

             elif angle_left > 90 and angle_left < 180:
            
                  GPIO.output(GPIO_ML, GPIO.LOW)
            
             if angle_left > 180 and angle_left < 270:
            
               GPIO.output(GPIO_ML, GPIO.HIGH)

             elif angle_left < 180 and angle_left > 270:
            
               GPIO.output(GPIO_ML, GPIO.LOW)
                         
             if angle_left > 270 and angle_left < 360:
            
               GPIO.output(GPIO_ML, GPIO.HIGH)

             elif angle_left > 270 and angle_left < 360:
            
               GPIO.output(GPIO_ML, GPIO.LOW)

#######################################################################################################################################################


# RIGHT JOYSTICK (FORWARD AND UP MOTION [TRANSLATIONAL]):
	     if event.code == 2:

                    x_right = event.value-65000/2
                    
             if event.code ==5:
                 
                    y_right =65000/2-event.value

             angle_right = angleFromCoordinates(x_right,y_right)
	     mag_right = math.sqrt(math.pow(x_right,2)+math.pow(y_right,2))
             print(angle_right)
	     print(mag_right)

# Joystick right/left = do nothing different
# Joystick neutral = fire two translational thrusters into negative z axis and fire negative x translational thrusters
# Joystick forward = fire all four translational thrusters into negative z axis and fire negative x translational thrusters
# Joystick backward = only fire negative x translational thrusters


#######################################################################################################################################################


# ROLLING (BUMPERS):
	     if event.code==310 and event.value ==1:
		    left_bump = 1;

	     if event.code==311 and event.value ==1:
		    right_bump = 1;


# Left bumper = for 1 second, (looking at back surface) fire left attitude trhuster into positive z axis and right attitude thruster into negative z axis
# Right bumper = for 1 second, (looking at back surface) fire right attitude trhuster into positive z axis and left attitude thruster into negative z axis


#######################################################################################################################################################


             #print(x)
             #print(y)
