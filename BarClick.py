#-----------------------------------------------------------------
#            	BarGraph CLICK BOARD UP COUNTER
#            	===============================
#
# In this project a BarGraph click board is used. The program
# counts up in binary every second and displays on the BarGraph
# display.
#
# Author: Dogan Ibrahim
# File  : BarClick.py
# Date  : October 2020
#-------------------------------------------------------------------
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)			# GPIO mode BCM

Sclock = 26				# BarGraph clock
Latch = 19				# BarGraph latch
DataIn = 13				# BarGraph data in

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
def BarGraphLatch():
   GPIO.output(Latch, 1)		# Latch = 1
   GPIO.output(Latch, 0)		# Latch = 0

#
# This function sends serial data to the shift register
#
def BarGraphIn(SerData):
   for dat in range(0, 10):
      GPIO.output(DataIn, 0x01 & (SerData >> dat))
      GPIO.output(Sclock, 1)
      GPIO.output(Sclock, 0)

#
# This function turns ON the LED whose binary value is LEDS
#
def Display(LEDS):
      BarGraphIn(LEDS)			# Shift data
      BarGraphLatch()			# Latch the output

#
# Start of main program
#
Setup()					# Configure interface
cnt = 0					# Set cnt to 0

try:
   while True:				# Do forever
      Display(cnt)			# Display cnt
      cnt = cnt + 1			# Increment cnt
      if cnt > 1023:			# End of 8 bits?
         cnt = 1			# Back to 0x01
      time.sleep(1)			# Wait 1 second

except KeyboardInterrupt:		# Keyboard interrupt
   GPIO.cleanup()





