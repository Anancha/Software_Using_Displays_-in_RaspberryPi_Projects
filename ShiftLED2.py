#-----------------------------------------------------------------
#            		SHIFT REGISTER LED CONTROL
#            		==========================
#
# In this project a 74H595 type serial-in parallel-out shift register
# is used. 8 LEDs are connected to the shift register and the shift
# register is controlled from the Raspberry Pi so that the LEDs turn
# ON and OFF as described in the text
#
# Author: Dogan Ibrahim
# File  : ShiftLED2.py
# Date  : October 2020
#-------------------------------------------------------------------
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)			# GPIO mode BCM

Sclock = 26				# 74HC595 clock
Latch = 19				# 74H595 latch
DataIn = 13				# 74HC595 data in

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
def HC595Latch():
   GPIO.output(Latch, 1)		# Latch = 1
   GPIO.output(Latch, 0)		# LAtch = 0

#
# This function sends serial data to the shift register
#
def HC595IN(SerData):
   for dat in range(0, 8):
      GPIO.output(DataIn, 0x80 & (SerData << dat))
      GPIO.output(Sclock, 1)
      GPIO.output(Sclock, 0)

#
# This function turns ON the LED whose binary value is LEDS
#
def Display(LEDS):
      HC595IN(LEDS)			# Shift data
      HC595Latch()			# Latch the output

#
# Start of main program
#
Setup()					# Configure interface
Display(0x0)				# Clear LEDs
time.sleep(0.5)				# Wait 0.5 second
cnt = 0x01				# cnt = 0x01

try:
   while True:				# Do forever
      Display(cnt)			# Display cnt
      cnt = cnt << 1			# Shift cnt left
      if cnt == 0x0100:			# End of 8 bits?
         cnt = 0x01			# Back to 0x01
      time.sleep(1)			# Wait 1 second

except KeyboardInterrupt:		# Keyboard interrupt
   GPIO.cleanup()





