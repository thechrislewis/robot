# control 2 motors with microbit

# motor1  on pin1
# motor2  on pin2

from microbit import *
import time
    
def main():
    motor_pin1 = pin1  # left motor
    motor_pin1.set_analog_period(20)  # Set the PWM period to 20ms
    motor_pin1.write_analog(0)      # Stop the motor (neutral position)
    
    #run motor forward at full speed 
    motor_pin1.write_analog(1023)
    
    motor_pin2 = pin2  # right motor
    motor_pin2.set_analog_period(20)  # Set the PWM period to 20ms
    motor_pin2.write_analog(0)      # Stop the motor (neutral position)
    
    #run motor forward at full speed 
    motor_pin2.write_analog(1023)
       
    
if __name__ == "__main__":
    main()
    