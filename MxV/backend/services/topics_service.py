from database import Select
from wtforms import BooleanField

class Topics:
	def __init__(self, topics_form, difficulty_form):
		self.topics_list = self.get_checked(topics_form)
		self.topics_count = len(self.topics_list)
		self.difficulties = self.get_checked(difficulty_form)
		self.difficulty_count = len(self.difficulties)


	# Check if the topics list is valid
	def check_valid(self):
		return {
			"result": self.topics_count > 0 and self.difficulty_count > 0,
			"error": "You must select at least one topic and difficulty."
		}
	
	# Get all of the questions with the selected topics
	def get_questions(self):
		questions = Select.get_topic_questions(self.topics_list, self.difficulties)

		return questions
	
	# Return the name of all checked checkboxes
	def get_checked(self, form):
		checked = []
		for field in form:
			if isinstance(field, BooleanField) and field.data:
				checked.append(field.name)

		return checked