#!/usr/bin/python

import RPi.GPIO as GPIO
import threading

# Other source files
import encoder
import motor
import button
import pin

def init():
    # Init GPIO
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)

    # Motor reverser
    GPIO.setup(pin.Rev, GPIO.OUT)

    # Encoder pins
    GPIO.setup(pin.EncA, GPIO.IN)
    GPIO.setup(pin.EncB, GPIO.IN)

    # Inputs
    GPIO.setup(pin.BtnA, GPIO.IN)
    GPIO.setup(pin.BtnB, GPIO.IN)
    
    # Setup PWM
    GPIO.setup(pin.PWM, GPIO.OUT)
    PWM = GPIO.PWM(pin.PWM, motor.freq)

    # Event detection for encoder
    GPIO.add_event_detect(pin.EncA, GPIO.RISING, callback=encoder.rotation_decode)

def main():
    encoder.encoderPos = 0
    init()
    #while True:
    #    inpt = int(input("Extend: 1\nRetract: -1\nEnter Input: "))
    #    if inpt == 1 and state == -1:
    #        state = 1
    #        motor.extend()
    #    elif inpt == -1 and state == 1:
    #        state = -1
    #        motor.retract()
    #    else:
    #        print("Invalid input or sheet is already at requested state")
    while True:
        pass

try:
    main()
except KeyboardInterrupt:
    GPIO.cleanup()
