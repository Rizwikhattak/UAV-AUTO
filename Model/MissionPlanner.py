from config import db
from datetime import datetime,date

class MissionPlanner(db.Model):
    __tablename__ = "mission_planner"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('Admin.id'), nullable=False)
    drone_id = db.Column(db.Integer, db.ForeignKey('Drone.id'), nullable=False)
    operator_id = db.Column(db.Integer, db.ForeignKey('Operator.id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False, default=date.today)
    start_time = db.Column(db.Time, nullable=False, default = datetime.now().time)
    status = db.Column(db.String(100), nullable=False, default='not set')
    validity = db.Column(db.Integer, nullable=False, default=1)

    admin = db.relationship('Admin',back_populates = 'missionPlanner')
    operator = db.relationship('Operator',back_populates = 'missionPlanner')
    drone = db.relationship('Drone',back_populates = 'missionPlanner')
    missionTask = db.relationship('MissionTask',back_populates = 'missionPlanner')
    sortie = db.relationship('Sortie',back_populates = 'missionPlanner')


