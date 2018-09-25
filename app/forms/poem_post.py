from flask_pagedown.fields import PageDownField
from wtforms import Form, StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError, Required


class PoemForm(Form):
    title = StringField("添加标题", validators=[
        DataRequired()
    ])
    poetry = SelectField('选择所属文集', coerce=int)
    content = PageDownField("编辑内容",
                            validators=[DataRequired()])
    submit = SubmitField('提交')

    def __init__(self, choices, formdata=None, obj=None, prefix='', data=None, meta=None, **kwargs):
        Form.__init__(self, formdata, obj, prefix, **kwargs)
        self.poetry.choices = choices


class PoetryForm(Form):
    name = StringField(validators=[
        DataRequired(), Length(1, 64)
    ])
    info = StringField()
