from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField
from wtforms.validators import DataRequired, Length


class DiaryForm(FlaskForm):
    date = DateField("Date", format="%Y-%m-%d")
    title = StringField(
        label="Record title",
        name="record-title",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
    )
    text = TextAreaField(validators=[DataRequired()])
