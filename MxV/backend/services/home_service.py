from database import Select

class Home:
	def __init__(self, user_id):
		self.id = user_id

	# Return a dictionary of the users question data
	def question_data(self):
		answers = Select.get_answer_data()
		accuracy = int(((answers.total - answers.wrong) / answers.total) * 100)

		return {
			"total": answers.total,
			"accuracy": accuracy
		}

	# Return a dictionary of the users momentum data
	def momentum_data(self):
		data = Select.get_all_momentum(self.id)

		for key in data:
			if key == "total": # Don't want to convert total to a percentage
				continue

			data[key] = self.to_percent(data[key], data["total"])

		return data
	
	# Convert a given value to a percentage of the whole
	def to_percent(self, data, total):
		return 100 * (data / total)
	
	# Return the users general data
	def user_data(self):
		return Select.get_user_data(self.id)