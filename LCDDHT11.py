
#----------------------------------------------------------------------
#
#		DISPLAY THE TEMPERATURE AND HUMIDITY
#		=====================================
#
# This program displays the temperature and humidity on the LCD
#
# Author: Dogan Ibrahim
# File  : LCDDHT11.py
# Date  : November 2020
#----------------------------------------------------------------------- 
import board
import digitalio
import time
import adafruit_character_lcd.character_lcd as characterlcd
import adafruit_dht

sensor = adafruit_dht.DHT11(board.D26)

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


while True:
  try:

     temperature = sensor.temperature		# Read temperature
     humidity = sensor.humidity			# Read humidity
     t = '{0:0.1f}'.format(temperature)		# Format temp
     h = '{0:0.1f}'.format(humidity)		# Format humidity
     lcd.clear()				# Clear display
     lcd.set_cursor = (0, 0)			# At (0,0)
     line1 = "T = " + str(t) + "C\n"		# Line 1 + \n
     line2 = "H = " + str(h) + "%"		# Line 2
     lcd.message = line1+line2			# Display
     time.sleep(5)				# Wait

  except RuntimeError as error:
     time.sleep(2)
     continue

  except Exception as error:
     raise error
     exit(0)

  except KeyboardInterrupt:
     exit(0)
 
