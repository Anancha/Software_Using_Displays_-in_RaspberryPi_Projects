#------------------------------------------------------------
#			DISPLAY TEXT
#			============
#
# This program displays the text E L E K T O R at (15,5)
#
# Author: Dogan Ibrahim
# File  : OLEDText.py
# Date  : November 2020
#--------------------------------------------------------------
from PIL import Image,ImageDraw,ImageFont
from board import SCL, SDA
import busio
import adafruit_ssd1306

i2c = busio.I2C(SCL, SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
font = ImageFont.load_default()				# Default font

display.fill(0)						# Clear display
display.show()

width = display.width					# Width
height = display.height					# Height
image = Image.new('1',(width,height))
draw = ImageDraw.Draw(image)
draw.text((15, 5), "E L E K T O R", font = font, fill = 255)
display.image(image)
display.show()

