#---------------------------------------------------------------------
#	    MATRIX DISPLAY DRAW RECTANGLE AND LETTERS
#	    =========================================
#
# In this program a rectangle box is drawn and letters rect are
# displayed inside this box
#
# Author: Dogan Ibrahim
# File  : matrixRectangle.py
# Date  : November 2020
#---------------------------------------------------------------------
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text
from luma.core.legacy.font import SINCLAIR_FONT

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial,width=32,height=8,rotate=0,block_orientation=-90)
device.contrast(100)

with canvas(device) as draw:
   draw.rectangle(device.bounding_box, outline="white")
   text(draw, (1, 0), "rect", fill="white", font=SINCLAIR_FONT)

while True:
   pass

