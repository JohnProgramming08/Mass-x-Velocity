from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileAllowed


class ProfileSettingsForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(), Length(min=4, max=10)],
        render_kw={"id": "username"},
    )
    bio = TextAreaField(
        "Bio", validators=[DataRequired(), Length(max=200)], render_kw={"id": "bio"}
    )

    profile_picture = FileField("Profile Picture", validators=[FileAllowed(["jpg", "jpeg", "png", "gif", "webp"], "Images only!")])

    submit = SubmitField("Submit")