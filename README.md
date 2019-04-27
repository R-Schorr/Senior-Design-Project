# Senior-Design-Project
Code of Demonstrator 
Python Code for Senior Design Project
Iowa State University
Aerospace Engineering 462 

The purpose of this code is to control our demonstrator with an Xbox One controller using Evdev on a raspberry pi zero
we remapped the coordinates of the Xbox controller to what believe is the exact center (or at least close enough) 
we have defined our pin-out connections for our solonoid valves based upon the pins that are being used in the raspberry pi
our code is designed to stop at the use of the x botton so that we can end our program instantly in the case that something goes wrong

Our input device is mapped at either /dev/input/event0 or /dev/input/event3 depending on if we have a keyboard and mouse attached or not
