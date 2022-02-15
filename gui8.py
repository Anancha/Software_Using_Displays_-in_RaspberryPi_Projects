#-------------------------------------------------------
#	   	Using Radio Buttons
#	   	===================
#
# In this example a country and 6 cities are displayed
# and the user is asked to click the capital city of
# the displayed country.
#
# Author: Dogan Ibrahim
# File  : gui8.py
# Date  : November 2020
#-------------------------------------------------------
from tkinter import *

window = Tk()

capcity = 0
window.geometry("400x150")

Label(window, text = "Capital city of France?").pack()
Radiobutton(window,text="London", variable = capcity, value = 1).pack(anchor="w")
Radiobutton(window,text="Rome", variable = capcity, value = 2).pack(anchor="w")
Radiobutton(window,text="Paris", variable = capcity, value = 3).pack(anchor="w")
Radiobutton(window,text="Ankara", variable = capcity, value = 4).pack(anchor="w")
Radiobutton(window,text="Istanbul", variable = capcity, value = 5).pack(anchor="w")
Radiobutton(window,text="Madrid", variable = capcity, value = 6).pack(anchor="w")

window.mainloop()


