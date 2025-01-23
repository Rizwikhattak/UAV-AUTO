from config import db

class MissionDataImage(db.Model):
    __tablename__ = 'mission_data_image'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mission_data_location_id = db.Column(db.Integer, db.ForeignKey('mission_data_location.id'), nullable=False)
    image_path = db.Column(db.String(300),nullable=False)
    validity = db.Column(db.Integer,nullable=False,default=1)

    missionDataLocation = db.relationship('MissionDataLocation',back_populates='missionDataImage')

