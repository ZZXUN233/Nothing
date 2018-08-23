from flask import flash
from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin
from app import login_manger

from app.models.base import Base


# 保存密码为密文
class User(Base, UserMixin):
    # __tablename = 'user1'  # 自定义表名
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    _password = Column('password', String(128), nullable=False)  # 自定义表字段
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    scores = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    review_counter = Column(Integer, default=0)
    can_review = Column(Boolean, default=False)

    @property  # 方法变属性
    def password(self):
        return self._password

    @password.setter  # 属性的写入，使_password设置为只读的
    def password(self, raw):
        self._password = generate_password_hash(raw)

    # 检查密码
    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    def change_pwd(self, old_pwd, new_pwd):
        if self.check_password(old_pwd):
            self._password = generate_password_hash(new_pwd)
        elif self.check_password(new_pwd):
            flash('密码与原密码相同！', category='warnings')
        else:
            flash('原密码有误！', category='warnings')

    def change_info(self, info_dict):
        self.nickname = info_dict['nickname']
        self.phone_number = info_dict['phone_number']
        self.email = info_dict['new_email']

    def show_info(self):
        info = {
            '昵称': self.nickname,
            '邮箱': self.email,
            '电话': self.phone_number,
            '发布文章数': self.send_counter,
            '发布评论数': self.review_counter,
            '审核权限': self.can_review,
            '积分': self.scores,
        }
        return info




# # 服务于login_in
# def get_id(self):
#     return self.id


# 属于独立模块，用于current_user获取当前用户
@login_manger.user_loader
def get_user(uid):
    return User.query.get(int(uid))
