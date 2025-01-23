from flask import Blueprint,jsonify,request
from Controller import MissionTaskController

mission_task_routes = Blueprint('mission_task_routes',__name__)

@mission_task_routes.route('/insert_mission_task',methods=['POST'])
def insert_mission_task():
    data = request.get_json()
    mission_task = MissionTaskController.insert_mission_task(data)
    mission_task_dict = {
        "id":mission_task.id,
        "mission_planner_id":mission_task.mission_planner_id,
        "description":mission_task.description
    }
    return {'success':True,'data':mission_task_dict},200