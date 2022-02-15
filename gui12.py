#-------------------------------------------------------
#	   	Using Scales (Slides)
#	   	=====================
#
# This example displays the scale's numeric value on
# the screen
#
# Author: Dogan Ibrahim
# File  : gui12.py
# Date  : November 2020
#------------------------------------------------------
from tkinter import *

window = Tk()

def get():
  print(S1.get()) 

S1 = Scale(window, from_=0, to=50)
S1.pack()
Button(window, text="Show", command=get).pack()

window.mainloop()

