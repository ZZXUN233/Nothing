from flask_login import current_user
from wtforms import Form, StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo

from app.models.user import User


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮箱不合规范')])
    password = PasswordField(validators=[
        DataRequired(message='密码不能为空，请输入规范的密码！'), Length(6, 32)
    ])
    password_again = PasswordField(validators=[
        DataRequired(message='密码不能为空，请输入规范的密码！'), Length(6, 32),
        EqualTo('password', message="两次密码不一致！")
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
        DataRequired(), Length(8, 64), Email(message='电子邮件不复合规范')
    ])
    password = PasswordField(validators=[
        DataRequired(message='密码不能为空，请输入你的密码'), Length(6, 32)
    ])


class ChangePwdForm(Form):
    old_password = PasswordField(validators=[
        DataRequired(message='必须填入原密码！'), Length(6, 32)
    ])
    new_password1 = PasswordField(validators=[
        DataRequired(message='请输入新密码！'), Length(6, 32)
    ])
    new_password2 = PasswordField(validators=[
        DataRequired(message='请输入新密码！'), Length(6, 32),
        EqualTo('new_password1', message='两次输入的密码不一致！')
    ])

    # def validate_old_password(self, field):
    #     if not User.check_password(field):
    #         raise ValidationError("原密码输入错误！")


class EmailForm(Form):
    email = StringField(validators=[
        DataRequired(), Length(8, 64), Email(message='电子邮件不复合规范')
    ])


class InfoForm(Form):
    new_nickname = StringField('新昵称', validators=[
        DataRequired(), Length(2, 10, message='昵称至少需要两个字符，最多10个字符')
    ])

    phone_number = IntegerField('电话号码')

    new_email = StringField('新的邮箱', validators=[
        DataRequired(), Length(8, 64), Email(message='电子邮件不复合规范')
    ])
    # submit = SubmitField('提交修改')

    # def validate_new_nickname(self, field):
    #     if current_user.nickname == field.data or \
    #             User.query.filter_by(nickname=field.data).first():
    #         raise ValidationError('昵称未修改或是新昵称已被注册！')


class ResetPasswordForm(Form):
    new_password = PasswordField(validators=[
        DataRequired(message='请出入重置的密码'), Length(6, 20, message="密码长度为6到20个字符之间！"),
        EqualTo('new_password2', message='两次密码不一致')
    ])
    new_password2 = PasswordField(validators=[
        DataRequired(message='请出入重置的密码'), Length(6, 20, message="密码长度为6到20个字符之间！"),
    ])
