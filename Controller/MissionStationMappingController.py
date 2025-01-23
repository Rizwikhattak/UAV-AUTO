from config import db
from Model import MissionStationMapping

class MissionStationMappingController():
    @staticmethod
    def insert_mission_station_mapping(data):
        mission_station_mapping = MissionStationMapping(mission_planner_id = data['mission_planner_id'],landing_station_id = data['landing_station_id'],departure_station_id = data['departure_station_id'])
        db.session.add(mission_station_mapping)
        db.session.commit()
        return mission_station_mapping