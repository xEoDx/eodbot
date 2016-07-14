import SimpleWordParser
import json
import requests
import time
import configparser

MAX_SLEEP_TIME = 15
MIN_SLEEP_TIME = 3

class HipChatManager:

	def __init__(self):
		print("Initializing HipChatManager")
		self.initializeHipChatConfiguration()
				
		self.sleepTime = MIN_SLEEP_TIME
		self.lastIdChecked = ""
		self.simpleWordParser = SimpleWordParser.SimpleWordParser({'hello': 'morning', 'goodbye': 'bye bitch', 'hey': 'hej hej'})
		self.url = 'http://hipchat.com/v2/room/'+self.room_name+'/history/latest?max-results=1&auth_token='+self.read_auth_token
		
	
	def initializeHipChatConfiguration(self):
		config = configparser.ConfigParser()
		config.read('config.ini')
		self.room_name=config['HIPCHAT']['hipchat.room_name']
		self.read_auth_token=config['HIPCHAT']['hipchat.read_auth_token']
		self.write_auth_token=config['HIPCHAT']['hipchat.write_auth_token']
	
	def adjustInterval(self, failed):
		if(failed == "true"):
			if(self.sleepTime < MAX_SLEEP_TIME):			
				self.sleepTime += 1
		else:
			self.sleepTime = MIN_SLEEP_TIME

	def fetch(self):		
		response = requests.get(self.url, data="")
		data = response.json()		
		return data["items"][0]
	'''
	def notifyIfMessageIsTooLong(message):
		if(len(message["message"]) > 90):
			print ("The message %s has more than 90 characters!", message["message"])
			url = 'http://hipchat.com/v2/room/VictorTest/message?auth_token='+self.write_auth_token
			values = {"message":"The message you've just sent is over 90 characters. No one will read it :("}
			req = urllib2.Request(url)
			req.add_header('Content-Type','application/json')
			data = json.dumps(values)
			response = urllib2.urlopen(req,data)                
			print (response)
	'''
	def start(self):	
		while 1==1:
			newestMessage = self.fetch()
			if(newestMessage["id"] != self.lastIdChecked):
				self.lastIdChecked = newestMessage["id"]
				print("Parsing message: ",newestMessage['message'])
				self.simpleWordParser.parse(newestMessage['message'])
				self.adjustInterval("false")
			else:
				self.adjustInterval("true")
				
			print("Sleeping for ",self.sleepTime," seconds")
			time.sleep(self.sleepTime)

hipChatManager = HipChatManager()
hipChatManager.start()