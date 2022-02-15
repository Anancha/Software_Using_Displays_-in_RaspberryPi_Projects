#--------------------------------------------------------------
#	   DISPLAY TEXT USING A LABEL
#	   ==========================
#
# This rogram displays the text "Hello From Raspberry Pi..."
# using a Label.
#
# Author: Dogan Ibrahim
# File  : gui1.py
# Date  : November 2020
#--------------------------------------------------------------
from tkinter import *

window = Tk()

window.title("MY FIRST TKINTER EXAMPLE")
labelfont = ('times', 30, 'bold')
LabelWidget = Label(window, text = "Hello From Raspberry Pi..")
LabelWidget.config(font=labelfont)
LabelWidget.pack()

window.mainloop()

