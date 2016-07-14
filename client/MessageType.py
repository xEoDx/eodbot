from enum import Enum
class MessageType(Enum):
	order = 0,
	text = 1,
	question = 2,
	exclamation = 3