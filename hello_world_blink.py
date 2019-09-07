# See https://github.com/tachyonlabs/raspberry_pi_pyladies_presentation
# for information on the wiring and the presentation in general

# The Rpi.GPIO library makes it easy for your programs to read from and write to
# the Raspberry Pi's GPIO (General Purpose Input/Output) pins
import RPi.GPIO as GPIO
import time

# GPIO.BCM mode selects the pin numbering system of GPIO pin channels
# as opposed to GPIO.BOARD mode which uses P1 connector pin numbers
GPIO.setmode(GPIO.BCM)

# Any Raspberry Pi pin you use needs to be set as either an input or an output
# Here we are setting pin GPIO 20 as an output to control the LED (I didn't choose
# GPIO pin 20 for any particular reason - you can use whichever GPIO pin or pins
# you like so long as you use the same pins in your circuit and your software)
led_pin = 20
GPIO.setup(led_pin, GPIO.OUT)

# Blink the LED twenty times, with a frequency of one second on, one second off
number_of_times_to_blink = 20
number_of_seconds = 1
for i in range(number_of_times_to_blink):
    # Output high (3.3 volts) on pin 20, to turn the LED on
    GPIO.output(led_pin, GPIO.HIGH)
    # Leave the LED on for one second
    time.sleep(number_of_seconds)
    # Output low (0 volts) on pin 20, to turn the LED off
    GPIO.output(led_pin, GPIO.LOW)
    # Leave the LED off for one second
    time.sleep(number_of_seconds)

# This resets any ports used in your program
GPIO.cleanup()

# Why not? :-)
print("Hello World!")
# This will print some general info about your Raspberry Pi
print("Raspberry Pi stats: {}".format(GPIO.RPI_INFO))
