from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError

from app.models.user import User


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮箱不合规范')])
    password = PasswordField(validators=[
        DataRequired(message='密码不能为空，请输入规范的密码！'), Length(6, 32)
    ])
    nickname = StringField(validators=[
        DataRequired(), Length(2, 10, message='昵称至少需要两个字符，最多10个字符')
    ])

    # 自定义数据校验
    def validate_email(self, field):
        # db.session
        if User.query.filter_by(email=field.data).first():  # 是否查询到同名的Email
            raise ValidationError('电子邮件已被注册！')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已被注册！')


class LoginForm(Form):
    email = StringField(validators=[
        DataRequired(), Length(8, 64),Email(message='电子邮件不复合规范')
    ])
    password = PasswordField(validators=[
        DataRequired(message='密码不能为空，请输入你的密码'), Length(6, 32)
    ])
