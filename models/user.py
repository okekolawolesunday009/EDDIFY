#!/usr/bin/python3
"""class user model"""
from base_model import BaseModel
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Table, ForeignKey
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
from hashlib import md5

if models.storage_t == 'db':
    """many to many  relationship it connect user to course and course to user"""
    user_course_association = Table('user_course_association',
                            Base.metadata, Column('UserID', Integer, ForeignKey('users.id')),
                  		    Column('CourseID', Integer, ForeignKey('courses.id')))

class User(BaseModel, Base):
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        username= Column(String(128), nullable=True)
        image_file = Column(String(50), nullable=False)
        country = Column(String(50), nullable=False)
        confirmed = Column(Boolean, default=False)
        review = relationship("Review", backref="user", viewonly=False)
        enrolled_courses = relationship('Course', secondary=user_course_association, back_populates='enrolled_user', viewonly=False)
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        username = ""
        image_file = ""
        password = ""
        phone_number = ""
        country = ""
        confirmed = ""
