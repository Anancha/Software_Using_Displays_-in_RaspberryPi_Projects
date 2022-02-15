#--------------------------------------------------------------
#	   	LABEL AND BUTTON EXAMPLE
#	   	========================
#
# This program displays text "You Clicked Me" when a button is
# clicked
#
# Author: Dogan Ibrahim
# File  : gui2.py
# Date  : November 2020
#--------------------------------------------------------------
from tkinter import *

window = Tk()

def disp():
   LabelWidget = Label(window, text = "You Clicked Me")
   LabelWidget.config(font=labelfont)
   LabelWidget.pack(side="top")

window.title("LABEL AND BUTTON EXAMPLE")
window.geometry("400x200")
labelfont = ('times', 20, 'bold')
ButtonWidget = Button(window, text = "Click Me", command=disp)
ButtonWidget.pack(side="top", expand="yes", fill="both")

window.mainloop()

