#-----------------------------------------------------------------
#            2 DIGIT SEVEN SEGMENT LED COUNTER
#            =================================
#
# This is a 2 digit 7-segment LED counter program. The program
# counts up every second from 0 to 99 continuously. The LED matrix
# is refreshed in a thread. The connections between the 7-segment
# LED and the RaspberryPi are as follows:
#
# 7-Segment LED    GPIO
#     a             2
#     b             3
#     c             4
#     d             17
#     e             27
#     f             22
#     g             10
#    E2 (digit)     9
#    E1 (digit)     11
#
# Author: Dogan Ibrahim
# File  : SevenCount.py
# Date  : November 2020
#-------------------------------------------------------------------
import RPi.GPIO as GPIO
import _thread
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)			# GPIO mode BCM

LED_Segments = (2, 3, 4, 17, 27, 22, 10)
LED_Digits = (9, 11)

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
      if len(cnt) < 2:
         cnt = "0" + cnt		# Make sure 2 digits
      for dig in range(2):		# Do for 2 digits
        for loop in range(0,7):		# Do for all segments
           GPIO.output(LED_Segments[loop], LED_Bits[cnt[dig]][loop])
        GPIO.output(LED_Digits[dig], 0)
        time.sleep(0.001)
        GPIO.output(LED_Digits[dig], 1)

#
# Thread to count up evey second
#
def UP_Count():				# Thread UP_Count
   global count
   while True:				# Do forever
      time.sleep(1)			# Wait a second
      count = count + 1			# Increment count
      if count == 100:			# If count = 100
         count = 0

#
# Create the threads
#
_thread.start_new_thread(Refresh, ())
_thread.start_new_thread(UP_Count, ())

while True:
    pass


