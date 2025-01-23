from config import db

class MissionStationMapping(db.Model):
    __tablename__ = 'mission_station_mapping'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mission_planner_id = db.Column(db.Integer, db.ForeignKey('mission_planner.id'), nullable=False)
    landing_station_id = db.Column(db.Integer, db.ForeignKey("Station.id"), nullable=False)
    departure_station_id = db.Column(db.Integer, db.ForeignKey("Station.id"), nullable=False)
    validity = db.Column(db.Integer, nullable=False, default=1)