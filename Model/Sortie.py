from config import db
from datetime import date,datetime
class Sortie(db.Model):
    __tablename__ = 'Sortie'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mission_planner_id = db.Column(db.Integer, db.ForeignKey('mission_planner.id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False, default=date.today)
    end_date = db.Column(db.Date, nullable=False, default=date.today)
    start_time = db.Column(db.Time, nullable=False, default=datetime.now().time)
    end_time = db.Column(db.Time, nullable=False, default=datetime.now().time)
    duration = db.Column(db.Float,nullable=False)
    validity = db.Column(db.Integer,nullable=False,default=1)

    missionPlanner = db.relationship('MissionPlanner',back_populates='sortie')
