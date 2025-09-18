# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
old = None # Variable to store the last gesture
while True:

    gesture = accelerometer.current_gesture()
    if gesture == old:
        continue
    display.scroll(gesture)
    old = gesture