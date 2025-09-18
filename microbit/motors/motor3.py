# Intro to classes

from microbit import *
import time

class Motors:
    
    def __init__(self, pin1, pin2):
        self.pin1 = pin1
        self.pin2 = pin2
        
        self.pin1.set_analog_period(20)  # Set the PWM period to 20ms
        self.pin2.set_analog_period(20)  # Set the PWM period to 20ms

        self.pin1.write_analog(0)      # Stop the motor (neutral position)
        self.pin2.write_analog(0)      # Stop the motor (neutral position)
        

if __name__ == "__main__":  # only run this code if this file is run directly      
    my_motors = Motors(pin1, pin2)

