#!/usr/bin/python3
""" holds class Category"""
import models
from models.base_model import BaseModel, Base
from models.course import Course
from models.quiz import Quiz
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Category(BaseModel, Base):
    """Representation of category """
    if models.storage_t == "db":
        __tablename__ = 'categorys'
        category_name = Column(String(128), nullable=False)
        course = relationship("Course",
                               backref="category",
                               cascade="all, delete, delete-orphan")
    else:
        title = ""

    def __init__(self, *args, **kwargs):
        """initializes Lesson"""
        super().__init__(*args, **kwargs)

