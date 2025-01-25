from flask import Blueprint,request,jsonify
from Controller import DroneAvailabilityLogController

drone_availability_log_routes = Blueprint('drone_availability_log_routes',__name__)

@drone_availability_log_routes.route('/insert_drone_availability_log',methods=['POST'])
def insert_drone_availibility_log():
    data = request.get_json()
    drone_availibility_log = DroneAvailabilityLogController.insert_drone_availability_log(data)
    if drone_availibility_log:
        return jsonify({'success':True,'data':drone_availibility_log}),200
    else:
        return jsonify({'success':False,'data':drone_availibility_log}),400

@drone_availability_log_routes.route('/get_drone_availability_log',methods=['GET'])
def get_drone_availability_log():
    data = DroneAvailabilityLogController.get_drone_availability_log()
    if data:
        return jsonify({'success':True,'data':data}),200
    else:
        return jsonify({'success':False,'data':data}),400

@drone_availability_log_routes.route('/get_drone_availability_log_by_id/<int:id>',methods=['GET'])
def get_drone_availability_log_by_id(id):
    data = DroneAvailabilityLogController.get_drone_availability_log_by_id(id)
    if data:
        return jsonify({'success':True,'data':data}),200
    else:
        return jsonify({'success':False,'data':data}),400

@drone_availability_log_routes.route('/update_drone_availability_log/<int:id>',methods=['PUT'])
def update_drone_availability_log(id):
    data = request.get_json()
    data['id'] = id
    drone_availibility_log = DroneAvailabilityLogController.update_drone_availability_log(data)
    if drone_availibility_log:
        return jsonify({'success':True,'data':drone_availibility_log}),200
    else:
        return jsonify({'success':False,'data':drone_availibility_log}),400

@drone_availability_log_routes.route('/delete_drone_availability_log/<int:id>',methods=['DELETE'])
def delete_drone_availability_log(id):
    data = DroneAvailabilityLogController.delete_drone_availability_log(id)
    if data:
        return jsonify({'success':True,'data':data}),200
    else:
        return jsonify({'success':False,'data':data}),400