#----------------------------------------------------------
#	   		Using Menu
#	   		==========
#
# This example shows how a menu and submenus can be created
#
# Author: Dogan Ibrahim
# File  : gui13.py
# Date  : November 2020
#----------------------------------------------------------
from tkinter import *

window = Tk()
window.title("MENU")

def NewFile():
  print("New File")

def OpenFile():
  print("Open File")

def SaveFile():
  print("Save File")

def SaveAs():
  print("Save As")

menu = Menu(window)
window.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_command(label="Save", command=SaveFile)
filemenu.add_command(label="Save As", command=SaveAs)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)

homemenu = Menu(menu)
menu.add_cascade(label="Home", menu=homemenu)

window.mainloop()

