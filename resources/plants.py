import models

# import the blueprint here
from flask import Blueprint, request, jsonify


from flask_login import current_user, login_required

from playhouse.shortcuts import model_to_dict

#declare the blueprints here
plants = Blueprint('plants', 'plants')


# Get index route for plants
@plants.route('/', methods=['GET'])
def get_all_plants():
    """This function will get all the plants"""

    all_plants = models.Plant.select()

    plants = [model_to_dict(plant) for plant in all_plants]

    # Remove password from response
    for plant in plants:
        plant['belongs_to'].pop('password')

    return jsonify(
        data=plants,
        message=f"Here are all {len(plants)} plants found!",
        status=200
    ), 200



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


# Show route for plants
@plants.route('/<id>', methods=['GET'])
def users_plants(id):

    plant = models.Plant.get_by_id(id)
    plant_dict = model_to_dict(plant)
    plant_dict['belongs_to'].pop('password')
    plant_dict['belongs_to'].pop('id')
    plant_dict['belongs_to'].pop('username')

    if current_user.is_authenticated:

        return jsonify(
            data=plant_dict,
            messagage="Here is the found plant"
        )
    else:
        return jsonify(
            data={},
            message="Something went wrong"
        )


#Delete route
@plants.route('/<id>', methods=['DELETE'])
@login_required
def plant_to_delete(id):

    try:
        #Get plants by id
        plant = models.Plant.get_by_id(id)

        if plant.belongs_to.id == current_user.id:
            plant.delete_instance()

            return jsonify(
                data={},
                message="Plant was deleted",
                status=200
            ), 200

        else :
            return jsonify(
                data={
                    'error': '403 forbidden'
                },
                message="Plant doesn't belongs to user",
                status=403
            ), 403


    except models.DoesNotExist:
        return jsonify(
            data={
                'error': 'Opps - 404'
            },
            message="No dog was found",
            status=404
        ), 404











    #
