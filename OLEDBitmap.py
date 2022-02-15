#--------------------------------------------------------------
#
#		DISPLAY BITMAP
#		==============
#
# This progra displays a bitmap image
#
# Author: Dogan Ibrahim
# File  : OLEDBitmap.py
# Date  : November 2020
#---------------------------------------------------------------
from PIL import Image,ImageDraw,ImageFont
from board import SCL, SDA
import busio
import adafruit_ssd1306

i2c = busio.I2C(SCL, SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

display.fill(0)
display.show()

width=(display.width)
height=(display.height)
image=Image.new('1',(width,height))
image=Image.open('LetterA.png').resize((width,height),\
Image.ANTIALIAS).convert('1')
display.image(image)
display.show()

