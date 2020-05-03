import models

#import blueprint
from flask import Blueprint, request, jsonify

from flask_bcrypt import generate_password_hash, check_password_hash

from playhouse.shortcuts import model_to_dict

from flask_login import login_user, current_user, logout_user, login_required

# Create a blueprint
users = Blueprint('users', 'users')

#declare the blueprints here
plants = Blueprint('plants', 'plants')

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



#Login route
@users.route('/login', methods=['POST'])
def log_in():

    payload = request.get_json()
    # Lower case all the user inputs
    # payload['name'] = payload['name'].lower()
    # payload['email'] = payload['email'].lower()
    payload['username'] = payload['username'].lower()

    try:

        #Check if user exsit
        user = models.User.get(models.User.username == payload['username'])

        #Convert users into dict
        user_dict = model_to_dict(user)

        #Chck if the password is correct
        check_password = check_password_hash(user_dict['password'], payload['password'])

        # if password is correct then move forward
        if (check_password):
            #log_in user here
            login_user(user)

            # Remove the password while reponding
            user_dict.pop('password')

            return jsonify(
                data=user_dict,
                message=f"Welcome back {user_dict['name']}",
                status=200
            ), 200

        # If password doesn't match
        else:
            return jsonify(
                data={},
                message="Username or password doesn't match",
                status=401
            ), 401

    # If user doesn't exsit in the database
    except models.DoesNotExist:

        return jsonify(
            data={},
            message="Can't find the user with the username. Signup to continue",
            status=401
        ), 401


#User show route
@users.route('/myplants', methods=['GET'])
@login_required
def show_user_plants():
    """This function will show the user's plants"""

    current_user_plants_dicts = [model_to_dict(plant) for plant in current_user.plants]

    for plants_dict in current_user_plants_dicts:
        plants_dict['belongs_to'].pop('password')

    return jsonify(
        data=current_user_plants_dicts,
        message=f"{current_user.name}'s Plants'"
    )


#User logout route
@users.route('/logout', methods=['GET'])
def user_logout():
    logout_user()

    return jsonify(
        message="User logged out"
    )

#User delete route
@users.route('/<id>', methods=['DELETE'])
def user_delete(id):

    try:
        f = current_user.plants
        for plant in f:
            plant.delete_instance()

        # Get user by id thru querieng
        user_to_delete = models.User.get_by_id(id)

        q = user_to_delete.delete_instance()
        # q.execute()

        return jsonify(
            data={},
            message=f"Sorry to see you go. User with id => {id} was deleted",
            status=200
        ), 200


    except models.DoesNotExist:
        return jsonify(
            data={
                'error': "404 not found",
            },
            message="User doesn't exist.",
            status=404
        ), 404












#
