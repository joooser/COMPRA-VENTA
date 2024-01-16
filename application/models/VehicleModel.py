from .base import db

class Vehicle(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    brand = db.Column(db.String(length=30), nullable=False)
    model = db.Column(db.String(length=30), nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    color = db.Column(db.String(length=30), nullable=False)
    type = db.Column(db.String(length=30), nullable=False)
    usage = db.Column(db.String(length=30), nullable=False)
    plate = db.Column(db.String(length=15), nullable=False)
    serial_motor = db.Column(db.String(length=30), nullable=False)
    serial_bodywork = db.Column(db.String(length=30), nullable=False)
    # ...