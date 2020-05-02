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
    try:
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


    except models.DoesNotExist:
        return jsonify(
            data={
                'error': 'oops'
            },
            message="'We didn't found any plants'"

        )



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
def show_plants(id):
    """This function will show the plants by id"""

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
    """This function will delete the plany by it's id"""

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

#Plant Update route
@plants.route('/<id>', methods=['PUT'])
@login_required
def update_plant(id):
    """This function will update the plant by it's id"""

    payload = request.get_json()

    plant_to_update = models.Plant.get_by_id(id)

    if plant_to_update.belongs_to.id == current_user.id:

        if 'name' in payload:
            plant_to_update.name = payload['name']
        if 'region' in payload:
            plant_to_update.region = payload['region']
        if 'description' in payload:
            plant_to_update.description = payload['description']

        plant_to_update.save()

        plant_to_update_dict = model_to_dict(plant_to_update)

        plant_to_update_dict['belongs_to'].pop('password')

        return jsonify(
            data=plant_to_update_dict,
            message=f"{plant_to_update_dict['name']} was updated!",
            status=200
        ), 200

    else:
        return jsonify(
            data={
                'error': 'Action can not be performed',
            },
            message="Can only update the plant that belongs to user",
            status=403
        ), 403








    #
