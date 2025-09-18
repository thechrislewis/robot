# Imports go at the top
from microbit import *
import neopixel

pixel_count = 5
np = neopixel.NeoPixel(pin0, pixel_count)

np[0] = (255,0,0)
np[1] = (0,255,0)
np[3] = (0,0,255)
np[4] = (255,255,0)
np.show()

# Code in a 'while True:' loop repeats forever
old = None
while True:

    gesture = accelerometer.current_gesture()
    if gesture == old:
        sleep(10)
        continue
    #display.scroll(gesture)
    if (gesture == "face up"):
        np.clear()
    elif (gesture == "up"):
        for pixel in range(pixel_count):
            np[pixel] = (255,0,0)
        np.show()
        
    old = gesture


   
