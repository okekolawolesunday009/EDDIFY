#!/usr/bin/python
""" holds class Review"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Quiz(BaseModel, Base):
    """Representation of Quiz """
    if models.storage_t == 'db':
        __tablename__ = 'quizs'
        title = Column(String(60), ForeignKey('places.id'), nullable=False)
        description= Column(String(60), ForeignKey('users.id'), nullable=False)
        Course_id = Column(String(60), ForeignKey('users.id'), nullable=False)
       
    else:
        title = ""
        description = ""

    def __init__(self, *args, **kwargs):
        """initializes Quiz"""
        super().__init__(*args, **kwargs)
