
import RPi.GPIO as GPIO
import pin

encoderPos = 0
deployedState = False

def rotation_decode(Edge): 
    BState = GPIO.input(pin.EncB)
    if BState == 0:
        encoderPos += 1
        print("Clockwise Rotation: ", encoderPos)
    if BState == 1:
        encoderPos -= 1
        print("Counterclockwise Rotation: ", encoderPos)
