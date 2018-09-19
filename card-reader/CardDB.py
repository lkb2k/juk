import csv
import os.path
import sys

class CardDB:
	def __init__(self):
		self.path = '/var/cache/juk'
		self.cardList = self.load()
        
	def load(self):
		if not os.path.exists(self.path + '/cardList.csv'):
			with open(self.path + '/cardList.csv', 'w'): pass
		with open(self.path + '/cardList.csv', mode='r') as infile:
			reader = csv.reader(infile)
			cardList = {rows[0]:rows[1] for rows in reader}
			infile.close()
		return cardList
	
	def getPlaylist(self,card):
		self.cardList = self.load()
		try:
			return self.cardList[card]
		except:
			print 'Card %s is not card list' % card
			with open(self.path + '/cardList.csv', mode='a') as infile:
				infile.write(str(card) + ',\n')			
			return ''