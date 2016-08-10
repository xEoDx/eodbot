class SimpleWordParser:
	def __init__(self, textHooksDictionary):
		print("Initialising SimpleWordParser")
		self.textHooksDictionary = textHooksDictionary
		
	def addKey(self, entry):
		print(entry," has been added to the dict")
		self.textHooksDictionary.update(entry)
		
	def updateDict(self, dict):
		self.textHooksDictionary = dict
		
	def parse(self, text):
		print ("Parsing text:[", text, "].")
		
		splittedText = text.split(' ', 1)		
		
		for word in splittedText:
			if(word in self.textHooksDictionary):
				print(self.textHooksDictionary[word])
				return self.textHooksDictionary[word]