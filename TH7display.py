#--------------------------------------------------------------
#	   	TEMPERATURE AND HUMIDITY
#	   	========================
#
# This program displays the ambient temperature and humidity
#
# Author: Dogan Ibrahim
# File  : TH7display.py
# Date  : November 2020
#--------------------------------------------------------------
#
# Import the libraries
#
from datetime import datetime
from tkinter import ttk
from tkinter import *
import time
import board
import adafruit_dht

sensor=adafruit_dht.DHT11(board.D2)

window = Tk()

#
# This function terminates the display
#
def end_me():
  exit(0)

#
# This function reads and displays the temperature and humidity
#
def timeout():
  timdat = datetime.now().strftime("%d-%m-%Y %H:%M:%S")  
  window.after(5000, timeout)
  a_label = ttk.Label(window, text=timdat)
  a_label.grid(column=3,row=1)
  a_label.configure(foreground='green',font=('times',20,'bold'))

  b_label=ttk.Label(window,text="Temperature (C):")
  b_label.grid(row=5,sticky=E)
  b_label.configure(foreground='red',font=('times',20,'bold'))

  c_label=ttk.Label(window,text="   Humidity (%):")
  c_label.grid(row=7,sticky=E)
  c_label.configure(foreground='blue',font=('times',20,'bold'))

  Temp=StringVar()
  Hum=StringVar()
  temperature=sensor.temperature
  humidity=sensor.humidity
  Temp=str(temperature)
  Hum=str(humidity)
  d_label=ttk.Label(window,text=Temp)
  d_label.grid(column=2,row=5,padx=10)
  d_label.configure(foreground='red',font=('times',20,'bold'))

  e_label=ttk.Label(window,text=Hum)
  e_label.grid(column=2,row=7)
  e_label.configure(foreground='blue',font=('times',20,'bold'))

  action = Button(window,text="END", command=end_me)
  action.grid(column=4,row=9)
  action.configure(foreground='red',font=('times',15,'bold'))

#
# Display title
#
window.title("AMBIENT TEMPERATURE AND HUMIDITY")
window.geometry("600x200")

try:
  timeout()

except RuntimeError:
  time.sleep(2)
  timeout()

except Exception as error:
  raise error
  exit(0)

window.mainloop()

