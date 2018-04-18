#!/usr/bin/python

import RPi.GPIO as GPIO
import threading

# Other source files
import encoder
import motor
import button

# Init GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# GPIO pin numbers using BCM numbering
pinPWM = 18
pinRev = 4
pinEncA = 2
pinEncB = 3
pinBtnA = 23
pinBtnB = 24

# Setup GPIO pins
GPIO.setup(pinPWM, GPIO.OUT)
GPIO.setup(pinRev, GPIO.OUT)
GPIO.setup(pinEncA, GPIO.IN)
GPIO.setup(pinEncB, GPIO.IN)
GPIO.setup(pinBtnA, GPIO.IN)
GPIO.setup(pinBtnB, GPIO.IN)

# Setup PWM
freq = 1 / 0.003
DC = 25
PWM = GPIO.PWM(pinPWM, freq)

# Other Vars
state = -1 # Should Start Retracted
encoderPos = 0

# Event detection for encoder
GPIO.add_event_detect(Enc_A, GPIO.RISING, callback=encoder.rotation_decode)

try:
    while True:
        inpt = int(input("Extend: 1\nRetract: -1\nEnter Input: "))
        if inpt == 1 and state == -1:
            state = 1
            motor.extend()
        elif inpt == -1 and state == 1:
            state = -1
            motor.retract()
        else:
            print("Invalid input or sheet is already at requested state")
except KeyboardInterrupt:
    GPIO.cleanup()
