# Import flask here in app.py
from flask import Flask, jsonify

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












#Setup the server here
if __name__ == '__main__':
    models.connect_to_database()
    app.run(debug=DEBUG, port=PORT)
