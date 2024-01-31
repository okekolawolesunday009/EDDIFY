#!/usr/bin/python
""" holds class Enrollmeny"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Enrollment(BaseModel, Base):
    """Representation of Enrollment """
    if models.storage_t == 'db':
        __tablename__ = 'quizs'
        course_id = Column(String(60), ForeignKey('courses.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        Course_id = Column(String(60), ForeignKey('course.id'), nullable=False)
        course = relationship('Course', back_populates='enrollments')
        user = relationship('User', back_populates='enrollments')

    else:
        title = ""
        description = ""

    def __init__(self, *args, **kwargs):
        """initializes Quiz"""
        super().__init__(*args, **kwargs)