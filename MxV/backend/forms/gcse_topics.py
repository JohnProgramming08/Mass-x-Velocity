from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField
from services import Json

class GCSETopicsForm(FlaskForm):
	submit = SubmitField("Practice")
	
	# Create a checkbox for each subtopic
	def __init__(self, *args, **kwargs):
		super(GCSETopicsForm, self).__init__(*args, **kwargs)
		gcse_topics = Json.get_gcse_topics()
        
		for topic, subtopics in gcse_topics.items():
			setattr(self, topic, BooleanField(topic, render_kw={"class": "topic", "id": topic}))
			for subtopic in subtopics:
				checkbox_class = f"subtopic {topic}"
				setattr(self, subtopic, BooleanField(subtopic, render_kw={"class": checkbox_class}))