#----------------------------------------------------------------
#
#		DRAW A RECTANGLE AND WRITE ETXT INSIDE
#		======================================
#
# In thir program a rectangle is drawn and the text ELEKTOR
# is written inside this rectangle
#
# Auhor: Dogan Ibrahim
# File : EPAPERtext.py
# Date : November 2020
#----------------------------------------------------------------
#
# Import libraries
#
from waveshare_epd import epd2in13d
import time
from PIL import Image,ImageDraw,ImageFont

try:

    display = epd2in13d.EPD()
    display.init()
    display.Clear(0xFF)
    time.sleep(1)

    w = display.width
    h = display.height
    print('width:',w)
    print('height:',h) 
 
    font18 = ImageFont.truetype('Font.ttc', 18)

    image = Image.new('1', (h,w), 255)  	# 255: clear the frame
    draw = ImageDraw.Draw(image)
    draw.rectangle((10, 10, 200, 100), outline = 0)
    draw.text((70, 50), 'ELEKTOR', font = font18, fill = 0)
    display.display(display.getbuffer(image))
    time.sleep(2)

    display.sleep()
    display.Dev_exit()

except KeyboardInterrupt:
    epd2in13d.epdconfig.module_exit()
    exit()
