#---------------------------------------------------------
#	   	Using Checkbuttons
#	   	===================
#
# In this example the user selects the programming
# languages that he/she knows
#
# Author: Dogan Ibrahim
# File  : gui10.py
# Date  : November 2020
#---------------------------------------------------------
from tkinter import *

window = Tk()
window.title("Programming Languages")
languages = ["Pascal","Basic","C"]

def choice():
  if Var1.get() == 1:
    Label(window,  text="Pascal").grid(row=1, column=5)
  if Var2.get() == 1:
    Label(window, text="Basic").grid(row=2,column=5)
  if Var3.get() == 1:
    Label(window, text="C").grid(row=3,column=5)


Button(window, text="Select all that apply", command=choice).grid(row=8,column=1)
Button(window, text="Quit", command=window.quit).grid(row=8,column=2)

Label(window, text = "Select the programming languages you know").grid(row=0,column=1)

Var1 = IntVar()
Var2 = IntVar()
Var3 = IntVar()

Checkbutton(window,text=languages[0],variable = Var1).grid(row=1,sticky="w")
Checkbutton(window,text=languages[1],variable = Var2).grid(row=2,sticky="w")
Checkbutton(window,text=languages[2],variable = Var3).grid(row=3,sticky="w")

window.mainloop()

