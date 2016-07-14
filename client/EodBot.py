import HipChatMonitor

class EodBot:
	def __init__(self):
		print("Initializing Eod Bot!")			
		
	def start(self):		
		hipChatMonitor = HipChatMonitor.HipChatMonitor()
		hipChatMonitor.start()
		
eodBot = EodBot()
eodBot.start()