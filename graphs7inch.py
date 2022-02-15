#--------------------------------------------------------------
#
#		DRAW LINEAR AND QUADRATIC GRAPHS
#		================================
#
# This program uses the matplotlib library to draw linear and
# quadratic graphs on th e7 inch display
#
# Author: Dogan Ibrahim
# File  : graphs7inch.py
# Date  : November 2020
#--------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-5,5,100)
plt.plot(x,x+5,label='x+5')
plt.plot(x,x**2,label='x**2')
plt.plot(x,x**2 + 4*x + 20,label='x**2+4x+20')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Graphs of linear and quadratic functions')
plt.legend()
plt.grid()
plt.show()

