from flask import Blueprint,request,jsonify
from Controller import StationController

station_routes = Blueprint('station_routes',__name__)

@station_routes.route('/insert_station',methods=['POST'])
def insert_station():
    data = request.get_json()
    station = StationController.insert_station(data)
    return jsonify({'success':True,'data':station}),200

@station_routes.route('/get_all_stations',methods=['GET'])
def get_all_stations():
    stations = StationController.get_all_stations()
    if stations:
        return jsonify({'success':True,'data':stations})
    return jsonify({'success':False,'data':stations})

@station_routes.route('/get_station_by_id/<int:id>',methods=['GET'])
def get_station_by_id(id):
    station = StationController.get_station_by_id(id)
    if station:
        return jsonify({'success':True,'data':station})
    return jsonify({'success':False,'data':station})

@station_routes.route('/update_station',methods=['PUT'])
def update_station():
    data = request.get_json()
    station = StationController.update_station(data)
    return jsonify({'success':True,'data':station})

@station_routes.route('/delete_station/<int:id>',methods=['DELETE'])
def delete_station(id):
    is_deleted = StationController.delete_station(id)
    return jsonify({'success':is_deleted})