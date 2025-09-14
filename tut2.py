#use robot class from robot.py to control robot
from robot import Robot

def main():
    robbie = Robot()
    while True:
        command = input("Enter command (fwd, back, left, right, stop, exit): ").strip().lower()
        if command == "fwd":
            robbie.fwd()
        elif command == "back":
            robbie.back()
        elif command == "left":
            robbie.left()
        elif command == "right":
            robbie.right()
        elif command == "stop":
            robbie.stop()
        elif command == "exit":
            print("Exiting program.")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

# End of program