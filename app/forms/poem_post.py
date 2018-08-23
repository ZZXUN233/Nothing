from flask_pagedown.fields import PageDownField
from wtforms import Form, StringField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError, Required
from app.models.poem import Poem


class PoemForm(Form):
    title = StringField("what's your title?", validators=[
        DataRequired(), Length(1, 64)
    ])
    content = PageDownField("What's your poem content?",
                            validators=[DataRequired()])

