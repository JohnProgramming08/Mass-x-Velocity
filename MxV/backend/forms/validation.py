from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length

class ValidationForm(FlaskForm):
	code = StringField("Code", validators=[Length(min=6, max=6), DataRequired()])
	submit = SubmitField("Submit")