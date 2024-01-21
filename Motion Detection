#Basic Python script to detect if motion is detected by a PIR sensor.

import RPi.GPIO as GPIO
import time

# Declare pin
pir = 27

# Setup GPIO inputs and outputs
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir,GPIO.IN)
time.sleep(45)
try:
    while True:
        if(GPIO.input(pir)):
            print("Motion Detected!")
        else:
            print("No Motion Detected!")
        time.sleep(1)

# Gracefully cleanup and free the GPIO when user terminates the program by pressing Ctrl-C
except KeyboardInterrupt:
    print("Stopping")
    GPIO.cleanup()
