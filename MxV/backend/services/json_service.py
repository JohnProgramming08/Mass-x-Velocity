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
	


