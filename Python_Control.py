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



if __name__ == '__main__':
    
    #ds=execfile("Xbox.py").read()
    i=1
    print(gamepad)
    running == True
        #print ds
    x=0
    y=0
       
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
             if event.code==307 and event.value ==1:

                running=False
                break

             if event.code == 0 and event.value != 0:

                    x = event.value-65000/2
                    
             if event.code ==1:
                 
                    y=65000/2-event.value

             angle = angleFromCoordinates(x,y)
	     mag = math.sqrt(math.pow(x,2)+math.pow(y,2))
             print(angle)
	     print(mag)
             #print(x)
             #print(y)
        
        #while angle == 0 or angle == 360:
            
    #GPIO.output(GPIO_ML, GPIO.HIGH)
            
    #while angle == 90:
            
            #GPIO.output(GPIO_ML, GPIO.HIGH)
            
        #while angle == 180:
            
            #GPIO.output(GPIO_ML, GPIO.HIGH)
            
        #while angle == 270:
            
            #GPIO.output(GPIO_ML, GPIO.HIGH)
            
        #while angle > 0 and angle < 90:
            
            #GPIO.output(GPIO_ML, GPIO.HIGH)
            
        #while angle > 90 and angle < 180:
            
            #GPIO.output(GPIO_ML, GPIO.HIGH)
            
        #while angle > 180 and angle < 270:
            
            #GPIO.output(GPIO_ML, GPIO.HIGH)
            
        #while angle > 270 and angle < 360:
            
            #GPIO.output(GPIO_ML, GPIO.HIGH)
        
    #x ,y = joy.rightStick()
        #angle = angleFromCoorinates(x,y)
        
        #while angle == 0 or angle == 360:
            
            #GPIO.output(GPIO_ML, GPIO.HIGH)
            
        #while angle == 90:
            
            #GPIO.output(GPIO_ML, GPIO.HIGH)
            
        #while angle == 180:
            
            #GPIO.output(GPIO_ML, GPIO.HIGH)
            
        #while angle == 270:
            
            #GPIO.output(GPIO_ML, GPIO.HIGH)
            
        #while angle > 0 and angle < 90:
            
            #GPIO.output(GPIO_ML, GPIO.HIGH)
            
        #while angle > 90 and angle < 180:
            
            #GPIO.output(GPIO_ML, GPIO.HIGH)
            
        #while angle > 180 and angle < 270:
            
            #GPIO.output(GPIO_ML, GPIO.HIGH)
            
        #while angle > 270 and angle < 360:
            
            #GPIO.output(GPIO_ML, GPIO.HIGH)
