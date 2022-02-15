#--------------------------------------------------------------
#	   DISPLAY TEXT USING A LABEL
#	   ==========================
#
# This rogram displays the text "Hello From Raspberry Pi..."
# using a Label. This program uses the ttk
#
# Author: Dogan Ibrahim
# File  : gui1.py
# Date  : November 2020
#--------------------------------------------------------------
from tkinter import *
from tkinter import ttk

window = Tk()

window.title("MY FIRST TKINTER EXAMPLE")
window.geometry("600x600")
a_label = ttk.Label(window, text = "Hello From Raspberry Pi..")
a_label.grid(column=0,row=0)
a_label.configure(foreground='red', font=('times',30,'bold'))

window.mainloop()

