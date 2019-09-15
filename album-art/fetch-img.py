import urllib2
import time
import json
import os

currentImg = ''

if not os.path.exists('/var/cache/juk'):
    os.makedirs('/var/cache/juk')

while True:
	try:
		img = currentImg
		state = json.load(urllib2.urlopen('http://127.0.0.1:5005/Living%20Room/state'))
		if state['currentTrack'] and state['currentTrack']['absoluteAlbumArtUri']:
	  		img = state['currentTrack']['absoluteAlbumArtUri']

		if not img == currentImg:
			currentImg = img
			print 'updating album art'
			bytes = urllib2.urlopen(img).read()
			with open('/var/cache/juk/album-art.jpg', 'w') as imgFile: 
				imgFile.write(bytes)
	except Exception as e: print(e)	
	time.sleep(2)	
