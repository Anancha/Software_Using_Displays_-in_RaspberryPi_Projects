#------------------------------------------------------
#	   	Using Dialogs
#	   	=============
#
# In this example two dialog type displays are shown
#
# Author: Dogan Ibrahim
# File  : gui11.py
# Date  : November 2020
#------------------------------------------------------
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Dialogs")

def error():
  messagebox.showerror("","You clicked error")

def okcancel():
  messagebox.askokcancel("","You clicked OK or CANCEL")

def yesno():
  messagebox.askyesno("","You clicked YES-NO")

def warning():
  messagebox.showwarning("","You clicked WARNING")

Button(window, text="Error", command=error).pack(fill="x")
Button(window, text="OK or CANCEL", command=okcancel).pack(fill="x")
Button(window, text="YES-NO", command=yesno).pack(fill="x")
Button(window, text="WARNING", command=warning).pack(fill="x")

window.mainloop()

