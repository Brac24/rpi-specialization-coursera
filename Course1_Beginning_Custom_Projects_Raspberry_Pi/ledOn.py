# This program will turn on an LED connected to GPIO 17 (pin 11) using an Rpi 4B

from gpiozero import LED
from signal import pause

# Create an LED object on GPIO 17 (Pin 11) on Rpi 4B
red = LED(17)

red.on()

# pause the script otherwise on close of the script gpio 17 turns off
# and we will not see the led turn on
pause()
