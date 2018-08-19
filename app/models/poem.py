"""
    Created by ZZXUN on 2018/8/6
"""
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base

__author__ = "ZZXUN"


class Poem(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    # author = Column(String(30), default='佚名')
    # publish_time = Column(DateTime())
    author = relationship('Author')
    aid = Column(Integer, ForeignKey(author.id), nullable=True)
    poetry = relationship('Poetry')
    pid = Column(Integer, ForeignKey('poetry.id'), nullable=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)

    content = Column(String(500))
    image = Column(String(50))

    def sample(self):
        pass
