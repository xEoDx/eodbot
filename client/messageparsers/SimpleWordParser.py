from messageparsers import EodBotParser

class SimpleWordParser(EodBotParser.EodBotParser):
	def __init__(self, textHooksDictionary):
		print("SimpleWordParser has been registered")
		self.textHooksDictionary = textHooksDictionary
		
		
	def updateDictionary(self, newDict):
		print("Updating dictionary current data: ",self.textHooksDictionary)		
		print("Updating dictionary with new data: ",newDict)		
		#self.textHooksDictionary = newDict
	
	def parse(self, text):
		print ("Parsing text:[", text, "].")
		
		splittedText = text.split(' ', 1)		
		
		for word in splittedText:
			if(word in self.textHooksDictionary):
				print(self.textHooksDictionary[word])
				return self.textHooksDictionary[word]