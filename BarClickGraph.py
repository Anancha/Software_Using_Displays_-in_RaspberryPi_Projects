#-----------------------------------------------------------------
#            	BAR GRAPH USING THE BarGraph CLICK
#            	==================================
#
# In this project a BarGraph click board is used. The program
# displays a bar graph on the LEDs as the input variable changes
# from 0% to 100%.
#
# Author: Dogan Ibrahim
# File  : BarClickGraph.py
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
# This function implements the bar graph
#
def BarGraph(dat):
     if dat > 95:
       Display(0x3FF)			# All LEDs ON
     elif dat > 85:
       Display(0x3FE)			# 9 LEDs ON
     elif dat > 75:
       Display(0x3FC)			# 8 LEDs ON
     elif dat > 65:
       Display(0x3F8)			# 7 LEDs ON
     elif dat > 55:
       Display(0x3F0)			# 6 LEDs ON
     elif dat > 45:
       Display(0x3E0)			# 5 LEDs ON
     elif dat > 35:
       Display(0x3C0)			# 4 LEDs ON
     elif dat > 25:
       Display(0x380)			# 3 LEDs ON
     elif dat > 15:
       Display(0x300)			# 2 LEDs ON
     elif dat > 5:
       Display(0x200)			# 1 LED ON
     else:
       Display(0x0)			# All LEDs OFF


#
# Start of main program
#
Setup()					# Configure interface
data = 0

try:
   while True:				# Do forever
      BarGraph(data)			# Display bar graph
      data = data + 10
      if data > 100:
         data = 0x0
      time.sleep(1)			# Wait 1 second

except KeyboardInterrupt:		# Keyboard interrupt
   GPIO.cleanup()





