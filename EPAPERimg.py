#----------------------------------------------------------------
#
#			DRAW AN IMAGE
#			=============
#
# This program draws an image on the screen
#
# Auhor: Dogan Ibrahim
# File : EPAPERimg.py
# Date : November 2020
#----------------------------------------------------------------
#
# Import libraries
#
from waveshare_epd import epd2in13d
import time
from PIL import Image,ImageDraw

try:

    display = epd2in13d.EPD()
    display.init()
    display.Clear(0xFF)

    time.sleep(1)

    w = display.width
    h = display.height
    print('width:',w)
    print('height:',h) 

    png = Image.open('X.png')			# Open the image
    display.display(display.getbuffer(png))
    time.sleep(2)

    display.sleep()
    display.Dev_exit()

except KeyboardInterrupt:
    epd2in13d.epdconfig.module_exit()
    exit()
