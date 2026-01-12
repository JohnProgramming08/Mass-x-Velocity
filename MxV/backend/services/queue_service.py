# Queue class allowing data to be enqueued and dequeued

class Queue:
	def __init__(self):
		self.data = []

	def enqueue(self, element):
		self.data.append(element)

	def dequeue(self):
		return self.data.pop(0)
		
	