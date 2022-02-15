
#----------------------------------------------------------------------
#
#			LCD SECONDS COUNTER
#			===================
#
# This program displays "Counter" at first row, column 4 of the LCD.
# The count is displayed in the second row in the following format:
#
#     Counter
# Count=nn
#
# Author: Dogan Ibrahim
# File  : LCDCounter.py
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
lcd.cursor_position(4, 0)			# Set at (4, 0)
lcd.message="Counter"				# Display text
cnt = 0						# Initialize cnt
lcd.cursor_position(0, 1)			# Set at (0, 1)
lcd.message="Count="				# Display text

try:

   while True:					# Do Forever
      lcd.cursor_position(6,1)			# Set at (6, 1)
      lcd.message=str(cnt)			# Display cnt
      cnt = cnt + 1				# Increment cnt
      time.sleep(1)				# Wait 1 second

except KeyboardInterrupt:
    exit(0)
 
