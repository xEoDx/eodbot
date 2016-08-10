import DictionaryManager

class DictionaryMonitor(object):
	def __init__(self):
		dictionaryManager = DictionaryManager()
		dictionaryManager.fetchDictionary()