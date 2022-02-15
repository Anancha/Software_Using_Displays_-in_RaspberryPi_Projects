#-----------------------------------------------------------------
#            MAX7219 BASED 8 DIGIT 7-SEGMENT DISPLAY COUNTER
#            ===============================================
#
# In this project the MAX7219 library is used
#
# Author: Dogan Ibrahim
# File  : MAX7219TEST.py
# Date  : November 2020
#-------------------------------------------------------------------
import RPi.GPIO as GPIO				# Import GPIO
import time					# Import time
from MAX7219 import *				# Import MAX7219

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#
# Start of main program
#
Setup()						# Configure interface
data = 0

try:
   while True:
      DisplayInt(data)				# Display data
      data = data + 1				# Increment data
      time.sleep(1)				# Wait 1 sec

except KeyboardInterrupt:	 		# Keyboard interrupt
      Display(0x1C00)				# Shutdown display
      time.sleep(1)				# Wait 1ms
      GPIO.cleanup()				# Clean exit





