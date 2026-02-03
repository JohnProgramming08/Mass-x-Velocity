from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class ProfileSettingsForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(), Length(min=4, max=10)],
        render_kw={"id": "username"},
    )
    bio = TextAreaField(
        "Bio", validators=[DataRequired(), Length(max=200)], render_kw={"id": "bio"}
    )
    submit = SubmitField("Submit")

# USE JS AND FIELD ID TO POPULATE WITH CURRENT USERNAME AND BIO