
import RPi.GPIO as GPIO
import threading
import pin

class Encoder:
    def __init__(self, pinA, pinB, initPos):
        self.chanA=pinA
        self.chanB=pinB
        GPIO.setup(pinA, GPIO.IN)
        GPIO.setup(pinB, GPIO.IN)
        GPIO.add_event_detect(self.chanA, GPIO.BOTH, callback=self.setArising)
        GPIO.add_event_detect(self.chanB, GPIO.RISING, callback=self.decode)
        self.encoderPos = initPos
        self.lastA = False

    def __del__(self):
        GPIO.remove_event_detect(self.chanA)
        GPIO.cleanup(self.chanA)
        GPIO.cleanup(self.chanB)

    def setArising(self, chan):
        self.lastA = not self.lastA

    def decode(self, chan):
        if not self.lastA:
            self.encoderPos += 1
            print("cw")
        else:
            self.encoderPos -= 1
            print("ccw")
