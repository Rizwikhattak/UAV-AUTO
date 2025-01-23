from config import db

class Drone(db.Model):
    __tablename__ = "Drone"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(200),nullable=False)
    speed = db.Column(db.Float,nullable=False, default=70)
    flight_duration = db.Column(db.Float,nullable=False,default=1)
    ceiling = db.Column(db.Float,nullable=False)
    fps = db.Column(db.Integer,nullable=False)
    image_path = db.Column(db.String(300),nullable=True)
    validity = db.Column(db.Integer,nullable=False,default=1)

    droneAvailabilityLog = db.relationship('DroneAvailabilityLog', back_populates='drone')
    droneStationMapping = db.relationship('DroneStationMapping', back_populates='drone')
    missionPlanner = db.relationship('MissionPlanner', back_populates='drone')