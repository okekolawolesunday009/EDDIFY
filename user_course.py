#!/usr/bin/python3
from models.base_model import BaseModel
from models.course import Course
from models.user import User
from models.category import Category
from models.enrollment import Enrollment
from models.lesson import Lesson
from models import storage

#crate a category
category_one = Category(category_name="HTML")
category_one.save()
#---------------------------
#creates a course and links it to  a category
course_one = Course(category_id=category_one.id, title="HTML TAGS", description="Learn about HTML Tags", number_lesson=2, hours_lesson=5)
course_one.save()
course_two =  Course(category_id=category_one.id, title="Advance TAGS", description="Advance", number_lesson=4, hours_lesson=2)
course_two.save()

#---------------------------
#creates a lesson ad n link it to a course which is attached to a category
lesson_one = Lesson(lesson_title="HTML5 TAGS", description="Html is a mark up language", content="ZhULGD5hNQs", course_id=course_one.id)
lesson_one.save()
#---------------------------
#creates a useg
user_one = User( first_name="victor", last_name="Osimehn", email="admin@gmail.com", password="12345678",phone_no="070000000", image_file="01")
user_one.save()
#---------------------------
#this is to be able to keep track of coures
#date and expiration
#it also links a user to the course
enrollment_user_one = Enrollment(course_id=course_one.id, user_id=user_one.id)
enrollment_user_one.save()
#---------------------------
#link courses to user
user_one.enrolled_courses.append(course_one)
user_one.enrolled_courses.append(course_two)

storage.save()

