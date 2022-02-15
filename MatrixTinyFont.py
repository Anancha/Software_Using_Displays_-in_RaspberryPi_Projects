#-----------------------------------------------------------------------
#
#			SCROLLING TINY LETTERS
#			======================
#
# In this program the printable ASCII characters from 33 to 127 are
# scrolled in small fonts
#
# Author: Dogan Ibrahim
# File  : MatrixTinyFont.py
# Date  : November 2010
#-----------------------------------------------------------------------
from luma.core.interface.serial import spi,noop
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional,TINY_FONT
from luma.led_matrix.device import max7219
import time

serial=spi(port=0,device=0,gpio=noop())
device=max7219(serial,width=32,height=8,rotate=0,block_orientation=-90)
device.contrast(100)

while True:
   for j in range(33, 128):
      show_message(device, chr(j), fill="white",scroll_delay=0.05,font=TINY_FONT)
   time.sleep(1)

while True:
   pass

