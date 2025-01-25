from config import db,app
from Model import MissionDataImage

class MissionDataImageController():
    @staticmethod
    def insert_mission_data_image(data):
        try:
            mission_data_image = MissionDataImage(mission_data_location_id=data['mission_data_location_id'],image_path = data['image_path'])
            db.session.add(mission_data_image)
            db.session.commit()
            return {'id':mission_data_image.id,
                    'mission_data_location_id':mission_data_image.mission_data_location_id,
                    'image_path':mission_data_image.image_path}
        except Exception as e:
            return {}

    @staticmethod
    def update_mission_data_image(data):
        try:
            mission_data_image = MissionDataImage.query.filter_by(id=data['id']).first()
            if mission_data_image:
                mission_data_image.mission_data_location_id = data['mission_data_location_id']
                mission_data_image.image_path = data['image_path']
                db.session.commit()
                return {'id':mission_data_image.id,
                        'mission_data_location_id':mission_data_image.mission_data_location_id,
                        'image_path':mission_data_image.image_path}
            else:
                return {}
        except Exception as e:
            return {}

    @staticmethod
    def get_all_mission_data_images():
        try:
            mission_data_images = MissionDataImage.query.filter_by(validity=1).all()
            if mission_data_images:
                return [{'id':mission_data_image.id,
                        'mission_data_location_id':mission_data_image.mission_data_location_id,
                        'image_path':mission_data_image.image_path} for mission_data_image in mission_data_images]
            else:
                return []
        except Exception as e:
            return []

    @staticmethod
    def get_mission_data_image_by_id(id):
        try:
            mission_data_image = MissionDataImage.query.filter_by(id=id,validity=1).first()
            if mission_data_image:
                return {'id':mission_data_image.id,
                        'mission_data_location_id':mission_data_image.mission_data_location_id,
                        'image_path':mission_data_image.image_path}
            else:
                return {}
        except Exception as e:
            return {}

    @staticmethod
    def delete_mission_data_image(id):
        try:
            mission_data_image = MissionDataImage.query.filter_by(id=id).first()
            if mission_data_image:
                mission_data_image.validity = 0
                db.session.commit()
                return {'id':mission_data_image.id,
                        'mission_data_location_id':mission_data_image.mission_data_location_id,
                        'image_path':mission_data_image.image_path}
            else:
                return {}
        except Exception as e:
            return {}






