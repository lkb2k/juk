import urllib2
import json 
import time

class Sonos:
	def __init__(self):
		self.host = 'http://localhost:5005'
		self.room = 'Living%20Room'
		self.endpoint = self.host+'/'+self.room
		self.playing = ''
		self.lastUpdate = time.time()

	def lastUpdateSeconds(self):
		return time.time() - self.lastUpdate 
		
	def play(self, uri):	
		if(self.playing == uri and self.lastUpdateSeconds() < 30):
			print('ignoring duplicate play request')
			return #ignore duplicates for 30 sec
	
		self.playing = uri
		self.lastUpdate = time.time()

		playlist = 'spotify/now'+'/'+uri
		urllib2.urlopen(self.endpoint+'/'+'clearqueue')
		urllib2.urlopen(self.endpoint+'/'+playlist)
	
	def next(self):
		urllib2.urlopen(self.endpoint+'/next')		
