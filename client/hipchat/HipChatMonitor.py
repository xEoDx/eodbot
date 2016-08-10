from messageparsers import SimpleWordParser
from hipchat import HipChatManager
import time

_MAX_SLEEP_TIME = 15
_MIN_SLEEP_TIME = 3
class HipChatMonitor:	
	def __init__(self):
		print("Initializing HipChatMonitor")
		self.sleepTime = _MIN_SLEEP_TIME
		self.lastIdChecked = ""
		self.simpleWordParser = SimpleWordParser.SimpleWordParser({'hello': 'morning', 'goodbye': 'bye bitch', 'hey': 'hej hej'})

		self.hipChatManager = HipChatManager.HipChatManager();
		self.hipChatManager.send("EodBot has been initialized!")
		
	def __adjustInterval(self, failed):
		if(failed == "true"):
			if(self.sleepTime < _MAX_SLEEP_TIME):			
				self.sleepTime += 1
		else:
			self.sleepTime = _MIN_SLEEP_TIME

	def start(self):	
		while 1==1:
			newestMessage = self.hipChatManager.fetch()
			if(newestMessage["id"] != self.lastIdChecked):
				self.lastIdChecked = newestMessage["id"]
				print("Parsing message: ",newestMessage['message'])
				messageToSend = self.simpleWordParser.parse(newestMessage['message'])
				if(messageToSend != None):
					self.hipChatManager.send(messageToSend)
				self.__adjustInterval("false")
			else:
				self.__adjustInterval("true")
				
			print("Sleeping for ",self.sleepTime," seconds")
			time.sleep(self.sleepTime)