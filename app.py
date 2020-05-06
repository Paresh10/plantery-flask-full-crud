import os

# Import flask here in app.py
from flask import Flask, jsonify, g

#Import cors here
from flask_cors import CORS

# Import models here
import models

#Import user blueprints here
from resources.users import users

#import plans blueprints here
from resources.plants import plants

#Import Login manager here
from flask_login import LoginManager






# For printing detailed error messages
DEBUG=True

#Declare Port as 8000. Default for Python
PORT=8000

# Instantiate flask class to create an app
app = Flask(__name__)

#Implement cors for users
CORS(users, origins=['http://localhost:3000'], supports_credentials=True)
CORS(plants, origins=['http://localhost:3000'], supports_credentials=True)

#Setup a secret key for session. Login manager comes with session
app.secret_key = "Creating RESTFUL REACT-FLASK APP. SO MUCH FUN!!!"

# Instantiate the LoginManager
login_manager = LoginManager()

#Connect the app with the login_manager
login_manager.init_app(app)


# Setup the user_loader in here
@login_manager.user_loader
def loading_user(user_id):

    try:
        print ('Loading the user from user_loader')
        user = models.User.get_by_id(user_id)

        # When found return the user here
        return user

    # If user is not found then return none in the except
    except models.DoesNotExist:
        return None

# Customize the response for json when user id not loggedIn
@login_manager.unauthorized_handler
def unauthorized():

    return jsonify(
        data={
            'error': "User not logged In"
        },
        message="Please login to continue",
        status=401
    ), 401

#setup the blueprint for users
app.register_blueprint(users, url_prefix='/api/v1/users')

#setup the blueprint for plants here
app.register_blueprint(plants, url_prefix='/api/v1/plants')






@app.before_request 
def before_request():
  """Connect to the db before each request"""
  # store the database as a global var in g
  print("you should see this before each request") 
  g.db = models.DATABASE
  g.db.connect()


@app.after_request 
def after_request(response):
  """Close the db connetion after each request"""
  print("you should see this after each request") 
  g.db.close()
  return response




if 'ON_HEROKU' in os.environ: 
  print('\non heroku!')
  models.connect_to_database()


#Setup the server here
if __name__ == '__main__':
    models.connect_to_database()
    app.run(debug=DEBUG, port=PORT)
