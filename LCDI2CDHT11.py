#-----------------------------------------------------------------
#            DISPLAY TEMPERATURE AND HUMIDITY ON I2C LCD
#            ==========================================
#
# In this project a DHT11 type temperatrue and humidity sensor is
# connected to the Raspberry Pi. The project displays the humidity
# and temperature on the display every 5 seconds
#
# Author: Dogan Ibrahim
# File  : LCDI2CDHT11.py
# Date  : November 2020
#-------------------------------------------------------------------
import time
import board
from RPLCD.i2c import CharLCD		# Import I2C LCD library
import adafruit_dht			# Adafruit DHT11 library

LCD = CharLCD('PCF8574',0x27)
sensor = adafruit_dht.DHT11(board.D26)

while True:

  try:

     temperature = sensor.temperature		# Read temperature
     humidity = sensor.humidity			# Read humidity
     LCD.clear()				# Clear LCD
     LCD.cursor_pos=(0,0)			# Cursor at (0,0)
     LCD.write_string("Temp and Hum")		# HEading
     temp = str(temperature)[:4]		# Format temp
     hum = str(humidity)[:4]			# Format hum
     dsp = temp + "C " + hum + "%"		# Combine temp+hum
     LCD.cursor_pos=(1,0)			# Cursor at (1,0)
     LCD.write_string(dsp)			# Display T and H
     time.sleep(5)				# Wait 5 seconds

  except RuntimeError as errro:
     time.sleep(2)
     continue

  except Exception as error:
     raise error
     exit(0)

  except KeyboardInterrupt:			# Keyboard interrupt
     exit(0)


