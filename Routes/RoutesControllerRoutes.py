from flask import Blueprint,request,jsonify
from Controller import RoutesController

routes_controller_routes = Blueprint('routes_controller_routes',__name__)

@routes_controller_routes.route('/insert_route',methods=['POST'])
def insert_route():
    data = request.get_json()
    routes = RoutesController.insert_route(data)
    if routes:
        return jsonify({'success':True,'data':routes}),200
    else:
        return jsonify({'success':False,'data':routes}),400

@routes_controller_routes.route('/get_all_routes_without_location_pins',methods=['GET'])
def get_all_routes_without_location_pins():
    routes = RoutesController.get_all_routes_without_location_pins()
    if routes:
        return jsonify({'success':True,'data':routes}),200
    else:
        return jsonify({'success':False,'data':routes}),400

@routes_controller_routes.route('/get_all_routes_with_location_pins',methods=['GET'])
def get_all_routes_with_location_pins():
    routes = RoutesController.get_all_routes_with_location_pins()
    if routes:
        return jsonify({'success':True,'data':routes}),200
    else:
        return jsonify({'success':False,'data':routes}),400

@routes_controller_routes.route('/delete_route/<int:id>',methods=['DELETE'])
def delete_route(id):
    routes = RoutesController.delete_route(id)
    if routes:
        return jsonify({'success':True,'data':routes}),200
    else:
        return jsonify({'success':False,'data':routes}),400

@routes_controller_routes.route('/get_route_by_id/<int:id>',methods=['GET'])
def get_route_by_id(id):
    routes = RoutesController.get_route_by_id(id)
    if routes:
        return jsonify({'success':True,'data':routes}),200
    else:
        return jsonify({'success':False,'data':routes}),400

@routes_controller_routes.route('/update_route_by_id/<int:id>',methods=['PUT'])
def update_route_by_id(id):
    data = request.get_json()
    data['id'] = id
    routes = RoutesController.update_route_by_id(data)
    if routes:
        return jsonify({'success':True,'data':routes}),200
    else:
        return jsonify({'success':False,'data':routes}),400
