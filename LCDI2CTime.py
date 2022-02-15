
#----------------------------------------------------------------------
#
#		DISPLAY THE CURRENT DATE AND TIME
#		=================================
#
# This program displays the current date and time on the I2C LCD
#
# Author: Dogan Ibrahim
# File  : LCDI2CTime.py
# Date  : November 2020
#----------------------------------------------------------------------- 
from datetime import datetime
from RPLCD .i2c import CharLCD
import time

lcd = CharLCD('PCF8574', 0x27)
lcd.home()					# Home cursor

try:

  while True:
     lcd.clear()
     lcd_line = datetime.now().strftime("%d-%m-%Y\r\n%H:%M:%S")
     cursor_pos = (0, 0)
     lcd.write_string(lcd_line)
     time.sleep(1)

except KeyboardInterrupt:
     exit()
 
