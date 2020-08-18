from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(120), unique=True)
    password_hash = Column(String(255), nullable=False)
    events = relationship("Event")

    def __init__(self, name, email, password_hash):
        self.name = name
        self.email = email
        self.password_hash = password_hash

    def __repr__(self):
        return self.name


class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(150))
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    last_modified = Column(DateTime, default=datetime.now())
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))

    def __init__(self, title, start_date, end_date, user_id, description=None):
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.user_id = user_id

    def __repr__(self):
        return "Event: "+self.title
