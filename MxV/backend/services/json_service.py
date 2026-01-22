import json

class Json:
	# Return a dictionary of all gcse topics
	@staticmethod
	def get_gcse_topics():
		with open("config/topics.json", "r") as file:
			topics = {}
			data = json.load(file)["GCSE"]

			# Iterate through the subtopics of each topic
			for topic in data:
				topics[topic] = []
				for subtopic in data[topic]:
					topics[topic].append(subtopic)

		return topics
	
	# Return an array all questions
	@staticmethod
	def get_questions():
		with open("config/questions.json", "r") as file:
			questions = []
			data = json.load(file)
			
			# Iterate through each question
			for level in data:
				for topic in data[level]:
					for question in data[level][topic]:
						temp = question
						temp["topic"] = topic
						temp["level"] = level
						temp["topic"] = topic
						questions.append(temp)

		return questions
	


