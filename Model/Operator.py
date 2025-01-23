from config import db

class Operator(db.Model):
    __tablename__ = "Operator"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer,db.ForeignKey('User.id'),nullable=False)
    image_path = db.Column(db.String(500), nullable=True)
    validity = db.Column(db.Integer,nullable=False,default=1)

    user = db.relationship('User',back_populates='operator')
    missionPlanner = db.relationship('MissionPlanner',back_populates='operator')