#------------------------------------------------------
#	   	Using Radio Buttons
#	   	===================
#
# In this example a country and 6 cities are displayed
# and the user is asked to click the capital city of
# the displayed country. Messages are displayed to let
# the user know if the chosen city is correct or not
#
# Author: Dogan Ibrahim
# File  : gui9.py
# Date  : November 2020
#------------------------------------------------------
from tkinter import *

window = Tk()
window.title("Capital Cities")

def choice():
  if capcity.get() == 3:
   Label(window,  text="     Correct").grid(row=1, column=5)
  else:
    Label(window, text="Not Correct").grid(row=1, column=5)
 

capcity = IntVar()
value = 0

Button(window, text="Select one", command=choice).grid(row=8,column=1)

Label(window, text = "Capital city of France?").grid(row=0,column=1)
Radiobutton(window,text="London  ",    variable = capcity, value = 1).grid(row=1,column=0)
Radiobutton(window,text="Rome     ",   variable = capcity, value = 2).grid(row=2,column=0)
Radiobutton(window,text="Paris      ", variable = capcity, value = 3).grid(row=3,column=0)
Radiobutton(window,text="Ankara  ",    variable = capcity, value = 4).grid(row=4,column=0)
Radiobutton(window,text="Istanbul",    variable = capcity, value = 5).grid(row=5,column=0)
Radiobutton(window,text="Madrid  ",    variable = capcity, value = 6).grid(row=6,column=0)

window.mainloop()

