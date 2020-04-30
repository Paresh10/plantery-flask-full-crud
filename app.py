# Import flask here in app.py
from flask import Flask

# Import models here
import models

#Import user blueprints here
from resources.users import users

# For printing detailed error messages
DEBUG=True

#Declare Port as 8000. Default for Python
PORT=8000

# Instantiate flask class to create an app
app = Flask(__name__)


#setup the blueprint fpr users
app.register_blueprint(users, url_prefix='/api/v1/users')

#Setup the server here
if __name__ == '__main__':
    models.connect_to_database()
    app.run(debug=DEBUG, port=PORT)
