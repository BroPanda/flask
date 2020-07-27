from app import db
from datetime import datetime

owners_and_pets = db.Table('owners_pets',
                           db.Column('pets_id', db.Integer, db.ForeignKey('pets_model.id', ondelete='CASCADE'), primary_key=True),
                           db.Column('owner_id', db.Integer, db.ForeignKey('owner_model.id', ondelete='CASCADE'), primary_key=True)
                           )


class OwnerModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(30), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now())
    work = db.Column(db.Integer)
    pets = db.relationship('PetsModel', secondary=owners_and_pets, lazy=True,
                           backref=db.backref('owners', lazy=True))


class PetsModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    type_pet = db.Column(db.String(30), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now())
    # ownerID = db.Column(db.Integer, db.ForeignKey('owner_model.id', ondelete='CASCADE'), nullable=False)
