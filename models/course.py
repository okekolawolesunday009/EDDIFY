# such as course ID, title, description, instructor ID (foreign key referencing Users table), etc.
#!/usr/bin/python
""" holds class Place"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship




class Course(BaseModel, Base):
    """Representation of Place """
    if models.storage_t == 'db':
        __tablename__ = 'courses'
        category_id = Column(String(60), ForeignKey('categories.id'), nullable=False)
        title = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_lesson = Column(Integer, nullable=False, default=0)
        hours_lesson = Column(Integer, nullable=False, default=0)
        number_quiz = Column(Integer, nullable=False, default=0)
        lessons = relationship("Lesson", backref="course", viewonly=False)
        enrollments = relationship("Enrollment", back_populates="course", cascade="all, delete, delete-orphan")

        

    else:
        lesson_id = ""
        user_id = ""
        title = ""
        description = ""
        number_lesson = 0
        hours_lesson = 0
        number_quiz = 0


    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)


