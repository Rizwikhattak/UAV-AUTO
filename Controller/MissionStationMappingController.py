from config import db
from Model import MissionStationMapping

class MissionStationMappingController():
    @staticmethod
    def insert_mission_station_mapping(data):
        try:
            mission_station_mapping = MissionStationMapping(mission_planner_id = data['mission_planner_id'],landing_station_id = data['landing_station_id'],departure_station_id = data['departure_station_id'])
            db.session.add(mission_station_mapping)
            db.session.commit()
            return {
                "id": mission_station_mapping.id,
                "mission_planner_id": mission_station_mapping.mission_planner_id,
                "landing_station_id": mission_station_mapping.landing_station_id,
                "departure_station_id": mission_station_mapping.departure_station_id
                }
        except Exception as e:
            return {}

    @staticmethod
    def get_mission_station_mapping():
        try:
            mission_station_mappings = MissionStationMapping.query.filter_by(validity=1).all()
            if mission_station_mappings:
                return [{
                    "id": mission.id,
                    "mission_planner_id": mission.mission_planner_id,
                    "landing_station_id": mission.landing_station_id,
                    "departure_station_id": mission.departure_station_id
                    } for mission in mission_station_mappings]
            else:
                return []
        except Exception as e:
            return []

    @staticmethod
    def get_mission_station_mapping_by_id(id):
        try:
            mission_station_mapping = MissionStationMapping.query.filter_by(id = id, validity=1).first()
            if mission_station_mapping:
                return {
                    "id": mission_station_mapping.id,
                    "mission_planner_id": mission_station_mapping.mission_planner_id,
                    "landing_station_id": mission_station_mapping.landing_station_id,
                    "departure_station_id": mission_station_mapping.departure_station_id
                    }
            else:
                return {}
        except Exception as e:
            return {}

    @staticmethod
    def update_mission_station_mapping(data):
        try:
            mission_station_mapping = MissionStationMapping.query.filter_by(id = data['id'], validity=1).first()
            if mission_station_mapping:
                mission_station_mapping.mission_planner_id = data['mission_planner_id']
                mission_station_mapping.landing_station_id = data['landing_station_id']
                mission_station_mapping.departure_station_id = data['departure_station_id']
                db.session.commit()
                return {
                    "id": mission_station_mapping.id,
                    "mission_planner_id": mission_station_mapping.mission_planner_id,
                    "landing_station_id": mission_station_mapping.landing_station_id,
                    "departure_station_id": mission_station_mapping.departure_station_id
                    }
            else:
                return {}
        except Exception as e:
            return {}

    @staticmethod
    def delete_mission_station_mapping(id):
        try:
            mission_station_mapping = MissionStationMapping.query.filter_by(id = id, validity=1).first()
            if mission_station_mapping:
                mission_station_mapping.validity = 0
                db.session.commit()
                return {
                    "id": mission_station_mapping.id,
                    "mission_planner_id": mission_station_mapping.mission_planner_id,
                    "landing_station_id": mission_station_mapping.landing_station_id,
                    "departure_station_id": mission_station_mapping.departure_station_id
                    }
            else:
                return {}
        except Exception as e:
            return {}
            