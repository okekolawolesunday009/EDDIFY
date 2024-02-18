#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Reviews """
from models.enrollment import Enrollment
from models.user import User
from models.course import Course
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from



@app_views.route('/user/<user_id>/enrollments', methods=['GET'],
                 strict_slashes=False)
def get_enrollment(user_id):
    """
    Retrieves the list of all Enrollments objects of a Course
    """
    user = storage.get(User, user_id)

    if not user:
        abort(404)

    enrollments = [enrollment.to_dict() for enrollment in user.enrollments]

    return jsonify(enrollments)


@app_views.route('/enrollments/<enrollment_id>', methods=['GET'], strict_slashes=False)
def get_review(enrollment_id):
    """
    Retrieves a enrollment object
    """
    enrollment = storage.get(Enrollment, enrollment_id)
    if not enrollment:
        abort(404)

    return jsonify(enrollment.to_dict())


@app_views.route('/enrollments/<enrollment_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_review(enrollment_id):
    """
    Deletes a Review Object
    """

    enrollment = storage.get(Enrollment, enrollment_id)

    if not enrollment:
        abort(404)

    storage.delete(enrollment)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/course/<user_id>/enrollments', methods=['POST'],
                 strict_slashes=False)
def post_enrollment(user_id):
    """
    Creates a Review
    """
    course = storage.get(Course, user_id)

    if not course:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'user_id' not in request.get_json():
        abort(400, description="Missing user_id")

    data = request.get_json()
    user = storage.get(User, data['user_id'])

    if not user:
        abort(404)

    if 'text' not in request.get_json():
        abort(400, description="Missing text")

    data['user_id'] = user_id
    instance = Enrollment(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/enrollments/<enrollment-id>', methods=['PUT'], strict_slashes=False)
def put_review(enrollment_id):
    """
    Updates a Enrollment
    """
    review = storage.get(Enrollment, enrollment_id)

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
    return make_response(jsonify(review.to_dict()), 200)


