from config import db

class LocationPin(db.Model):
    __tablename__ = "location_pin"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    route_id = db.Column(db.Integer, db.ForeignKey('Routes.id'), nullable=False)  # Foreign key
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    validity = db.Column(db.Integer, nullable=False, default=1)

    routes = db.relationship('Routes',back_populates='location_pin')
    mission_video = db.relationship('MissionVideo', back_populates='location_pin')

