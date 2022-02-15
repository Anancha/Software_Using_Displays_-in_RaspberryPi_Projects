#----------------------------------------------------------------------
#
#		LED STRIP - SCAN DIFFERENT COLOURS
#		==================================
#
# In this program the LEDs on teh strip are scanned with different
# colours
#
# Author: Dogan Ibrahim
# File  : LEDStripScan.py
# Date  : November 2020
#----------------------------------------------------------------------- 
from rpi_ws281x import *
import time
 
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
def colourScan(strip, colour):
    for clr in range(strip.numPixels()):
        strip.setPixelColor(clr, colour)
        strip.show()
        time.sleep(0.05)

#
# Create NeoPixel
#
strip = Adafruit_NeoPixel(LED_COUNT,LED_PIN,FREQ,DMA,INVERT,BRIGHTNESS,PWM)
strip.begin()
strip.setBrightness(100)

try:

   while True:
       colourScan(strip, Color(255, 0, 0))     # Red
       colourScan(strip, Color(0, 255, 0))     # Green
       colourScan(strip, Color(0, 0, 255))     # Blue
       colourScan(strip, Color(255, 255, 0))   # Yellow
       colourScan(strip, Color(255, 0, 255))   # Violet
       colourScan(strip, Color(255, 255, 255)) # White

except KeyboardInterrupt:
       colourScan(strip, Color(0, 0, 0))
       print("End")
 
