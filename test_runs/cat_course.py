#!/usr/bin/python3
from models import *
from models.category import Category
from models.course import Course 
from models.user import User
from models.enrollment import Enrollment
from models import storage

user_1 = User(first_name="james")
user_1.save()
cat_1 = Category(title="programming") 
cat_1.save()
cat_course = Course(title="js", category_id=cat_1.id, user_id=user_1.id) 
cat_course.save()
cat_course_2 = Course(title="html", category_id=cat_1.id) 
cat_course_2.save()

enrol_1 = Enrollment(course_id=cat_course.id, user_id=user_1.id)
enrol_1.save() 

print(cat_course)

#----------------------------#
#enrolled course
print(enrol_1)

#-------------------------------#
user_2 = User(first_name="timishot")
user_2.save()

cat_2 = Category(title="Devops") 
cat_2.save()
cat_course_3 = Course(title="ssh_key", category_id=cat_2.id) 
cat_course_3.save()
cat_course_4 = Course(title="datadog", category_id=cat_2.id) 
cat_course_4.save()
print(cat_course_3)
#-------------------------------#

enrol_2 = Enrollment(course_id=cat_course_3.id, user_id=user_2.id) 
enrol_2.save()

print(enrol_2)


first_course_id = list(storage.all(Course).values())[0].id
print("First course: {}".format(storage.get(Course, first_course_id)))