from flask import Blueprint,request,jsonify,send_file
from Controller import MissionDataImageController

mission_data_image_routes = Blueprint('mission_data_image_routes',__name__)

@mission_data_image_routes.route('/insert_mission_data_image',methods=['POST'])
def insert_mission_data_image():
    data = request.get_json()
    mission_data_image = MissionDataImageController.insert_mission_data_image(data)
    mission_data_image_dict = {
        "id":mission_data_image.id,
        "mission_data_location_id":mission_data_image.mission_data_location_id,
        "image_path":mission_data_image.image_path,
    }
    return jsonify({'success':True,'data':mission_data_image_dict}),200

@mission_data_image_routes.route('/upload_image',methods=['POST'])
def upload_image():
    data = request.files['image']
    data_path = MissionDataImageController.upload_image(data)
    # return send_file(data_path, mimetype='image/jpeg')
    return jsonify({'success':True,'is_damaged':True,'data':data_path}),200

@mission_data_image_routes.route('/uploads/missions/<int:mission_planner_id>/model_results/<int:location_pin_id>/<filename>',methods=['GET'])
def serve_damaged_frame(mission_planner_id,location_pin_id,filename):
    return send_file(f"uploads/missions/{mission_planner_id}/model_results/{location_pin_id}/{filename}")