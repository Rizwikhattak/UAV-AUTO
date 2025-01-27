from flask import Blueprint,jsonify,request
from Controller import MissionTaskController

mission_task_routes = Blueprint('mission_task_routes',__name__)

@mission_task_routes.route('/insert_mission_task',methods=['POST'])
def insert_mission_task():
    data = request.get_json()
    mission_task = MissionTaskController.insert_mission_task(data)
    if mission_task:
        return {'success':True,'data':mission_task},200
    else:
        return {'success':False,'data':mission_task},400

@mission_task_routes.route('/get_all_mission_tasks',methods=['GET'])
def get_all_mission_tasks():
    mission_tasks = MissionTaskController.get_all_mission_tasks()
    if mission_tasks:
        return {'success':True,'data':mission_tasks},200
    else:
        return {'success':False,'data':mission_tasks},400

@mission_task_routes.route('/get_mission_task_by_id/<int:id>',methods=['GET'])
def get_mission_task_by_id(id):
    mission_task = MissionTaskController.get_mission_task_by_id(id)
    if mission_task:
        return {'success':True,'data':mission_task},200
    else:
        return {'success':False,'data':mission_task},400

@mission_task_routes.route('/update_mission_task_by_id/<int:id>',methods=['PUT'])
def update_mission_task_by_id(id):
    data = request.get_json()
    data['id'] = id
    mission_task = MissionTaskController.update_mission_task_by_id(data)
    if mission_task:
        return {'success':True,'data':mission_task},200
    else:
        return {'success':False,'data':mission_task},400

@mission_task_routes.route('/delete_mission_task_by_id/<int:id>',methods=['DELETE'])
def delete_mission_task_by_id(id):
    mission_task = MissionTaskController.delete_mission_task_by_id(id)
    if mission_task:
        return {'success':True,'data':mission_task},200
    else:
        return {'success':False,'data':mission_task},400