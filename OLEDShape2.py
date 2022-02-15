#--------------------------------------------------------------
#
#		DISPLAY A CHORD AND A POLYGON
#		=============================
#
# In this program a chord and a polygon are drawn. The polygon is
# filled with white
#
# Author: Dogan Ibrahim
# File  : OLEDShape2.py
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
draw.chord((0, 0, 90, 30), 10, 180, fill = 255)
draw.polygon([(100,5), (120,9), (120,25), (100,30)],outline=255,fill=255)
display.image(image)
display.show()

