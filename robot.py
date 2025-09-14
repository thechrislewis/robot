#robot.py - lib and class definition for robot control

class Robot:

    #initialize robot
    def __init__(self, ):
        print("Robot Initialized")


    def fwd(self):
        print("Moving Forward")

    def back(self):
        print("Moving Backward")        

    def left(self):
        print("Turning Left")

    def right(self):
        print("Turning Right")

    def stop(self):
        print("Stopping")

# End of robot.py

#test code
if __name__ == "__main__":

    robbie = Robot()
    robbie.fwd()
    robbie.back()
    robbie.left()
    robbie.right()
    robbie.stop()
