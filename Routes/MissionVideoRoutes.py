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
