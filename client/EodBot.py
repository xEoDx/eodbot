from hipchat import HipChatMonitor

class EodBot:
	def __init__(self):
		print("Initialising Eod Bot!")			
		
	def start(self):		
		
		hipChatMonitor = HipChatMonitor.HipChatMonitor()
		hipChatMonitor.start()
		
eodBot = EodBot()
eodBot.start()