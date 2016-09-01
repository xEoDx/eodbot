from messageparsers import EodBotParser
from random import randint

class SentenceWordParser(EodBotParser.EodBotParser):
	def __init__(self, textHooksDictionary):
		print("SimpleWordParser has been registered")
		self.textHooksDictionary = textHooksDictionary
		
		
	def updateDictionary(self, newDict):
		print("Updating dictionary with new data: ",newDict)	
		self.textHooksDictionary = newDict			
	
	def parse(self, text):
		print ("Parsing text:[", text, "].")		
		for message in self.textHooksDictionary:				
			if(message['key'].lower() in text.lower()):
				responsesLength = len(message['responses'])
				randAnswer = randint(0,responsesLength-1)	
				answer = "[EodBot] "+message['responses'][randAnswer]
				print("Answering: ",answer)			
				return answer