from flask import Blueprint,request,jsonify,send_file
from Controller import MissionDataImageController

mission_data_image_routes = Blueprint('mission_data_image_routes',__name__)

@mission_data_image_routes.route('/insert_mission_data_image',methods=['POST'])
def insert_mission_data_image():
    data = request.get_json()
    mission_data_image = MissionDataImageController.insert_mission_data_image(data)
    if mission_data_image:
        return jsonify({'success':True,'data':mission_data_image}),200
    else:
        return jsonify({'success':False,'data':mission_data_image}),400

@mission_data_image_routes.route('/update_mission_data_image_by_id/<int:id>',methods=['PUT'])
def update_mission_data_image_by_id(id):
    data = request.get_json()
    data['id'] = id
    mission_data_image = MissionDataImageController.update_mission_data_image_by_id(data)
    if mission_data_image:
        return jsonify({'success':True,'data':mission_data_image}),200
    else:
        return jsonify({'success':False,'data':mission_data_image}),400

@mission_data_image_routes.route('/get_all_mission_data_images',methods=['GET'])
def get_all_mission_data_images():
    mission_data_images = MissionDataImageController.get_all_mission_data_images()
    if mission_data_images:
        return jsonify({'success':True,'data':mission_data_images}),200
    else:
        return jsonify({'success':False,'data':mission_data_images}),400

@mission_data_image_routes.route('/get_mission_data_image_by_id/<int:id>',methods=['GET'])
def get_mission_data_image_by_id(id):
    mission_data_image = MissionDataImageController.get_mission_data_image_by_id(id)
    if mission_data_image:
        return jsonify({'success':True,'data':mission_data_image}),200
    else:
        return jsonify({'success':False,'data':mission_data_image}),400

@mission_data_image_routes.route('/delete_mission_data_image_by_id/<int:id>',methods=['DELETE'])
def delete_mission_data_image_by_id(id):
    mission_data_image = MissionDataImageController.delete_mission_data_image_by_id(id)
    if mission_data_image:
        return jsonify({'success':True,'data':mission_data_image}),200
    else:
        return jsonify({'success':False,'data':mission_data_image}),400


@mission_data_image_routes.route('/uploads/missions/<int:mission_planner_id>/model_results/<int:location_pin_id>/<filename>',methods=['GET'])
def serve_damaged_frame(mission_planner_id,location_pin_id,filename):
    return send_file(f"uploads/missions/{mission_planner_id}/model_results/{location_pin_id}/{filename}")