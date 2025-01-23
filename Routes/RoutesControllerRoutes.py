from flask import Blueprint,request,jsonify
from Controller import RoutesController

routes_controller_routes = Blueprint('routes_controller_routes',__name__)

@routes_controller_routes.route('/insert_route',methods=['POST'])
def insert_route():
    data = request.get_json()
    routes = RoutesController.insert_route(data)
    return jsonify({'success':True,'data':routes})

@routes_controller_routes.route('/get_routes',methods=['GET'])
def get_routes():
    routes = RoutesController.get_routes()
    if routes:
        return jsonify({'success':True,'data':routes})
    else:
        return jsonify({'success':False,'data':routes})

@routes_controller_routes.route('/get_all_routes',methods=['GET'])
def get_all_routes():
    routes = RoutesController.get_all_routes()
    if routes:
        return jsonify({'success':True,'data':routes})
    else:
        return jsonify({'success':False,'data':routes})

@routes_controller_routes.route('/delete_route/<int:id>',methods=['DELETE'])
def delete_route(id):
    routes = RoutesController.delete_route(id)
    if routes:
        return jsonify({'success':True,'data':routes})
    else:
        return jsonify({'success':False,'data':routes})