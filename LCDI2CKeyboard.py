
#----------------------------------------------------------------------
#
#		READ FROM KEYBOARD AND DISPLAY ON I2C LCD
#		=========================================
#
# This program reads text from the keyboard and displays on the LCD
#
# Author: Dogan Ibrahim
# File  : LCDI2CKeyboard.py
# Date  : November 2020
#----------------------------------------------------------------------- 
from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', 0x27)

lcd.home()					# Home cursor
YN = "Y"

try:

  while YN == "Y":
    txt = input("Enter text (not more than 16 characters): ")
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string(txt)
    YN = input("Any more (Y/N)?")
    YN = YN.upper()

except KeyboardInterrupt:
    exit(0)
 
