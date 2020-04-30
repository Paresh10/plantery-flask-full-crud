import models

#import blueprint
from flask import Blueprint

# Create a blueprint
users = Blueprint('users', 'users')

#Test route
@users.route('/', methods=['GET'])
def test_route():
    return "User route is working now"
