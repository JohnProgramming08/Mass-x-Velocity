from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length

class StudyForm(FlaskForm):
	units = SelectField("Units", choices= [
		("m/s", "m/s"),
		("kg", "kg"),
		("N", "N"),
		("J", "J"),
	])
	answer = StringField("Answer", render_kw={"placeholder": "Answer"})
	submit = SubmitField("Submit")