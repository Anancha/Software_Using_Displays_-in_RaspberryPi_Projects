#---------------------------------------------------------
#	   	Using Grids
#	   	===========
#
# In this example the names of 6 countries are displayed
#
# Author: Dogan Ibrahim
# File  : gui7.py
# Date  : November 2020
#---------------------------------------------------------
from tkinter import *

window = Tk()

countries = ['UK','Germany','France','Italy','Belgium','Ireland']

r = 0
for country in countries:
  Button(window, text = country, width = 50).grid(row = r, column = 0)
  r = r + 1

window.mainloop()

