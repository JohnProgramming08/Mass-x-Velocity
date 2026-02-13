from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, EmailField, PasswordField
from wtforms.validators import DataRequired, Length

class ResetForm(FlaskForm):
	email = EmailField(
        "Email", render_kw={"placeholder": "Email"}, validators=[DataRequired()]
    )
	new_password = PasswordField("New Password", render_kw={"placeholder": "New Password"}, validators=[DataRequired(), Length(min=5, max=25)])
	confirm_password = PasswordField("Confirm Password", render_kw={"placeholder": "Confirm Password"}, validators=[DataRequired(), Length(min=5, max=25)])

	submit_email = SubmitField("Submit")

