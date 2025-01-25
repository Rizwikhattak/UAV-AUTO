from flask import Blueprint,request,jsonify
from Controller import LocationPinController

location_pin_routes = Blueprint('location_pin_routes',__name__)

@location_pin_routes.route('/insert_location_pins',methods=['POST'])
def insert_location_pin():
    data = request.get_json()
    location_pin = LocationPinController.insert_location_pins(data)
    if location_pin:
        return jsonify({'success':True,'data':location_pin}),200
    else:
        return jsonify({'success':False,'data':location_pin}),400

@location_pin_routes.route('/get_location_pins',methods=['GET'])
def get_location_pins():
    location_pins = LocationPinController.get_location_pins()
    if location_pins:
        return jsonify({'success':True,'data':location_pins}),200
    else:
        return jsonify({'success':False,'data':location_pins}),400

@location_pin_routes.route('/get_location_pin_by_id/<int:id>',methods=['GET'])
def get_location_pin_by_id(id):
    location_pin = LocationPinController.get_location_pin_by_id(id)
    if location_pin:
        return jsonify({'success':True,'data':location_pin}),200
    else:
        return jsonify({'success':False,'data':location_pin}),400

@location_pin_routes.route('/update_location_pin/<int:id>',methods=['PUT'])
def update_location_pin(id):
    data = request.get_json()
    data['id'] = id
    location_pin = LocationPinController.update_location_pin(data)
    if location_pin:
        return jsonify({'success':True,'data':location_pin}),200
    else:
        return jsonify({'success':False,'data':location_pin}),400

@location_pin_routes.route('/delete_location_pin/<int:id>',methods=['DELETE'])
def delete_location_pin(id):
    location_pin = LocationPinController.delete_location_pin(id)
    if location_pin:
        return jsonify({'success':True,'data':location_pin}),200
    else:
        return jsonify({'success':False,'data':location_pin}),400
