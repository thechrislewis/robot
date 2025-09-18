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



   
