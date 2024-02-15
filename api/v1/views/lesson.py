#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Reviews """
from models.lesson import Lesson
from models.course import Course
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/course/<course_id/lesson', methods=['GET'],
                 strict_slashes=False)
def get_lessons(course_id):
    """
    Retrieves the list of all lesson objects of a Course
    """
    course = storage.get(Course, course_id)

    if not course:
        abort(404)

    lessons = [lesson.to_dict() for lesson in course.lessons]

    return jsonify(lessons)


@app_views.route('/lesson/<lesson_id>', methods=['GET'], strict_slashes=False)
def get_review(lesson_id):
    """
    Retrieves a Lesson object
    """
    lesson = storage.get(Lesson, lesson_id)
    if not lesson:
        abort(404)

    return jsonify(lesson.to_dict())


@app_views.route('/lesson/<lesson_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_review(lesson_id):
    """
    Deletes a lesson Object
    """

    lesson = storage.get(Lesson, lesson_id)

    if not lesson:
        abort(404)

    storage.delete(lesson)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/course/<course_id>/lesson', methods=['POST'],
                 strict_slashes=False)
def post_review(course_id):
    """
    Creates a Lesson
    """
    course = storage.get(Course, course_id)

    if not course:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")


    data = request.get_json()
    course = storage.get(Course, data['course_id'])

    if not course:
        abort(404)

    if 'content' not in request.get_json():
        abort(400, description="Missing content")

    if 'lesson_title' not in request.get_json():
        abort(400, description="Missing lesson_title")

    data['course_id'] = course_id
    instance = Lesson(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/lesson/<lesson_id>', methods=['PUT'], strict_slashes=False)
def put_lesson(lesson_id):
    """
    Updates a Lesson
    """
    review = storage.get(Lesson, lesson_id)

    if not review:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'course_id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(review, key, value)
    storage.save()
    return make_response(jsonify(review.to_dict()), 200)