from messageparsers import EodBotParser
from random import randint

class SimpleWordParser(EodBotParser.EodBotParser):
	def __init__(self, textHooksDictionary):
		print("SimpleWordParser has been registered")
		self.textHooksDictionary = textHooksDictionary
		
		
	def updateDictionary(self, newDict):
		print("Updating dictionary current data: ",self.textHooksDictionary)		
		print("Updating dictionary with new data: ",newDict)	
		self.textHooksDictionary = newDict			
	
	def parse(self, text):
		print ("Parsing text:[", text, "].")		
		splittedText = text.split(' ', 1)		
		for word in splittedText:
			for message in self.textHooksDictionary:				
				if(message['key'] == word):
					responsesLength = len(message['responses'])
					randAnswer = randint(0,responsesLength-1)	
					answer = message['responses'][randAnswer]
					print("Answering: ",answer)			
					return answer		