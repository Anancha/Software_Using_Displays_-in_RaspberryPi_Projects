#-----------------------------------------------------------------
#            	UT-M 7-SEG R CLICK DISPLAY COUNTER
#            	==================================
#
# In this project a UT-M 7-SEG R Click board is conencted to the
# Raspberry Pi. The program counts up from 0 to 99 and displays
# the result on the 2 digit 7-segment display. The count is updated
# every second. When the count reaches 99, it is reset to 0
#
# Author: Dogan Ibrahim
# File  : UTM7SEG.py
# Date  : November 2020
#-------------------------------------------------------------------
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)			# GPIO mode BCM

Sclock = 26				# Shift register clock
Latch = 19				# Shift register latch
DataIn = 13				# Shift register data in

SEGMENTS = [0xFC,0x60, 0xDA, 0xF2, 0x66, 0xB6, 0xBE, 0xE0, 0xFE, 0xF6]
#            0    1     2     3     4     5     6     7     8     9

#
# This function configures ports as outputs and clears them
#
def Setup():
   GPIO.setup(Sclock, GPIO.OUT)		# Sclock is output
   GPIO.setup(Latch, GPIO.OUT)		# Latch is output
   GPIO.setup(DataIn, GPIO.OUT)		# DataIn is output
   GPIO.output(Sclock, 0)		# Sclock = 0
   GPIO.output(Latch, 0)		# Latch = 0
   GPIO.output(DataIn, 0)		# DataIn = 0

#
# This function latches the data to output registers
#
def RegisterLatch():
   GPIO.output(Latch, 1)		# Latch = 1
   GPIO.output(Latch, 0)		# Latch = 0

#
# This function sends serial data to the shift register
#
def ShiftIn(SerData):
   for dat in range(0, 16):
      GPIO.output(DataIn, 0x01 & (SerData >> dat))
      GPIO.output(Sclock, 1)
      GPIO.output(Sclock, 0)

#
# This function turns ON the LED whose binary value is LEDS
#
def Display(LEDS):
      ShiftIn(LEDS)			# Shift data
      RegisterLatch()			# Latch the output
#
# This function extracts the bit pattern for a given number. MSD
# and LSD store the higher and lower digits of the number. First
# and Second store the 7-segment bit patterns corresponding to
# integer numbers MSD and LSD respectively. Leading zero is supressed
# if the number to be displayed is less than 10
#
def Extract(N):
     MSD = int(N /10)			# Extract MSD
     LSD = int(N % 10)			# Extract LSD
     First = SEGMENTS[MSD]		# MSD bit pattern
     Second = SEGMENTS[LSD]		# LSD bit pattern
     if MSD != 0:			# If > 9
         No = Second | First << 8	# Combine MSD, LSD
     else:
         No = Second
     return No				# Return No

#
# Start of main program
#
Setup()					# Configure interface
i=0					# Initial count

try:
   while True:				# Do forever
      Number = Extract(i)		# Extract bits
      Display(Number)			# Display Number
 
      i = i + 1				# Increment count
      if i > 99:			# if > 99, reset
        i = 0
      time.sleep(1) 			# Wait 1 second

except KeyboardInterrupt:		# Keyboard interrupt
   GPIO.cleanup()





