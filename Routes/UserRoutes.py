from flask import Blueprint, jsonify, request,send_from_directory
from Controller import UserController
from config import app

# Create a blueprint for user routes
user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/insert_user', methods=['POST'])
def insert_user():
    data = request.get_json()
    user = UserController.insert_user(data)
    if user:
        return jsonify({'success': True,'data':user}),200
    else:
        return jsonify({'success': False ,'data':user}),400

@user_routes.route('/insert_admin',methods=['POST'])
def insert_admin():
    data = request.get_json()
    admin = UserController.insert_admin(data)
    if admin:
        return jsonify({'success': True,'data':admin}),200
    else:
        return jsonify({'success': False,'data':admin}),400

@user_routes.route('/get_all_admins',methods=['GET'])
def get_all_admins():
    admins = UserController.get_all_admins()
    if admins:
        return jsonify({'success':True,'data':admins}),200
    else:
        return jsonify({'success':False,'data':admins}),400

@user_routes.route('/get_admin_by_id/<int:id>',methods=['GET'])
def get_admin_by_id(id):
    admin = UserController.get_admin_by_id(id)
    if admin:
        return jsonify({'success':True,'data':admin}),200
    else:
        return jsonify({'success':False,'data':admin}),400

@user_routes.route('/update_admin/<int:id>',methods=['PUT'])
def update_admin(id):
    data = request.get_json()
    data['id'] = id
    admin = UserController.update_admin(data)
    if admin:
        return jsonify({'success':True,'data':admin}),200
    else:
        return jsonify({'success':False,'data':admin}),400

@user_routes.route('/delete_admin/<int:id>',methods=['DELETE'])
def delete_admin(id):
    admin = UserController.delete_admin(id)
    if admin:
        return jsonify({'success':True,'data':admin}),200
    else:
        return jsonify({'success':False,'data':admin}),400



@user_routes.route('/insert_operator',methods=['POST'])
def insert_operator():
    data = request.form.to_dict()
    op_image = request.files.get('image')
    operator = UserController.insert_operator(data,op_image)
    if operator:
        return jsonify({'success':True,'data':operator}),200
    else:
        return jsonify({'success':False,'data':operator}),400


@user_routes.route('/login',methods=['POST'])
def login_user():
    data = request.get_json()
    user = UserController.login_user(data)
    if user:
        return jsonify({'success':True,'data':user}),200
    else:
        return jsonify({'success':False,'data':user}),400

@user_routes.route('/update_operator/<int:id>',methods=['PUT'])
def update_operator(id):
    data = request.form.to_dict()
    data['id'] = id
    op_image = request.files.get('image')
    operator = UserController.update_operator(data,op_image)
    if operator:
        return jsonify({'success':True,'data':operator}),200
    else:
        return jsonify({'success':False,'data':operator}),400

@user_routes.route('/delete_operator/<int:id>',methods=['DELETE'])
def delete_operator(id):
    operator = UserController.delete_operator(id)
    if operator:
        return jsonify({'success':True,'operator':operator}),200
    else:
        return jsonify({'success':False,'operator':operator}),400


@user_routes.route('/get_all_operators',methods=['GET'])
def get_all_operators():
    operators = UserController.get_all_operators()
    if operators:
        return jsonify({'success':True,'data':operators}),200
    else:
        return jsonify({'success':False,'data':operators}),400

@user_routes.route('/get_operator_by_id/<int:id>',methods=['GET'])
def get_operator_by_id(id):
    operator = UserController.get_operator_by_id(id)
    if operator:
        return jsonify({'success':True,'data':operator}),200
    else:
        return jsonify({'success':False,'data':operator}),400

@user_routes.route('/uploads/operators/profile_pictures/<filename>')
def serve_profile_picture(filename):
    return send_from_directory(app.config['OPERATOR_PROFILE_PICTURES_FOLDER'], filename)