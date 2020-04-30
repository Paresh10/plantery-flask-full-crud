import models

# import the blueprint here
from flask import Blueprint,


from flask_login import current_user, login_required

#declare the blueprints here
plants = Blueprint('plants', 'plants')
