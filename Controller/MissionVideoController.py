from config import db
from Model import MissionVideo
import os
from Directories import make_mission_dirs
from ProcessImage import extract_frames
class MissionVideoController():
    @staticmethod
    def insert_video(data):
        mission_video = MissionVideo(location_pin_id=data['location_pin_id'],
                                     mission_task_id=data['mission_task_id'],
                                     file_path=data['video_path'])
        db.session.add(mission_video)
        db.session.commit()
        return {'id': mission_video.id, 'location_pin_id': mission_video.location_pin_id, 'mission_task_id': mission_video.mission_task_id, 'file_path': mission_video.file_path}

    @staticmethod
    def upload_video(data, mission_video):
        video_folder, predictions_folder = make_mission_dirs(data)
        mission_video_filename = mission_video.filename.replace(" ", "")
        full_video_path = os.path.join(video_folder, f"{data['location_pin_id']}_{mission_video_filename}")
        for filename in os.listdir(video_folder):
            if filename == f"{data['location_pin_id']}_{mission_video_filename}":
                os.remove(full_video_path)
        mission_video.save(full_video_path)
        data['video_path'] = full_video_path
        mission_video_data = MissionVideoController.insert_video(data)
        data['mission_video_id'] = mission_video_data.get('id')
        all_mission_data_location_data = extract_frames(data, predictions_folder, 1)
        return all_mission_data_location_data
