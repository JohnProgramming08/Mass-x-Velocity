# Queue class allowing data to be enqueued, dequeued and peeked

class Queue:
	def __init__(self, questions):
		self.data = questions

	def enqueue(self, element):
		self.data.append(element)

	def dequeue(self):
		return self.data.pop(0)
	
	def peek(self):
		return self.data[0]
	