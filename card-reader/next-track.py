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
    pressed =  not GPIO.input(24)
    if pressed and now - last_pressed > .5:
	last_pressed = now
        print("Next track pressed")
        sonos.next()
