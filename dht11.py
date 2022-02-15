#-----------------------------------------------------------------
#            DISPLAY TEMPERATURE ON 7-SEGMENT LED
#            ====================================
#
# In this program the ambient temperature is displayed on a 2 digit
# 7-segment LED every minute. DHT11 type temperature sensor is used
# in this project and is connected to GPIO 26. The 7-segment LED is
# connected to the Raspberry Pi as follows:
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
#
# Author: Dogan Ibrahim
# File  : dht11.py
# Date  : November 2020
#-------------------------------------------------------------------
import RPi.GPIO as GPIO
import _thread
import time
import Adafruit_DHT			# Adafruit DHT11 library
sensor = Adafruit_DHT.DHT11
S = 26					# DHT11 on GPIO 26
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

temp = 0				# Initialzie count

#
# Thread to refresh the 7-segment LED
#
def Refresh():				# Thread Refresh
   global temp
   while True:				# Do forever
      cnt = str(temp)			# into string
      if len(cnt) < 2:
         cnt = " " + cnt		# Make sure 2 digits
      for dig in range(2):		# Do for 2 digits
         for loop in range(0,7):	# Do for all segments
             GPIO.output(LED_Segments[loop], LED_Bits[cnt[dig]][loop])
         GPIO.output(LED_Digits[dig], 0)
         time.sleep(0.001)
         GPIO.output(LED_Digits[dig], 1)

#
# Thread to get the ambient temperature from DHT11 every minute
#
def Get_Temp():				# Thread Get_Temp
   global temp
   while True:				# Do forever
      humidity,temperature = Adafruit_DHT.read_retry(sensor, S)
      temp = int(temperature)
      time.sleep(60)

#
# Create the threads
#
_thread.start_new_thread(Refresh, ())
_thread.start_new_thread(Get_Temp, ())

while True:
    pass


