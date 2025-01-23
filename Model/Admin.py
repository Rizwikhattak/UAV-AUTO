from config import db

class Admin(db.Model):
    __tablename__ = "Admin"

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer,db.ForeignKey('User.id'),nullable=False)
    age = db.Column(db.Integer,nullable=False)
    gender = db.Column(db.String(20),nullable=False)
    phone_no = db.Column(db.Integer,nullable=False)
    validity = db.Column(db.Integer,nullable=False,default=1)

    user = db.relationship('User',back_populates='admin')
    missionPlanner = db.relationship('MissionPlanner',back_populates='admin')
    routes = db.relationship('Routes',back_populates='admin')
