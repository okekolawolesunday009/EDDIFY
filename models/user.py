#!/usr/bin/python3
"""class user model"""
from models.base_model import BaseModel, Base
import models
from os import getenv
from sqlalchemy import Table, ForeignKey
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
from hashlib import md5
"""This imported function are to be used for user authentication"""
# from web_dynamic import login_manager, app
from flask_login import UserMixin

if models.storage_t == 'db':
    """many to many  relationship it connect user to course and course to user"""
    user_course_association = Table('user_course_association',
                            Base.metadata, Column('UserID', String(60), ForeignKey('users.id')),
                  		    Column('CourseID', String(60), ForeignKey('courses.id')))
    
# if models.storage_t == 'db':
#     @login_manager.user_loader
#     def load_user(user_id):
# 	    return models.storage.get(User, user_id)

class User(BaseModel, UserMixin, Base):
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False, unique=True)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        username= Column(String(128), nullable=True, unique=True)
        image_file = Column(String(50), nullable=False, default='default.jpg')
        country = Column(String(50), nullable=False)
        confirmed = Column(Boolean, default=False)
        review = relationship("Review", backref="user", viewonly=False)
        enrollments = relationship('Enrollment', back_populates='user')
        enrolled_courses = relationship('Course', secondary=user_course_association, viewonly=False)
        # enrolled_courses = relationship('Course', secondary=user_course_association, back_populates='enrolled_user', viewonly=False)
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

    def __init__(self, *args, **kwargs):
        """initializes User"""
        super().__init__(*args, **kwargs)

    if models.storage_t != 'db':
        @property
        def reviews(self):
            """getter attribute returns the list of Review instances"""
            from models.review import Review
            review_list = []
            all_reviews = models.storage.all(Review)
            for review in all_reviews.values():
                if review.user_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def users(self):
            """getter attribute returns the list of user instances"""
            from models.course import Course
            course_list = []
            all_courses =  models.storage.all(Course)
            for course in all_courses.values():
                if course.user_id == self.id:
                    course_list.append(course)
            return course_list 