from flask import Blueprint,request,jsonify
from Controller import MissionStationMappingController

mission_station_mapping_routes = Blueprint('mission_station_mapping_routes',__name__)

@mission_station_mapping_routes.route('/insert_mission_station_mapping',methods=['POST'])
def insert_mission_station_mapping():
    data = request.get_json()
    mission_station_mapping = MissionStationMappingController.insert_mission_station_mapping(data)
    if mission_station_mapping:
        return jsonify({'success':True,'data':mission_station_mapping}),200
    else:
        return jsonify({'success':False,'data':mission_station_mapping}),400

@mission_station_mapping_routes.route('/get_all_mission_station_mappings',methods=['GET'])
def get_all_mission_station_mappings():
    data = MissionStationMappingController.get_all_mission_station_mappings()
    if data:
        return jsonify({'success':True,'data':data}),200
    else:
        return jsonify({'success':False,'data':data}),400

@mission_station_mapping_routes.route('/get_mission_station_mapping_by_id/<int:id>',methods=['GET'])
def get_mission_station_mapping_by_id(id):
    data = MissionStationMappingController.get_mission_station_mapping_by_id(id)
    if data:
        return jsonify({'success':True,'data':data}),200
    else:
        return jsonify({'success':False,'data':data}),400

@mission_station_mapping_routes.route('/update_mission_station_mapping_by_id/<int:id>',methods=['PUT'])
def update_mission_station_mapping_by_id(id):
    data = request.get_json()
    data['id'] = id
    mission_station_mapping = MissionStationMappingController.update_mission_station_mapping_by_id(data)
    if mission_station_mapping:
        return jsonify({'success':True,'data':mission_station_mapping}),200
    else:
        return jsonify({'success':False,'data':mission_station_mapping}),400

@mission_station_mapping_routes.route('/delete_mission_station_mapping_by_id/<int:id>',methods=['DELETE'])
def delete_mission_station_mapping_by_id(id):
    data = MissionStationMappingController.delete_mission_station_mapping_by_id(id)
    if data:
        return jsonify({'success':True,'data':data}),200
    else:
        return jsonify({'success':False,'data':data}),400