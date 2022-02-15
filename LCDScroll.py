
#----------------------------------------------------------------------
#
#		READ FROM KEYBOARD AND SCROLL LEFT ON LCD
#		=========================================
#
# This program reads text from the keyboard and scrolls left on the LCD
#
# Author: Dogan Ibrahim
# File  : LCDScroll.py
# Date  : November 2020
#----------------------------------------------------------------------- 
import board
import digitalio
import time
import adafruit_character_lcd.character_lcd as characterlcd

#
# Interface between the LCD and Raspberry Pi
#
D4 = digitalio.DigitalInOut(board.D21)		# Pin 40
D5 = digitalio.DigitalInOut(board.D20)		# Pin 38
D6 = digitalio.DigitalInOut(board.D16)		# Pin 36
D7 = digitalio.DigitalInOut(board.D12)		# Pin 32
RS = digitalio.DigitalInOut(board.D7)		# Pin 36
E = digitalio.DigitalInOut(board.D8)		# Pin 24
Columns = 16
Rows = 2


lcd = characterlcd.Character_LCD_Mono(RS,E,D4,D5,D6,D7,Columns,Rows)

lcd.home()					# Home cursor

try:

   txt = input("Enter text (not more than 16 characters): ")
   while True:
      lcd.cursor_position(15, 0)
      lcd.message = txt
      for i in range(len(txt)):
         lcd.move_left()
         time.sleep(0.5)

except KeyboardInterrupt:
    exit(0)
 
