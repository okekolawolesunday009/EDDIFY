#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.course import Course

fs = FileStorage()

# All States
all_course = fs.all(Course)
print("All Course: {}".format(len(all_course.keys())))
for course_key in all_course.keys():
    print(all_course[course_key])

# Create a new State
new_course = Course()
new_course.name = "California"
fs.new(new_course)
fs.save()
print("New State: {}".format(new_course))

# All States
all_course = fs.all(Course)
print("All States: {}".format(len(all_course.keys())))
for state_key in all_course.keys():
    print(all_course[state_key])

# Create another State
another_course = Course()
another_course.name = "Nevada"
fs.new(another_course)
fs.save()
print("Another State: {}".format(another_course))

# All States
all_states = fs.all(Course)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])        

# Delete the new State
fs.delete(new_course)

# All States
all_states = fs.all(Course)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])
