from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from app.models.base import Base, db
from sqlalchemy.orm import relationship


class Poetry(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    # author = relationship('Author')
    # aid = Column(Integer, ForeignKey('author.id'))
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    information = Column(String(200), nullable=True)

    # 为每个新用户默认创建一个为空的诗集
    @staticmethod
    def default_poetry(user):
        d_poetry = Poetry()
        d_poetry.set_attrs({
            'name': '默认的诗集',
            'user': user,
            'information': '每个用户都有一个默认的诗集，就像每个人都有一个生活一样。'
        })
        with db.auto_commit():
            print('已经创建一个默认的诗集')
            db.session.add(d_poetry)

    @staticmethod
    def get_poetry_by_user(user):
        poetrys = Poetry.query.filter_by(user=user).all()
        choices = [(poetry.id, poetry.name) for poetry in poetrys]
        print(choices)
        return choices
