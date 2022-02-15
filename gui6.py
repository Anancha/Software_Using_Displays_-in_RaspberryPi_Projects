#=================================================
#	   	Entry WIDGET
#	   	============
#
# This program reads user's text and displays it
#
# Author: Dogan Ibrahim
# File  : gui6.py
# Date  : November 2020
#=================================================
from tkinter import *

window = Tk()

def get():
  value=ent.get()
  print("%s" %value)

ent = Entry(window)
ent.insert(0, '')
ent.pack(side="top", fill="x")

ent.focus()
butn = Button(window, text="Get", command=get)
butn.pack(side="left")

window.mainloop()

