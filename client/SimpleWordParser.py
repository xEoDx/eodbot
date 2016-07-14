from enum import Enum
class MessageType(Enum):
	order = 0,
	text = 1,
	question = 2,
	exclamation = 3
	

	
class SimpleWordParser:
	def __init__(self, textHooksDictionary):
		print("Initializing SimpleWordParser")
		self.textHooksDictionary = textHooksDictionary
		
	def addKey(self, dict):
		print(dict," has been added to the dict")
		self.textHooksDictionary.update(dict)
		
	def parse(self, text):
		print ("Parsing text:[", text, "].")
		
		splittedText = text.split(' ', 1)		
		
		for word in splittedText:
			if(word in self.textHooksDictionary):
				print(self.textHooksDictionary[word])
				return self.textHooksDictionary[word]

'''	
parser  = SimpleWordParser({'hello': 'morning', 'goodbye': 'bye bitch', 'hey': 'hej hej'})
parser.parse("Testtt")
parser.parse("hello")
parser.parse("goodbie")
parser.parse("goodbye")
parser.parse("goodbie")
parser.parse("goodbie hey")
parser.addKey({'goodbie':'learn how to wriet'})
parser.parse("goodbie")
'''