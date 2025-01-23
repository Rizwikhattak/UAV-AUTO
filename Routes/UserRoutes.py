from flask import Blueprint, jsonify, request,send_from_directory
from Controller import UserController
from config import app

# Create a blueprint for user routes
user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/insert_user', methods=['POST'])
def insert_user():
    data = request.get_json()
    user = UserController.insert_user(data)
    user_dict = {
        "user_id": user.id,
        "name": user.name,
        "password": user.password,
        "role": user.role,
        "email": user.email
    }
    return jsonify({'success': 'Data inserted successfully','data':user_dict}),200

@user_routes.route('/insert_admin',methods=['POST'])
def insert_admin():
    data = request.get_json()
    admin = UserController.insert_admin(data)
    if admin:
        return jsonify({'success': True,'data':admin}),200
    return jsonify({'success': False,'data':"This user already exists"}),400

@user_routes.route('/insert_operator',methods=['POST'])
def insert_operator():
    data = request.form.to_dict()
    op_image = request.files.get('image')
    operator = UserController.insert_operator(data,op_image)
    if operator:
        return jsonify({'success':True,'data':operator}),200
    return jsonify({'success':False,'data':"This user already exists"}),400

@user_routes.route('/upload_operator_profile_picture',methods=['POST'])
def upload_operator_profile_picture():
    # data = request.get_json()
    UserController.upload_operator_profile_picture()
    # return jsonify({'success':True,'data':image_path}),200
    return {}
@user_routes.route('/login',methods=['POST'])
def login_user():
    data = request.get_json()
    is_valid = UserController.login_user(data)
    return {'success':is_valid}

@user_routes.route('/update_operator',methods=['PUT'])
def update_operator():
    data = request.form.to_dict()
    op_image = request.files.get('image')
    operator = UserController.update_operator(data,op_image)
    if operator:
        return jsonify({'success':True,'data':operator}),200
    else:
        return jsonify({'success':False,'data':operator}),400

@user_routes.route('/delete_operator/<int:id>',methods=['DELETE'])
def delete_operator(id):
    isDeleted = UserController.delete_operator(id)
    return jsonify({'success':isDeleted})

@user_routes.route('/get_all_operators',methods=['GET'])
def get_all_operators():
    operators = UserController.get_all_operators()
    if operators:
        return jsonify({'success':True,'data':operators}),200
    return jsonify({'success':False,'data':operators}),400

@user_routes.route('/get_operator_by_id/<int:id>',methods=['GET'])
def get_operator_by_id(id):
    operator = UserController.get_operator_by_id(id)
    if operator:
        return jsonify({'success':True,'data':operator}),200
    return jsonify({'success':False,'data':operator}),400

@user_routes.route('/uploads/operators/profile_pictures/<filename>')
def serve_profile_picture(filename):
    return send_from_directory(app.config['OPERATOR_PROFILE_PICTURES_FOLDER'], filename)