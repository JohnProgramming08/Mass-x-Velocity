from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length


class SignUpForm(FlaskForm):
    email = EmailField(
        "Email", render_kw={"placeholder": "Email"}, validators=[DataRequired()]
    )
    password = PasswordField(
        "Password",
        render_kw={"placeholder": "Password"},
        validators=[DataRequired(), Length(min=5, max=25)],
    )
    confirm_password = PasswordField(
        "Confirm Password",
        render_kw={"placeholder": "Confirm Password"},
        validators=[DataRequired(), Length(min=5, max=25)],
    )
    sign_up = SubmitField("Sign up")
