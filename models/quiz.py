#!/usr/bin/python
""" holds class Quiz"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey

Base.metadata.clear()

class Quiz(BaseModel, Base):
    """Representation of Quiz """
    if models.storage_t == 'db':
        __tablename__ = 'quiz'
        quiz_title = Column(String(128), nullable=False)
        content = Column(String(250), nullable=False)
        lesson_id = Column(String(60), ForeignKey('lessons.id'), nullable=False)
       
    else:
        title = ""
        description = ""

    def __init__(self, *args, **kwargs):
        """initializes Course"""
        super().__init__(*args, **kwargs)
