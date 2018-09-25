"""
    Created by ZZXUN on 2018/8/6
"""
import datetime

from flask import flash
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime

import bleach
from markdown import markdown
from sqlalchemy.orm import relationship

from app.models.base import Base, db

__author__ = "ZZXUN"


class Poem(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='佚名')
    publish_time = Column(DateTime())
    # author = relationship('Author')
    # aid = Column(Integer, ForeignKey('author.id'), nullable=True)
    poetry = relationship('Poetry')
    pid = Column(Integer, ForeignKey('poetry.id'), nullable=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)

    timestamp = Column(DateTime, index=True, default=datetime.datetime.now())
    content = Column(Text, nullable=False)
    body_html = Column(Text)
    image = Column(String(50))

    def sample(self):
        pass

    # 每次发布诗歌就更新诗歌用户对应的投稿数
    def update_send_counter(self):
        # print(Poem.query.filter_by(uid=self.uid))
        self.user.send_counter = len(Poem.query.filter_by(uid=self.uid).all())
        db.session.add(self.user)
        db.session.commit()

    def show_detail(self):
        poem_info = {
            'title': self.title,
            'content': self.content,
            'body_html': self.body_html,
            'timestamp': self.timestamp
        }
        return poem_info

    def fake_del(self):
        if self.status == 1:
            self.status = 0
            db.session.add(self)
            db.session.commit()
        else:
            db.session.delete(self)
            db.session.commit()

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        allowed_tags = [
            'a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
            'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul', 'h1',
            'h2', 'h3', 'p'
        ]
        target.body_html = bleach.linkify(bleach.clean(
            markdown(value, output_format='html'),
            tags=allowed_tags, strip=True
        ))


db.event.listen(Poem.content, 'set', Poem.on_changed_body)
