from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, SmallInteger

db = SQLAlchemy()


# 其它的数据库对应类继承于Base
# 用于记录软删除，方便用户找回记录

class Base(db.Model):
    # _abstract_ = True
    __abstract__ = True  # 让base位基类
    status = Column(SmallInteger, default=1)

    # 共同的赋值方法
    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':  # 如果字典中有该属性
                setattr(self, key, value)  # 动态赋值
