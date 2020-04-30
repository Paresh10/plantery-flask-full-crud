import models

# import the blueprint here
from flask import Blueprint, request, jsonify


from flask_login import current_user, login_required

from playhouse.shortcuts import model_to_dict

#declare the blueprints here
plants = Blueprint('plants', 'plants')


# Creae route for plants
@plants.route('/', methods=['POST'])
@login_required
def create_plant():
    """This function Create new plants"""

    payload = request.get_json()

    create_new_plant = models.Plant.create(
        name=payload['name'],
        region=payload['region'],
        description=payload['description'],

        #This will get id from logged in user
        belongs_to = current_user.id
    )

    #Convert it to a dictionary
    create_new_plant_dic = model_to_dict(create_new_plant)

    print(create_new_plant_dic)

    # Remove the password before returning the response
    create_new_plant_dic['belongs_to'].pop('password')

    return jsonify(
        data=create_new_plant_dic,
        message=f"{create_new_plant_dic['name']} was just created!",
        status=201
    ), 201

















    #