from app import db
from datetime import datetime


class OwnerModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(30), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now())


class PetsModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    type_pet = db.Column(db.String(30), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now())
    ownerID = db.Column(db.Integer, nullable=False)
