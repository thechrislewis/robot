#python prog to control robot

# empty functions for fwd, back, left, right,stop
def fwd():
    print("Moving Forward")

def back():
    print("Moving Backward")        

def left():
    print("Turning Left")

def right():
    print("Turning Right")

def stop():
    print("Stopping")

# main function to take user input and call appropriate function
def main():
    while True:
        command = input("Enter command (fwd, back, left, right, stop, exit): ").strip().lower()
        if command == "fwd":
            fwd()
        elif command == "back":
            back()
        elif command == "left":
            left()
        elif command == "right":
            right()
        elif command == "stop":
            stop()
        elif command == "exit":
            print("Exiting program.")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

# End of program

