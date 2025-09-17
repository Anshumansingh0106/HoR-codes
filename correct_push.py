from machine import Pin
import time

led = Pin(2, Pin.OUT)
push = Pin(18, Pin.IN)

while True:
    if push.value() == 1:  # Check if the button is pressed
        led.value(1)       # Turn the LED on
    else:
        led.value(0)       # Turn the LED off
    time.sleep(0.1)        # Add a small delay for stability
