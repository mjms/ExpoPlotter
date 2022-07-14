import RPi.GPIO as GPIO
import time
import numpy as np

GPIO.setmode(GPIO.BCM)

ControlPin = [5,6,13,19]

for pin in ControlPin:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)

seq = [ [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1] ]

def runStepper(rotations):
    cycles = int(np.ceil(512*rotations))

    for i in range(cycles):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(ControlPin[pin],seq[halfstep][pin])
            time.sleep(0.001)
    for pin in range(4):
        GPIO.output(ControlPin[pin],seq[0][pin])
    time.sleep(0.001)


    rotations = input("number of rotations?")
    runStepper(rotations)


GPIO.cleanup()
