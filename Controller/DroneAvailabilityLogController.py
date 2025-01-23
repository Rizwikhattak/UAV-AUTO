from config import db
from Model import DroneAvailabilityLog

class DroneAvailabilityLogController():
    @staticmethod
    def insert_drone_availability_log(data):
        drone_availability_log = DroneAvailabilityLog(drone_id=data['drone_id'],start_date=data['start_date'],start_date_limit=data['start_date_limit'],start_time_limit=data['start_time_limit'],end_date_limit=data['end_date_limit'],end_time_limit=data['end_time_limit'])
        db.session.add(drone_availability_log)
        db.session.commit()
        return drone_availability_log