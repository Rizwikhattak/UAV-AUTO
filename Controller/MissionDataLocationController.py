from config import db
from Model import MissionDataLocation

class MissionDataLocationController():
    @staticmethod
    def insert_mission_data_location(data):
        mission_data_location = MissionDataLocation(mission_task_id=data['mission_task_id'],latitude=data['latitude'],longitude=data['longitude'],damage=data['damage'])
        db.session.add(mission_data_location)
        db.session.commit()
        return mission_data_location
