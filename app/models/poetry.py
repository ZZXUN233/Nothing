from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey

from app.models.base import Base

from sqlalchemy.orm import relationship


class Poetry(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    author = relationship('Author')
    aid = Column(Integer, ForeignKey('author.id'))
    information = Column(String(200), nullable=True)
