from .queue_service import Queue
from database import Update

class Study:
	def __init__(self, questions, user_id):
		self.queue = Queue(questions)
		self.user_id = user_id
		self.current_question = []
	
	# Return the next question and push it to the back of the queue
	def get_next_question(self):
		question = Queue.pop()
		self.queue.enqueue(question)
		self.current_question = question
		return question
	
	# Return the users increase in momentum
	def calculate_momentum(self, question):
		level_momentum = {
			"GCSE": 5
		}
		difficulty_momentum = {
			"practice1": 1,
			"practice2": 1.2,
			"practice3": 1.5,
			"exam1": 1.5,
			"exam2": 2
		}

		initial = level_momentum[question.level]
		multiplier = difficulty_momentum[question.difficulty]
		return int(initial * multiplier)

	# Submit an answer
	def submit_answer(self, user_units, user_answer):
		answer = self.current_question.answer
		units = self.current_question.answer_units

		# User got correct answer
		if user_answer == answer and user_units == units:
			momentum = self.calculate_momentum(self.current_question)
			Update.update_correct_answer(self.user_id, momentum, self.current_question.difficulty)
			return True
		
		# User got incorrect answer
		Update.update_incorrect_answer(self.user_id)
		return False


