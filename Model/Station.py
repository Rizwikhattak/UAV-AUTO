from config import db

class Station(db.Model):
    __tablename__ = 'Station'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    num_drones = db.Column(db.Integer, nullable=False, default=0)
    validity = db.Column(db.Integer,nullable=False, default=1)

    droneStationMapping = db.relationship('DroneStationMapping', back_populates='station')