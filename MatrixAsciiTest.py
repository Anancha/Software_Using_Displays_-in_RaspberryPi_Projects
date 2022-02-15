#-----------------------------------------------------------------
#            		DOT MATRIX R CLICK
#            		==================
#
# In this project a Dot Matrix R Click board is used to display
# letters: ELEC
#
# This program uses teh Matrix library
#
# Author: Dogan Ibrahim
# File  : MatrixAsciiTest.py
# Date  : November 2020
#-------------------------------------------------------------------
import RPi.GPIO as GPIO
from MatrixAscii import *		# Include Matrix library

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)			# GPIO mode BCM

try:

   Display('E', 'L', 'E', 'C')		# Display ELEC
   while True:
      pass

except KeyboardInterrupt:
   GPIO.cleanup()			# Clean exit





