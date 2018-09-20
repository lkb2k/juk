import RPi.GPIO as GPIO
import time
from Sonos import Sonos
        
sonos = Sonos()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.IN)
GPIO.setup(18, GPIO.OUT)

def beep():
  GPIO.output(18, GPIO.HIGH)
  time.sleep(0.1)
  GPIO.output(18, GPIO.LOW)

last_pressed = time.time()
while True:
    now = time.time()
    if GPIO.input(24) and now - last_pressed > .5:
	last_pressed = now
	beep()
        sonos.next()
