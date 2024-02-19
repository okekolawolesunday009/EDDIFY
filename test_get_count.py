#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.course import Course

print("All objects: {}".format(storage.count()))
print("Course objects: {}".format(storage.count(Course)))

first_state_id = list(storage.all(Course).values())[0].id
print("First state: {}".format(storage.get(Course, first_state_id)))