#--------------------------------------------------------------------
#	DISPLAY THE TEMPEATURE WITH IMAGE ON TFT DISPLAY
#	------------------------------------------------
#
# This program displays the temperature on the TFT display. If the
# temperature is less than 25 Degrees then it will be displayed in
# Blue colour. If on the other hand it is greater than 25 Degrees
# then it will be displayed in Red colour. The program also displays
# a thermometer image
#
# Author: Dogan Ibrahim
# File  : TFTImgtemperature.py
# Date  : November 2020
#---------------------------------------------------------------------
# Import libraries
#
import digitalio
import board
import time
import adafruit_dht
from PIL import Image,ImageDraw,ImageFont
import adafruit_rgb_display.st7735 as st7735

sensor = adafruit_dht.DHT11(board.D21)

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

img = Image.new("RGB",(width,height))
draw = ImageDraw.Draw(img)

FONTSIZE = 20
fontdir = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
font = ImageFont.truetype(fontdir, FONTSIZE)

#
# Open the thermometer image
#
image2 = Image.open("Thermometer.png")

#
# Start of program loop.Clear the scren if there is change in temp
#
temperature_old = 0
temperature = 0

while True:
 try:

   temperature = int(sensor.temperature)

   if temperature_old != temperature:		# Any change?
      temperature_old = temperature
      draw.rectangle((0,0, width,height), outline=0,fill=(0,255,0))

      temp = "T = " + str(temperature) + chr(176)+ "C"
      if temperature < 25:
          draw.text((5, 30),temp,font=font,fill=(0,0,255))
      else:
          draw.text((5, 30), temp, font=font, fill=(255, 0, 0))

      image2.paste(img, (40,0))			# Overlay images
      disp.image(image2)			# Display image
      time.sleep(10)				# Wait 10 seconds

 except RuntimeError as error:
   time.sleep(2)
   continue

 except Exception as error:
   raise error
   exit(0)

 except KeyboardInterrupt:
   exit(0)

