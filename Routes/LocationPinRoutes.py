from flask import Blueprint,request,jsonify
from Controller import LocationPinController

location_pin_routes = Blueprint('location_pin_routes',__name__)

@location_pin_routes.route('/insert_location_pins',methods=['POST'])
def insert_location_pin():
    data = request.get_json()
    location_pin = LocationPinController.insert_location_pins(data)
    return jsonify({'success':True,'data':location_pin}),200

@location_pin_routes.route('/get_location_pins',methods=['GET'])
def get_location_pins():
    location_pins = LocationPinController.get_location_pins()
    if location_pins:
        return jsonify({'success':True,'data':location_pins})
    else:
        return jsonify({'success':False,'data':location_pins})