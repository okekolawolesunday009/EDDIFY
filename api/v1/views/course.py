#!/usr/bin/python3
""" objects that handles all default RestFul API actions for Amenities"""
from models.course import Course 
from models.category import Category
from models.enrollment import Enrollment
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from



@app_views.route('/category', methods=['GET'], strict_slashes=False)
def get_catgory():
    """
    Retrieves all categories
    """
    list_category = []
    category = storage.all(Category).values()
    print(category)
    if not category:
        abort(404)
    for cat in category:
        list_category.append(cat.to_dict())
    return jsonify(list_category)


@app_views.route('/category/<category_id>/courses', methods=['GET'], strict_slashes=False)
def get_courses(category_id):
    """
    Retrieves a list of all cities
    """
    list_courses = []
    category = storage.get(Category, category_id)
    if not category:
        abort(404)
    for course in category.course:
        list_courses.append(course.to_dict())
    return jsonify(list_courses)


@app_views.route('/courses/<course_id>/', methods=['GET'],
                 strict_slashes=False)
def get_course(course_id):
    """ Retrieves an course """
    course = storage.get(Course, course_id)
    print(course)
    if not course:
        abort(404)
    return jsonify(course.to_dict())

@app_views.route('/courses', methods=['GET'],
                 strict_slashes=False)
def get_all_course():
    """ Retrieves all course """
    courses = storage.all(Course).values()
    if not courses:
        abort(404)

    courses_data = [course.to_dict() for course in courses]
    return jsonify(courses_data)
    #jsonify(course.to_dict())


@app_views.route('/profile/courses/<user_id>/enrolled-courses', methods=['GET'],
                 strict_slashes=False)
def get_user_course(user_id):
    """ Retrieves a user so we can get courses enrolled """
    user_course = storage.get(Enrollment, user_id)
    print(user_course)
    if not user_course:
        abort(404)
    return jsonify(user_course.to_dict())



@app_views.route('/courses/<course_id>/', methods=['DELETE'],
                 strict_slashes=False)
def delete_course(course_id):
    """
    Deletes a course based on id provided
    """
    course = storage.get(Course, course_id)

    if not course:
        abort(404)
    storage.delete(course)
    storage.save()

    return make_response(jsonify({}), 200)

@app_views.route('/category/<category_id>/courses', methods=['POST'], strict_slashes=False)
def post_course(category_id):
    """
    Creates a Course
    """
    category= storage.get(Category, category_id)
    if not category:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'title' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = Course(**data)
    instance.category_id = category.id
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/courses/<course_id>/', methods=['PUT'],
                 strict_slashes=False)
def put_course(course_id):
    """
    Updates a Course
    """
    course = storage.get(Course, course_id)
    if not course:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'state_id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(course, key, value)
    storage.save()
    return make_response(jsonify(course.to_dict()), 200)
