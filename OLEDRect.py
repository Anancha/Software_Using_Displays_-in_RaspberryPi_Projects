#--------------------------------------------------------------
#
#		DISPLAY A RECTANGLE WITH TEXT INSIDE
#		====================================
#
# In this progra a rectangle is displayed at the corners of the
# display and text R E C T A N G L E is displayed inside
#
# Author: Dogan Ibrahim
# File  : OLEDRect.py
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
draw.text((15, 12),"R E C T A N G L E", font = font, fill = 255)
display.image(image)
display.show()

