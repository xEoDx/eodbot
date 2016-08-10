import abc

class EodBotParser(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def updateDictionary(self, newDict):
		pass
	
	@abc.abstractmethod
	def parse(self, text):
		pass
		
	