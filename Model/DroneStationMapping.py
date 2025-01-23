from config import db

class DroneStationMapping(db.Model):
    __tablename__ = "drone_station_mapping"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    station_id = db.Column(db.Integer, db.ForeignKey('Station.id'), nullable=False)
    drone_id = db.Column(db.Integer, db.ForeignKey('Drone.id'), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    validity = db.Column(db.Integer, nullable=False, default=1)

    drone = db.relationship('Drone',back_populates='droneStationMapping')
    station = db.relationship('Station',back_populates='droneStationMapping')