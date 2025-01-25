from flask import Blueprint,request,jsonify,send_file
from Controller import MissionVideoController

mission_video_routes = Blueprint('mission_video_routes',__name__)

@mission_video_routes.route('/upload_video',methods=['POST'])
def upload_video():
    data = request.form.to_dict()
    video = request.files.get('video')
    mission_data = MissionVideoController.upload_video(data,video)
    if mission_data:
        return jsonify({'success':True,'data':mission_data}),200
    else:
        return jsonify({'success':False,'data':mission_data}),400

# Generic API, wont be used anywhere
@mission_video_routes.route('/insert_video',methods=['POST'])
def insert_video():
    data = request.form.to_dict()
    video = request.files.get('video')
    mission_video = MissionVideoController.insert_video(data,video)
    if mission_video:
        return jsonify({'success':True,'data':mission_video}),200
    else:
        return jsonify({'success':False,'data':mission_video}),400

@mission_video_routes.route('/get_all_mission_videos',methods=['GET'])
def get_all_mission_videos():
    mission_videos = MissionVideoController.get_all_mission_videos()
    if mission_videos:
        return jsonify({'success':True,'data':mission_videos}),200
    else:
        return jsonify({'success':False,'data':mission_videos}),400

@mission_video_routes.route('/get_mission_video_by_id/<int:id>',methods=['GET'])
def get_mission_video_by_id(id):
    mission_video = MissionVideoController.get_mission_video_by_id(id)
    if mission_video:
        return jsonify({'success':True,'data':mission_video}),200
    else:
        return jsonify({'success':False,'data':mission_video}),400

@mission_video_routes.route('/delete_mission_video_by_id/<int:id>',methods=['DELETE'])
def delete_mission_video_by_id(id):
    mission_video = MissionVideoController.delete_mission_video_by_id(id)
    if mission_video:
        return jsonify({'success':True,'data':mission_video}),200
    else:
        return jsonify({'success':False,'data':mission_video}),400

@mission_video_routes.route('/update_mission_video_by_id/<int:id>',methods=['PUT'])
def update_mission_video_by_id(id):
    data = request.form.to_dict()
    data['id'] = id
    mission_video = MissionVideoController.update_mission_video_by_id(data)
    if mission_video:
        return jsonify({'success':True,'data':mission_video}),200
    else:
        return jsonify({'success':False,'data':mission_video}),400


@mission_video_routes.route('/uploads/missions/<int:mission_planner_id>/videos/<filename>')
def get_video(mission_planner_id, filename):
    print(f'/uploads/missions/{mission_planner_id}/videos/{filename}')
    return send_file(f'uploads/missions/{mission_planner_id}/videos/{filename}',as_attachment=True)
