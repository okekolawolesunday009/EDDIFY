#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Reviews """
from models.enrollment import Enrollment
from models.user import User
from models.course import Course
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/user/<user_id>/enrollments', methods=['GET'], strict_slashes=False)
def get_user_enrollment(user_id):
    """
    Retrieves the list of all Enrollments objects of a Course
    """
    user = storage.get(User, user_id)

    if not user:
        abort(404)

    enrollments = [enrollment.to_dict() for enrollment in user.enrollments]
    enrollments_with_courses = []

    for enrollment in enrollments:
        course_id = enrollment["course_id"]
        course = storage.get(Course, course_id)
        if course:
            enrollment["course"] = course.to_dict()
        enrollments_with_courses.append(enrollment)

    return jsonify(enrollments_with_courses)


@app_views.route('/enrollments/<enrollment_id>', methods=['GET'], strict_slashes=False)
def get_enrollment(enrollment_id):
    """
    Retrieves a enrollment object
    """
    enrollment = storage.get(Enrollment, enrollment_id)
    if not enrollment:
        abort(404)

    return jsonify(enrollment.to_dict())


@app_views.route('/enrollments/<enrollment_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_enrollment(enrollment_id):
    """
    Deletes a Review Object
    """

    enrollment = storage.get(Enrollment, enrollment_id)

    if not enrollment:
        abort(404)

    storage.delete(enrollment)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/course/<course_id>/enrollments', methods=['POST'],
                 strict_slashes=False)
def post_enrollment(course_id):
    """
    Creates a enrollemt
    """
    course = storage.get(Course, course_id)

    if not course:
        abort(404)
    print(request.get_json)

    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'user_id' not in request.get_json():
        abort(400, description="Missing user_id")

    data = request.get_json()
    user = storage.get(User, data['user_id'])
    print(user)

    if not user:
        abort(404)


    instance = Enrollment(course_id=course.id, user_id=user.id)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/enrollment/<enrollment_id>', methods=['PUT'], strict_slashes=False)
def put_enrollment(enrollment_id):
    """
    Updates a Enrollment
    """
    en = storage.get(Review, review_id)

    if not review:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'user_id', 'user_id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(review, key, value)
    storage.save()
    return make_response(jsonify(en.to_dict()), 200)
