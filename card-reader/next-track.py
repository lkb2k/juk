from button import *
import time
from Sonos import Sonos
        
button = Button(17)
sonos = Sonos()

while True:
    if button.is_pressed():
        print(time.time())
        sonos.next()
