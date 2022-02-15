#-----------------------------------------------------------------------
#
#			DISPLAY LETTERS
#			===============
#
# Thsi program displays letters ELECT on the matrix display
#
# Author: Dogan Ibrahim
# File  : MatrixLetters.py
# Date  : November 2010
#-----------------------------------------------------------------------
from luma.core.interface.serial import spi,noop
from luma.core.render import canvas
from luma.core.legacy import text
from luma.core.legacy.font import proportional,LCD_FONT
from luma.led_matrix.device import max7219

serial=spi(port=0,device=0,gpio=noop())
device=max7219(serial,width=32,height=8,rotate=0,block_orientation=-90)
device.contrast(100)

with canvas(device) as draw:
  text(draw,(0,0),"ELECT",fill="white",font=proportional(LCD_FONT))

while True:
   pass

