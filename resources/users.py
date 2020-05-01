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
# @users.route('/<id>', methods=['GET'])
# @login_required
# def show_user(id):
#     """This function will show the users by it's id"""
#     user = models.User.get_by_id(id) #.join(Plant).where(Plant.id == id)
#     user_dict = model_to_dict(user)
#
#     plants = models.Plant.get_by_id(id)
#
#     plant_dict = model_to_dict(plants)
#
#     # plant_dict = [model_to_dict(plant) for plant in plants]
#
#     # if plants.belongs_to.id == current_user.id:
#
#     return jsonify(
#         data={
#             'plant': plant_dict,
#             'user': user_dict
#         },
#         message="Here is the found user"
#     )

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
        # Get user by id thru querieng
        user_to_delete = models.User.get_by_id(id)

        # For now delette the user.
        # COME BACK TO THIS AFTER USERS HAVE PLANTS AND RE-WRITE THE DELETE QUERY
        user_to_delete.delete_instance()

        return jsonify(
            data={},
            message=f"Sorry to see you go user with id => {id} was deleted",
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
