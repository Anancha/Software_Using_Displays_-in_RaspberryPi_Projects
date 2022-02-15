#-----------------------------------------------------------------
#            		LED BAR GRAPH
#            		=============
#
# In this project 8 LEDs are connected to the Raspberry Pi. The
# project simulates a bar graph. Each LED is turned ON in steps
# of 11.1. For example, if the value is greater than 88.8 then 
# all the LEDs are turned ON
#
# Author: Dogan Ibrahim
# File  : BarLED.py
# Date  : October 2020
#-------------------------------------------------------------------
import RPi.GPIO as GPIO
import time
import random

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)			# GPIO mode BCM

LEDS = (26, 19, 13, 6, 5, 11, 9, 10)	# LED connections

#
# This function sends 8-bit data (0-255) to the port
#
def Port_Output(x, PORT):
   b = bin(x)				# Convert to binary
   b = b.replace("0b", "")		# Remove leading "0b"
   diff = 8 - len(b)			# Find the length
   for i in range (0, diff):
      b = "0" + b			# insert leading 0s

   for i in range (0, 8):
      if b[i] == "1":
         GPIO.output(PORT[i], 1)	# Send 1
      else:
         GPIO.output(PORT[i], 0)	# Send 0
   return

#
# This function displays the bar graph depending on dat
#
def Bar(dat):
   if dat >= 88.8:
      Port_Output(0xFF, LEDS)			# 8 LEDS ON
   elif dat >= 77.7:
      Port_Output(0xFE, LEDS)			# 7 LEDS ON
   elif dat >= 66.6:
      Port_Output(0xFC, LEDS)			# 6 LEDS ON
   elif dat >= 55.5:
      Port_Output(0xF8, LEDS)			# 5 LEDS ON
   elif dat >= 44.4:
      Port_Output(0xF0, LEDS)			# 4 LEDS ON
   elif dat >= 33.3:
      Port_Output(0xE0, LEDS)			# 3 LEDS ON
   elif dat >= 22.2:
      Port_Output(0xC0, LEDS)			# 2 LEDS ON
   elif dat >= 11.1:
      Port_Output(0x80, LEDS)			# 1 LED ON
   else:
      Port_Output(0x0, LEDS)			# NO LEDS ON
   return

#
# Configure the LEDs as outputs and turn them all OFF
#
for led in LEDS:
   GPIO.setup(led, GPIO.OUT)			# LEDs are outputs
   GPIO.output(led, 0)				# All OFF

#
# Start of main program
#
cnt = 10

while True:
   Bar(cnt)					# Display bar
   cnt = cnt + 10
   time.sleep(1)
   if cnt > 100:
     cnt = 10




