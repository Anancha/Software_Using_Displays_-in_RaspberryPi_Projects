
#----------------------------------------------------------------------
#
#		DISPLAY THE CURRENT DATE AND TIME
#		=================================
#
# This program displays the current date and time on the LCD
#
# Author: Dogan Ibrahim
# File  : LCDTime.py
# Date  : November 2020
#----------------------------------------------------------------------- 
import board
import digitalio
import time
import adafruit_character_lcd.character_lcd as characterlcd
from datetime import datetime

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

  while True:
     line1 = datetime.now().strftime("%d-%m-%Y\n%H:%M:%S")
     lcd.message = line1
     time.sleep(1)

except KeyboardInterrupt:
     exit()
 
