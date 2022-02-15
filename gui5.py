#---------------------------------------------------
#	   	USING COLOURS
#	   	=============
#
# Using foreground and background colours and
# height and width
#
# Author: Dogan Ibrahim
# File  : gui5.py
# Date  : November 2020
#---------------------------------------------------
from tkinter import *

window = Tk()

window.title("EXAMPLE")
labelfont=('times', 18, 'bold')
L1=Label(window,text="Hello Tkinter")
L1.config(bg='black', fg='white')
L1.config(font=labelfont)
L1.config(height=4, width=20)
L1.pack(expand="yes", fill="both")

window.mainloop()

