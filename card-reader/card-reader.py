#!/usr/bin/env python

import time
import datetime
import RPi.GPIO as GPIO
import SimpleMFRC522
from CardDB import CardDB
from Sonos import Sonos

cardDB = CardDB()
sonos = Sonos()

reader = SimpleMFRC522.SimpleMFRC522()

try:
	while True:
		try: 
			id, text = reader.read()
			print(datetime.datetime.now().isoformat()+ ':' + str(id))
			playlist = cardDB.getPlaylist(str(id))
			if playlist:			
				print(playlist)
				sonos.play(playlist)
				time.sleep(2) #debounce
				
			#grab album art			
			#swap album art
			time.sleep(0.2)	 
		except OSError as e:
			print "Execution failed:" 
			time.sleep(0.2)	

finally:
	print("cleaning up")
	GPIO.cleanup()
