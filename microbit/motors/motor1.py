# motor1 
# MicroPython for the micro:bit
# Control a continuous rotation servo motor

# motor1  on pin1

from microbit import *
import time
    
def main():
    motor_pin = pin1  # Use pin1 for the motor
    
    motor_pin.set_analog_period(20)  # Set the PWM period to 20ms
    motor_pin.write_analog(0)      # Stop the motor (neutral position)
    
    #run motor forward at full speed 
    motor_pin.write_analog(1023)
       
    
if __name__ == "__main__":
    main()
    