from flask import Blueprint,request,jsonify
from Controller import MissionDataLocationController

mission_data_location_routes = Blueprint('mission_data_location_routes',__name__)

@mission_data_location_routes.route('/insert_mission_data_location',methods=['POST'])
def insert_mission_data_location():
    data = request.get_json()
    mission_data_location = MissionDataLocationController.insert_mission_data_location(data)
    if mission_data_location:
        return jsonify({'success':True,'data':mission_data_location}),200
    else:
        return jsonify({'success':False,'data':mission_data_location}),400

@mission_data_location_routes.route('/get_mission_data_location_by_id/<int:id>',methods=['GET'])
def get_mission_data_location_by_id(id):
    mission_data_location = MissionDataLocationController.get_mission_data_location_by_id(id)
    if mission_data_location:
        return jsonify({'success':True,'data':mission_data_location}),200
    else:
        return jsonify({'success':False,'data':mission_data_location}),400

@mission_data_location_routes.route('/get_all_mission_data_location',methods=['GET'])
def get_all_mission_data_location():
    mission_data_locations = MissionDataLocationController.get_all_mission_data_location()
    if mission_data_locations:
        return jsonify({'success':True,'data':mission_data_locations}),200
    else:
        return jsonify({'success':False,'data':mission_data_locations}),400

@mission_data_location_routes.route('/update_mission_data_location/<int:id>',methods=['PUT'])
def update_mission_data_location(id):
    data = request.get_json()
    data['id'] = id
    mission_data_location = MissionDataLocationController.update_mission_data_location(data)
    if mission_data_location:
        return jsonify({'success':True,'data':mission_data_location}),200
    else:
        return jsonify({'success':False,'data':mission_data_location}),400

@mission_data_location_routes.route('/delete_mission_data_location/<int:id>',methods=['DELETE'])
def delete_mission_data_location(id):
    mission_data_location = MissionDataLocationController.delete_mission_data_location(id)
    if mission_data_location:
        return jsonify({'success':True,'data':mission_data_location}),200
    else:
        return jsonify({'success':False,'data':mission_data_location}),400

