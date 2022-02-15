#-----------------------------------------------------------------
#            		DOT MATRIX R CLICK
#            		==================
#
# In this project a Dot Matrix R Click board is used to display:
# Letter A, right arrow, left arrow, up arrow.
#
# This program uses teh Matrix library
#
# Author: Dogan Ibrahim
# File  : MatrixTEST.py
# Date  : November 2020
#-------------------------------------------------------------------
import RPi.GPIO as GPIO
from Matrix import *			# Include Matrix library

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)			# GPIO mode BCM

try:

   Display()
   while True:
      pass

except KeyboardInterrupt:
   GPIO.cleanup()				# Clean exit





