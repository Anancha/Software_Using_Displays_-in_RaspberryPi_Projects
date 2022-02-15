#------------------------------------------------------------------
#		SHOW THE PIXELS AT CORNERS OF THE DISPLAY
#		=========================================
#
# This program shows the pixels at the four corners of the display
#
# Author: Dogan Ibrahim
# File  : OLEDCorners.py
# Date  : November 2020
#------------------------------------------------------------------
from board import SCL, SDA
import busio
import adafruit_ssd1306

i2c = busio.I2C(SCL, SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

display.fill(0)				# Clear pixels
display.show()				# Display data

display.pixel(0,0,1)			# Pixel at (0,0)
display.pixel(127,0,1)			# Pixel at (127,0)
display.pixel(0,31,1)			# Pixel at (0,31)
display.pixel(127, 31, 1)		# Pixel at (127,31)
display.show()				# Display the data


