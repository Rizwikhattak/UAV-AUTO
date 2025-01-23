from flask import Blueprint,request,jsonify
from Controller import DroneStationMappingController

drone_station_mapping_routes = Blueprint('drone_station_mapping_routes',__name__)

@drone_station_mapping_routes.route('/insert_drone_station_mapping',methods=['POST'])
def insert_drone_station_mapping():
    data = request.get_json()
    drone_station_mapping = DroneStationMappingController.insert_drone_sation_mapping(data)
    drone_station_mapping_dict = {
        "id":drone_station_mapping.id,
        "drone_id":drone_station_mapping.drone_id,
        "station_id":drone_station_mapping.station_id,
        "status":drone_station_mapping.status
    }
    return jsonify({'success':True,'data':drone_station_mapping_dict}),200

@drone_station_mapping_routes.route('/get_all_drone_station_mapping',methods=['GET'])
def get_all_drone_station_mapping():
    drone_station_mappings = DroneStationMappingController.get_all_drone_station_mapping()
    return {'success':True,'data':drone_station_mappings}
