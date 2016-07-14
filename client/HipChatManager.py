import requests

import configparser

class HipChatManager:
	def __init__(self):
		print("Initializing HipChatManager. Config: ")
		config = configparser.ConfigParser()
		config.read('config.ini')
		
		self.room_name=config['HIPCHAT']['hipchat.room_name']
		self.read_auth_token=config['HIPCHAT']['hipchat.read_auth_token']
		self.write_auth_token=config['HIPCHAT']['hipchat.write_auth_token']
		
		self.read_url = 'http://hipchat.com/v2/room/'+self.room_name+'/history/latest?max-results=1&auth_token='+self.read_auth_token
		self.write_url = 'http://hipchat.com/v2/room/'+self.room_name+'/message?auth_token='+self.write_auth_token
		
	def fetch(self):
		response = requests.get(self.read_url, data="")
		data = response.json()		
		return data["items"][0]		
		
	def send(self, message):
		data = {"message":message}
		print("Writing into chat: ",data)
		response = requests.post(self.write_url, json=data)
		print (response)	