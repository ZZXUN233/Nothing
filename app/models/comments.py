from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base


class Comment(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    poem = relationship('Poem')
    pid = Column(Integer, ForeignKey('poem.id'), nullable=True)
    poetry = relationship('Poetry')
    poid = Column(Integer, ForeignKey('poetry.id'), nullable=True)
    author = relationship('Author')
    aid = Column(Integer, ForeignKey('author.id'), nullable=True)
    content = Column(String(500), nullable=False)
