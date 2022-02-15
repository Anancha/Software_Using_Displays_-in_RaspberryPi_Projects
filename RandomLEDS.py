#-----------------------------------------------------------------
#            		RANDOMLY FLASHING LEDS
#            		======================
# In this project 8 LEDs are connected to the Raspberry Pi. The
# program generates random numbers between 1 and 255 and these
# numbers are used to turn the LEDs ON and OFF
#
# Author: Dogan Ibrahim
# File  : RandomLEDS.py
# Date  : October 2020
#-------------------------------------------------------------------
import RPi.GPIO as GPIO
import time
import random

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)			# GPIO mode BCM

LEDS = (26, 19, 13, 6, 5, 11, 9, 10)	# LED connections
					# LSB=10, MSB=26
#
# This function sends 8-bit data (0-255) to the port
#
def Port_Output(x, PORT):
   b = bin(x)				# Convert to binary
   b = b.replace("0b", "")		# Remove leading "0b"
   diff = 8 - len(b)			# Find the length
   for i in range (0, diff):
      b = "0" + b			# insert leading 0s

   for i in range (0, 8):
      if b[i] == "1":
         GPIO.output(PORT[i], 1)	# Send 1
      else:
         GPIO.output(PORT[i], 0)	# Send 0
   return

#
# Configure the LEDs as outputs
#
for led in LEDS:
   GPIO.setup(led, GPIO.OUT)		# LEDs are outputs

#
# Start of main program
#
try:
   while True:				# Do Forever
      r = random.randint(1, 255)	# Generate random number
      Port_Output(r, LEDS)		# Send to LEDs
      time.sleep(0.1)			# Wait 100 ms

except KeyboardInterrupt:		# Keyboard interrupt
   Port_Output(0, LEDS)			# Set all LEDS to OFF
   GPIO.cleanup()			# Cleanup GPIO
   print("End of program")




