#--------------------------------------------------------------------
#			1.8 INCH TFT DISPLAY
#			--------------------
#
# This program draws a Green filled rectangle and writes the text:
# ELEKTOR in Blue colour inside this rectangle
#
# Author: Dogan Ibrahim
# File  : TFT1.py
# Date  : November 2020
#---------------------------------------------------------------------
# Import libraries
#
import digitalio
import board
from PIL import Image,ImageDraw,ImageFont
import adafruit_rgb_display.st7735 as st7735
#
# Define CS, DC(A0), and RESET pin connections
#
cs_pin = digitalio.DigitalInOut(board.D8)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D24)
BAUDRATE = 24000000
spi = board.SPI()

disp = st7735.ST7735R(spi,rotation=90,bgr=True,height=160,dc=dc_pin,cs=cs_pin,\
baudrate=BAUDRATE,rst=reset_pin)

height = disp.width			# Display is rotated 90 degrees
width = disp.height			# Display is rotated 90 degrees

#
# Draw a Green filled rectangle starting at (10,10)
#
image = Image.new("RGB",(width,height))
draw = ImageDraw.Draw(image)
draw.rectangle((10,10,width-20,height-20),outline=0,fill=(0,255,0))
disp.image(image)

#
# Write Blue text at (30,50). First set the fontsize and use TrueType font
#
FONTSIZE = 20
font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",FONTSIZE)
text = "Elektor"
draw.text((30,50),text,font=font,fill=(0,0,255))
disp.image(image)
