from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, EmailField
from wtforms.validators import DataRequired, Length

class ResetForm(FlaskForm):
	email = EmailField(
        "Email", render_kw={"placeholder": "Email"}, validators=[DataRequired()]
    )
	submit_email = SubmitField("Submit")

