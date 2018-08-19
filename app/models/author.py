from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base


class Author(Base):
    id = Column(Integer, primary_key=True)
    information = Column(String(100), nullable=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'), nullable=True)
    alive = Column(Boolean, default=False)
    photo = Column(String(20), nullable=True)

