# Import flask here in app.py
from flask import Flask

# Import models here
import models

#Import user blueprints here
from resources.users import users

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

#setup the blueprint fpr users
app.register_blueprint(users, url_prefix='/api/v1/users')

#Setup the server here
if __name__ == '__main__':
    models.connect_to_database()
    app.run(debug=DEBUG, port=PORT)
