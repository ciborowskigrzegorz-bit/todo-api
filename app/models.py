from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base
from pydantic import BaseModel, ConfigDict


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    role = Column(String, default='user')
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    todos = relationship('Todo', back_populates='owner', cascade='all, delete-orphan')


class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text, nullable=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='todos')
    done = Column(Boolean, default=False)
    status = Column(String, default='todo')  # todo, in-progress, done
    priority = Column(Integer, default=0)
    due_date = Column(String, nullable=True)
    tags = Column(String, nullable=True)  # comma-separated simple tags
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class YourModel(BaseModel):
    # your fields here
    
    model_config = ConfigDict(from_attributes=True)