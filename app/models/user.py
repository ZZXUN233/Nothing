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

    # # 服务于login_in
    # def get_id(self):
    #     return self.id


# 属于独立模块
@login_manger.user_loader
def get_user(uid):
    return User.query.get(int(uid))
