from config import db

class MissionDataLocation(db.Model):
    __tablename__ = 'mission_data_location'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mission_video_id = db.Column(db.Integer, db.ForeignKey('mission_video.id'), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    damage = db.Column(db.String(50),nullable=False)
    validity = db.Column(db.Integer,nullable=False, default=1)

    missionDataImage = db.relationship('MissionDataImage',back_populates='missionDataLocation')
    mission_video = db.relationship('MissionVideo',back_populates='missionDataLocation')