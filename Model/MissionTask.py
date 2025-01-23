from config import db

class MissionTask(db.Model):
    __tablename__ = "mission_task"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mission_planner_id = db.Column(db.Integer, db.ForeignKey('mission_planner.id'),nullable=False)
    route_id = db.Column(db.Integer,db.ForeignKey('Routes.id'),nullable=False)
    description = db.Column(db.String(1000),nullable=False)
    validity = db.Column(db.Integer,nullable=False,default=1)

    missionPlanner = db.relationship('MissionPlanner',back_populates='missionTask')
    routes = db.relationship('Routes',back_populates='missionTask')
    mission_video = db.relationship('MissionVideo',back_populates='missionTask')