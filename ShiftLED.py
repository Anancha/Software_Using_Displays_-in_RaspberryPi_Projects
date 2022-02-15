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
# File  : ShiftLED.py
# Date  : October 2020
#-------------------------------------------------------------------
import RPi.GPIO as GPIO
import time

LEDClear = [0x0]
LEDShift = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]

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
# This function calls HC595 and then sets the Latch
#
def Display(LEDS):
   k = len(LEDS)
   for j in range(0, k):
      HC595IN(LEDS[j])
      HC595Latch()
      time.sleep(1)

#
# Start of main program
#
Setup()					# Configure the GPIO
Display(LEDClear)			# Clear LEDs

while True:				# Do forever
   Display(LEDShift)			# Shift LEDs left
   time.sleep(2)			# Wait 2 seconds






