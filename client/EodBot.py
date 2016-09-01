from messageparsers import EodBotParser
from messageparsers import SentenceWordParser as parser
from hipchat import HipChatMonitor
from dictionary import DictionaryMonitor

class EodBot:
	def __init__(self):
		print("Initialising Eod Bot!")			
		
	def start(self):				
		eodBotParser = parser.SentenceWordParser([[{}]])
		
		dictionaryMonitor = DictionaryMonitor.DictionaryMonitor(eodBotParser)
		dictionaryMonitor.start()
		
		hipChatMonitor = HipChatMonitor.HipChatMonitor(eodBotParser)
		hipChatMonitor.start()
		
eodBot = EodBot()
eodBot.start()