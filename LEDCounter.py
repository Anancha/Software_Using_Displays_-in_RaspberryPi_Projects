#-----------------------------------------------------------------
#            		LED BINARY COUNTER
#            		==================
# In this project 8 LEDs are connected to the Raspberry Pi. The
# program counts up in binary and displays the results on these
# LEDs. 1 second delay is inserted between each output
#
# Author: Dogan Ibrahim
# File  : LEDCounter.py
# Date  : October 2020
#-------------------------------------------------------------------
import RPi.GPIO as GPIO
import time
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
# Configure the LEDs as outputs and turn them all OFF
#
for led in LEDS:
   GPIO.setup(led, GPIO.OUT)		# LEDs are outputs
   GPIO.output(led, 0)			# Turn OFF all LEDs

count = 1				# Initialize count

try:
   while True:				# Do Forever
      Port_Output(count, LEDS)		# Send to LEDs
      time.sleep(1)			# Wait 1 second
      count = count + 1			# Increment count
      if count > 255:			# If > 255 ...
        count = 0			# Back to 0

except KeyboardInterrupt:		# Keyboard interrupt
   Port_Output(0, LEDS)			# Set all LEDS to OFF
   GPIO.cleanup()			# Cleanup GPIO
   print("End of program")




