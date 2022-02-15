#-----------------------------------------------------------------------
#
#			SCROLL LETTERS
#			==============
#
# In this program the letters Elektor is scrolled on the display
#
# Author: Dogan Ibrahim
# File  : MatrixScroll.py
# Date  : November 2010
#-----------------------------------------------------------------------
from luma.core.interface.serial import spi,noop
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional,LCD_FONT
from luma.led_matrix.device import max7219
import time

serial=spi(port=0,device=0,gpio=noop())
device=max7219(serial,width=32,height=8,rotate=0,block_orientation=-90)
device.contrast(100)
msg = "Elektor"

while True:
   show_message(device, msg, fill="white",scroll_delay=0.1)
   time.sleep(1)

while True:
   pass

