from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, Form
from services import Json


class GCSETopicsForm(FlaskForm):
    submit = SubmitField("Practice")


gcse_topics = Json.get_gcse_topics()
for topic, subtopics in gcse_topics.items():
    field = BooleanField(topic, render_kw={"class": "topic", "id": topic})
    setattr(GCSETopicsForm, topic, field)

    for subtopic in subtopics:
        checkbox_class = f"subtopic {topic}"
        field = BooleanField(subtopic, render_kw={"class": checkbox_class})
        setattr(GCSETopicsForm, subtopic, field)
