
def rotation_decode(pin_EncA):
    global encoderPos

    BState = GPIO.input(pin_EncB)
    if BState == 0:
        encoderPos += 1
    if BState == 1:
        encoderPos -= 1
