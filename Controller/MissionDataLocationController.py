from config import db
from Model import MissionDataLocation

class MissionDataLocationController():
    @staticmethod
    def insert_mission_data_location(data):
        try:
            mission_data_location = MissionDataLocation(mission_video_id=data['mission_video_id'],latitude=data['latitude'],longitude=data['longitude'],damage=data['damage'])
            db.session.add(mission_data_location)
            db.session.commit()
            return {'id':mission_data_location.id,
                    'mission_video_id':mission_data_location.mission_video_id,
                    'latitude':mission_data_location.latitude,
                    'longitude':mission_data_location.longitude,
                    'damage':mission_data_location.damage}
        except Exception as e:
            print(e)
            return {}

    @staticmethod
    def get_mission_data_location_by_id(id):
        try:
            mission_data_location = MissionDataLocation.query.filter_by(id=id,validity=1).first()
            if mission_data_location:
                return {'id':mission_data_location.id,
                        'mission_video_id':mission_data_location.mission_video_id,
                        'latitude':mission_data_location.latitude,
                        'longitude':mission_data_location.longitude,
                        'damage':mission_data_location.damage}
            else:
                return {}
        except Exception as e:
            print(e)
            return {}

    @staticmethod
    def get_all_mission_data_locations():
        try:
            mission_data_locations = MissionDataLocation.query.filter_by(validity=1).all()
            if mission_data_locations:
                return [{'id':mission_data_location.id,
                        'mission_video_id':mission_data_location.mission_video_id,
                        'latitude':mission_data_location.latitude,
                        'longitude':mission_data_location.longitude,
                        'damage':mission_data_location.damage} for mission_data_location in mission_data_locations]
            else:
                return []
        except Exception as e:
            print(e)
            return []

    @staticmethod
    def update_mission_data_location_by_id(data):
        try:
            mission_data_location = MissionDataLocation.query.filter_by(id=data['id'],validity=1).first()
            if mission_data_location:
                mission_data_location.mission_video_id = data['mission_video_id']
                mission_data_location.latitude = data['latitude']
                mission_data_location.longitude = data['longitude']
                mission_data_location.damage = data['damage']
                db.session.commit()
                return {'id':mission_data_location.id,
                        'mission_video_id':mission_data_location.mission_video_id,
                        'latitude':mission_data_location.latitude,
                        'longitude':mission_data_location.longitude,
                        'damage':mission_data_location.damage}
            else:
                return {}
        except Exception as e:
            print(e)
            return {}

    @staticmethod
    def delete_mission_data_location_by_id(id):
        try:
            mission_data_location = MissionDataLocation.query.filter_by(id=id,validity=1).first()
            if mission_data_location:
                mission_data_location.validity = 0
                db.session.commit()
                return {'id':mission_data_location.id,
                        'mission_video_id':mission_data_location.mission_video_id,
                        'latitude':mission_data_location.latitude,
                        'longitude':mission_data_location.longitude,
                        'damage':mission_data_location.damage}
            else:
                return {}
        except Exception as e:
            print(e)
            return {}

