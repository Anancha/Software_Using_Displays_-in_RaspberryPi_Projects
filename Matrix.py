#-----------------------------------------------------------------
#            		DOT MATRIX R CLICK LIBRARY
#            		==========================
#
# This is the library file for the Dot Matrix R Click display
#
# Author: Dogan Ibrahim
# File  : Matrix.py
# Date  : November 2020
#-------------------------------------------------------------------
import RPi.GPIO as GPIO
from Fonts import *

CLK = 26				# Shift register clock
CE = 19					# Shift register CE
DIN = 13				# Shift register data in
RESET = 5				# Shift register RESET
RS = 6					# Shift register RS
#
# This function configures ports as outputs and clears them. Also,
# the display is configur, 0x04, 0x04,ed
#
def Setup():
   GPIO.setup(CLK, GPIO.OUT)		# CLK is output
   GPIO.setup(CE, GPIO.OUT)		# CE is output
   GPIO.setup(DIN, GPIO.OUT)		# DIN is output
   GPIO.setup(RESET, GPIO.OUT)		# RESET is output
   GPIO.setup(RS, GPIO.OUT)		# RS is output
   GPIO.output(CLK, 0)			# CLK = 0
   GPIO.output(CE, 1)			# CE = 1
   GPIO.output(DIN, 0)			# DIN = 0
   GPIO.output(RESET, 0)		# RESET = 0
   GPIO.output(RS, 0)			# RS = 0
#
# Now setup the display, remove RESET mode
#
   GPIO.output(RESET, 1)

#
# This function loads Control Word 0 to: remove sleep mode,set pixel
# current to 4mA, and set 11.7% brightness
#
def LoadControlWord0():
   GPIO.output(RS, 1)
   GPIO.output(CE, 0)
   ctrl0 = 0x66
   for dat in range(0, 8):
      GPIO.output(DIN, 0x80 & (ctrl0 << dat))
      GPIO.output(CLK, 1)
      GPIO.output(CLK, 0)
   GPIO.output(CE, 1)

#
# This function sends serial data to the shift register
#
def ShiftIn(SerData):
   for dat in range(0, 8):
      GPIO.output(DIN, 0x80 & (SerData << dat))
      GPIO.output(CLK, 1)
      GPIO.output(CLK, 0)

def ClearDisplay():
   GPIO.output(RS, 0)
   GPIO.output(CE, 0)
   for i in range(0,20):
     ShiftIn(0x0)
   GPIO.output(CE, 1)

#
# This function calls ShiftIn to send data to the display
#
def Display():
   Setup()
   ClearDisplay()
   LoadControlWord0()
   GPIO.output(RS, 0)
   GPIO.output(CE, 0)

   for i in range(0,20):
      ShiftIn(FONTS[i])
   GPIO.output(CE, 1)







