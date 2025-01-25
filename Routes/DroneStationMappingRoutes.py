from flask import Blueprint,request,jsonify
from Controller import DroneStationMappingController

drone_station_mapping_routes = Blueprint('drone_station_mapping_routes',__name__)

@drone_station_mapping_routes.route('/insert_drone_station_mapping',methods=['POST'])
def insert_drone_station_mapping():
    data = request.get_json()
    drone_station_mapping = DroneStationMappingController.insert_drone_sation_mapping(data)
    if drone_station_mapping:
        return jsonify({'success':True,'data':drone_station_mapping}),200
    else:
        return jsonify({'success':False,'data':drone_station_mapping}),400

@drone_station_mapping_routes.route('/get_all_drone_station_mapping',methods=['GET'])
def get_all_drone_station_mapping():
    drone_station_mappings = DroneStationMappingController.get_all_drone_station_mapping()
    if drone_station_mappings:
        return jsonify({'success':True,'data':drone_station_mappings}),200
    else:
        return jsonify({'success':False,'data':drone_station_mappings}),400

@drone_station_mapping_routes.route('/get_drone_station_mapping_by_drone_id/<int:id>',methods=['GET'])
def get_drone_station_mapping_by_drone_id(id):
    drone_station_mapping = DroneStationMappingController.get_drone_station_mapping_by_drone_id(id)
    if drone_station_mapping:
        return jsonify({'success':True,'data':drone_station_mapping}),200
    else:
        return jsonify({'success':False,'data':drone_station_mapping}),400

@drone_station_mapping_routes.route('/update_drone_station_mapping',methods=['PUT'])
def update_drone_station_mapping():
    data = request.get_json()
    drone_station_mapping = DroneStationMappingController.update_drone_station_mapping(data['drone_id'],data['station_id'])
    if drone_station_mapping:
        return jsonify({'success':True,'data':drone_station_mapping}),200
    else:
        return jsonify({'success':False,'data':drone_station_mapping}),400

@drone_station_mapping_routes.route('/delete_drone_station_mapping/<int:id>',methods=['DELETE'])
def delete_drone_station_mapping(id):
    drone_station_mapping = DroneStationMappingController.delete_drone_station_mapping(id)
    if drone_station_mapping:
        return jsonify({'success':True,'data':drone_station_mapping}),200
    else:
        return jsonify({'success':False,'data':drone_station_mapping}),400

