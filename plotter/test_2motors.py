import RPi.GPIO as GPIO
import time
import sys
import numpy as np

GPIO.setmode(GPIO.BCM)

ControlPin = [ [5,6,13,19],
               [26,16,20,21] ]

for motor in range(len(ControlPin)):
    for pin in ControlPin[motor]:
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
                for motor in range(len(ControlPin)):
                    GPIO.output(ControlPin[motor][pin],seq[halfstep][pin])
            time.sleep(0.001)
    for pin in range(4):
        for motor in range(len(ControlPin)):
            GPIO.output(ControlPin[motor][pin],seq[0][pin])
    time.sleep(0.001)

while True:
    try:

        rotations = input("number of rotations?")
        runStepper(rotations)

    except KeyboardInterrupt:
        break

## KeyboardInterrupt
print("\nSession was interrupted...")
GPIO.cleanup()
print("\nthe program will now shutdown")

sys.exit()
