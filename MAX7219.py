#--------------------------------------------------------------------
#            		MAX7219 LED LIBRARY
#            		===================
#
# This is the LED library for the MAX7219. The connections must be
# as follows:
#
# GPIO26 CLK
# GPIO19 CS (LOAD)
# GPIO13 DIN
#
# Connect Vcc to +5V, GND to GND. Also, 10K resistor from CS to +3.3V
#
# include:                      from  MAX7219 import *
# include before main program:  Setup()
# display data by calling:      DisplayInt(data)
#
# Author: Dogan Ibrahim
# File  : MAX7219.py
# Date  : November 2020
#
# (c) Dogan Ibrahim, 2020
#----------------------------------------------------------------------
import RPi.GPIO as GPIO
import time

Sclock = 26				# Shift register clock
Load = 19				# Shift register load
DataIn = 13				# Shift register data in

#
# This function configures ports as outputs and clears them. Also,
# the display is configured
#
def Setup():
   GPIO.setup(Sclock, GPIO.OUT)		# Sclock is output
   GPIO.setup(Load, GPIO.OUT)		# Latch is output
   GPIO.setup(DataIn, GPIO.OUT)		# DataIn is output
   GPIO.output(Sclock, 0)		# Sclock = 0
   GPIO.output(Load, 0)			# Latch = 0
   GPIO.output(DataIn, 0)		# DataIn = 0
#
# Now setup the display
#
   Display(0x1C01)			# Exit shutdown
   time.sleep(0.001)			# Wait 1ms
   Display(0x19FF)			# Decode all digits
   Display(0x1B07)			# Scan mode for all LEDs
   Display(0x1A01)			# Set intensity to 3/32

#
# This function sends serial data to the shift register
#
def ShiftIn(SerData):
   for dat in range(0, 16):
      GPIO.output(DataIn, 0x8000 & (SerData << dat))
      GPIO.output(Sclock, 1)
      GPIO.output(Sclock, 0)

#
# This function turns ON the LED whose binary value is LEDS
#
def Display(LEDS):
      GPIO.output(Load, 0)			# Load = 0
      ShiftIn(LEDS)				# Shift data
      GPIO.output(Load, 1)			# Load the output

#
# This function converts the integer data to 8 BCD numbers,stored
# in list BCD. Also, leading zeros are blanked. Function returns
# the 8 BCD numbers in list BCD
#
def ConvBCD(i):
   BCD = [None] * 8				# Blank list
   j = i

   for indx in range(0, 8):
      Digit = j % 10
      BCD[indx] = Digit				# Save BCD number
      j = int(j / 10)
#
# Now, blank the leading zeroes
#
   Blank = 0x0F					# Value to blank a digit
   if BCD[7] == 0:				# Digit7 = 0?
      BCD[7] = Blank				# Blank it
      if BCD[6] == 0:				# Digit6 = 0?
         BCD[6] = Blank				# Blank it
         if BCD[5] == 0:			# Digit5 = 0?
            BCD[5] = Blank			# Blank it
            if BCD[4] == 0:			# Digit4 = 0?
               BCD[4] = Blank			# Blank it
               if BCD[3] == 0:			# Digit3 = 0?
                  BCD[3] = Blank		# Blank it
                  if BCD[2] == 0:		# Digit2 = 0?
                     BCD[2] = Blank		# Blank it
                     if BCD[1] == 0:		# Digit1 = 0?
                        BCD[1] = Blank		# Blank it

   for indx in range(0, 8):
       BCD[indx] = BCD[indx] | (indx + 1) << 8
   return BCD					# Return BCD

#
# This function displays the given integer number
#
def DisplayInt(dat):
    BCDData = ConvBCD(dat)			# Conv to BCD
    for i in range(0, 8):			# Display
       Display(BCDData[i])


