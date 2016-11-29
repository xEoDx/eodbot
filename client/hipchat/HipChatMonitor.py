from hipchat import HipChatManager
import time
import configparser

_MAX_SLEEP_TIME = 5
_MIN_SLEEP_TIME = 2
_SPAM_EODBOT_URL = 3500
class HipChatMonitor:	
	def __init__(self, eodBotParser):
		print("Initializing HipChatMonitor with eodBotParser: ",eodBotParser)
		self.sleepTime = _MIN_SLEEP_TIME
		self.lastIdChecked = ""
		
		self.eodBotParser = eodBotParser
		
		config = configparser.ConfigParser()
		config.read('config.ini')
		self.bot_id=config['HIPCHAT']['hipchat.bot_id']

		self.hipChatManager = HipChatManager.HipChatManager();
		self.spamLastEodBotUrlTime = 0
		self.hipChatManager.send("[EodBot] I've been initialised! Troll time just started :)")
		self.hipChatManager.send("[EodBot] Visit http://6dc1e2bd.fbdev.midasplayer.com/ to teach me how to troll")
		
	def __adjustInterval(self, failed):
		if(failed == "true"):
			if(self.sleepTime < _MAX_SLEEP_TIME):			
				self.sleepTime += 1
		else:
			self.sleepTime = _MIN_SLEEP_TIME

	def start(self):	
		while 1==1:
			newestMessage = self.hipChatManager.fetch()			
			if((str(newestMessage["from"]) != "Sassy") and (str(newestMessage["from"]["id"]) != self.bot_id) and (newestMessage["id"] != self.lastIdChecked)):
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
			
			self.spamLastEodBotUrlTime += 1
			if(self.spamLastEodBotUrlTime >= _SPAM_EODBOT_URL):
				self.hipChatManager.send("[EodBot] Visit http://6dc1e2bd.fbdev.midasplayer.com/ to teach me how to troll")
				self.spamLastEodBotUrlTime = 0
