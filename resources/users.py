import models

#import blueprint
from flask import Blueprint, request, jsonify

from flask_bcrypt import generate_password_hash

from playhouse.shortcuts import model_to_dict

from flask_login import login_user

# Create a blueprint
users = Blueprint('users', 'users')

#Test route
@users.route('/', methods=['GET'])
def test_route():
    return "User route is working now"


# Sign up route for user
@users.route('/signup', methods=['POST'])
def sign_up():
    payload = request.get_json()

    # Lower case all the user inputs
    payload['name'] = payload['name'].lower()
    payload['email'] = payload['email'].lower()
    payload['username'] = payload['username'].lower()
    print(payload)

    try:
        # Check if the user exist
        models.User.get(models.User.username == payload['username'])

        # if user's username already exist
        return jsonify(
            data={},
            message=f"Username {payload['username']}  already taken",
            status=401
        ), 401


    # handle ModelDoesNotExist error in the except
    except models.DoesNotExist:

        # hash the password with bcrypt
        hashed_password = generate_password_hash(payload['password'])

        # Create user
        user_created = models.User.create(
            name=payload['name'],
            email=payload['email'],
            username=payload['username'],
            password=hashed_password
        )

        #This will start the session for the user
        login_user(user_created)

        # Convert it to dict for responce
        user_created_dict = model_to_dict(user_created)

        print(user_created_dict)

        # Password can not be jsonify so we are gonna remove it while returning
        user_created_dict.pop('password')

        return jsonify(
            data=user_created_dict,
            message=f"New User with username {user_created_dict['username']} was created",
            status = 201
        ), 201
















#
