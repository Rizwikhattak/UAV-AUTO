from flask import Blueprint,request,jsonify
from Controller import MissionStationMappingController

mission_station_mapping_routes = Blueprint('mission_station_mapping_routes',__name__)

@mission_station_mapping_routes.route('/insert_mission_station_mapping',methods=['POST'])
def insert_mission_station_mapping():
    data = request.get_json()
    mission_station_mapping = MissionStationMappingController.insert_mission_station_mapping(data)
    mission_station_mapping_dict = {
        "id":mission_station_mapping.id,
        "mission_planner_id":mission_station_mapping.mission_planner_id,
        "landing_station_id":mission_station_mapping.landing_station_id,
        "departure_station_id":mission_station_mapping.departure_station_id
    }
    return jsonify({'success':True,'data':mission_station_mapping_dict}),200