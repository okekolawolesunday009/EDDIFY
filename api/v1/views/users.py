#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
import jwt
from flask import Flask
from functools import wraps
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = "8745E34566SDFF"


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'Alert': 'Token missing'}), 401
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            user_id = payload['user']
            print("this is the payload: ", user_id)
            current_user = storage.get(User, user_id)

            # Perform any additional checks on the payload if needed
        except jwt.ExpiredSignatureError:
            return jsonify({'Alert': 'Token expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'Alert': 'Invalid token'}), 401
        return func(current_user, *args, **kwargs)
    return decorated


@app_views.route('/users', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/all_users.yml')
def get_users():
    """
    Retrieves the list of all user objects
    or a specific user
    """
    all_users = storage.all(User).values()
    list_users = []
    for user in all_users:
        list_users.append(user.to_dict())
    return jsonify(list_users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/get_user.yml', methods=['GET'])
def get_user(user_id):
    """ Retrieves an user """
    user = storage.get(User, user_id)
    if not user:
        abort(404)

    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/user/delete_user.yml', methods=['DELETE'])
def delete_user(user_id):
    """
    Deletes a user Object
    """

    user = storage.get(User, user_id)

    if not user:
        abort(404)

    storage.delete(user)
    storage.save()

    return make_response(jsonify({}), 200)

@app_views.route('/signup', methods=['POST'], strict_slashes=False)
@swag_from('documentation/user/post_user.yml', methods=['POST'])
def post_user():
    """
    Create a user
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    required_fields = ['first_name', 'last_name', 'email', 'password', 'phone_no', 'image_file']
    missing_fields = [field for field in required_fields if field not in request.get_json()]
    if missing_fields:
        abort(400, description=f"Missing fields: {', '.join(missing_fields)}")

    data = request.get_json()
    instance = User(**data)
    instance.save()
    
    token = jwt.encode({
        "user": instance.id,
        "expiration": str(datetime.utcnow() + timedelta(minutes=120))
        },
        app.config['SECRET_KEY'])
    return jsonify({
            "token" : token
            }), 200

#return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/login', methods=['POST'], strict_slashes=False)
@swag_from('documentation/user/post_user_login.yml', methods=['POST'])
def login_user():
    """
    login a user
    """
    if not request.get_json():
            abort(400, description="Not a JSON")

    if 'email' not in request.json or 'password' not in request.json:
        abort(400, description="Missing email or password")

    email = request.json['email']
    password = request.json['password']

    # Find the user by email
    user = storage.get_user(User, email)

    if request.method == 'POST':

        if not user:
            abort(401, description="Invalid email or password")

        # Verify the password
        if not user.password:
            abort(401, description="Invalid email or password")
        print(user.id)
        # Set the user_id cookie
        response = make_response(jsonify({'user': user.to_dict()}), 200)
        response.set_cookie('user', str(user.id))

        token = jwt.encode({
            "user": user.id,
            "expiration": str(datetime.utcnow() + timedelta(minutes=120))
            },
            app.config['SECRET_KEY'])
        return jsonify({
            "token" : token
            }), 200



@app_views.route('/auth', methods=['GET'], strict_slashes=False)
@token_required
@swag_from('documentation/user/auth.yml', methods=['GET'])
def auth(current_user):
    try:
        # Get the user ID from the current_user object obtained from token_required decorator
        print(current_user.to_dict())
        user = current_user.to_dict()

        if user:
            return jsonify({"user": user})
        else:
            return jsonify({"message": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/user/put_user.yml', methods=['PUT'])
def put_user(user_id):
    """
    Updates a user
    """
    user = storage.get(User, user_id)

    if not user:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'email', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
    storage.save()
    return make_response(jsonify(user.to_dict()), 200)
