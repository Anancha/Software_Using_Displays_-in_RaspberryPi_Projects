#--------------------------------------------------------------
#	   	LABEL AND TWO BUTTONS
#	   	=====================
#
# This program displays text "Button 1 Pressed" when one button is
# is pressed, and terminates the program when other one is pressed
#
# Author: Dogan Ibrahim
# File  : gui3.py
# Date  : November 2020
#--------------------------------------------------------------
from tkinter import *

window = Tk()

def disp():
   LabelWidget = Label(window, text = "Button 1 Pressed")
   LabelWidget.config(font=labelfont)
   LabelWidget.pack()

window.title("LABEL AND 2 BUTTONS EXAMPLE")
window.geometry("600x200")
labelfont = ('times', 20, 'bold')
Button1 = Button(window, text = "Click Me", command=disp)
Button1.pack(side="left")
Button2 = Button(window, text="Quit", command=window.quit)
Button2.pack(side="right")

window.mainloop()

