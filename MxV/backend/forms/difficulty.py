from flask_wtf import FlaskForm
from wtforms import BooleanField

class DifficultyForm(FlaskForm):
	class Meta:
		csrf = False
	practice1 = BooleanField("Practice 1")
	practice2 = BooleanField("Practice 2")
	practice3 = BooleanField("Practice 3")
	exam1 = BooleanField("Exam Question 1")
	exam2 = BooleanField("Exam Question 2")