#--------------------------------------------------------------
#
#              		SELFIE WITH DISPLAY
#              		===================
#
# In this program the camera is connected to the Raspberry Pi.
# In addition, a button is connected to GPIO 2, and a buzzer
# is connected to GPIO3. The buzzer is activated briefly after
# a picture is taken by pressing the button. i.e. the buzzer
# simulates the shutter sound.The captured pictures are stored
# with the names made up of the current date and time
#
# In this program 4 pictures are taken before the program exits
#
# Author: Dogan Ibrahim
# File  : camdisp2.py
# Date  : November 2020
#--------------------------------------------------------------
from picamera import PiCamera			# import picamera
import RPi.GPIO as GPIO				# import GPIO
import time					# import time
import datetime as dt				# import datetime
GPIO.setwarnings(False)				# disable warnings

camera = PiCamera()
GPIO.setmode(GPIO.BCM)				# set BCM pin number
Button = 2					# Button at GPIO 2
Buzzer = 3					# Buzzer at GPIO 3
GPIO.setup(Button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Buzzer, GPIO.OUT)
GPIO.output(Buzzer, 0)				# Buzzer OFF 

camera.start_preview()
n = 0
#
# Start of the program loop. Check if the button is pressed
# and if so capture a picture and save it. The buzzzer simulates the 
# shutter sound. This version of teh program takes 4 pictures before
# terminating
#

for x in range(4):				# Do 4 times
  while GPIO.input(Button) == 1:
     pass
  camera.capture('/home/pi/mypics/Pic%s.jpg' %(dt.datetime.now()))
  GPIO.output(Buzzer, 1)			# Buzzer ON
  time.sleep(0.25)			        # Wait 250ms
  GPIO.output(Buzzer, 0)		  	# Buzzer OFF
camera.stop_preview()
camera.close()
exit(0)



