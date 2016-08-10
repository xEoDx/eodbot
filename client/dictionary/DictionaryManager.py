import requests
import configparser

class DictionaryManager(object):
	
	def __init__(self):
		print("Initialising DictionaryManager")
		config = configparser.ConfigParser()
		config.read('config.ini')
		
		self.server_host=config['EODBOT']['eodbot.server.host']
		self.server_port=config['EODBOT']['eodbot.server.port']
		
		self.dictionary_request_url = 'http://'+self.server_host+':'+self.server_port+'/message'

	def fetchDictionary(self):
		response = requests.get(self.dictionary_request_url, data="")
		data = response.json()
		return data