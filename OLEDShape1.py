#--------------------------------------------------------------
#
#	DISPLAY 4 RECTANGLES WITH NUMBERS 1,2,3,4
#	=========================================
#
# In this progra 4 rectangles are displayed. Number 1 is displayed
# inside rectangle 1, number 2 inside rectangle 2 and so on
#
# Author: Dogan Ibrahim
# File  : OLEDShape1.py
# Date  : November.py
#---------------------------------------------------------------
from PIL import Image,ImageDraw,ImageFont
from board import SCL, SDA
import busio
import adafruit_ssd1306

i2c = busio.I2C(SCL, SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
font = ImageFont.load_default()

display.fill(0)
display.show()

width=(display.width)
height=(display.height)
image=Image.new('1',(width,height))
draw=ImageDraw.Draw(image)
draw.rectangle((0,0, 127, 31),outline = 255, fill = 0)
draw.line((64, 0, 64, 31), fill = 255)
draw.line((0, 16, 127, 16), fill = 255)
draw.text((32, 4), "1", font = font, fill = 255)
draw.text((94, 4), "2", font = font, fill = 255)
draw.text((32, 17),"3", font = font, fill = 255)
draw.text((94, 17),"4", font = font, fill = 255)
display.image(image)
display.show()

