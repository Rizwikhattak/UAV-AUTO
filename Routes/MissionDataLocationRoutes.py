from flask import Blueprint,request,jsonify
from Controller import MissionDataLocationController

mission_data_location_routes = Blueprint('mission_data_location_routes',__name__)

@mission_data_location_routes.route('/insert_mission_data_location',methods=['POST'])
def insert_mission_data_location():
    data = request.get_json()
    mission_data_location = MissionDataLocationController.insert_mission_data_location(data)
    mission_data_location_dict = {
        "id":mission_data_location.id,
        "mission_task_id":mission_data_location.mission_task_id,
        "latitude":mission_data_location.latitude,
        "longitude":mission_data_location.longitude,
        "damage":mission_data_location.damage,
    }
    return jsonify({'success':True,'data':mission_data_location_dict}),200