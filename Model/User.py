from enum import unique

from config import db

class User(db.Model):
    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(300), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(200), nullable=False,default='operator')
    validity = db.Column(db.Integer, nullable=False, default=1)

    operator = db.relationship('Operator',back_populates='user')
    admin = db.relationship('Admin',back_populates='user')
