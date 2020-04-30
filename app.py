# Import flask here in app.py
from flask import Flask

# For printing detailed error messages
DEBUG=True

#Declare Port as 8000. Default for Python
PORT=8000

# Instantiate flask class to create an app
app = Flask(__name__)


#Setup the server here
if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
