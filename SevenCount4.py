#-----------------------------------------------------------------
#            4 DIGIT SEVEN SEGMENT LED SECONDS COUNTER
#            =========================================
#
# This is a 4 digit 7-segment LED seconds counter program. The
# program counts up every second from 0 to 9999 continuously.
# The LED matrix is refreshed in a thread. The connections between
# the 7-segment LED and the RaspberryPi are as follows:
#
# 7-Segment LED    GPIO
#     a             2
#     b             3
#     c             4
#     d             17
#     e             27
#     f             22
#     g             10
#    E1 module1     11
#    E2 module1     9
#    E1 module2     21
#    E2 module2     20 
#
# Author: Dogan Ibrahim
# File  : SevenCount4.py
# Date  : November 2020
#-------------------------------------------------------------------
import RPi.GPIO as GPIO
import _thread
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)			# GPIO mode BCM

LED_Segments = (2, 3, 4, 17, 27, 22, 10)
LED_Digits = (11, 9, 21, 20)

#
# Configure the segments and digits as outputs and clear them
#
for seg in LED_Segments:
   GPIO.setup(seg, GPIO.OUT)		# Segments are outputs
   GPIO.output(seg, 0)			# Clear all segments

for dig in LED_Digits:
   GPIO.setup(dig, GPIO.OUT)		# Digits are outputs
   GPIO.output(dig, 0)			# Clear all digits

LED_Bits ={
' ':(0,0,0,0,0,0,0),			# Blank
'0':(1,1,1,1,1,1,0),			# 0
'1':(0,1,1,0,0,0,0),			# 1
'2':(1,1,0,1,1,0,1),			# 2
'3':(1,1,1,1,0,0,1),			# 3
'4':(0,1,1,0,0,1,1),			# 4
'5':(1,0,1,1,0,1,1),			# 5
'6':(1,0,1,1,1,1,1),			# 6
'7':(1,1,1,0,0,0,0),			# 7
'8':(1,1,1,1,1,1,1),			# 8
'9':(1,1,1,1,0,1,1)}			# 9

count = 0				# Initialzie count

#
# Thread to refresh the 7-segment LED
#
def Refresh():				# Thread Refresh
   global count
   while True:				# Do forever
      cnt = str(count)			# into string
      if len(cnt) == 3:			# If 3 digits
         cnt = " " + cnt		# Add " "
      elif len(cnt) == 2:		# If 2 digits
         cnt = "  " + cnt		# Add "  "
      elif len(cnt) == 1:		# If 1 digit
         cnt = "   " + cnt		# Add "   "
      for dig in range(4):		# Do for 4 digits
        for loop in range(0,7):		# Do for all segments
           GPIO.output(LED_Segments[loop], LED_Bits[cnt[dig]][loop])
        GPIO.output(LED_Digits[dig], 1)
        time.sleep(0.0005)
        GPIO.output(LED_Digits[dig], 0)

#
# Thread to count up evey second
#
def UP_Count():				# Thread UP_Count
   global count
   while True:				# Do forever
      time.sleep(1)			# Wait a second
      count = count + 1			# Increment count
      if count == 10000:		# If count = 10000
         count = 0

#
# Create the threads
#
_thread.start_new_thread(Refresh, ())
_thread.start_new_thread(UP_Count, ())

while True:
    pass


