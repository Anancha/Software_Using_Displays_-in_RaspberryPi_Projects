#-----------------------------------------------------------------
#            		DOT MATRIX R CLICK
#            		==================
#
# In this project a Dot Matrix R Click board is used to display:
# Letter A, right arrow, left arrow, up arrow
#
# Author: Dogan Ibrahim
# File  : DotMatrix.py
# Date  : November 2020
#-------------------------------------------------------------------
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)			# GPIO mode BCM

CLK = 26				# Shift register clock
CE = 19					# Shift register CE
DIN = 13				# Shift register data in
RESET = 5				# Shift register RESET
RS = 6					# Shift register RS
#
# This function configures ports as outputs and clears them. Also,
# the display is configured
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
# This function clears the displays at starup
#
def ClearDisplay():
   Display(0, 0, 0, 0, 0)
   Display(0, 0, 0, 0, 0)
   Display(0, 0, 0, 0, 0)
   Display(0, 0, 0, 0, 0)
   GPIO.output(CE, 1)

#
# This function sends serial data to the shift register
#
def ShiftIn(SerData):
   for dat in range(0, 8):
      GPIO.output(DIN, 0x80 & (SerData << dat))
      GPIO.output(CLK, 1)
      GPIO.output(CLK, 0)

#
# This function calls ShiftIn to send data to the display
#
def Display(Data0, Data1, Data2, Data3, Data4):
   GPIO.output(RS, 0)
   GPIO.output(CE, 0)
   ShiftIn(Data0)
   ShiftIn(Data1)
   ShiftIn(Data2)
   ShiftIn(Data3)
   ShiftIn(Data4)

#
# Start of main program
#
Setup()						# Configure interface
ClearDisplay()
LoadControlWord0()
#
# Required but patterns:
# 0x7E,0x09,0x09,0x09,0x7E			# Letter A
# 0x04,0x04,0x15,0x0E,0x04			# Right arrow
# 0x04,0x0E,0x15,0x04,0x04			# Left arrow
# 0x04,0x02,0x7F,0x02,0x04			# Up arrow
#
try:

   Display(0x7E, 0x09, 0x09, 0x09, 0x7E)	# Disp A
   Display(0x04, 0x04, 0x15, 0x0E, 0x04)	# Disp right arrow
   Display(0x04, 0x0E, 0x15, 0x04, 0x04)	# Disp left arrow
   Display(0x04, 0x02, 0x7F, 0x02, 0x04)	# Disp up arrow
   GPIO.output(CE, 1)

   while True:
      pass

except KeyboardInterrupt:	 		# Keyboard interrupt
      GPIO.cleanup()				# Clean exit





