from flask import Blueprint,request,jsonify
from Controller import SortieController

sortie_routes = Blueprint('sortie_routes',__name__)

@sortie_routes.route('/insert_sortie',methods=['POST'])
def insert_sortie():
    data = request.get_json()
    sortie = SortieController.insert_sortie(data)
    sortie_dict ={
        "id":sortie.id,
        "mission_planner_id":sortie.mission_planner_id,
        "start_date":sortie.start_date,
        "start_time":str(sortie.start_time),
        "end_date":sortie.end_date,
        "end_time":str(sortie.end_time),
        "duration":sortie.duration
    }
    return jsonify({'success':True,'data':sortie_dict}),200