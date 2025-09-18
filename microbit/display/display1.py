#import microbit libraries
from microbit import *



microbit.display.scroll('Hello!', wait=False, loop=True)
sleep(3000)

old_gesture = None # Variable to store the last gesture
while True:

    gesture = accelerometer.current_gesture()
    
    if gesture == old_gesture:
        sleep(10) # sleep 10 milliseconds to avoid busy loop
        continue
    old_gesture = gesture
    
    display.scroll(gesture)
    sleep(1000) 
    display.clear()
    sleep(1000)
    