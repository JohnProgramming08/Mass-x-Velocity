from .queue_service import Queue
from database import Update, Select

class Study:
	def __init__(self, question_ids, user_id):
		self.queue = Queue(question_ids)
		self.user_id = user_id
	
	# Return the next question and push it to the back of the queue
	def get_next_question(self):
		question_id = self.queue.peek()
		self.queue.enqueue(question_id)
		return Select.get_questions([question_id])[0]
		
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
		question_id = self.queue.dequeue()
		self.queue.enqueue(question_id)
		question = Select.get_questions([question_id])[0]
		answer = question.answer
		units = question.answer_units

		# User got correct answer
		if int(user_answer) == answer and user_units == units:
			momentum = self.calculate_momentum(question)
			Update.update_correct_answer(self.user_id, momentum, question.difficulty)
			return momentum
		
		# User got incorrect answer
		Update.update_incorrect_answer(self.user_id)
		return 0
	
	def get_current_question(self):
		question_id = self.queue.data[-1]
		question = Select.get_questions([question_id])[0]
		return question


