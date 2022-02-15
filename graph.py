#-------------------------------------------------------------------
#
#       	REAL TIME GRAPH OF HUMIDITY AND TEMPERATURE
#       	===========================================
#
# This program reads the ambient temperature and himidity from
# a DHT11 type sensor and displays them on the monitor in real-time
# as a graph.
#
# In this program data is collected every 2 seconds, for a period
# of 100 seconds.
#
#
# Program: graph.py
# Date   : November 2020
# Author : Dogan Ibrahim
#------------------------------------------------------------------
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import time
import board
import adafruit_dht

sensor = adafruit_dht.DHT11(board.D2)

#
# Start of main program. Humidity and temperature are read from
# DHT11 and are plotted in real time as the data are being read
#
plt.axis([0,100,0,100])
plt.title('Humidity and Temperature')
plt.xlabel('Time')
plt.ylabel('Hum. & Temp')

j=1
plt.ion()

#
# Read the humidity and temperature every 2 seconds for 100 seconds
#
i = 0
while i < 102:
  try:
    for i in range (0,102,2):
       temperature = sensor.temperature
       humidity = sensor.humidity
       x = float(i)
       plt.scatter(x,temperature,color='blue',label='Tempeature')
       plt.scatter(x,humidity,color='black',label='Humidity')
       plt.draw()
       if j == 1:
           j=0
           plt.legend()
       plt.pause(0.0001)
       time.sleep(2)

  except RuntimeError as error:
       time.sleep(2)
       continue

  except Exception as error:
       raise error
       exit(0)

  except KeyboardInterrupt:
       exit(0)


