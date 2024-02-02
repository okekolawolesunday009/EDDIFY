#!/usr/bin/python
""" holds class Quiz"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Quiz(BaseModel, Base):
    """Representation of Quiz """
    if models.storage_t == 'db':
        __tablename__ = 'quizs'
        quiz_title = Column(String(128), nullable=False)
        content = Column(String(250), nullable=False)
        lesson_id = Column(String(60), ForeignKey('lessons.id'), nullable=False)

        __table_args__ = {'extend_existing': True}
       
    else:
        title = ""
        description = ""

    def __init__(self, *args, **kwargs):
        """initializes Course"""
        super().__init__(*args, **kwargs)
