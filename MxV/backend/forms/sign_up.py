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
    log_in = SubmitField("Log in")
    