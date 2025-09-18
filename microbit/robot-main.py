#robot.py - lib and class definition for robot control
# using micropython on microbit

# leds are on pin0
# motors are on pin1 and pin2


from microbit import *
from neopixel import NeoPixel
import time


class Robot:

    #initialize robot
    def __init__(self, ):

        # setup leds
        self.pixel_count = 5
        self.leds = NeoPixel(pin0, self.pixel_count)
        self.leds[0] = (255,0,0)
        self.leds[1] = (0,255,0)
        self.leds[2] = (0,0,0)
        self.leds[3] = (0,0,255)
        self.leds[4] = (255,255,0)
        self.leds.show()
        
        #setup servos
        pin1.set_analog_period(20)
        pin2.set_analog_period(20)
        pin1.write_analog(0) # stop
        pin2.write_analog(0) # stop
        
        display.show(Image.HEART)

    def setLeds(self, r, g, b):
        for i in range(self.pixel_count):
            self.leds[i] = (r, g, b)
        self.leds.show()

    def fwd(self):
        display.show(Image.ARROW_N)
        pin1.write_analog(180) # full forward
        pin2.write_analog(180)   # full forward

    def back(self):
        display.show(Image.ARROW_S)
        pin1.write_analog(0) # full forward
        pin2.write_analog(0)   # full forward

        
    def left(self):
        pin1.write_analog(180) # full forward
        pin2.write_analog(0)   # full forward
        display.show(Image.ARROW_W)
        self.leds.clear()
        self.leds[0] = (255,0,0)
        self.leds.show()
        
    def right(self):
        pin1.write_analog(0) # full forward
        pin2.write_analog(180)   # full forward
        display.show(Image.ARROW_E)
        self.leds.clear()
        self.leds[4] = (255,0,0)
        self.leds.show()
        
    def stop(self):
        display.show(Image.SQUARE)
        pin1.write_analog(0) # stop
        pin2.write_analog(0) # stop
        self.setLeds(0,0,0)  # when we control leds inside object then use self

# End of robot.py

#test code
if __name__ == "__main__":

    robbie = Robot() # create robot 'instance'

    run_code = False # don't run robot until button pressed

    while True: # loop forever
        if button_a.is_pressed():
            run_code = True
            # when we control leds outside object, we use Robot 'instance'
            robbie.setLeds(128,128,128) 
        if button_b.is_pressed():
            run_code = False
            robbie.stop()

        # why does the code below takes at least 4 seconds to run before a button press can be checked...
        if run_code: 
            robbie.fwd()
            sleep(1000)
            robbie.back()
            sleep(1000)
            robbie.left()
            sleep(1000)
            robbie.right()
            sleep(1000)
            robbie.stop()
            run_code = False
