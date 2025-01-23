from config import db
from datetime import datetime, date

class DroneAvailabilityLog(db.Model):
    __tablename__ = "drone_availability_log"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    drone_id = db.Column(db.Integer, db.ForeignKey('Drone.id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False, default=date.today)
    start_date_limit = db.Column(db.Date, nullable=False, default=date.today)
    start_time_limit = db.Column(db.Time, nullable=False, default=datetime.now().time)
    end_date_limit = db.Column(db.Date, nullable=False, default=date.today)
    end_time_limit = db.Column(db.Time, nullable=False, default=datetime.now().time)
    validity = db.Column(db.Integer, nullable=False, default=1)

    drone = db.relationship('Drone', back_populates='droneAvailabilityLog')
