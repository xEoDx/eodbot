from hipchat import HipChatManager
import time

_MAX_SLEEP_TIME = 5
_MIN_SLEEP_TIME = 2
class HipChatMonitor:	
	def __init__(self, eodBotParser):
		print("Initializing HipChatMonitor with eodBotParser: ",eodBotParser)
		self.sleepTime = _MIN_SLEEP_TIME
		self.lastIdChecked = ""
		
		self.eodBotParser = eodBotParser

		self.hipChatManager = HipChatManager.HipChatManager();
		self.hipChatManager.send("EodBot has been initialised!")
		self.hipChatManager.send("Add your messages at: http://6dc1e2bd.fbdev.midasplayer.com/")
		
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
				messageToSend = self.eodBotParser.parse(newestMessage['message'])
				if(messageToSend != None):
					self.hipChatManager.send(messageToSend)
				self.__adjustInterval("false")
			else:
				self.__adjustInterval("true")
				
			print("Sleeping for ",self.sleepTime," seconds")
			time.sleep(self.sleepTime)