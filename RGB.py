#---------------------------------------------------------------
#			RED AND GREEN FLASHING LED
#			--------------------------
# In this project an RGB LED is connected to the Raspberry Pi.
# The program flashes the RED, GREEN, and BLUE LEDs alternately
# every 0.5 second
#
# Author: Dogan Ibrahim
# File  : RGB.py
# Date  : October, 2020
#---------------------------------------------------------------
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

RED = 2					# RED LED at GPIO2
GREEN = 3				# GREEN LED at GPIO3
BLUE = 4				# BLUE LED at GPIO4
GPIO.setmode(GPIO.BCM)			# Set BCM mode

GPIO.setup(RED, GPIO.OUT)		# RED LED is output
GPIO.setup(GREEN, GPIO.OUT)		# GREEN LED is output
GPIO.setup(BLUE, GPIO.OUT)		# BLUE LED is output

while True:				# Do forever
   GPIO.output(RED, 1)			# RED LED is ON
   time.sleep(0.5)			# Wait 0.5 second
   GPIO.output(RED, 0)			# RED LED is OFF
   time.sleep(0.5)			# Wait 0.5 second
   GPIO.output(GREEN, 1)		# GREEN LED is ON
   time.sleep(0.5)			# Wait 0.5 second
   GPIO.output(GREEN, 0)		# GREEN LED is OFF
   time.sleep(0.5)			# Wait 0.5 second
   GPIO.output(BLUE, 1)			# BLUE LED is ON
   time.sleep(0.5)			# Wait 0.5 second
   GPIO.output(BLUE, 0)			# BLUE LED is OFF
   time.sleep(0.5)			# Wait 0.5 second

