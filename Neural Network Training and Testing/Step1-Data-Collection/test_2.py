from MotorModule import Motor
import KeypressModule as kp
import cv2
import time

# Import image capture and logging functions
from DataCollectionModule import saveData, saveLog

# Initialize motor and keypad modules
motor = Motor(20, 21, 4, 17, 22, 27)
kp.init()

# Function to control motor based on keypress
def main():
    if kp.getKey('UP'):
        # Save image and steering angle
        _, img = cap.read()
        saveData(img, 0.6)
        
        # Move motor forward
        motor.move(0.6, 0, 0.1)
        
    elif kp.getKey('DOWN'):
        # Save image and steering angle
        _, img = cap.read()
        saveData(img, -0.6)
        
        # Move motor backward
        motor.move(-0.6, 0, 0.1)
        
    elif kp.getKey('LEFT'):
        # Save image and steering angle
        _, img = cap.read()
        saveData(img, 0.5)
        
        # Move motor left
        motor.move(0.5, 0.3, 0.1)
        
    elif kp.getKey('RIGHT'):
        # Save image and steering angle
        _, img = cap.read()
        saveData(img, -0.5)
        
        # Move motor right
        motor.move(0.5, -0.3, 0.1)
        
    else:
        # Stop motor
        motor.stop(0.1)

if __name__ == '__main__':
    # Open video capture device
    cap = cv2.VideoCapture(0)
    
    # Main loop for motor control
    while True:
        main()
        
        # Save log after every iteration
        saveLog()
        
        # Add a small delay to prevent busy looping
        time.sleep(0.1)
