from flask import Blueprint,request,jsonify
from Controller import DroneAvailabilityLogController

drone_availability_log_routes = Blueprint('drone_availability_log_routes',__name__)

@drone_availability_log_routes.route('/insert_drone_availability_log',methods=['POST'])
def insert_drone_availibility_log():
    data = request.get_json()
    drone_availibility_log = DroneAvailabilityLogController.insert_drone_availability_log(data)
    drone_availibility_log_dict = {
        "id":drone_availibility_log.id,
        "drone_id":drone_availibility_log.drone_id,
        "start_date":drone_availibility_log.start_date,
        "start_date_limit":drone_availibility_log.start_date_limit,
        "start_time_limit":str(drone_availibility_log.start_time_limit),
        "end_date_limit":drone_availibility_log.end_date_limit,
        "end_time_limit":str(drone_availibility_log.end_time_limit)
    }
    return jsonify({'success':True,'data':drone_availibility_log_dict}),200