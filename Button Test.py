#Simple script that prints "Button was pressed" if a button is attached properly to a GPIO pin.

import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM) # Use Broadcom pin numbering
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set up GPIO 4 as an input with pull-up resistor

try:
    while True: # Run forever
        if GPIO.input(4) == False: # If button is pressed
            print("Button was pressed!")
            time.sleep(0.2) # Debounce delay

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
