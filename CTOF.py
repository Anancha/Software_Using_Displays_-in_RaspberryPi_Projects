#--------------------------------------------------------------
#	   	TEMPERATURE CONVERSION
#	   	======================
#
# This rogram converts Degrees Centigrade to Degrees Fahrenheit
#
# Author: Dogan Ibrahim
# File  : CTOF.py
# Date  : November 2020
#--------------------------------------------------------------
from tkinter import ttk
from tkinter import *

window = Tk()

#
# This function convert the given C to F
#
def click_me():
   value = float(C_entered.get())
   Fahrenheit.set(1.8*value + 32)


window.title("TEMPERATURE CONVERSION")
window.geometry("500x150")
window.config(bg='yellow')

a_label = ttk.Label(window, text = "Centigrade")
a_label.grid(column=1,row=1)
a_label.configure(foreground='red', font=('times',10,'bold'))

Cname=StringVar()
C_entered=ttk.Entry(window,width=10,textvariable=Cname)
C_entered.grid(column=3, row=1)
Fahrenheit=StringVar()
ttk.Label(window,textvariable=Fahrenheit).grid(column=2,row=3)

action = ttk.Button(window,text="Calculate",command=click_me)
action.grid(column=6,row=2)

ttk.Label(window,text = "is equal to").grid(column=4,row=1,sticky=E)
ttk.Label(window,text="Fahrenheit",foreground='blue').grid(column=3,row=3)

C_entered.focus()

window.mainloop()

