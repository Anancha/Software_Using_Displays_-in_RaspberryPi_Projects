#-----------------------------------------------------------------
#            		LUCKY DAY OF THE WEEK
#            		======================
#
# In this project 7 LEDs are connected to the Raspberry Pi, where
# each LED corresponds to a day of the week. Pressing a button
# turns ON an LED and the day represented by this LED is assumed
# to be your lucky day of the week.
#
# Author: Dogan Ibrahim
# File  : LuckyDay.py
# Date  : October 2020
#-------------------------------------------------------------------
import RPi.GPIO as GPIO
import time
import random

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)			# GPIO mode BCM

LEDS = (19, 13, 6, 5, 11, 9, 10)	# LED connections
Button = 21				# Button connection
GPIO.setup(Button, GPIO.IN)		# Button is input

#
# This function sends 8-bit data (0-255) to the port
#
def Port_Output(x, PORT):
   b = bin(x)				# Convert to binary
   b = b.replace("0b", "")		# Remove leading "0b"
   diff = 7 - len(b)			# Find the length
   for i in range (0, diff):
      b = "0" + b			# insert leading 0s

   for i in range (0, 7):
      if b[i] == "1":
         GPIO.output(PORT[i], 1)	# Send 1
      else:
         GPIO.output(PORT[i], 0)	# Send 0
   return

#
# Configure the LEDs as outputs and turn them all OFF
#
for led in LEDS:
   GPIO.setup(led, GPIO.OUT)		# LEDs are outputs
   GPIO.output(led, 0)			# All OFF

#
# Start of main program
#
print("Press the Button...")
random.seed()				# System time as seed

while GPIO.input(Button) == 1:		# If Button not pressed
   pass
r = random.randint(1, 7)		# Generate random number
r = pow(2, r-1)				# LED to be turned ON
Port_Output(r, LEDS)			# Send to LEDs





