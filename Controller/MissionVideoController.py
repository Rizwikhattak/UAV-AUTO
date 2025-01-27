from config import db
from Model import MissionVideo
import os
from Directories import make_mission_dirs
from ProcessVideos import extract_frames
class MissionVideoController():
    @staticmethod
    def insert_video(data,mission_video):
        try:
            video_folder, predictions_folder = make_mission_dirs(data)

            mission_video_filename = mission_video.filename.replace(" ", "")
            full_video_path = os.path.join(video_folder, f"{data['location_pin_id']}_{mission_video_filename}")
            for filename in os.listdir(video_folder):
                if filename == f"{data['location_pin_id']}_{mission_video_filename}":
                    os.remove(full_video_path)

            mission_video.save(full_video_path)
            full_video_path = full_video_path.replace("\\", "/")
            mission_video = MissionVideo(location_pin_id=data['location_pin_id'],
                                         mission_task_id=data['mission_task_id'],
                                         file_path=full_video_path)
            db.session.add(mission_video)
            db.session.commit()
            return {'id': mission_video.id, 'location_pin_id': mission_video.location_pin_id, 'mission_task_id': mission_video.mission_task_id, 'file_path': mission_video.file_path}
        except Exception as e:
            print(e)
            return {}

    @staticmethod
    def upload_video(data, mission_video):
        try:
            video_folder, predictions_folder = make_mission_dirs(data)

            mission_video_data = MissionVideoController.insert_video(data,mission_video)
            data['video_path'] = mission_video_data.get('file_path')
            data['mission_video_id'] = mission_video_data.get('id')
            all_mission_data_location_data = extract_frames(data, predictions_folder, 5)
            return all_mission_data_location_data
        except Exception as e:
            print(e)
            return []

    @staticmethod
    def get_all_mission_videos():
        try:
            mission_videos = MissionVideo.query.filter_by(validity=1).all()
            if mission_videos:
                return [{'id': mission_video.id, 'location_pin_id': mission_video.location_pin_id, 'mission_task_id': mission_video.mission_task_id, 'file_path': mission_video.file_path} for mission_video in mission_videos]
            else:
                return []
        except Exception as e:
            print(e)
            return []

    @staticmethod
    def get_mission_video_by_id(id):
        try:
            mission_video = MissionVideo.query.filter_by(id=id, validity=1).first()
            if mission_video:
                return {'id': mission_video.id, 'location_pin_id': mission_video.location_pin_id, 'mission_task_id': mission_video.mission_task_id, 'file_path': mission_video.file_path}
            else:
                return {}
        except Exception as e:
            print(e)
            return {}

    @staticmethod
    def delete_mission_video_by_id(id):
        try:
            mission_video = MissionVideo.query.filter_by(id=id, validity=1).first()
            if mission_video:
                mission_video.validity = 0
                db.session.commit()
                return {'id': mission_video.id, 'location_pin_id': mission_video.location_pin_id, 'mission_task_id': mission_video.mission_task_id, 'file_path': mission_video.file_path}
            else:
                return {}
        except Exception as e:
            print(e)
            return {}

    @staticmethod
    def update_mission_video_by_id(data):
        try:
            mission_video = MissionVideo.query.filter_by(id=data.get('id'), validity=1).first()
            if mission_video:
                mission_video.location_pin_id = data.get('location_pin_id',mission_video.location_pin_id)
                mission_video.mission_task_id = data.get('mission_task_id',mission_video.mission_task_id)
                mission_video.file_path = data.get('file_path',mission_video.file_path)
                db.session.commit()
                return {'id': mission_video.id, 'location_pin_id': mission_video.location_pin_id, 'mission_task_id': mission_video.mission_task_id, 'file_path': mission_video.file_path}
            else:
                return {}
        except Exception as e:
            print(e)
            return {}
