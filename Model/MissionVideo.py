from config import db

class MissionVideo(db.Model):
    __tablename__ = 'mission_video'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location_pin_id = db.Column(db.Integer, db.ForeignKey('location_pin.id'), nullable=False)
    mission_task_id = db.Column(db.Integer, db.ForeignKey('mission_task.id'), nullable=False)
    file_path = db.Column(db.String(255), nullable=False)
    validity = db.Column(db.Integer, nullable=False, default=1)

    location_pin = db.relationship('LocationPin', back_populates='mission_video')
    missionTask = db.relationship('MissionTask', back_populates='mission_video')
    missionDataLocation = db.relationship('MissionDataLocation', back_populates='mission_video')
