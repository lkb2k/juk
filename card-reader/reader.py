#!/usr/bin/env python

import datetime
import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

try:
    while True:
        id, text = reader.read()
        print(datetime.datetime.now().isoformat()+ ':' + str(id))

finally:
    print("cleaning up")
    GPIO.cleanup()
