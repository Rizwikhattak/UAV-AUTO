from config import db
from Model import DroneAvailabilityLog

class DroneAvailabilityLogController():
    @staticmethod
    def insert_drone_availability_log(data):
        try:
            drone_availability_log = DroneAvailabilityLog(drone_id=data['drone_id'],start_date=data['start_date'],start_date_limit=data['start_date_limit'],start_time_limit=data['start_time_limit'],end_date_limit=data['end_date_limit'],end_time_limit=data['end_time_limit'])
            db.session.add(drone_availability_log)
            db.session.commit()
            return {
                "id": drone_availability_log.id,
                "drone_id": drone_availability_log.drone_id,
                "start_date": drone_availability_log.start_date,
                "start_date_limit": drone_availability_log.start_date_limit,
                "start_time_limit": str(drone_availability_log.start_time_limit),
                "end_date_limit": drone_availability_log.end_date_limit,
                "end_time_limit": str(drone_availability_log.end_time_limit)
            }
        except Exception as e:
            return {}

    @staticmethod
    def get_drone_availability_log():
        try:
            drone_availability_logs = DroneAvailabilityLog.query.filter_by(validity=1).all()
            if drone_availability_logs:
                return [{
                "id": drone_availability_log.id,
                "drone_id": drone_availability_log.drone_id,
                "start_date": drone_availability_log.start_date,
                "start_date_limit": drone_availability_log.start_date_limit,
                "start_time_limit": str(drone_availability_log.start_time_limit),
                "end_date_limit": drone_availability_log.end_date_limit,
                "end_time_limit": str(drone_availability_log.end_time_limit)
            } for drone_availability_log in drone_availability_logs]
            else:
                return []
        except Exception as e:
            return []

    @staticmethod
    def get_drone_availability_log_by_id(id):
        try:
            drone_availability_log = DroneAvailabilityLog.query.filter_by(id=id,validity=1).first()
            if drone_availability_log:
                return {
                "id": drone_availability_log.id,
                "drone_id": drone_availability_log.drone_id,
                "start_date": drone_availability_log.start_date,
                "start_date_limit": drone_availability_log.start_date_limit,
                "start_time_limit": str(drone_availability_log.start_time_limit),
                "end_date_limit": drone_availability_log.end_date_limit,
                "end_time_limit": str(drone_availability_log.end_time_limit)
            }
            else:
                return {}
        except Exception as e:
            return {}

    @staticmethod
    def update_drone_availability_log(data):
        try:
            drone_availability_log = DroneAvailabilityLog.query.filter_by(id=data['id'],validity=1).first()
            if drone_availability_log:
                drone_availability_log.start_date = data['start_date']
                drone_availability_log.start_date_limit = data['start_date_limit']
                drone_availability_log.start_time_limit = data['start_time_limit']
                drone_availability_log.end_date_limit = data['end_date_limit']
                drone_availability_log.end_time_limit = data['end_time_limit']
                db.session.commit()
                return {
                "id": drone_availability_log.id,
                "drone_id": drone_availability_log.drone_id,
                "start_date": drone_availability_log.start_date,
                "start_date_limit": drone_availability_log.start_date_limit,
                "start_time_limit": str(drone_availability_log.start_time_limit),
                "end_date_limit": drone_availability_log.end_date_limit,
                "end_time_limit": str(drone_availability_log.end_time_limit)
                }
            else:
                return {}
        except Exception as e:
            return {}

    @staticmethod
    def delete_drone_availability_log(id):
        try:
            drone_availability_log = DroneAvailabilityLog.query.filter_by(id=id,validity=1).first()
            if drone_availability_log:
                drone_availability_log.validity = 0
                db.session.commit()
                return {
                "id": drone_availability_log.id,
                "drone_id": drone_availability_log.drone_id,
                "start_date": drone_availability_log.start_date,
                "start_date_limit": drone_availability_log.start_date_limit,
                "start_time_limit": str(drone_availability_log.start_time_limit),
                "end_date_limit": drone_availability_log.end_date_limit,
                "end_time_limit": str(drone_availability_log.end_time_limit)
                }
            else:
                return {}
        except Exception as e:
            return {}
