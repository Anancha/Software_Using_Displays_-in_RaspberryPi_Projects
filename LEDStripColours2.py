#----------------------------------------------------------------------
#
#		LED STRIP - DISPLAY RANDOMCOLOURS
#		=================================
#
# In this program the LEDs on the strip display random colours. Each
# LED displays a different colour
#
# Author: Dogan Ibrahim
# File  : LEDStripColours2.py
# Date  : November 2020
#----------------------------------------------------------------------- 
from rpi_ws281x import *
import time
import random
 
# Strip configuration
#
LED_COUNT      = 64      	# Number of LED pixels
LED_PIN        = 18      	# LED strip GPIO pin
FREQ           = 800000  	# LED signal frequency in hertz (800khz)
DMA            = 10      	# DMA channel to use for generating signal
BRIGHTNESS     = 50     	# 0 to 255 (255 is the brightess)
INVERT         = False   	# True to invert, if using invert logic
PWM            = 0       	# For PWM 1 use: GPIO: 13, 19, 41, 45 or 53

#
# Scan the strip with a given colour
#
def colourScan():
  while True:
       for i in range(strip.numPixels()):
           r1 = random.randint(0, 255)
           r2 = random.randint(0, 255)
           r3 = random.randint(0, 255)
           strip.setPixelColor(i,Color(r1,r2,r3))
           strip.show()
           time.sleep(0.01)

#
# All LEDs Black (OFF)
#
def AllOFF():
  for i in range(strip.numPixels()):
     strip.setPixelColor(i, Color(0,0,0))
     strip.show()
#
# Create NeoPixel
#
strip = Adafruit_NeoPixel(LED_COUNT,LED_PIN,FREQ,DMA,INVERT,BRIGHTNESS,PWM)
strip.begin()
strip.setBrightness(100)

try:

   while True:
       colourScan()
 
except KeyboardInterrupt:
    AllOFF()
    print("End")

  
