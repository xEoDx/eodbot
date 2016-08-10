from threading import Thread
from dictionary import DictionaryManager
import time

class DictionaryMonitor(Thread):
	def __init__(self, eodBotParser):
		super(DictionaryMonitor, self).__init__()
		
		print("Initialising DictionaryMonitor with parser: ",eodBotParser)
		self.eodBotParser = eodBotParser
		self.dictionaryManager = DictionaryManager.DictionaryManager()
		self.dictionaryManager.fetchDictionary()
		
		self.cancelled = False
		self.daemon = True
	
	def run(self):
		while not self.cancelled:
			self.update()
			time.sleep(60)
			
	def update(self):
		print("Updating dictionary from backend...")
		data = self.dictionaryManager.fetchDictionary()
		self.eodBotParser.updateDictionary(data)
			
	def cancel(self):        
		self.cancelled = True