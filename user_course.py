#!/usr/bin/python3
from models.base_model import BaseModel
from models.course import Course
from models.user import User
from models.category import Category
from models.enrollment import Enrollment
from models.lesson import Lesson


category_one = Category(category_name="HTML")
category_one.save()
#---------------------------
course_one = Course(category_id=category_one.id, title="HTML TAGS", description="Learn about HTML Tags", number_lesson=2, hours_lesson=5)
course_one.save()
#---------------------------
lesson_one = Lesson(lesson_title="HTML5 TAGS", content="https://www.youtube.com/watch?v=ZhULGD5hNQs", course_id=course_one.id)
lesson_one.save()
#---------------------------
user_one = User(email="admin@gmail.com", password="12345678", first_name="victor Osimehn", last_name="Omologo", username="admin", image_file="01", country="NG")
user_one.save()
#---------------------------
enrollment_user_one = Enrollment(course_id=course_one.id, user_id=user_one.id)
enrollment_user_one.save()
#---------------------------

