from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class StudyForm(FlaskForm):
    units = SelectField(
        "Units",
        choices=[
            ("m/s", "m/s"),
            ("kg", "kg"),
            ("N", "N"),
            ("J", "J"),
            ("m", "m")
        ],
    )
    answer = StringField(
        "Answer", render_kw={"placeholder": "Answer"}, validators=[DataRequired()]
    )
    submit = SubmitField("Submit")
